
class Account:
    def __init__(self):
        self.rentals = []

    def add_rental(self, rental_instance):
        self.rentals.append(rental_instance)
