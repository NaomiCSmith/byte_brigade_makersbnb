from lib.booking import *

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["listing_id"], row["user_id"], row["check_in"], row["check_out"], row["status"])
            bookings.append(item)
        return bookings
    

    def find_property_bookings_for_host(self, listing_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE listing_id = %s", [listing_id])
        bookings = [Booking(row["id"], row["listing_id"], row["user_id"], row["check_in"], row["check_out"], row["status"]) for row in rows]
        return bookings
    
    def find_property_bookings_for_guest(self, user_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE user_id = %s", [user_id])
        bookings = [Booking(row["id"], row["listing_id"], row["user_id"], row["check_in"], row["check_out"], row["status"]) for row in rows]
        return bookings

    def create(self, booking):
        rows = self._connection.execute("INSERT INTO bookings (listing_id, user_id, check_in, check_out, status) VALUES (%s, %s, %s, %s, %s)", [booking.listing_id, booking.user_id, booking.check_in, booking.check_out, booking.status]) #status pending should be auto added
        return None

    def delete(self, id):
        self._connection.execute("DELETE FROM bookings WHERE id = %s", [id])
        return None
