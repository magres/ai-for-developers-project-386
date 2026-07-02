import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Container, Title, Loader, Center, Alert, Stack } from '@mantine/core';
import { fetchSlots, fetchEventTypes } from '../api';
import type { EventType, TimeSlot } from '../types';
import SlotPicker from '../components/SlotPicker';
import dayjs from 'dayjs';

export default function BookingPage() {
  const { eventTypeId } = useParams<{ eventTypeId: string }>();
  const [eventType, setEventType] = useState<EventType | null>(null);
  const [slots, setSlots] = useState<TimeSlot[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!eventTypeId) return;

    const dateFrom = dayjs().startOf('day').toISOString();
    const dateTo = dayjs().add(14, 'day').endOf('day').toISOString();
    const userTz = Intl.DateTimeFormat().resolvedOptions().timeZone;

    setLoading(true);
    Promise.all([
      fetchEventTypes().then((types) => types.find((t) => t.id === eventTypeId) || null),
      fetchSlots(eventTypeId, dateFrom, dateTo, userTz),
    ])
      .then(([et, slotsData]) => {
        setEventType(et);
        setSlots(slotsData);
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [eventTypeId]);

  if (loading) {
    return <Center h={300}><Loader /></Center>;
  }

  if (error) {
    return (
      <Container>
        <Alert color="red" title="Failed to load slots">
          {error}
        </Alert>
      </Container>
    );
  }

  return (
    <Container size="sm">
      <Stack>
        <Title order={2}>
          {eventType ? `Book: ${eventType.name}` : 'Select a Slot'}
        </Title>
        <SlotPicker
          slots={slots}
          eventTypeId={eventTypeId!}
          loading={loading}
        />
      </Stack>
    </Container>
  );
}
