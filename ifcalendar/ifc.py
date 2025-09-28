"""
The International Fixed Calendar (also known as the IFC, Cotsworth plan, the
Cotsworth calendar and the Eastman plan) is a proposed calendar reform designed
by Moses B. Cotsworth, first presented in 1902.[1] The International Fixed Calendar
divides the year into 13 months of 28 days each. A type of perennial calendar,
every date is fixed to the same weekday every year. Though it was never officially
adopted at the country level, the entrepreneur George Eastman instituted its use
at the Eastman Kodak Company in 1928, where it was used until 1989.[2] While it is
sometimes described as the 13-month calendar or the equal-month calendar,
various alternative calendar designs share these features.

Source: https://en.wikipedia.org/wiki/International_Fixed_Calendar

# https://github.com/python/cpython/blob/master/Lib/datetime.py
"""

from datetime import datetime as _datetime


MAX_MONTH = 13
MAX_DAYS = 28
LEAP_DAY = "Sun"
YEAR_DAY = "Sun"

MONTHS = """
January
February
March
April
May
June
Sol
July
August
September
October
November
December
""".strip().splitlines()

WEEKDAYS = """
Sun
Mon
Tue
Wed
Thu
Fri
Sat
""".strip().splitlines()


def ifc_now():
    tt = _datetime.now()
    return IFCDate(tt.timetuple().tm_yday, tt.year)


def leap_year(year):
    if (year % 4) == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False

        return True
    else:
        return False


def get_week_ct(day, is_leap):
    # Neither Year Day nor Leap Day are considered to be part of any week as per IFC
    if is_leap:
        if day == 169:
            return 0
        if day == 366:
            return 0
        if day > 169:
            day = day - 1

    return day // 7


def get_day_of_week(day):
    return day % 7 - 1


def get_week_day(day, is_leap):

    if is_leap:
        if day == 169:
            return LEAP_DAY
        if day == 366:
            return YEAR_DAY
        if day > 169:
            day = day - 1
    else:
        if day == 365:
            return YEAR_DAY

    return WEEKDAYS[day % 7 - 1]


def get_month_name(mon_ct):
    return MONTHS[mon_ct - 1][:3].upper()


def get_month(day_ct, is_leap):
    if not (0 < day_ct < 367):
        raise Exception("DayCount is not between 0 and 366")

    if is_leap:
        if day_ct == 169:  # Leap Day
            return 6
        if day_ct > 169:
            day_ct -= 1

    if day_ct >= 365:  # Year Day
        return 13

    mon, day = divmod(day_ct, MAX_DAYS)
    if day == 0:
        return mon
    return mon + 1


def get_day(day_ct, is_leap):
    if not (0 < day_ct < 367):
        raise Exception("DayCount is not between 0 and 366")

    if is_leap:
        if day_ct == 169:  # Leap Day
            return 29
        if day_ct == 366:  # Year Day
            return 29
        if day_ct > 169:
            day_ct -= 1
    else:
        if day_ct == 365:  # Year Day
            return 29
        if day_ct == 366:
            raise Exception("Not a leap year to exist 366 days")

    rem = day_ct % MAX_DAYS
    if rem == 0:
        return MAX_DAYS
    return rem


def to_ifc(obj_datetime):
    """To convert a datetime.datetime object to IFC date time object.

    Example:
        >>> from datetime import datetime
        >>> to_ifc(datetime.now())
        Tue 10 MAY 2024

        >>> date = to_ifc(datetime.now())
        >>> date.day, date.week, date.week_day, date.month, date.month_name, date.year
        (10, 17, 'Tue', 5, 'MAY', 2024)
    """
    if not obj_datetime.__class__ == _datetime:
        raise Exception(
            "Expected `datetime` class object received `{}`".format(
                obj_datetime.__class__
            )
        )
    time_tuple = obj_datetime.timetuple()
    return IFC(time_tuple.tm_yday, time_tuple.tm_year)


class IFC:
    def __init__(self, day_of_the_year, year):
        self._day_of_the_year = day_of_the_year
        self._year = year
        self.is_leap = leap_year(year)

    def get_month_id(self):
        return get_month(self._day_of_the_year, self.is_leap)

    def get_month_name(self):
        return get_month_name(self.month)

    def get_week_id(self):
        return get_week_ct(self._day_of_the_year, self.is_leap)

    def get_week_day(self):
        return get_week_day(self._day_of_the_year, self.is_leap)

    def get_year(self):
        return self._year

    def get_day(self):
        return get_day(self._day_of_the_year, self.is_leap)

    def __repr__(self):
        return "{} {} {} {}".format(self.week_day, self.day, self.month_name, self.year)

    day = property(get_day)
    week = property(get_week_id)
    week_day = property(get_week_day)
    month = property(get_month_id)
    month_name = property(get_month_name)
    year = property(get_year)


if __name__ == "__main__":

    def print_year():
        for i in range(1, 367):
            t = IFC(day_of_the_year=i, year=2020)
            print(t)

    IFCDate = IFC
    print_year()
