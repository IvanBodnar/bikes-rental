from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def check_promotion_applies(self):
        pass

    @abstractmethod
    def get_promotion_discount(self, total_price):
        pass


class FamilyRental(Promotion):
    def __init__(self, rental_list):
        self.rental_list = rental_list
        self.rentals_quantity = len(rental_list)

    def check_promotion_applies(self):
        return 3 <= self.rentals_quantity <= 5

    def get_promotion_discount(self, total_price):
        discount = (total_price / 100) * 30
        return total_price - discount

