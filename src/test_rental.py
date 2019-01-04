from .rental import HourRental, DayRental, WeekRental, PurchasedRental


def test_hour():
    instance = HourRental()
    assert instance.detail.price == 5
    assert instance.detail.total_expense(2) == 10


def test_day():
    instance = DayRental()
    assert instance.detail.price == 20
    assert instance.detail.total_expense(2) == 40


def test_week():
    instance = WeekRental()
    assert instance.detail.price == 60
    assert instance.detail.total_expense(2) == 120


def test_purchased_rental():
    instance = PurchasedRental(WeekRental(), 1)
    assert isinstance(instance.time, int)
    assert isinstance(instance.rental_type, WeekRental)
