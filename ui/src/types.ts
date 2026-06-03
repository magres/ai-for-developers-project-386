export interface EventType {
  id: string;
  name: string;
  description: string;
  durationMinutes: number;
}

export interface Booking {
  id: string;
  eventTypeId: string;
  startTime: string;
  endTime: string;
}

export interface TimeSlot {
  startTime: string;
  endTime: string;
}

export interface EventTypeCreate {
  name: string;
  description: string;
  durationMinutes: number;
}

export interface BookingCreate {
  eventTypeId: string;
  startTime: string;
}
