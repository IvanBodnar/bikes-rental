from src import HourRental, DayRental, WeekRental


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

