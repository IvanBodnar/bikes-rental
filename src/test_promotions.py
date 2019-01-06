from .promotions import FamilyRental
from .rental import PurchasedRental, HourRental, DayRental, WeekRental

rentals_2 = [
    PurchasedRental(DayRental(), 1),
    PurchasedRental(WeekRental(), 1)
]

rentals_3 = [
    PurchasedRental(DayRental(), 1),
    PurchasedRental(WeekRental(), 1),
    PurchasedRental(HourRental(), 1)
]

rentals_5 = rentals_3 + [
    PurchasedRental(WeekRental(), 1),
    PurchasedRental(HourRental(), 1)
]

rentals_7 = rentals_5 + [
    PurchasedRental(WeekRental(), 1),
    PurchasedRental(DayRental(), 1)
]


def test_split_promotion():
    promo = FamilyRental(rentals_3)
    promo._split_promotion()
    assert len(promo.promotion_list) == 3

    promo = FamilyRental(rentals_5)
    promo._split_promotion()
    assert len(promo.promotion_list) == 5

    promo = FamilyRental(rentals_7)
    promo._split_promotion()
    assert len(promo.promotion_list) == 5
    assert len(promo.no_promotion_list) == 2


def test_check_promotion_applies():
    assert FamilyRental(rentals_3).check_promotion_applies()
    assert FamilyRental(rentals_5).check_promotion_applies()
    assert FamilyRental(rentals_7).check_promotion_applies()
    assert not FamilyRental(rentals_2).check_promotion_applies()


def test_get_promotion_discount():
    promo = FamilyRental(rentals_3)
    assert promo.get_promotion_discount() == 59.5

    promo = FamilyRental(rentals_5)
    assert promo.get_promotion_discount() == 105.0

    promo = FamilyRental(rentals_7)
    assert promo.get_promotion_discount() == 164.0

