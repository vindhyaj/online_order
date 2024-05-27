import pycountry
from errors import InvalidArgumentError

class Address:
    def __init__(self, house_numer: str, street_name: str, city: str, post_code: str, country: str):

        if not street_name or not city or not post_code or not country:
            raise InvalidArgumentError("street_name, city, post_code & country cannot be empty")
            
        self.house_numer = house_numer
        self.street_name = street_name
        self.city = city
        self.post_code = post_code
        self.country = pycountry.countries.search_fuzzy(country)
