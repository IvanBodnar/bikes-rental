
class Rental:
    def __init__(self, price):
        self.price = price

    def total_expense(self, time_units):
        return self.price * time_units
