from .promotions import FamilyRental
from .rental import PurchasedRental, HourRental


class Account:
    def __init__(self):
        self.rentals = []

    def add_rental(self, rental_instance):
        self.rentals.append(rental_instance)

    def get_total_usage(self):
        return sum([rental.get_total_cost() for rental in self.rentals])

    def check_promotion(self, promotion_instance):
        promotion = promotion_instance()
        return promotion.check_promotion_applies(self.rentals)
