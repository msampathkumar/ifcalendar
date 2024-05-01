Timeline charts have always been center of many statistical analysis and
report. In many timeline based statistical analysis, generating reports
by month or week is a common practice. But the standard everyday
Calendar or Georgian Calendar is used which comes with few challenges
that influence business decisions.

For example, lets say an entertainment industry, generates majority
sales on saturday and sunday than rest of the weeks. Now lets look at
following calender of 2019. For the sake of understanding, lets say we
generate 0.1 \$ Million for Sunday and Saturday

```
                            2019
      January               February               March
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
       1  2  3  4  5                  1  2                  1  2
 6  7  8  9 10 11 12   3  4  5  6  7  8  9   3  4  5  6  7  8  9
13 14 15 16 17 18 19  10 11 12 13 14 15 16  10 11 12 13 14 15 16
20 21 22 23 24 25 26  17 18 19 20 21 22 23  17 18 19 20 21 22 23
27 28 29 30 31        24 25 26 27 28        24 25 26 27 28 29 30
                                            31
```

A simple statistical report would look like following

|S.No | Month  |  EstimatedProfit<br>(inMillion)  | Difference(%) |
|:---:|:------:|:--------------------------------:|:-------------:|
|  1  |  Jan   |               0.8                |       0       |
|  2  |  Feb   |               0.8                |       0       |
|  3  |  Mar   |               1.0                |      25       |

Based on above report one would easily assume that there is 25% growth
in sales. But, the increase in growth due to increase in Profit days not
necessarily due to improvement in sales.

When we add count of Saturday and Sunday, the report would look like,.



As you can see, these differences will becomes significant for business
planning and in statical projection of numbers(profits).

International Fixed Calendar(IFC) solves these challenges by having
fixed days in months. In IFC, along with 12 months in Georgian we add
SOL month making it a 13 month Calendar with 4 weeks each.

    13 Months * 4 Weeks =  13 Months * 24 Days = 364 Days

As for IFC, 1 extra day is added December as Dec 29 making it 365 days
calendar. For leap years, the International Fixed Calendar inserts the
extra day in leap year as June 29 - between Saturday June 28 and Sunday
Sol 1.


| S.No  | Month  | Count of<br>Sat&Sun | Estimated Profit<br>(inMillion) | Difference(%) |
|:-----:|:------:|:-------------------:|:-------------------------------:|:-------------:|
|   1   |  Jan   |          8          |               0.8               |       0       |
|   2   |  Feb   |          8          |               0.8               |       0       |
|   3   |  Mar   |         10          |               1.0               |      25       |

But when we use IFC calendar, the same initial report would look like below



| S.No  | Month  | Count of<br>Sat&Sun | Estimated Profit<br>(inMillion) | Difference(%) |
|:-----:|:------:|:-------------------:|:-------------------------------:|:-------------:|
|   1   |  Jan   |          8          |               0.8               |       0       |
|   2   |  Feb   |          8          |               0.8               |       0       |
|   3   |  Mar   |          8          |               0.8               |       0       |


**Notable Statistical Advantages**

-   Every month has exactly 4 weeks
    -   8 Saturday & 8 Sundays
-   Every month starts with Sunday
-   Every month 1 is Sunday and 7 is Saturday and so on all 28 days

Although it has several advantages, for everyday practical uses of this calendar has some interesting disadvantages related to holidays dates or extra day of year or the number 13 is a prime and so.on.

Looking at benifits of IFC, in this package we offer required tools to convert Georgian dates to IFC.

For a deeper understanding we suggest you to go to [Wikipedia](https://en.wikipedia.org/wiki/International_Fixed_Calendar).

_Disclaimer:_ This package is developed for educational, experimental and enrichment of statistical analysis purposes only.
 

 