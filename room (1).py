class Room:
    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, availability_status: bool = True):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__availability_status = availability_status

    def update_availability(self, status: bool):
        self.__availability_status = status

    def get_room_number(self):
        return self.__room_number

    def get_room_type(self):
        return self.__room_type

    def get_amenities(self):
        return self.__amenities

    def get_price_per_night(self):
        return self.__price_per_night

    def get_availability_status(self):
        return self.__availability_status