---
title: Initial Debris
version: 2016
category: Debris
original_file: 31_Initial Debris_2016.md
---

[Trees page or Crops page : *Initial
Debris* button]

[Initial Conditions page : *Forest*
panel : *Trees* button]

Describe the debris present in the plot at the start of the simulation.

**Introduction**

All of the initial forest debris belongs to the initial tree species,
which is specified in the Initial Trees
window (regardless of whether or not there are trees initially growing
on the plot).

All of the initial agricultural debris belongs to the initial crop
species, which is specified in the Initial
Crops window (regardless of whether or not
there is a crop initially growing on the plot).

If different species are planted later in the simulation, the debris of
each species is treated separately because each species may have
different breakdown rates (see Debris
Properties).

**Carbon Masses**

Enter the mass of carbon in the various debris pools, in tonnes per
hectare.

Debris is classified as either *decomposable* or *resistant*, which is
an indication of how resistant it is to decay in the soil. Decomposable
debris becomes decomposable plant matter (DPM) in the soil after it
breaks down, while the resistant debris becomes resistant plant material
(RPM). The DPM and RPM categories are defined by the
RothC model. Decomposable debris decays more easily
than resistant plant material in the soil.

The "decomposable deadwood" carbon mass is the mass of carbon in the
decomposable deadwood that is "debris" but not yet "soil", and so on.

The "chopped wood" pools only have material in them due to a Chopper
Roller event, which can only occur in a forest
with no trees.

**Insert Standard Values**

[Only present when the window is accessed via the Initial
Conditions page.]

Press the *Insert Standard Values* button to insert the standard initial
debris values of the initial species. The button is disabled if the
standard initial debris information for that species is not ready
(incomplete or has invalid values).