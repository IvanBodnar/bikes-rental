from .promotions import FamilyRental


def test_check_promotion_applies():
    assert FamilyRental([1, 1, 1]).check_promotion_applies()
    assert not FamilyRental([1, 1]).check_promotion_applies()
    assert not FamilyRental([1, 1, 1, 1, 1, 1]).check_promotion_applies()


def test_get_promotion_discount():
    assert FamilyRental([]).get_promotion_discount(10) == 7
