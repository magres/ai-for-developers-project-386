import type { EventType, Booking, TimeSlot, BookingCreate, EventTypeCreate } from './types';

const BASE_URL = '/api';

async function request<T>(url: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${BASE_URL}${url}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  if (!response.ok) {
    const text = await response.text().catch(() => 'Unknown error');
    throw new Error(`API Error (${response.status}): ${text}`);
  }
  if (response.status === 204) return undefined as T;
  return response.json();
}

export function fetchEventTypes(): Promise<EventType[]> {
  return request<EventType[]>('/event-types');
}

export function fetchSlots(eventTypeId: string, dateFrom?: string, dateTo?: string): Promise<TimeSlot[]> {
  const params = new URLSearchParams();
  if (dateFrom) params.set('dateFrom', dateFrom);
  if (dateTo) params.set('dateTo', dateTo);
  const qs = params.toString();
  return request<TimeSlot[]>(`/event-types/${eventTypeId}/slots${qs ? `?${qs}` : ''}`);
}

export function createBooking(data: BookingCreate): Promise<Booking> {
  return request<Booking>('/bookings', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

export function createEventType(data: EventTypeCreate): Promise<EventType> {
  return request<EventType>('/admin/event-types', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

export function fetchUpcomingBookings(): Promise<Booking[]> {
  return request<Booking[]>('/admin/bookings');
}
