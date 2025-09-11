---
title: Forest Percentage
version: 2020
category: general
original_file: 206_Forest Percentage_2020.md
---

The forest percentage specifies proportional allocations for a number of
parameters in forest and agricultural systems within a mixed plot (see
Plots, Systems, Layers, and
Pools and Configure
the Plot).

**Introduction**

The concept of the "forest percentage" arises only in a mixed multilayer
plot. A mixed multilayer plot has a multilayer forest system and a
multilayer agricultural system. In such a system, the forest percentage
scales most initial conditions and agricultural behaviour in accordance
with this percentage. For example, if the forest percentage in 30%, then
the agricultural percentage is 70%.

**Definition**

The *forest percentage* is defined as the percentage of the plot covered
by the tree canopy.

For example, a plot with 10 ha of forest and 30 ha of agricultural
system has a forest percentage of 25% (because 10 / 40 = 25% of the plot
is forest).

**Discussion**

The forest percentage is the percentage of the sunlight going to the
trees and not to crop species. In the plot simulator, this requires that
the agricultural activity be limited but that forest growth be
unimpeded. This is because forest systems are calibrated to an endemic
canopy cover for their location where a continuous forest cover
definition applies (>2m in height and >20% canopy cover), but
agricultural systems are calibrated to 100% sunlight. If the forest
fraction is *f* then:

- Tree production (growth) is no different to if the plot were a forest
  plot.
- Crop production (growth) is (1 -- *f* ) times what it would be if the
  plot were wholly agricultural.
- The mass present due to initial conditions in the soil and debris
  layers are scaled down by *f* and (1 - *f*) for forest and
  agricultural systems respectively.

For example, suppose a mixed plot has the forest fraction equal to 30%.
Then the forest growth is the same as what it would be if the whole plot
were forest, but the agricultural growth is limited to 70% of what it
would be if the whole plot were agricultural. The initial soil and
debris levels in the forest system are 30% of what they would be if the
whole plot were forest, and in the agricultural system are 70% of what
they would be if the whole plot were agricultural. No non-growth
processes are affected by the forest percentage.

The forest percentage can vary with time in response to events. Forest
Percentage Change events should
be created when land management practices change alongside other events
giving effect to that change, such as the removal or planting of trees.
If 3PG is in
use, the percentage can also change as the tree canopy grows.
