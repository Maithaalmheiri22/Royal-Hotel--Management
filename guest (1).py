class Guest:
    def __init__(self, guest_id: int, name: str, contact_info: str, loyalty_status: str = "None"):
        self.__guest_id = guest_id
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_status = loyalty_status
        self.__reservation_history = []

    def create_account(self, name, contact_info):
        self.__name = name
        self.__contact_info = contact_info

    def update_profile(self, name, contact_info):
        self.__name = name
        self.__contact_info = contact_info

    def view_reservations(self):
        return self.__reservation_history

    def get_guest_id(self):
        return self.__guest_id

    def get_name(self):
        return self.__name

    def get_contact_info(self):
        return self.__contact_info

    def get_loyalty_status(self):
        return self.__loyalty_status