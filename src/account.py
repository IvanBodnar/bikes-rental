
class Account:
    def __init__(self):
        self.rentals = []
        self.promotion = None

    def add_rental(self, rental_instance):
        self.rentals.append(rental_instance)

    def add_promotion(self, promotion_class):
        self.promotion = promotion_class

    def _get_total(self):
        return sum([rental.get_total_cost() for rental in self.rentals])

    def check_promotion(self):
        if self.promotion:
            promotion = self.promotion(self.rentals)
            return promotion.check_promotion_applies()
        return False

    def apply_promotion(self, total_cost):
        if self.promotion:
            promotion = self.promotion(self.rentals)
            return promotion.get_promotion_discount(total_cost)
        return total_cost

    def get_total_cost(self):
        if self.check_promotion():
            return self.apply_promotion(self._get_total())
        return self._get_total()

