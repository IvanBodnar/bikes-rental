from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def check_promotion_applies(self, rental_list):
        pass

    @abstractmethod
    def get_promotion_discount(self, rental_list):
        pass


class FamilyRental(Promotion):
    def __init__(self, rental_list):
        self.rental_list = rental_list
        self.rentals_quantity = len(rental_list)

    def check_promotion_applies(self, rental_list):
        return 3 <= self.rentals_quantity <= 5

    def get_promotion_discount(self, rental_list):
        pass

