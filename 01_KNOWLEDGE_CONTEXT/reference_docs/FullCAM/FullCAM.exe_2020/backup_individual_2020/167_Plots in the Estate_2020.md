---
title: Plots in the Estate
version: 2020
category: estate
original_file: 167_Plots in the Estate_2020.md
---

This page is for specifying the plots in an estate.

**Introduction**

An estate is a collection of plots, each of which has an area and a
starting time. For example, you may have plots for plantations of
different species of trees on various sites, and your estate may be all
of the plantations belonging to a certain timber grower.

The listing on the left shows all of the plots in the estate, one per
line. Plots whose starting time is before the estate simulation starts
are coloured light blue. Plots whose starting time is after the estate
simulation ends are coloured dull orange.

Plots that are not ready for simulation are shown in red: edit them to
correct missing or invalid data.

To add a plot to the estate use the 'New...' button. After pressing the
'New...', a dialog box opens in which a Start Time for the plot is
specified by entering the Calender year and simulation step within that
year when the plot was initiated. The Area of the plot is entered. The
Plot File is selected from the drop-down list. Press 'OK...' to accept
the clause and enter the Plot file, its area and start time into the
estate.

To alter the Area or Start Time of a plot file within the estate, press
the 'Edit...' button and alter the values that appear in the dialog box
as required.

The 'Clone...&rdsquo; button can be used to enter an exact copy of the
plot file into the estate. This is useful when multiple plots of the
same tree or crop type with different areas or start times need to be
specified within the estate.

To remove a plot from the estate, select the plot and then press the
'Delete...' button.

The All Plots and Selected Plots boxes to the right of the list provide
a summary of the number of plots and area of plots in the estate or
selected.

**The Estate Simulation**

Simulate the estate by choosing *Run Simulation* from the *Simulate*
menu (if that menu choice is greyed out then the estate is not ready ---
attend to anything marked in red).

Each plot in the list of plots is simulated in turn. The results for
each plot, over the whole of the estate simulation period, are added
together to form the estate results, which are reported as the estate
outputs.

The estate timing is used to simulate every plot in the estate,
overriding the plot timing in each plot. That is, the plot simulation
will start at the time dictated by the time specified in the estate plot
window. The alignment of plot and estate timings is very difficult if
calendar (actual year instead of time since commencement) timing is used
in plot files. It is recommended that plot files for use in estates be
developed or converted to remove calendar dates and that FullCAM users
specify time since commencement instead.

Each plot simulation within the estate simulation begins at the start
year and start step of the plot, called the *start time* of the plot.
There are three possibilities for the start time of the plot and estate
simulation period. One of two types of timing can be applied to
individual 'Plots in the Estate' - Plot Timing and Estate Timing. The
timing option can be toggled between by selecting any number of plots in
the 'Plots in the Estate' window, right-clicking on the selected plots
and choosing either 'Use Plot Timing' or 'Use Estate Timing'.

If Plot Timing is chosen there are three possibilities for the start
time of the plot and estate simulation period:

1.  Plot start time is before the estate start time. The plot simulation
    begins at the start plot time and ends at the end of the estate
    simulation period, but the plot results only contribute to the
    estate totals during the estate simulation period.
2.  Plot start time is after the estate start time but before the estate
    stop time. From the estate start time to the plot start time, the
    plot contributes the initial conditions of the plot to the estate
    total --- that is, the plot is assumed to be frozen at its starting
    point for all of that time. The plot is simulated from its start
    time to the end time of the estate simulation period, during which
    the plot results contribute to the estate totals.
3.  Plot start time is after the estate stop time. The start time of the
    plot is after the end time of the estate simulation period. During
    all of the estate simulation period, the plot contributes the
    starting conditions of the plot to the estate total --- that is, the
    plot is assumed to be frozen at its starting point for all of the
    estate simulation period. The plot is not simulated during the
    estate simulation.

If 'Use Estate Timing' is chosen then the plot start time will begin at
the estate start time. However, unlike using Plot start time, the plot
does not remain frozen at the starting point of the initial conditions.
Instead normal plot dynamics will occur from the beginning of the estate
simulation, and the 'Start Year' and 'Start Step' of the plot will
determine when the event queue for the plot begins to simulate.

When the plot results are added to the estate totals, the plot results
in units (usually tonnes) per hectare are multiplied by the plot area
(in hectares) and then added to the corresponding estate total in units.

See Estate Simulation.

**Times: Growth Time Series and Events**

A single plot file can be used many times in an estate, and each of
these plots may have a different start time. If any of the species time
series (see Growth Properties) or events
(such as planting or thinning) are specified in terms of calendar years
then the plot file might become invalid (and thus not ready for
simulation) for some plot start times. If this occurs, FullCAM will
notify you and then abandon the estate simulation.

To avoid this possibility, in your plot files you should specify:

- The species time series using times since planting
- Events in terms of time since the start of the simulation.

Use species or event timing in terms of calendar years with caution,
because they must make sense in terms of how the plot file is used in
the estate simulation.

**Example**. Suppose you have a plot file for a plantation forest, in
which all the time series data (such as rainfall) and events (such as
forest fires) are specified in terms of years since the start of the
simulation. You then create an estate, simulated from 1940 to 2000, with
three plots that use this same plot file:

1.  10 ha, starting in 1940
2. 20 ha, starting in 1950
3. 30 ha, starting in 1960.

The plot file will then be simulated in the estate three times, and each
result will be the same, except displaced 10 years apart. Thus, the 1940
plot in 1970 will be identical to the 1950 plot in 1980 and the 1960
plot in 1990 (despite differing in size)..

Now suppose you add a forest fire to the plot file, but specify it as
occurring in 1956 (a calendar year). Now when you run the estate, each
of the three simulations will be different --- in the 1940 plantation
the forest fire in 1956 occurs in the 16th year of the plantation, in
the 1950 plantation the forest fire in 1956 occurs in the 6th year of
the plantation, in the 1960 plantation the forest fire in 1956 does not
occur (remember, a plot contributes its starting conditions to each
estate simulation step before the plot simulation starts, so the 1960
plot would show no effects from the 1956 fire).
