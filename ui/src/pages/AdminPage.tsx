import { useState, useEffect } from 'react';
import {
  Container, Title, TextInput, Button, Stack, Table, Loader,
  Center, Alert, NumberInput, Paper, Text,
} from '@mantine/core';
import { useForm } from '@mantine/form';
import { createEventType, fetchUpcomingBookings, fetchEventTypes } from '../api';
import type { EventType, Booking } from '../types';
import dayjs from 'dayjs';
import { notifications } from '@mantine/notifications';

export default function AdminPage() {
  const [bookings, setBookings] = useState<Booking[]>([]);
  const [eventTypes, setEventTypes] = useState<EventType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const form = useForm({
    initialValues: {
      name: '',
      description: '',
      durationMinutes: 30,
    },
    validate: {
      name: (v: string) => (v.trim().length > 0 ? null : 'Name is required'),
      description: (v: string) => (v.trim().length > 0 ? null : 'Description is required'),
      durationMinutes: (v: number) => (v > 0 ? null : 'Duration must be positive'),
    },
  });

  const loadData = () => {
    setLoading(true);
    Promise.all([
      fetchEventTypes(),
      fetchUpcomingBookings(),
    ])
      .then(([types, bookingsData]) => {
        setEventTypes(types);
        setBookings(bookingsData);
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  };

  useEffect(loadData, []);

  const handleCreateType = async (values: typeof form.values) => {
    try {
      await createEventType(values);
      notifications.show({ title: 'Created', message: 'Event type created', color: 'green' });
      form.reset();
      loadData();
    } catch (err: any) {
      notifications.show({ title: 'Error', message: err.message, color: 'red' });
    }
  };

  if (loading) {
    return <Center h={300}><Loader /></Center>;
  }

  if (error) {
    return (
      <Container>
        <Alert color="red" title="Failed to load data">
          {error}
        </Alert>
      </Container>
    );
  }

  const typeMap = new Map(eventTypes.map((t) => [t.id, t.name]));

  return (
    <Container size="lg">
      <Stack>
        <Paper withBorder p="md" radius="md">
          <Title order={3} mb="md">Create Event Type</Title>
          <form onSubmit={form.onSubmit(handleCreateType)}>
            <Stack>
              <TextInput
                label="Name"
                placeholder="e.g. 30-min Chat"
                {...form.getInputProps('name')}
              />
              <TextInput
                label="Description"
                placeholder="Brief description"
                {...form.getInputProps('description')}
              />
              <NumberInput
                label="Duration (minutes)"
                min={1}
                {...form.getInputProps('durationMinutes')}
              />
              <Button type="submit">Create</Button>
            </Stack>
          </form>
        </Paper>

        <Paper withBorder p="md" radius="md">
          <Title order={3} mb="md">Upcoming Bookings</Title>
          <Table striped highlightOnHover>
            <Table.Thead>
              <Table.Tr>
                <Table.Th>Date</Table.Th>
                <Table.Th>Time</Table.Th>
                <Table.Th>Event Type</Table.Th>
              </Table.Tr>
            </Table.Thead>
            <Table.Tbody>
              {bookings.length === 0 ? (
                <Table.Tr>
                  <Table.Td colSpan={3}>
                    <Text c="dimmed" ta="center" py="md">
                      No bookings yet.
                    </Text>
                  </Table.Td>
                </Table.Tr>
              ) : (
                bookings.map((b) => (
                  <Table.Tr key={b.id}>
                    <Table.Td>{dayjs(b.startTime).format('MMMM D, YYYY')}</Table.Td>
                    <Table.Td>
                      {dayjs(b.startTime).format('HH:mm')} – {dayjs(b.endTime).format('HH:mm')}
                    </Table.Td>
                    <Table.Td>{typeMap.get(b.eventTypeId) || b.eventTypeId}</Table.Td>
                  </Table.Tr>
                ))
              )}
            </Table.Tbody>
          </Table>
        </Paper>
      </Stack>
    </Container>
  );
}
