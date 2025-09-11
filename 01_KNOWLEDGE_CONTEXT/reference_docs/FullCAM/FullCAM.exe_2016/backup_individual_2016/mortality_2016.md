---
title: Mortality
version: 2016
category: Plant Properties
original_file: 121_Mortality_2016.md
---

[Plant Properties window : *Mortality*
section]

Specify mortality rates for the plant species.

**Introduction**

Specify what percentage of plants die, what percentage of the plant
components die, and the average age of the plants that die. By
specifying the average age of the plants that die, and whether or not
new plants replace them, you can control the change in the average age
of the plants. This is only of interest if you are using the average age
of the plants to determine relative allocations or growth (see the
Growth Properties window), in which case
you can control how mortality moves the plants along their growth
curves.

Plant mass that "dies due to mortality" becomes turnover and is treated
in all ways as turnover, except that mortality mass is added to turnover
after yield-versus-production has been determined. (Yield measurements
do include the effects of regular turnover, but do not include the
effects of mortality or site biomass limits.)

**Stem or Stalk Loss**

Specify the percentages of the plants that die each year in the Stem
Loss and Stalk Loss
time-series.

**Ratios of Component Losses to Stem Loss**

When a given percentage of the stems or stalks die, the percentages of
other plant components on the plot that die may be different. Specify
these differences in the "Ratio..." fields. For example, if the *ratio
of leaf loss to stem loss* is 0.3 and 2% of the tree stems die in a
given year, then the percentage of leaves on the plot that are lost is
only 2% * 0.3 = 0.6% (perhaps the trees close to death have fewer
leaves than the other trees?)

**Effect on Average Age of Plants**

Specify the average age (in years) of the plants that die by specifying
the three coefficients in a formula:

1.  The multiplier for the current average age of the plants (A)
2.  The multiplier for the age of the oldest plants in the forest or
    crop (B)
3.  An additive constant, in years (C)

The average age of plants that die is

> A * (average age of plants) + B * (age of oldest plants) + C.

If this average age is less than zero or greater than the age of the
oldest plants, no plant mortality occurs (that is, no plants die in that
step due to "mortality"). This feature allows you to specify, for
example,

- a constant age of death
- a constant mortality in the Stem Loss or Stalk Loss time-series and
  mortality losses will not start until the oldest plants reach the
  specified average age of death.

**Example 1**. If A = 0, B = 0, C = 50 then the average age of the dying
plants is 50 years. Thus there is no plant loss due to mortality unless
the age of the oldest plant exceeds 50 years. If the age of the oldest
plants is over 50, and the average age of the plants is 40 years and 10%
of the plants die, then the average age of the plants that die is 50
years and the average age after mortality is 38.89 years (assuming no
replacement).

**Example 2**. If A = 1.2, B = 0, C = --3 then the average age of the
dying plants is 20% greater than the average age of plants (before the
mortality is taken into account) less three years. So if the average age
of the plants was 10 years, then the average age of the dying plants
would be 1.2 * 10 -- 3 = 9 years.

The average age of the dying plants is only used to calculate the
average age of the remaining plants. It is your responsibility to
specify the average age of the dying plants sensibly, and so that it
interacts properly with the times or ages in the Stem Loss or Stalk Loss
time-series. If the average age of the plants after mortality is applied
is greater than the age of the oldest plants then it is changed to the
age of the oldest plants.

The age of the oldest plants is not affected by mortality --- it is only
altered by planting or clearing events, and the passage of time.

**Replacement**

Check the "Replace dying trees" or "Replace dying plants" field if you
want new plants to start up from age 0 in the spaces left behind by the
dead plants. The only effect of this choice is on the average age of the
forest or crop. In a plantation you will usually not check this field
(as established trees will expand to fill the space of the dying
(removed) trees, intermingled with the retained trees). In a native
forest, however, you should check this field (because there is usually a
constant regeneration of trees).