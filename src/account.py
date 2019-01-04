
"""
This class represents a client's account.
It holds the rentals purchased by the client,
and a promotion can be also added.
"""
class Account:
    def __init__(self):
        self.rentals = []
        self.promotion = None

    def add_rental(self, rental_instance):
        """
        Add a rental instance
        :param rental_instance: PurchasedRental
        :return: void
        """
        self.rentals.append(rental_instance)

    def add_promotion(self, promotion_class):
        """
        Add a promotion (only one is supported)
        :param promotion_class: Promotion
        :return: void
        """
        self.promotion = promotion_class

    def _get_total(self):
        """
        Get the sum of the total cost of
        each rental
        :return: int
        """
        return sum([rental.get_total_cost() for rental in self.rentals])

    def _check_promotion(self):
        """
        Check if there's a promotion added.
        If there's one, check if it's applicable
        :return: bool
        """
        if self.promotion:
            promotion = self.promotion(self.rentals)
            return promotion.check_promotion_applies()
        return False

    def _apply_promotion(self, total_cost):
        """
        If there's a promotion, apply it
        to the total cost and return the result
        :param total_cost: int
        :return: int
        """
        if self.promotion:
            promotion = self.promotion(self.rentals)
            return promotion.get_promotion_discount(total_cost)
        return total_cost

    def get_total_cost(self):
        """
        Return the total cost
        :return: int
        """
        if self._check_promotion():
            return self._apply_promotion(self._get_total())
        return self._get_total()
