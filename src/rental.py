
"""
Main class for rental type. Used to
compose the specific types of rentals
"""
class Rental:

    def __init__(self, price):
        """
        Price established for the rental
        :param price: int
        """
        self.price = price

    def total_expense(self, time_units):
        """
        Calculates the cost of a rental
        based on the time consumed. The
        unit of time varies according the type
        of rental (hour, day, week)
        :param time_units: int
        :return: int
        """
        return self.price * time_units


"""
Kinds of rentals
"""
class HourRental:
    def __init__(self):
        self.detail = Rental(5)


class DayRental:
    def __init__(self):
        self.detail = Rental(20)


class WeekRental:
    def __init__(self):
        self.detail = Rental(60)


"""
Specific rental: this is the class that 
is used to represent a specific rental.
It's instantiated with the type of rental + 
the time the rental lasted.
"""
class PurchasedRental:
    def __init__(self, rental_type_instance, time):
        self.rental_type = rental_type_instance
        self.time = time

    def get_total_cost(self):
        """
        Get the total cost of the rental
        :return: int
        """
        return self.rental_type.detail.total_expense(self.time)
