+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Edit Regime Window**

\[*Events* page : Regime *Edit* button\]

This window is for editing an individual Regime.

**Name**

Every Regime needs a (non-blank) name, and the name must be unique
within the regime list.

**Timing**

Specify the regime time, as either:

1.  . Calendar date\
    Examples: 1 Jan 2001, 31 Dec 2010.

    Enter the date in any unambiguous way, such as "4 Sep 2010", "s4",
    "au9 1999", "4s2000", "8/4/0" or "8.4.1999", except that you cannot
    use hyphens because they are interpreted as negative signs (for
    example 8 4 -35 is 8 Apr -35).

2.  Calendar years and days since the start of the simulation\
    Example: -10, 0, 2345.

A calendar year is from a date in one year to the same date in the next
year, and can contain either 365 or 366 days depending on leap years.
For exmplae, to set a two year calendar time period, set the calendar
years equal to two and the days to zero. For exactly 730 days then set
the calendar years to zero and the days to 730.

Changes in one date type are reflected in the other.

An event always occurs at midnight of the day on which it is specified
to occur, even if that time is in the middle of a simulation step.
FullCAM computes the continuous processes for the partial step up to the
event, executes it, then computes the continuous processes up to the
next event or the end of the step.

Each event occurs instantaneously - it begins and ends at midnight of
the same day.

**Add Days**

A offset may be applied to an event by entering a value in the *Days*
field and clicking *Add Days* button. This can be either positive or
negative and will move the event that number of days forward or back in
the event queue.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
