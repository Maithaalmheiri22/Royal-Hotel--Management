class Invoice:
    def __init__(self, booking: Booking):
        self.__invoice_id = booking.get_booking_id()
        self.__booking = booking
        self.__total_amount = booking.calculate_total()
        self.__payment_status = "Pending"

    def generate_invoice(self):
        return f"Invoice ID: {self.__invoice_id}, Total: ${self.__total_amount}, Status: {self.__payment_status}"

    def update_payment_status(self, status):
        self.__payment_status = status