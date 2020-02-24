"""
International Fixed Calander or Cotsworth Calender is a 13 month fixed calender.
"""

# https://github.com/python/cpython/blob/master/Lib/datetime.py

from datetime import datetime as _datetime

MAX_MONTH = 13
MAX_DAYS = 28

MONTHS = '''
January
February
March
April
May
June
Sol
July
Augest
September
October
November
December
'''.strip().splitlines()

WEEKDAYS = '''
Sun
Mon
Tue
Wed
Thu
Fri
Sat
'''.strip().splitlines()


def ifc_now():
    tt = _datetime.now()
    return IFCDate(tt.timetuple().tm_yday, tt.year)


def leap_year(year):
    if (year % 4) == 0:
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False

        return True
    else:
        return False


def get_week_ct(day):
    return day // 7


def get_day_of_week(day):
    return day % 7 - 1


def get_week_day(day):
    return WEEKDAYS[day % 7 - 1]


def get_month_name(mon_ct):
    return MONTHS[mon_ct - 1][:3].upper()


def get_month_and_day(day_ct):
    if not (0 < day_ct < 367):
        raise Exception("DayCount is not between 0 and 366")

    if day_ct == 365 or day_ct == 366:
        return 13, 29

    mon, day = divmod(day_ct, MAX_DAYS)
    if day == 0 & mon != 13:
        return mon, day

    return mon + 1, day


def get_day(day_ct):
    if not (0 < day_ct < 367):
        raise Exception("DayCount is not between 0 and 366")

    rem = (day_ct % MAX_DAYS)
    if rem == 0:
        return MAX_DAYS
    else:
        return rem


def to_ifc(obj_datetime):
    if not obj_datetime.__class__ == _datetime:
        raise Exception('Expected `datetime` class object received `{}`'.format(obj_datetime.__class__))
    time_tuple = obj_datetime.timetuple()
    return CotsDate(time_tuple.tm_yday, time_tuple.tm_year)


class CotsDate:
    def __init__(self, dayofyear, year):
        self._dayofyear = dayofyear
        self._year = year

    def get_month_id(self):
        return get_month_and_day(self._dayofyear)[0]

    def get_month_name(self):
        return get_month_name(self.month)

    def get_week_id(self):
        return get_week_ct(self._dayofyear)

    def get_week_day(self):
        return get_week_day(self._dayofyear)

    def get_year(self):
        return self._year

    def get_day(self):
        return get_day(self._year_day_count)

    def __repr__(self):
        return '{} {} {} {}'.format(self.week_day, self.day, self.month_name, self.year)

    day = property(get_day)
    week = property(get_week_id)
    week_day = property(get_week_day)
    month = property(get_month_id)
    month_name = property(get_month_name)
    year = property(get_year)


def print_year():
    for i in range(1, 367):
        t = CotsDate(i, 2020)
        print(t.day, t.week, t.week_day, t.month, t.month_name, t.year)


IFCDate = CotsDate
