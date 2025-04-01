from datetime import datetime
from guest import Guest
from room import Room
from booking import Booking

# Testing the cration of the Guest object
guest1 = Guest(1, "John Doe", "john@example.com")
print(f"Guest Created: {guest1.get_name()}, Contact: {guest1.get_contact_info()}")

guest2 = Guest(2, "Jane Smith", "jane@example.com")
print(f"Guest Created: {guest2.get_name()}, Contact: {guest2.get_contact_info()}")

# Testing the Room Availability
room1 = Room(101, "Single", ["Wi-Fi", "TV"], 100.0)
print(f"Room {room1.get_room_number()} Availability: {room1.get_availability_status()}")

# Testing the Booking object Creation
booking1 = Booking(1, guest1, room1, datetime(2025, 4, 1), datetime(2025, 4, 5))
print(f"Booking Status: {booking1.get_status()}")

# Testing the method for Booking Cancellation
print(booking1.cancel_booking())
print(f"Updated Booking Status: {booking1.get_status()}")