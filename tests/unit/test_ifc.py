import sure
import unittest
from ifcalendar import ifc as _ifc


class TestGlobalVars(unittest.TestCase):
    def test_months_count(self):
        _ifc.MONTHS.should.be.a(list)
        _ifc.MAX_MONTH.should.be.a(int)
        self.assertEqual(_ifc.MAX_MONTH, len(_ifc.MONTHS))

    def test_four_weeks_month(self):
        _ifc.MAX_DAYS.should.be.a(int)
        _ifc.WEEKDAYS.should.be.a(list)
        self.assertEqual(len(_ifc.WEEKDAYS) * 4, _ifc.MAX_DAYS)


class TestGetDay(unittest.TestCase):
    def test_get_day_leap_year(self):
        # Test leap year
        self.assertEqual(_ifc.get_day(1, True), 1)
        self.assertEqual(_ifc.get_day(28, True), 28)
        self.assertEqual(_ifc.get_day(168, True), 28)
        self.assertEqual(_ifc.get_day(169, True), 29)
        self.assertEqual(_ifc.get_day(170, True), 1)
        self.assertEqual(_ifc.get_day(364, True), 27)
        self.assertEqual(_ifc.get_day(365, True), 28)
        self.assertEqual(_ifc.get_day(366, True), 29)

    def test_get_day_non_leap_year(self):
        # Test non-leap year
        self.assertEqual(_ifc.get_day(1, False), 1)
        self.assertEqual(_ifc.get_day(28, False), 28)
        self.assertEqual(_ifc.get_day(168, False), 28)
        self.assertEqual(_ifc.get_day(169, False), 1)
        self.assertEqual(_ifc.get_day(364, False), 28)
        self.assertEqual(_ifc.get_day(365, False), 29)


class TestGetMonth(unittest.TestCase):
    def test_get_month_leap_year(self):
        # Test leap year
        self.assertEqual(_ifc.get_month(1, True), 1)
        self.assertEqual(_ifc.get_month(28, True), 1)
        self.assertEqual(_ifc.get_month(168, True), 6)
        self.assertEqual(_ifc.get_month(169, True), 6)
        self.assertEqual(_ifc.get_month(170, True), 7)
        self.assertEqual(_ifc.get_month(364, True), 13)
        self.assertEqual(_ifc.get_month(365, True), 13)
        self.assertEqual(_ifc.get_month(366, True), 13)

    def test_get_month_non_leap_year(self):
        # Test non-leap year
        self.assertEqual(_ifc.get_month(1, False), 1)
        self.assertEqual(_ifc.get_month(28, False), 1)
        self.assertEqual(_ifc.get_month(168, False), 6)
        self.assertEqual(_ifc.get_month(169, False), 7)
        self.assertEqual(_ifc.get_month(364, False), 13)
        self.assertEqual(_ifc.get_month(365, False), 13)
