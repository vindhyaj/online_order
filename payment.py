from enum import Enum
from address import Address

class PaymentType(Enum):
    CARD = 1

class PaymentStatus(Enum):
    SUCCESS = 1
    FAILED = 2
    PENDING = 3

class CardDetails:
    def __init__(self, number: str, expiry_month: int, expiry_year: int, cvv: int, name_on_card: str, billing_address: Address ):

        if not number or not expiry_month or not expiry_year or not cvv or not name_on_card or not billing_address:
            raise InvalidArgumentError("card details cannot be empty")

        self.number = number
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.cvv = cvv
        self.name_on_card = name_on_card
        self.billing_address = billing_address

class PaymentMethod:
    def __init__(self, card: CardDetails):
        self.payment_type = PaymentType.CARD
        self.card = card

    def ProcessPayment(self):
        pass

    def CancelPayment(self):
        pass

