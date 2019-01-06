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
    def get_promotion_discount(self):
        """
        Applies the discount
        :return: float
        """
        pass


"""
Family Rental promotion implementing
Promotion's interface
"""
class FamilyRental(Promotion):
    def __init__(self, rental_list):
        self.rental_list = sorted(rental_list, key=lambda rental: rental.get_total_cost(), reverse=True)
        self.promotion_list = None
        self.no_promotion_list = None
        self.lower_limit = 3
        self.upper_limit = 5
        self.discount = 30
        self.rentals_quantity = len(rental_list)

    def _split_promotion(self):
        amount = self.rentals_quantity if self.rentals_quantity < self.upper_limit else self.upper_limit
        self.promotion_list, self.no_promotion_list = self.rental_list[:amount], self.rental_list[amount:]

    def check_promotion_applies(self):
        return self.rentals_quantity >= self.lower_limit

    def get_promotion_discount(self):
        self._split_promotion()

        total_promotion_list = sum( [rental.get_total_cost() for rental in self.promotion_list] )
        total_no_promotion_list = sum( [rental.get_total_cost() for rental in self.no_promotion_list] )
        discount = (total_promotion_list / 100) * self.discount
        return (total_promotion_list - discount) + total_no_promotion_list

