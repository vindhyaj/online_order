from price import Price

class Item:
    def __init__(self, id: str, product_code: str, name: str, description: str, image_url: str, price: int, currency: str):
        self.id = id
        self.product_code = product_code
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = Price(value=value, currency=currency)
