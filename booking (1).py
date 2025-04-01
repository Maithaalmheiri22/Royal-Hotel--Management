from datetime import datetime
from invoice import Invoice

class Booking:
    def __init__(self, booking_id: int, guest: Guest, room: Room, check_in_date: datetime, check_out_date: datetime):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = "Confirmed"
        self.__invoice = Invoice(self)

    def confirm_booking(self):
        self.__room.update_availability(False)
        return "Booking Confirmed"

    def cancel_booking(self):
        self.__room.update_availability(True)
        self.__status = "Cancelled"
        return "Booking Cancelled"

    def calculate_total(self):
        num_nights = (self.__check_out_date - self.__check_in_date).days
        return num_nights * self.__room.get_price_per_night()

    def get_booking_id(self):
        return self.__booking_id

    def get_guest(self):
        return self.__guest

    def get_room(self):
        return self.__room

    def get_check_in_date(self):
        return self.__check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def get_status(self):
        return self.__status