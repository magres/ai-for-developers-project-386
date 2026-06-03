import { useState, useEffect } from 'react';
import { Container, Title, SimpleGrid, Loader, Center, Alert } from '@mantine/core';
import { fetchEventTypes } from '../api';
import type { EventType } from '../types';
import EventTypeCard from '../components/EventTypeCard';

export default function EventTypesPage() {
  const [eventTypes, setEventTypes] = useState<EventType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchEventTypes()
      .then(setEventTypes)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return <Center h={300}><Loader /></Center>;
  }

  if (error) {
    return (
      <Container>
        <Alert color="red" title="Failed to load event types">
          {error}
        </Alert>
      </Container>
    );
  }

  return (
    <Container size="lg">
      <Title order={2} mb="lg">Available Event Types</Title>
      <SimpleGrid cols={{ base: 1, sm: 2, lg: 3 }}>
        {eventTypes.map((et) => (
          <EventTypeCard key={et.id} eventType={et} />
        ))}
      </SimpleGrid>
    </Container>
  );
}
