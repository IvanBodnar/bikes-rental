from .account import Account
from .rental import HourRental, PurchasedRental


class TestAccount:
    account = Account()

    def test_add_rental(self):
        TestAccount.account.add_rental(PurchasedRental(HourRental(), 1))
        assert len(TestAccount.account.rentals) == 1

    def test_get_total_usage(self):
        TestAccount.account.add_rental(PurchasedRental(HourRental(), 1))
        assert TestAccount.account.get_total_usage() == 10

