---
title: One Plot in the Estate
version: 2016
category: Estate
original_file: 186_One Plot in the Estate_2016.md
---

[Plots in the Estate : *New* or
*Edit* button]

This window specifies the properties of one of the Plots in the
Estate.

**Details**

Simulation of the plot begins in the year and step of the start time
specified here. For example, if a plot's start year is set to 1985 and
its start step to 6 (which would be June, if the estate timing was 12
steps per year), then the plot will be simulated starting with step 6 in
1985 of the estate simulation.

If the estate simulation starts before the plot simulation (the estate
simulation start time is before the plot's start time), then the plot
contributes its initial conditions to the estate up until the plot
simulation starts. For example, if the estate simulation is from 1980
(step 1) to 2000 (step 21) and a given plot starts in 1985 (step 6),
then when the estate totals are calculated this plot will contribute its
initial conditions for 1980 through step 5 of 1985. So if the plot has
an initial debris carbon of 5 tC/ha, it will contribute 5 tC/ha to the
estate's debris carbon for each step from step 1 in 1980 through step 5
of 1985.

The *Step* of the start time cannot be greater than the steps-per-year
in the estate timing. If the value violates this condition, then it
appears in red, and the plot and the estate cannot be simulated (the
plot in need of editing is shown in red in the list of plots in the
*Plots in the Estate* page). If you change the estate timing, some plots
in the estate may change their readiness.

The area is the size of the plot, in hectares (a hectare is an area
equal to a square 100 meters by 100 meters, 1 hectare = 2.471 acres).
Note that plot files do not have an area, and their masses are described
in tonnes per hectare. In an estate simulation, a plot result expressed
in tonnes per hectare is multiplied by the plot area to arrive at its
contribution in tonnes to the estate.

The plot files are in the same order in the menu as they are in the
*Plot Files* page of the estate document (where they can be sorted).