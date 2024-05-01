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
