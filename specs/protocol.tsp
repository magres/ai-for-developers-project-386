import "@typespec/http";
import "@typespec/rest";

using TypeSpec.Http;
using TypeSpec.Rest;

@service(#{
  title: "Calendar Booking API"
})
@server("http://localhost:3000", "Development server")
namespace CalendarBooking;

// ─── Models ───────────────────────────────────────────────────────

model EventType {
  id: string;
  name: string;
  description: string;
  durationMinutes: int32;
}

model Booking {
  id: string;
  eventTypeId: string;
  startTime: utcDateTime;
  endTime: utcDateTime;
}

model TimeSlot {
  startTime: utcDateTime;
  endTime: utcDateTime;
}

// ─── Request Bodies ───────────────────────────────────────────────

model EventTypeCreate {
  name: string;
  description: string;
  durationMinutes: int32;
}

model BookingCreate {
  eventTypeId: string;
  startTime: utcDateTime;
}

// ─── Public Endpoints (Guest) ────────────────────────────────────

@route("/api/event-types")
interface EventTypes {
  @get
  op list(): EventType[];

  @get
  @route("{eventTypeId}/slots")
  op getSlots(
    @path eventTypeId: string,
    @query dateFrom?: utcDateTime,
    @query dateTo?: utcDateTime,
  ): TimeSlot[];
}

@route("/api/bookings")
interface Bookings {
  @post
  op create(body: BookingCreate): Booking;
}

// ─── Admin Endpoints (Owner) ─────────────────────────────────────

@route("/api/admin/event-types")
interface AdminEventTypes {
  @post
  op create(body: EventTypeCreate): EventType;
}

@route("/api/admin/bookings")
interface AdminBookings {
  @get
  op listUpcoming(): Booking[];
}
