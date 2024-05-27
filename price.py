class Price:
    def __init__(self, value: int, currency: str):
        if not currency:
            raise InvalidArgumentError("currency cannot be empty")

        self.value = value
        self.currency = currency