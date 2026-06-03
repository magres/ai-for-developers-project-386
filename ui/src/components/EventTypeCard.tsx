import { Card, Text, Badge, Button, Group } from '@mantine/core';
import { useNavigate } from 'react-router-dom';
import type { EventType } from '../types';

interface EventTypeCardProps {
  eventType: EventType;
}

export default function EventTypeCard({ eventType }: EventTypeCardProps) {
  const navigate = useNavigate();

  return (
    <Card shadow="sm" padding="lg" radius="md" withBorder>
      <Group justify="space-between" mb="xs">
        <Text fw={500}>{eventType.name}</Text>
        <Badge color="blue">{eventType.durationMinutes} min</Badge>
      </Group>
      <Text size="sm" c="dimmed" mb="md">
        {eventType.description}
      </Text>
      <Button
        fullWidth
        variant="light"
        onClick={() => navigate(`/book/${eventType.id}`)}
      >
        Select Slot
      </Button>
    </Card>
  );
}
