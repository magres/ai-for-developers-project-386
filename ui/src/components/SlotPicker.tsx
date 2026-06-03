import { useMemo, useState } from 'react';
import { Calendar } from '@mantine/dates';
import {
  Stack, Text, Button, Group, Modal, Badge,
} from '@mantine/core';
import { notifications } from '@mantine/notifications';
import dayjs from 'dayjs';
import { createBooking } from '../api';
import type { TimeSlot } from '../types';

interface SlotPickerProps {
  slots: TimeSlot[];
  eventTypeId: string;
  loading: boolean;
}

export default function SlotPicker({ slots, eventTypeId, loading }: SlotPickerProps) {
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);

  const today = dayjs().startOf('day').toDate();
  const maxDate = dayjs().add(14, 'day').endOf('day').toDate();

  const effectiveSlots = useMemo(() => {
    if (slots.length > 0) return { slots, isDemo: false };

    const demo: TimeSlot[] = [];
    let hour = 9;
    while (hour < 18) {
      const t = dayjs().add(1, 'day').hour(hour).minute(0).second(0).millisecond(0);
      demo.push({
        startTime: t.toISOString(),
        endTime: t.add(30, 'minute').toISOString(),
      });
      hour += hour === 12 ? 2 : 1;
    }
    if (demo.length === 0) return { slots: [], isDemo: false };
    return { slots: demo, isDemo: true };
  }, [slots]);

  const datesWithSlots = new Set(
    effectiveSlots.slots.map((s) => dayjs(s.startTime).format('YYYY-MM-DD')),
  );

  const selectedDateSlots = selectedDate
    ? effectiveSlots.slots
        .filter((s) => dayjs(s.startTime).isSame(selectedDate, 'day'))
        .sort((a, b) => dayjs(a.startTime).unix() - dayjs(b.startTime).unix())
    : [];

  return (
    <Stack align="center">
      {effectiveSlots.isDemo && (
        <Badge color="yellow" size="lg">Demo data — no real backend</Badge>
      )}

      <Calendar
        minDate={today}
        maxDate={maxDate}
        getDayProps={(date) => {
          const key = dayjs(date).format('YYYY-MM-DD');
          const hasSlots = datesWithSlots.has(key);
          return {
            onClick: hasSlots ? () => setSelectedDate(date) : undefined,
            selected: selectedDate ? dayjs(date).isSame(selectedDate, 'day') : false,
          };
        }}
        renderDay={(date) => {
          const key = dayjs(date).format('YYYY-MM-DD');
          const hasSlots = datesWithSlots.has(key);
          return (
            <div style={{ position: 'relative' }}>
              <div>{date.getDate()}</div>
              {hasSlots && (
                <div
                  style={{
                    position: 'absolute',
                    bottom: -2,
                    left: '50%',
                    transform: 'translateX(-50%)',
                    width: 4,
                    height: 4,
                    borderRadius: '50%',
                    background: 'var(--mantine-color-blue-6)',
                  }}
                />
              )}
            </div>
          );
        }}
      />

      {selectedDate ? (
        <Stack align="center" w="100%">
          <Text fw={600}>
            {dayjs(selectedDate).format('dddd, MMMM D')}
          </Text>
          {selectedDateSlots.length === 0 ? (
            <Text c="dimmed" size="sm">No slots available on this day.</Text>
          ) : (
            <Group gap="sm" justify="center">
              {selectedDateSlots.map((slot, i) => (
                <SlotButton
                  key={i}
                  slot={slot}
                  eventTypeId={eventTypeId}
                />
              ))}
            </Group>
          )}
        </Stack>
      ) : !loading && (
        <Text c="dimmed" size="sm">Select a day with a blue dot to see available times.</Text>
      )}
    </Stack>
  );
}

function SlotButton({ slot, eventTypeId }: { slot: TimeSlot; eventTypeId: string }) {
  const [opened, setOpened] = useState(false);
  const [confirming, setConfirming] = useState(false);

  const handleConfirm = async () => {
    setConfirming(true);
    try {
      await createBooking({ eventTypeId, startTime: slot.startTime });
      notifications.show({ title: 'Booked!', message: 'Slot booked successfully.', color: 'green' });
      window.location.href = '/';
    } catch (err: any) {
      notifications.show({ title: 'Error', message: err.message, color: 'red' });
    } finally {
      setConfirming(false);
      setOpened(false);
    }
  };

  return (
    <>
      <Button variant="outline" onClick={() => setOpened(true)}>
        {dayjs(slot.startTime).format('HH:mm')}
      </Button>

      <Modal
        opened={opened}
        onClose={() => setOpened(false)}
        title="Confirm Booking"
        centered
      >
        <Stack>
          <Text size="sm">
            <strong>Date:</strong> {dayjs(slot.startTime).format('MMMM D, YYYY')}
          </Text>
          <Text size="sm">
            <strong>Time:</strong> {dayjs(slot.startTime).format('HH:mm')} – {dayjs(slot.endTime).format('HH:mm')}
          </Text>
          <Group justify="flex-end">
            <Button variant="default" onClick={() => setOpened(false)}>
              Cancel
            </Button>
            <Button onClick={handleConfirm} loading={confirming}>
              Confirm
            </Button>
          </Group>
        </Stack>
      </Modal>
    </>
  );
}
