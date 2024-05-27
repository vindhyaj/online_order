from enum import Enum
from item import Item
from payment import PaymentMethod, Address
from types import dict

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    PENDING_PAYMENT = 3
    DELIVERY_SCHEDULED = 4
    IN_TRANSIT = 5
    DELIVERED = 6
    COMPLETE = 7
    CANCELED = 8
    FAILED = 9


class Order:
    def __init__(self, user_id):
        self.customer = user_id
        self.items = []
        self.payment_method = nil
        self.shipping_address = nil
        self.status = nil

    def AddItem(self, item: Item):
        self.items.append(item)

    def PaymentMethod(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def ShippingAddress(self, address: Address):
        self.shipping_address = address

    def Place(self):
        pass

    def Cancel(self):
        pass

def parse_order(order_request: dict):
    pass

