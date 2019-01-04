
class Rental:
    def __init__(self, price):
        self.price = price

    def total_expense(self, time_units):
        return self.price * time_units


class HourRental:
    def __init__(self):
        self.detail = Rental(5)


class DayRental:
    def __init__(self):
        self.detail = Rental(20)


class WeekRental:
    def __init__(self):
        self.detail = Rental(60)


class PurchasedRental:
    def __init__(self, rental_type_instance, time):
        self.rental_type = rental_type_instance
        self.time = time

    def get_total_cost(self):
        return self.rental_type.detail.total_expense(self.time)
