from .account import Account
from .rental import HourRental, DayRental, WeekRental


def test_add_rental():
    account = Account()
    account.add_rental(HourRental())
    assert len(account.rentals) == 1