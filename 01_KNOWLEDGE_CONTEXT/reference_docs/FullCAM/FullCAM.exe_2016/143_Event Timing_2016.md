+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Event Timing**

\[[Event Window](137_Event%20Window.htm) (via the
[Events](136_Events.htm) page): *Timing* panel\]

Enter timing information for the event.

**"Simulate" Checkbox**

The *Simulate* checkbox specifies whether or not the event is to be
simulated. Uncheck this box to effectively turn the event off --- it
will still be on the event queue, but it will not be simulated (it will
have no effect on a simulation). This is useful for temporarily
suspending an event from the simulation.

The *Simulate* checkbox may be checked or unchecked on the [Event
Window](137_Event%20Window.htm), or on the [Events](136_Events.htm) page
by the secondary mouse button and selecting either *Simulate Events* or
*Do Not Simulate Events*.

**Type and Time**

Specify the event time, as either a:

1\. Calendar date\
Examples: 1 Jan 2001, 31 Dec 2010.

Enter the date in any unambiguous way, such as \"4 Sep 2010\", \"s4\",
\"au9 1999\", \"4s2000\", \"8/4/0\" or \"8.4.1999\", except that you
cannot use hyphens because they are interpreted as negative signs (for
example 8 4 -35 is 8 Apr -35).

2\. Calandar years and days since the start of the simulation\
Example: -10, 0, 2345.

A calendar year is from a date in one year to the same date in the next
year, and can contain either 365 or 366 days depending on leap years.
The number of days can also be huge. So if you mean the same date in two
years time, set the calendar years equal to two and the days to zero,
but if you mean exactly 730 days then set the calendar years to zero and
the days to 730.

Go back and forth between the date types to see how they compare -
changes in one are reflected in the other, that is, they both show the
same date.

An event always occurs at noon of the day on which it is specified to
occur, even if that time is in the middle of a simulation step. FullCAM
computes the continuous processes for the partial step up to the event,
executes the event, then computes the continuous processes up to the
next event or the end of the step.

Each event occurs instantaneously --- it begins and ends at noon of the
same day.

Event timing may be updated for multiple events by multi-selecting the
events on the Event List, and then selecting the right mouse option
*Apply Offset to Events*. The timing may then be updated by the [Event
Update](248_Event%20Update.htm) dialog.

**Add Days**

A offset may be applied to an event by entering a value in the *Days*
field and clicking *Add Days* button. This can be either positive or
negative and will move the event that number of days forward or back in
the event queue.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
