from lib.booking_repository import *
from lib.booking import *

# find all
def test_find_all_bookings(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repository = BookingRepository(db_connection)
    bookings = booking_repository.all()
    assert bookings == [
        Booking(1, 1, 2, "2024-11-30", "2024-12-01", "pending"),
        Booking(2, 1, 3, "2024-12-03", "2024-12-04", "pending"),
        Booking(3, 2, 3, "2024-12-06", "2024-12-07", "pending"),
        Booking(4, 2, 4, "2024-12-07", "2024-12-08", "pending"),
        Booking(5, 3, 4, "2024-12-12", "2024-12-13", "pending"),
        Booking(6, 3, 2, "2024-12-24", "2024-12-25", "pending"),
    ]

# find booking requests for host
def test_find_property_bookings_for_host(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repository = BookingRepository(db_connection)
    booking = booking_repository.find_property_bookings_for_host(2)
    assert booking == [
        Booking(3, 2, 3, '2024-12-06', '2024-12-07', 'pending'),
        Booking(4, 2, 4, '2024-12-07', '2024-12-08', 'pending')
    ]

# find booking requests for guest
def test_find_property_bookings_for_guest(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repository = BookingRepository(db_connection)
    booking = booking_repository.find_property_bookings_for_guest(2)
    assert booking == [
        Booking(1, 1, 2, '2024-11-30', '2024-12-01', 'pending'),
        Booking(6, 3, 2, '2024-12-24', '2024-12-25', 'pending')
    ]

# create
def test_create_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repository = BookingRepository(db_connection)
    booking = booking_repository.create(Booking(None, 2, 2, '2025-01-01', '2025-01-02', 'pending'))
    bookings = booking_repository.all()
    assert bookings == [
        Booking(1, 1, 2, '2024-11-30', '2024-12-01', 'pending'),
        Booking(2, 1, 3, '2024-12-03', '2024-12-04', 'pending'),
        Booking(3, 2, 3, '2024-12-06', '2024-12-07', 'pending'),
        Booking(4, 2, 4, '2024-12-07', '2024-12-08', 'pending'),
        Booking(5, 3, 4, '2024-12-12', '2024-12-13', 'pending'),
        Booking(6, 3, 2, '2024-12-24', '2024-12-25', 'pending'),
        Booking(7, 2, 2, '2025-01-01', '2025-01-02', 'pending')
    ]

# delete
def test_delete_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repository = BookingRepository(db_connection) 
    booking_repository.delete(2)
    bookings = booking_repository.all()
    assert bookings == [
        Booking(1, 1, 2, '2024-11-30', '2024-12-01', 'pending'),
        Booking(3, 2, 3, '2024-12-06', '2024-12-07', 'pending'),
        Booking(4, 2, 4, '2024-12-07', '2024-12-08', 'pending'),
        Booking(5, 3, 4, '2024-12-12', '2024-12-13', 'pending'),
        Booking(6, 3, 2, '2024-12-24', '2024-12-25', 'pending')
    ]