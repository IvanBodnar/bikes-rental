from .account import Account
from .rental import HourRental, PurchasedRental
from .promotions import FamilyRental


def test_add_rental():
    account = Account()
    account.add_rental(PurchasedRental(HourRental(), 1))
    assert len(account.rentals) == 1


def test_add_promotion():
    account = Account()
    account.add_rental(PurchasedRental(HourRental(), 2))
    account.add_promotion(FamilyRental)
    assert account.promotion is FamilyRental


def test_get_total():
    account = Account()
    account.add_rental(PurchasedRental(HourRental(), 1))
    assert account._get_total() == 5


def test_check_promotion():
    account = Account()
    account.add_rental(PurchasedRental(HourRental(), 1))
    account.add_rental(PurchasedRental(HourRental(), 1))
    account.add_rental(PurchasedRental(HourRental(), 1))
    account.add_promotion(FamilyRental)
    assert account.check_promotion()

    account1 = Account()
    account1.add_rental(PurchasedRental(HourRental(), 1))
    account1.add_rental(PurchasedRental(HourRental(), 1))
    account1.add_promotion(FamilyRental)
    assert not account1.check_promotion()

    account2 = Account()
    account2.add_rental(PurchasedRental(HourRental(), 1))
    account2.add_rental(PurchasedRental(HourRental(), 1))
    account2.add_rental(PurchasedRental(HourRental(), 1))
    account2.add_rental(PurchasedRental(HourRental(), 1))
    account2.add_rental(PurchasedRental(HourRental(), 1))
    account2.add_rental(PurchasedRental(HourRental(), 1))
    account2.add_promotion(FamilyRental)
    assert not account1.check_promotion()


def test_get_total_cost():
    account = Account()
    account.add_rental(PurchasedRental(HourRental(), 1))
    account.add_rental(PurchasedRental(HourRental(), 1))
    account.add_rental(PurchasedRental(HourRental(), 1))
    assert account.get_total_cost() == 15

    account1 = Account()
    account1.add_rental(PurchasedRental(HourRental(), 1))
    account1.add_rental(PurchasedRental(HourRental(), 1))
    account1.add_rental(PurchasedRental(HourRental(), 1))
    account1.add_promotion(FamilyRental)
    assert account1.get_total_cost() == 10.5

