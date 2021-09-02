class Currency:

    def __init__(self, code: str, name: str, value_in_dollar: float):
        self.code = code
        self.name = name
        self.value_in_dollar = value_in_dollar

    def __str__(self):
        return self.name
