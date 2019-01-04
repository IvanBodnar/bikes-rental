from abc import ABC, abstractmethod


"""
This abstract class defines the 
interface that every specific promotion
must implement to interact with an Account
instance.
"""
class Promotion(ABC):
    @abstractmethod
    def check_promotion_applies(self):
        """
        Checks that the number of promotions is
        inside the range to qualify for this promotion
        :return: bool
        """
        pass

    @abstractmethod
    def get_promotion_discount(self, total_price):
        """
        Applies the discount to the total_price
        :param total_price: int
        :return: float
        """
        pass


"""
Family Rental promotion implementing
Promotion's interface
"""
class FamilyRental(Promotion):
    def __init__(self, rental_list):
        self.rental_list = rental_list
        self.rentals_quantity = len(rental_list)

    def check_promotion_applies(self):
        return 3 <= self.rentals_quantity <= 5

    def get_promotion_discount(self, total_price):
        discount = (total_price / 100) * 30
        return total_price - discount

