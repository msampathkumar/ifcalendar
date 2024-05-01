IFC or Internaltional Fixed Calendar for Yearly Reports by Monthly
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

How to Usage
============

To install `ifcalender` using PIP

```python
pip install -U ifcalendar
```

How to use in your ML/Data Science Project

```python
>>> import ifcalendar
>>> 
>>> t = ifcalendar.IFCDate(123, 2020) # passing (year_day, year)
>>> print(t)
Wed 11 JUN 2020
>>> t.day
11
>>> t.month
5
>>> print(t.day, t.week, t.week_day, t.month, t.month_name, t.year)
11 17 Wed 5 JUN 2020
```

Developer Setup
===============

**System Requirement:**
1. Python3
2. `git pull`

For a developer setup, run following command from your Mac/Ubuntu system

    make all

This will do following tasks for you
 
1. Setup a virtual environment
2. Install developer dependencies
3. Run nose tests 

**Code Development, Helper Sites**

-  https://github.com/msampathkumar/ifcalendar
-  https://pandoc.org/

**Future Improvements**

- [Done] Packaging: https://packaging.python.org/
- [WIP] Nose TestCases
- [] Pandas/Numpy Support
- [] Matplotlib, Seaborn Examples

Use https://github.com/msampathkumar/ifcalendar/projects to know on our progress on bugs & lastest features we are working on.

LICENCE
=======

MIT License
