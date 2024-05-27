from price import Price

class Item:
    def __init__(self, id: str, product_code: str, name: str, description: str, image_url: str, price: int, currency: str):

        # we're probably okay if the item description and image url are not available. 

        if not id:
            raise InvalidArgumentError("item id cannot be empty")

        if not name:
            raise InvalidArgumentError("item name cannot be empty")

        if not product_code:
            raise InvalidArgumentError("product code cannot be empty")

        if not price or not currency:
            raise InvalidArgumentError("price and currency cannot be empty")

        self.id = id
        self.product_code = product_code
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = Price(value=price, currency=currency)
