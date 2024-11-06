from lib.booking import *

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["listing_id"], row["guest_id"], row["check_in"], row["check_out"], row["status"])
            bookings.append(item)
        return bookings
    

    def find_property_bookings_for_host(self, listing_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE listing_id = %s", [listing_id])
        return (Booking(row["id"], row["listing_id"], row["guest_id"], row["check_in"], row["check_out"], row["status"]) for row in rows)
    
    def find_property_bookings_for_guest(self, guest_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE fuest_id = %s", [guest_id])
        return (Booking(row["id"], row["listing_id"], row["guest_id"], row["check_in"], row["check_out"], row["status"]) for row in rows)

    def create(self, booking):
        rows = self._connection.execute("INSERT INTO bookings (listing_id, guest_id, check_in, check_out) VALUES (%s, %s, %s, %s)", [booking.listing_id, booking.guest_id, booking.check_in, booking.check_out]) #status pending should be auto added
        return None

    def delete(self, id):
        self._connection.execute("DELETE FROM bookings WHERE id = %s", [id])
        return None
