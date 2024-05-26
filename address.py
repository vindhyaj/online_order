from pycountrycodes import countries

class Address:
    def __init__(self, house_numer: str, street_name: str, city: str, post_code: str, country: str)
        self.house_numer = house_numer
        self.street_name = street_name
        self.city = city
        self.post_code = post_code
        self.country = countries.get(name=country)
