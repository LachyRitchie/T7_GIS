---
title: "Processes and Events"
version: 2020
category: Events
original_file: 58_Processes and Events_2020.md
---

This topic provides a broad overview of the more common actions that are
simulated in FullCAM.

**Processes**

A *process* is an action that occurs continuously. The main processes
included in the various layers are:

Plant Processes

Production

Moves carbon from the atmosphere to the plant pools. Production is the
combination of photosynthesis, which moves carbon from the atmosphere to
the plant pools, and respiration, which moves a lesser amount of
material in the opposite direction. The net result represents plant
growth.

*Turnover*

Moves material from a plant pool to a debris pool as the material dies.

*Grazing*

Moves material from the crops (via animals) to animal products, soil,
and the atmosphere.

Debris Processes

Breakdown

Moves material from the debris to the mulch or active soil.

Mulch Processes

Decomposition

Moves material from the dead pools in the mulch to the atmosphere and to
the live microbe pool in the mulch. This process is caused by microbial
activity.

*Humification*

Moves material from the mulch pools to the active soil, which includes
the humus pool. Caused by slaters, earthworms and so on.

*Microbe death*

Moves material within the mulch, from the live microbe pool to the dead
microbe pools.

Soil Processes

Decomposition

Moves material from each of the active soil pools to the atmosphere and
to the two "bio" pools and the humus pools in the active soil. Caused by
soil microbes.

*Conversion*

Moves material from the humus pool within the active soil to the inert
soil layer.

*Products Processes*

*Decomposition*

Moves material from each of the product pools to the atmosphere.

Depending on the configuration of FullCAM, some or all of the above
processes are simulated.

**Events**

An event is a particular management action that occurs. An event is
instantaneous, generally causing perturbation of the biological
processes involved. Events are usually human management actions.

FullCAM allows for the following events within each of the three plot
types:

- Forest plot --- Tree planting, thinning, fire, chopper roller,
  termites.
- Agricultural plot --- Crop planting, harvest, fire, plough, herbicide,
  grazing change.
- Mixed plot --- Forest fraction change (change the proportion of
  sunlight incident on the forest system; the remainder of the sunlight
  falls on the agricultural system), in addition to types for either
  forest or agricultural plots.

You may specify any number of events and the times at which they occur,
thereby forming an "event queue", on the  page
on the input window of a plot document. During a simulation, FullCAM
simply applies the events at the times they are specified to occur.

------------------------------------------------------------------------