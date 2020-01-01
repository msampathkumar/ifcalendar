IFCalendar
==========

The International Fixed Calendar (also known as the Cotsworth plan, the
Eastman plan, the 13 Month calendar or the Equal Month calendar) is a
solar calendar proposal for calendar reform designed by Moses B.
Cotsworth, who presented it in 1902. It divides the solar year into 13
months of 28 days each. It is therefore a perennial calendar, with every
date fixed to the same weekday every year.

Advantage
=========

In most time based statistical analysis, generating reports by month or
week is a common practice. But the standard Georgian Calendar Months,
have differences in each month and following concerns.

-  Days count in a month can be 28 or 31
-  Sundays & Saturdays count varies
-  Dates & weekdays have no alignments

In IFC, the total day counts in a month is fixed. There are standard
four weeks in a month and 13 months a year which makes for 365 days. In
Leap year, 13 th months will be having 29 day.

Usage
=====

::

   >>> import ifcalendar
   >>> 
   >>> t = ifcalendar.IFCDate(123, 2020)
   >>> print(t)
   Wed 11 JUN 2020
   >>> t.day
   11
   >>> t.month
   5
   >>> print(t.day, t.week, t.week_day, t.month, t.month_name, t.year)
   11 17 Wed 5 JUN 2020

**Code Development, Helper Sites**

-  https://github.com/msampathkumar/ifcalendar
-  https://pandoc.org/

**Future Improvements**

-  Packaging: https://packaging.python.org/
-  Nose TestCases
-  Pandas/Numpy Support
-  Matplotlib, Seaborn Examples