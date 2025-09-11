+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Thin or Harvest : Plant Removal and Replacement**

\[[Event Window](137_Event%20Window.htm) : *Thin* panel : *Tree/Plant
removal and replacement* section\]

Specify how the [Thin](140_Thin.htm) or [Harvest](153_Harvest.htm)
affects the average age of the plants.

**Introduction**

In this topic:

  ---------- -- --------------------------------------------------------
  Thins         \"Plants\" are trees; the \"event\" is a thin
  Harvests      \"Plants\" are crop plants; the \"event\" is a harvest
  ---------- -- --------------------------------------------------------

The only effect of this section is to specify how the average age of the
plants changes due to the event. By specifying the average age of the
plants that are removed from the plot, and whether or not new plants
spring up to replace them, you can control the change in the average age
of the plants.

This is only of interest if you are using the average age of the plants
to determine relative allocations or growth (see the [Growth
Properties](42_Growth%20Properties.htm) windows), in which case you can
control how the event moves the plants along their growth curves.

These settings are only relevant (and thus enabled) for thinnings that
leave some stems or stalks (that is, the fraction of plants removed is
less than 100%).

**Default Setting**

Most people will want the default setting:

1.0 in the top box\
0.0 in the middle\
0.0 in the bottom box,\
Do not check the *Replace removed plants\...* box.

Under this setting:

- The average age of the removed plants is equal to the average age of
  the existing plants
- The average age of the plants on the plot is not changed by the event
- No new plants grow to replace the removed plants.

**Removal-Age Formula**

Specify the average age (in years) of the plants that are removed by the
event by specifying the three coefficients in a formula:

1.  The multiplier for the current average age of the plants (*A*)
2.  The multiplier for the age of the oldest plants in the forest or
    crop (*B*)
3.  An additive constant, in years. (*C*)

The average age of the removed plants is

> *A* \* (average age of plants) + *B* \* (age of oldest plants) + *C*.

If this average age is less than zero it is changed to zero; if it is
greater than the age of the oldest plants it is changed to the age of
the oldest plants.

**Example 1**. If *A* = 0, *B* = 0, *C* = 15 then the average age of the
removed plants is 15 years. So if the average age of the plants at the
time of the event was 10 years, then the average age of the removed
plants would be 15 years. So if 50% of the stems or stalks were removed
and there was no replacement, then the average age of the plants after
the event would be 5 years.

**Example 2**. If *A* = 1.2, *B* = 0, *C* = --0.5 then the average age
of the removed plants is 20% greater than the average age of plants
(before the event) less half a year. So if the average age of the plants
at the time of the event was 10 years, then the average age of the
removed plants would be 1.2 \* 10 -- 0.5 = 11.5 years. So if 50% of the
stems or stalks were removed without replacement then the average age of
the plants after the event would be 8.5 years.

The average age of the removed plants is only used to calculate the
average age of the remaining plants. It is your responsibility to
specify the average age of the removed plants sensibly. If the average
age of the plants after the event is greater than the age of the oldest
plants then it is changed to the age of the oldest plants.

The age of the oldest plants is not affected by the event --- it is only
altered by planting or clearing events, and the passage of time.

**Replacement**

Check the *Replace removed plants with new plants (of age 0)* box if you
want new plants to grow spontaneously, starting from age zero at the
time of the event and without a planting event, in the spaces left
behind by the removed plants.

Checking this box is appropriate for a native forest, but usually not
appropriate for a plantation forest. If the thinned trees were
intermingled through the forest, the non-thinned trees may bulk up to
fill the space previously occupied by the thinned trees (so consider a
forest treatment event that lowers the effective age of the trees). If
the thinned trees all come from the same portion of the plot and that
portion is completely cleared by the thin, then it would be better to
model the forest with an [Estate
Simulation](72_Estate%20Simulation.htm), using multiple plot files to
reflect the different management, rather than as a single plot file.

**Coppices**

If there are no stems or stalks left after the event yet the event is
not a clearing event (so the affected portion is 100% but the sum of the
destination percentages for at least one pool is less than 100%), then
the average age of the plants is not changed by the event (thus, you can
create coppices).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
