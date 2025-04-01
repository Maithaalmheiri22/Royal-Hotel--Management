class Payment:
    def __init__(self, payment_id: int, invoice: Invoice, payment_method: str, amount: float):
        self.__payment_id = payment_id
        self.__invoice = invoice
        self.__payment_method = payment_method
        self.__amount = amount
        self.__status = "Processing"

    def process_payment(self):
        if self.__amount >= self.__invoice._Invoice__total_amount:
            self.__invoice.update_payment_status("Paid")
            self.__status = "Completed"
            return "Payment Successful"
        return "Payment Failed"

    def get_payment_id(self):
        return self.__payment_id

    def get_invoice(self):
        return self.__invoice

    def get_payment_method(self):
        return self.__payment_method

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status
