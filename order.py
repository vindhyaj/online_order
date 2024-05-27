from enum import Enum
from item import Item
from payment import PaymentMethod, Address
from config import Keys
from errors import InvalidArgumentError

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
        if not user_id:
            raise InvalidArgumentError("user_id cannot be empty")

        self.customer = user_id
        self.items = []
        self.payment_method = None
        self.shipping_address = None
        self.status = None

    def AddItem(self, item: Item):
        self.items.append(item)

    def AddPaymentMethod(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def AddShippingAddress(self, address: Address):
        self.shipping_address = address

    def Place(self):
        pass

    def Cancel(self):
        pass

def ParseOrder(order_request: dict):
    try:
        customer_id = order_request.get(Keys.CUSTOMER_ID)

        order = Order(customer_id)
    
        address = order_request.get(Keys.SHIPPING_ADDRESS)

        if not address or not address.get(Keys.STREET_NAME) or not address.get(Keys.CITY) or not address.get(Keys.POST_CODE) or not address.get(Keys.COUNTRY):
            raise InvalidArgumentError("shipping address cannot be empty")

        shipping_address = Address(
                address.get(Keys.HOUSE_NUMBER), 
                address.get(Keys.STREET_NAME),
                address.get(Keys.CITY),
                address.get(Keys.POST_CODE),
                address.get(Keys.COUNTRY)
            )

        order.AddShippingAddress(address)

    except InvalidArgumentError as e:
        raise e 
    except Exception as e:
        print(f"Exception {e}")
        raise Exception("An unexpected error occured")

