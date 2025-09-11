---
version: 2020
batch_range: 016-050
batch_name: Site_Configuration_Plot_Setup
creation_date: 2025-08-28
total_files: 20
---

# FullCAM 2020 - Batch 016-050: Site Configuration Plot Setup

## Table of Contents

- [019. Stem Loss and Stalk Loss 2020](#019-stem-loss-and-stalk-loss-2020)
- [020. General Features 2020](#020-general-features-2020)
- [023. Table Window 2020](#023-table-window-2020)
- [025. Output Windows 2020](#025-output-windows-2020)
- [026. Start and End of Simulation 2020](#026-start-and-end-of-simulation-2020)
- [027. Output Steps 2020](#027-output-steps-2020)
- [031. Initial Debris 2020](#031-initial-debris-2020)
- [032. Initial Soil 2020](#032-initial-soil-2020)
- [033. Initial Products 2020](#033-initial-products-2020)
- [036. Site Maximum Aboveground Biomass 2020](#036-site-maximum-aboveground-biomass-2020)
- [039. Site Growth Multipliers 2020](#039-site-growth-multipliers-2020)
- [042. Growth Properties 2020](#042-growth-properties-2020)
- [043. Plant Properties 2020](#043-plant-properties-2020)
- [044. Soil Water 2020](#044-soil-water-2020)
- [045. Debris Properties 2020](#045-debris-properties-2020)
- [046. Soil for the Whole Plot 2020](#046-soil-for-the-whole-plot-2020)
- [047. Product Properties 2020](#047-product-properties-2020)
- [048. Research Edition 2020](#048-research-edition-2020)
- [049. Further Documentation 2020](#049-further-documentation-2020)
- [050. Diagrams Window 2020](#050-diagrams-window-2020)

---

## 019. Stem Loss and Stalk Loss 2020

**Stem Loss and Stalk Loss**

\[[Plant Properties](43_Plant%20Properties.htm) window : *Stem Loss*
button\]

The [Time Series Window](135_time-series%20window.htm) is where you
enter the stem loss rate of a tree species or the stalk loss rate of a
crop species. See [Mortality](121_Mortality.htm).

**Details**

  Vegetation Type   Definition of \'Plant Death\'
  ----------------- -------------------------------
  Forest            stem death
  Agricultural      stalk death

This time series specifies plant mortality --- the percentage of stems
or stalks (and thus plants) that die per year. To make the mortality
rate a function of tree age, set the *Years are* in the *Timing* panel
to *Years since plants sprouted*.

The type of plant age to use in this time series, if it is expressed in
years since the plants sprouted, is chosen in the *Properties of the
Species Time Series* section in the [Growth
Properties](42_Growth%20Properties.htm) window.

The percentages in this time series are limited to less than 100% ---
use one of the [Events](136_Events.htm) to kill the whole forest or
crop.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 020. General Features 2020

**General Features**

Some general features that every user of FullCAM should know.

**Readiness**

A FullCAM document (plot, estate, spatial, database) has many inputs,
even in the simpler configurations. When all the inputs have been filled
with valid values, and some outputs specified, then the document is
ready to simulate. You cannot simulate a plot until it is ready.

Parts of the document that are not ready are coloured red.

The status bar at the bottom of the document window says whether a
document is ready. When the document is ready the \'Run Plot
Simulation\' item in the \'Simulate\' menu and its corresponding icon on
the toolbar of the [Main Window](217_Main%20Window.htm) become enabled.

The interface will only let you enter valid values. It will immediately
reject an invalid value. For some inputs, the valid range depends on
other inputs --- so if those other inputs change then the input can
become invalid, in which case it is shown with a red background.

**Fractions and Percentages**

In FullCAM:

A *fraction* is a number in the range 0.0 to 1.0.\
A *percentage* is a number in the range 0.0 to 100.0.

The fraction *f* corresponds to the percentage (100 \* *f)*. For
example, the fraction 0.25 corresponds to the percentage value of 25.

**Timing**

The timing of land use actions can impact carbon and nitrogen levels.
FullCAM has been designed to be flexible in relation to the timing of
these activities. Time is simulated as a series of equal-length steps.
There can be anywhere from 1 to 8760 steps per year, so FullCAM can run
a simulation on a yearly to an hourly basis. None of the other inputs
depends on this time scale, so you are free to run any model over any
time scale. Time scales can be changed by just re-entering the number of
steps per year --- so you could run a plot model with monthly time
steps, change the number of steps to 52 per year, and then run it on a
weekly time scale. You can instruct FullCAM to record the output data
after any number of steps (every step, every twelfth step, and so on),
so you can run the model with many steps per year and avoid being
overwhelmed with output data.

Input time series are always interpolated or extrapolated appropriately
to match the simulation steps. For example, if you enter annual rainfall
data but run the model daily, then the daily rainfall will simply be the
annual rainfall divided by 365 days. See the [Time Series
Window](135_time-series%20window.htm) for more information.

The primary unit of time in FullCAM is the year. A year in FullCAM
always has 365 days, there are no leap years.

**Units**

- The unit of mass is the metric tonne abbreviated "t", or kilogram
  abbreviated to "kg". Masses are often measured in tonnes of dry mass
  (tdm), tonnes of carbon (tC), or tonnes of nitrogen (tN).
- The unit of time is the year, abbreviated "yr".
- The unit of area is the hectare, abbreviated "ha".
- The unit of distance is the meter, abbreviated "m".
- The unit of water is the millimetre, abbreviated "mm".
- The unit of temperature is the degree Celsius, abbreviated "deg C".

**Inputs**

An *input* is a numerical input that you enter into a FullCAM document.
There are two types of inputs:

1.  *Single number* inputs - A single number, other than a data point of
    a time series.
2.  *Time series* inputs - A time series is a single value that varies
    with time.

The *regular value* of an input is what you type into the FullCAM
document, and is what is used in a plot simulation for a plot or spatial
document.

Double-click on any input (if a time series, on its multiplier) to get
information about it. Alternatively, press F2 while the input is
selected.

**Compatibility with Previous Versions of FullCAM**

FullCAM is under continual development; features are being added and,
occasionally, removed.

Each version of FullCAM generally has a unique file format. Newer
versions of FullCAM can open and read files that were created with the
older formats allowing them to be updated to the new current format.

**Windows**

Quit FullCAM by choosing *Exit* from the *Program* menu of the main
window (shortcut ctrl-Q), or by closing the main window by its close
box.

All FullCAM windows can be moved, and most can be resized. Move a window
by dragging it by its title bar; resize a window by dragging an edge or
a corner with the mouse. All FullCAM windows remember their sizes from
when you last resized them.

**Menus and Commands**

All the commands are either:

- In the menus (either the fixed menu in the [Main
  Window](217_Main%20Window.htm), or the mouse right click context
  menu).
- On buttons in the toolbars of the various windows.

All of the keyboard shortcuts are noted in the menus or in the tool tips
of toolbar buttons, except for those noted in [Special
Keys](15_Special%20Keys.htm).

Most buttons have an shortcut key so you can activate it using the
keyboard instead of clicking it with the mouse. In the button's label,
its shortcut is underlined. You can always activate the key by holding
down the *Alt* key while pressing the underlined key. However if the
cursor is not currently in an object that accepts keyboard input (not in
a text box or drop-down list box), you can omit the *Alt* key and simply
press the underlined key.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 023. Table Window 2020

**Table Window**

\[[Site](200_Site.htm) : [Water](12_Site_Water.htm) :
[Rainfall](88_Rainfall.htm)\]\
\[[Site](200_Site.htm) : [Water](12_Site_Water.htm) : [Open-pan
evaporation](98_Open-Pan%20Evaporation.htm)\]\
\[[Site](200_Site.htm) : [Water](12_Site_Water.htm) : define irrigation\
\[[Site](200_Site.htm) : [Temperature](13_Site_Temperature.htm) :
[Average Air Temperature](89_Average%20Air%20Temperature.htm)\]\
\[[Crops](216_Crops.htm) Crop: Growth: *All Allocations tabs*\]\
\[[Site](200_Site.htm) : [Productivity](64_Site_Productivity.htm) :
Productivity\
\[[Crops](216_Crops.htm) : [Growth](42_Growth%20Properties.htm) : *All
Increments tabs*\]\
\[[Crops](216_Crops.htm) : [Growth](42_Growth%20Properties.htm) :
[Manure from Offsite](62_Manure-from-offsite%20Change.htm)\]\
\[[Trees](215_Trees.htm) : [Growth](42_Growth%20Properties.htm) : *All
Allocation tabs*\]\
\[[Trees](215_Trees.htm) : [Growth](42_Growth%20Properties.htm) : *All
Increments tabs*\]\
\[[Trees](215_Trees.htm) : [Plants](201_Plants.htm) : [Stem
Density](9_Stem%20Density.htm)\]

This window is for viewing and editing a table. See also [Find Request
in a
Table](http://www.fullcam.au/FullCAMServer2020/Help/59_Find%20Request%20in%20a%20Table.htm).

**Overview**

The smallest lump of information that always stays together is shown in
the table as a single row, and is called a *record*.

This window has a *table grid*, which shows the whole table, one record
per line.

Some tables also come with a *detailed view*, which shows one record in
complete detail on a panel in the right hand side of the window. If
there is a detailed view, you can move the navy blue dividing line
between the table grid and the detailed view by grabbing it with the
mouse.

**Table**

The row in purple is the row that is currently being edited (and if
there is a detailed view, the row shown in the detailed view). The light
bands of colouring on every fifth row is to help guide your eye across
large tables.

The table is very flexible:

- Resize the columns by moving the column dividers in the title row.
- Change the column order by grabbing them in the title row and moving
  them.

The table can be operated mainly from the keyboard:

- Press the *Tab* key to go the next cell
- Press *Shift + Tab* to go to the previous cell.
- Use the up and down arrow keys to move to cells above and below the
  current cell being edited.
- Use the *Enter* key also moves you to the cell below.

**Sorting**

Press the Sort button on the tool bar to sort the visible records by the
leftmost table columns (sort by the leftmost column, use the next
leftmost column to break ties, and so on). Change the column order by
grabbing and moving them in order to get the exact sort that you want.

You can also sort the table by double-clicking on the title of a column.
Ties in that column are resolved in the standard order for that table.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 025. Output Windows 2020

**Output Windows**

\[*Output Windows* page of the input window of a plot, estate, or
spatial document\]

Control the output windows of the document.

Note that the **contents** of an [Output
Window](168_Output%20Window.htm), such as which simulation outputs to
display, are controlled from the output window itself.

**List**

This page lists the output windows. A check beside the name means that
the output window will open after you run a simulation. At least one
output window must exist - you cannot delete the last output window, but
you can uncheck it.

**Estate Outputs**

You may obtain any non-timing FullCAM outputs in the output windows of
an estate, because an estate consists of plot files with configurations
that may vary, and these configurations are not necessarily known when
you specify the estate outputs.

If an output is not possible for a plot that is simulated during an
estate simulation due to the configuration settings, then the plot will
not contribute, or will contribute zeroes, to that estate output. For
example, if you choose to report forest products but these are not
included in the plot files they will contribute zero to the estate
outputs.

**Subrule**

Create [Subrule
Report](http://www.fullcam.au/FullCAMServer2020/Help/227_Subrule%20Report.htm)
output windows and enable subrule calculations.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 026. Start and End of Simulation 2020

**Start and End of Simulation**

\[[Timing](199_Timing.htm) page : *Start and End of Simulation* panel\]

Set the time period over which the simulation runs.

**Daily Timing**

The simulation runs from the beginning of the start date to the end of
the end date.

Enter dates as, for example, "12 jan 1956" or "12 1 1956".

**Yearly Timing**

The starting time and ending times each consist of:

- A calendar year (such as 2005).
- A step number, which can be any number from one to the number of steps
  per year. If the simulation steps are yearly (one step per year) then
  the only valid step number is "1". The step number can never exceed
  8760, the maximum number of simulation steps per year and the number
  of hours in a year

A number with a red background is not ready:

- A year is not ready if the start year is greater than the end year.
- A step number is not ready if it greater than the number of simulation
  steps per year, or if the start and end years are the same and the
  start step number is greater than the end step number.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 027. Output Steps 2020

**Output Steps**

\[[Timing](199_Timing.htm) page : *Output Steps* panel\]

Choose which simulation steps produce outputs, that you can view on the
[Output Window](168_Output%20Window.htm).

**Output Steps**

An output step is a simulation step in which the state of the simulation
is recorded.

The simulation state is recorded at the END of the output step, after
the movements of material for that step have occurred.

FullCAM always records the simulation step at the beginning and the end
of the simulation - the step immediately before the simulation starts is
always an output step, and the last step of the simulation is always an
output step.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 031. Initial Debris 2020

**Initial Debris**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Initial
Debris* button\]

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest*
panel : *Trees* button\]

Describe the debris present in the plot at the start of the simulation.

**Introduction**

All of the initial forest debris belongs to the initial tree species,
which is specified in the [Initial Trees](185_Initial%20Trees.htm)
window.

All of the initial agricultural debris belongs to the initial crop
species, which is specified in the [Initial
Crops](184_Initial%20Crops.htm) window.

If different species are planted later in the simulation, the debris of
each species is treated separately because each species may have
different breakdown rates (see [Debris
Properties](45_Debris%20Properties.htm)).

**Carbon Masses**

Enter the mass of carbon in the various debris pools, in tonnes per
hectare.

Debris is classified as either *decomposable* or *resistant*, which is
an indication of how resistant it is to decay in the soil. Decomposable
debris becomes decomposable plant matter (DPM) in the soil after it
breaks down, while the resistant debris becomes resistant plant matter
(RPM). The DPM and RPM categories are defined by the
[RothC](114_RothC.htm) model. Decomposable debris decays more easily
than resistant plant material in the soil.

The "decomposable deadwood" carbon mass is the mass of carbon in the
decomposable deadwood that is "debris" but not yet "soil" or "mulch",
and so on.

The "chopped wood" pools only have material in them due to a [Chopper
Roller](52_Chopper%20Roller.htm) event, which can only occur in a forest
with no trees.

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
debris values (set via the *Initial Debris* button on the *Standard
Information for the Species* panel of the *Trees* or *Crops* pages, see
[Standard Information for the
Species](146_Standard%20Information%20for%20the%20Species.htm)) of the
initial species (specified via the *Trees* or *Crops* buttons of the
*Initial Conditions* page).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 032. Initial Soil 2020

**Initial Soil**

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest* or
*Agricultural* panel : *Soil* button\]

Describe the soil in the plot at the start of the simulation.

See the [RothC](114_RothC.htm) soil pool abbreviations.

**Carbon Masses**

Enter the mass of carbon in the various soil pools, in tonnes per
hectare as a time series.

**Water**

The topsoil moisture deficit (TSMD) is the amount of rainfall, in mm,
required to saturate the topsoil with water. It is a moisture *deficit*,
so the number you enter is zero or positive. The TSMD is used by RothC
to simulate soil decomposition.

The available soil water (ASW) is the amount of water available to the
trees, in mm, to rooting depth. It is used by
[3PG](http://www.fullcam.au/FullCAMServer2020/Help/115_3PG.htm) to
simulate tree growth and by 3PG-lite to compute the forest productivity
index (FPI).

FullCAM uses the two forest water balances, TSMD and ASW, separately and
simultaneously.

In an agricultural system FullCAM only uses the TSMD, but the
agricultural TSMD and the forest water balances (TSMD and ASW) are
completely unconnected.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 033. Initial Products 2020

**Initial Products**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Initial
Products* button\]

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest* or
*Agricultural* panel : *Products* button\]

Describe the plot products existing at the start of the simulation.

**Introduction**

All of the initial forest products belong to the initial tree species,
which is specified in the [Initial Trees](185_Initial%20Trees.htm)
window.

All of the initial agricultural products belong to the initial crop
species, which is specified in the [Initial
Crops](184_Initial%20Crops.htm) window.

If different species are planted later in the simulation, the products
of each species are treated separately because each species may have
different product decomposition rates (see [Product
Properties](47_Product%20Properties.htm)).

Forest products can start the simulation either in use as products or in
the landfill. Agricultural products can only start the simulation in use
as products (in FullCAM, agricultural products cannot go to landfill).

**Carbon Masses**

Enter the mass of carbon in the various product pools, in tonnes per
hectare as a time series.

The names of the products are only indicative: the various product
categories are effectively defined by their decomposition fractions
(entered as species inputs). All CAMFor cares about is that a hectare of
plot produces X tonnes of a product that decomposes at a given rate.

Suppose the plot is a forest that produces fence palings for suburban
back yards. There is no category here called "fence palings". The only
thing that matters to carbon accounting is how fast those fence palings
decompose. Suppose you find that 1/20 of the carbon in the fence palings
returns to the atmosphere each year. Then the decomposition fraction of
the fence palings is 0.05 / year. Make sure that one of the wood product
decomposition fractions is 0.05 / year, and add the fence palings to
that category.

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
product values (set via the *Initial Product* button on the *Standard
Information for the Species* panel of the *Trees* or *Crops* pages, see
[Standard Information for the
Species](146_Standard%20Information%20for%20the%20Species.htm)) of the
initial species (specified via the *Trees* or *Crops* buttons of the
*Initial Conditions* page). The button is disabled if the standard
initial product information for that species is not ready (incomplete or
has invalid values).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 036. Site Maximum Aboveground Biomass 2020

**Site : Maximum Aboveground Biomass**

\[[Site](200_Site.htm) page : *Maximum Aboveground Biomass* panel\]

Enter information about the maximum aboveground biomass that can be
supported by the plot.

The *aboveground biomass* is the combined mass of the aboveground plant
components:

- For tree systems: Stems, branches, bark, and leaves
- For agricultural systems: Grains, buds, fruit, stalks, and leaves.

It does not include the roots, debris, standing dead material, mulch, or
soil matter. It is measured in tonnes per hectare of dry matter
(tDM/ha).

The maximum aboveground biomass provides an upper limit on the amount of
aboveground biomass of trees and crops that can exist on the plot during
a simulation.

The growth of plants is calculated as specified under [Growth
Properties](42_Growth%20Properties.htm). After growth and turnover has
been calculated for the plant components, if the aboveground biomass of
the plants exceeds the maximum aboveground biomass for the site, then
the masses of all of the plant components are reduced, in proportion to
their pre-reduction masses.

If the aboveground biomass of the plants never exceeds the maximum
aboveground biomass, then the maximum aboveground biomass has no effect
on the simulation --- except if the Tree Yield Formula is used, in which
case the maximum forest aboveground biomass affects the tree growth rate
at all times (see [Growth Properties](42_Growth%20Properties.htm)).

If you do not wish there to be any upper limit on growth in cases where
the Tree Yield Formula is not being applied, simply set the maximum
aboveground biomass to a number high enough so as not to act as a
limiting effect (such as 9,999) --- effectively rendering it
inoperative.

**Relationship to the Tree Yield Formula**

For tree systems and mixed systems, if the option to use the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) is used (see [Configure Tree
Production](108_Configure%20Tree%20Production.htm)), the aboveground
biomass of the trees will asymptotically approach the specified maximum
aboveground biomass.

Information on aboveground biomass estimates can be found in NCAS
Technical Report No.44 and Roxburgh *et al.* 2019. Values for *Maximum
Aboveground Biomass* can be downloaded from the FullCAM server using
[Data Builder](132_Data%20Builder.htm) for specified spatial
coordinates.

[NCAS Technical Report
No.44](reps/TR44%20Spatial%20Estimates%20of%20Biomass%20in%20'Mature'%20Native%20Vegetation.pdf),
*Spatial Estimates of Biomass in \'Mature\' Native Vegetation* (2003).

Roxburgh, S., Karunaratne, S., Paul, K., Lucas, R., Armston, J., Sun,
J., 2019. *A revised above-ground maximum biomass layer for the
Australian continent*. Forest Ecology and Management **432**: 264--275.

**Plantation Species simulations**

When simulating a plantation tree species, changing this maximum
aboveground biomass (M) value will make the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) default parameters (G and *r*)
invalid. Therefore you will need to recalibrate these tree yield formula
parameters.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 039. Site Growth Multipliers 2020

**Site : Growth Multipliers**

\[[Site](200_Site.htm) page : *Growth Multipliers* button\]

Enter information about growth variations on the plot compared to the
standard site for which the plant growth information is intended.

**Use**

The growth multipliers multiply the growth of the trees and crops, to
reflect site variation from a standard site.

Each input multiplies the growth of its component in every step of the
simulation. A setting of 1.0 is neutral (no adjustment); a setting of
1.10 will cause the plant component to grow 10% more than the amount
otherwise calculated; a setting of 0.0 cuts off growth altogether.
"Growth" here means NPP if the growth is calculated using NPPs, or yield
if the growth is calculated using yields.

These inputs should generally remain neutral (that is, 1.0) when
developing a model, but may be used to model the effect of different
environmental conditions --- such as less allocation to roots with
better moisture and nutrient availability. These growth multipliers can
be used as a shortcut to altering the relative growth tables.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 042. Growth Properties 2020

**Growth Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Growth* button\]

These two windows, the tree growth and crop growth windows, are where
you specify how the current species grows ([Select a
Species](56_Select%20a%20Species.htm)).

**Growth**

"Growth" on this window can mean either "production and turnover" or
"production only", depending on the second setting in the *Properties*
section. See [Yield and
NPP](131_Yield%20and%20Net%20Primary%20Production.htm).

**Properties of the Allocations, Increments and Other Species Time
Series**

- [Tree Growth Allocations](112_Tree%20Growth%20Allocations.htm)
- [Crop Growth Allocations](124_Crop%20Growth%20Allocations.htm)
- [Tree Growth Increments](110_Tree%20Growth%20Increments.htm)
- [Crop Growth Increments](118_Crop%20Growth%20Increments.htm)
- [Mortality](121_Mortality.htm) ([Plant
  Properties](43_Plant%20Properties.htm))
- [Stem Density](9_Stem%20Density.htm) ([Plant
  Properties](43_Plant%20Properties.htm) window)

Specify here whether the plant age used in any species time series is
the average or the maximum age of the plants. This input only applies to
species time series that are expressed in terms of times since the
plants were sprouted (although it is always a required input, regardless
of whether or not any species time series are in terms of times since
sprouting). The average and maximum plant age only differ if there have
been thinning or harvesting events that do not clear the plot, and thus
allow new plants to sprout alongside the older plants --- see the
[Thin](140_Thin.htm) and [Harvest](153_Harvest.htm) events.

**Tree Growth Method**

The tree growth method is set in the [Configure Tree
Production](108_Configure%20Tree%20Production.htm) panel. The methods
are:

1.  *Increments* - Use one of the increment time series on this window.
    Set whether the allocations and increments are in terms of NPP or
    yields.
2.  *Tree yield formula* - The increments are not used. The allocations,
    like the increments computed by the tree yield formula, are
    automatically in terms of yields.
3.  *[3PG](http://www.fullcam.au/FullCAMServer2020/Help/115_3PG.htm)*
    ([Research Edition](48_Research%20Edition.htm) only) - The
    increments are not used. The allocation time series, like the NPP
    computed by 3PG, are automatically in terms of NPP.

**Crop and Pasture Growth Methods**

Crop and pasture growth is always specified by increment time series,
and the allocation and increment time series are set in terms of NPP or
yields. There are two methods for modelling crop and pasture growth:

1.  *Sigmoidal* - Use for annual species. Grows using a sigmoidal curve
    to achieve the target yield amount.
2.  *Perennial* - Used for modelling perennial pastures. The growth
    curve is constructed from an initial value and steply (generally
    monthly) increments of growth and die-off.

A more detailed description on the different types of Crop and Pasture
growth is detailed on the [Crop growth
page](118_Crop%20Growth%20Increments.htm).

**Allocations**

The allocation time series specify the growth of the plant components.
An allocation time series is required for each plant component.

The numbers in the allocation time series are the

*relative* allocations of yield or NPP to the various plant components
and they must be positive numbers. (See [Time Series
Window](135_Time-Series%20Window.htm).)

**Increments**

An increment time series specifies the increase in one or a combination
of plant components. Only one increment time series is used by the
species --- select one by clicking on the radio button to the left of
the rectangular button displaying the name of the increment time series.

**Parameters in the Tree Yield Formula**

See the [Tree Yield Formula](130_Tree%20Yield%20Formula.htm). Variation
in site, management, species and other factors greatly impact forest
growth and hence, vary growth curve characteristics.

Enter the tree age in years at which the tree's growth (measured in
tonnes per year) is highest. This is *G* in the description of the yield
formula.

The roles of the non-endemic species multiplier *r* of the maximum
aboveground biomass *M* (entered in the *Site : Maximum Aboveground
Biomass* panel) are:

- To change the effective maximum biomass in the tree yield formula from
  *M* to *r \* M*.
- To change the maximum tree biomass limit for the plot from *M* to *r
  \* M*.

Because *r* is species-dependent, the site's growth rate and maximum
biomass can vary by species for the same site. Normally r will be close
to 1 (assuming that *M*, entered in the *Site : Maximum Aboveground
Biomass* panel, is a realistic value).

When using [Data Builder](132_Data%20Builder.htm) to download tree
species, the values of *G* and *r* or *y* that it downloads to your plot
are based on statistically calibrated models.

*Calculation of G and r for plantation tree species*

Default vaules for plantation tree species are based on statistically
calibrated models that are unique to combinations of regions and
management factors.

The age of maximum biomass increment *G* varies with productivity and
management regime. It is calculated using a linear model:

> *G = ag + bg \* M*

where

*M* = Maximum aboveground biomass of trees, in tdm/ha (*Site* page).
This is the unadjusted value, prior to multiplication by *r* and prior
to any type 2 forest treatments.

*ag* = Maximum age at which the trees reach maximum aboveground biomass
increment at the lowest *M* values (that is, on the lowest quality site
on which the plantation species is used). *ag* is constant for a given
species, but varies between species.

*bg* = Multiplier. Constant for a given species, but varies between
species.

Thus, for a given species, the downloaded *G* only varies with *M*.

The non-endemic species multiplier *r* varies with region and management
regime. It is calculated by:

> *r* = exp(*ar* + *br* \* ln(*M*)) = exp(*ar*) \* (*M* \^ *br*)

where

*M* = As defined above.

*ar* = Constant, Depends on rotation length and region. *ar* is constant
for a given species, but varies between species.

*br* = Multiplier. Depends on the region. Constant for a given species,
but varies between species.

> *x* \^ *y* = *x* to the power of *y* (for example, 5 \^ 2 = 25).

This equation only applies within a range of allowable *r \* M* values
in which a species is expected to occur. If *r\*M* exceeds parameter
*r\*Mmax*, then *r* is set to *r\*Mmax/M* and *G* is assigned parameter
*Gmax*. Conversely, if *r\*M* is less than parameter *r\*Mmin*, then *r*
is set to *r\*Mmin/M* and *G* is assigned parameter *Gmin*. This
provides a growth curve that is consistent with the maximum (*Mmax*) and
minimum (*Mmin*) feasible values of *M* for the species.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 043. Plant Properties 2020

**Plant Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Plants* button\]

Specify the non-growth properties of the species, for the current
species ([Select a Species](56_Select%20a%20Species.htm)).

**Carbon Percentages**

The carbon percentage of a tree or crop component is the mass of carbon
in the component.

The carbon percentages for a range of tree components can be found in
the NCAS Technical Reports No.s
[7](reps/TR7%20Carbon%20Content%20of%20Woody%20Roots%20Revised%20Analysis%20and%20a%20Comparison%20with%20Woody%20Shoot%20Components%20(Revision%201).pdf){target="_blank"}
and
[22](reps/TR22%20Carbon%20Contents%20of%20Above-Ground%20Tissues%20of%20Forest%20and%20Woodland%20Trees.pdf){target="_blank"}.

**Typical carbon contents for tree species (taken from Table 9 of the
*Land Use Change Methods* Report):**

  Tree component      Carbon Content
  ------------------ ----------------
  Stems                    50.0
  Branches                 47.0
  Bark                     49.0
  Leaves and twigs         52.0
  Coarse Roots             50.0
  Fine Roots               48.0

**Typical carbon contents for some plant species:**

Crop Type

GBF

Stalks

Leaves

Coarse Roots

Fine Roots

Cereal

43.43

43.75

44.1

Improved Pasture

37.46

37.46

Unimproved/Native Pasture

40.9

40.9

Irrigated Cotton

43.43

45.0

43.25

45.0

43.25

Sugarcane

39.0

43.75

44.1

**Turnover Percentages**

Turnover represents the part of a plant component being shed by the
plant. Turnover material is dead, and moves to the debris. All of the
parts of a plant except tree stems are subject to turnover.

The turnover percentage of a plant pool determines how much material is
turned over. Setting a turnover percentage to 0 means that there is no
turnover. A turnover percentage of 100% means that in each simulation
step all of the pool dies and moves to debris, so the only material in
the pool at the end of the step is new material that was produced during
the step.

In FullCAM, turnover rates are assumed to be constant throughout the
year using the same turnover fraction in every simulation step. This
would be an unrealistic assumption for the turnover of leaves for
deciduous trees and perennial grasses.

The turnover percentage of a plant pool is the percentage lost per year
due to turnover. It assumes exponential decay at a constant decay rate.

Typical turnover rates for trees are described in Table 10 of the report
*Land Use Change in Australia: In Integrated Application of the National
Carbon Accounting System*. Turnover rates for additional species can be
extracted from the FullCAM database.

\

Typical turnover rates for tree species, (taken from Table 10 of the
*Land Use Change Methods* Report) :

  Tree component    Turnover Rate
  ---------------- ---------------
  Leaf                  4.70
  Branch                0.56
  Bark                  0.83
  Coarse Root           5.60
  Fine Root             10.42

\

Typical turnover rates for crop species

  Crop component    Turnover Rate
  ---------------- ---------------
  GBF                    0.0
  Leaf                  86.0
  Stalk                 10.0
  Coarse Root           10.0
  Fine Root             150.0

**Stem Density**

For trees only. See the [Stem Density](9_Stem%20Density.htm) time
series.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 044. Soil Water 2020

**Soil Water**

\[[Soil](203_Soil.htm) page : *Forest* or *Agricultural* panel : *Water*
button\]

Enter the water-related properties of the soil. It differs slightly
between agricultural and forest systems. See

[Site : Water](12_Site_Water.htm).

**Ratio of Evapotranspiration to Open-Pan Evaporation**

The *Ratio of evapotranspiration to open-pan evaporation* is the ratio
of water lost through evapotranspiration (in mm) to water lost by
open-pan evaporation (in mm).

[RothC](114_RothC.htm) uses rainfall and evapotranspiration to calculate
the topsoil moisture deficit (TSMD), which is difficult to measure. They
calculate the evapotranspiration as the product of the open-pan
evaporation (which is easy to measure) and this ratio. This ratio is
0.75 for temperate soils.

Alternatively, obtain monthly evapotranspiration with adequate accuracy
from Muller's (1982) collection of meteorological data for sites around
the world, then enter the evapotranspiration data in the open-pan
evaporation time series and set this ratio to one.

**Ratio of Bare-to-Covered Maximum TSMD**

The *ratio of maximum TSMD for bare soil to maximum TSMD for covered
soil* is the ratio of the maximum topsoil moisture deficit (TSMD) for
bare soil to the maximum TSMD for covered soil.

This input is generally taken to be 0.556 (= 5 / 9).

**Water Info**

Opens a window of text information about the partition of the total
saturated water capability of the soil into:

**Parameters for the Top Soil Moisture Deficit (TSMD)**

Let

> c = the fraction of the soil that is clay, by weight (see [Soil for
> the Whole Plot](46_Soil%20for%20the%20Whole%20Plot.htm))\
> b = the bulk density of the soil, in t/m^3^ (see [Soil for the Whole
> Plot](46_Soil%20for%20the%20Whole%20Plot.htm))\
> d = depth of soil sampled, in cm (see [Soil
> Properties](3_Soil%20Properties.htm))\
> r = ratio of max TSMD for bare soil to max TSMD for covered soil (see
> above).

Then the maximum TSMD in mm is, by soil cover and RothC version,

(20 + 130 \* c - 100 \* c \* c) \* (d / 23), v26.3, Soil covered\
(20 + 130 \* c - 100 \* c \* c) \* (d / 23) \* r, v26.3, Soil bare

(0.688405334 + 4.4746369 \* c - 3.44203 \* c \* c) \* d

\+ ln(9) \* (0.082530817 + 0.5364083 \* c - 0.41268 \* c \* c) \* d,
v26.5, Covered or bare

The depth of inaccessible water (water always in the soil, no matter how
long a dry spell continues, but it is inaccessible to plants) in mm is

> (0.0445 + 0.41 \* c) \* 10 \* d.

The total porosity (WFPS) (the water from totally dry to completely
saturated, after which any additional added water runs off) in mm is

> (1 - b / 2.65) \* 10 \* d.

The maximum drainage water is the total porosity less the maximum TSMD
less the inaccessible water:

total porosity = drainage (soil canot hold this water, it drains)

> \+ available water (measured by TSMD, varying from 0 to maximum TSMD)\
> + inaccessible water (awlays present, no matter how dry the weather).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 045. Debris Properties 2020

**Debris Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Debris* button\]

Specify the properties of the debris produced by the current species
([Select a Species](56_Select%20a%20Species.htm)). Debris from separate
species is treated entirely separately by FullCAM. See the discussion of
debris vs. mulch in [Configure the Plot](6_Configure%20the%20Plot.htm).

**Resistant Percentages**

The resistant percentage of a tree or crop pool is the percentage of the
mass of the pool that is resistant to decomposition.

The resistant percentage of a tree or crop pool is the percentage of
material that would go into the resistant plant material (RPM) pool
rather than the decomposable plant material (DPM) pool. The DPM and RPM
definitions are part of the [RothC](114_RothC.htm) model.

The tree or crop material that is not resistant is decomposable. When
material from the trees and crops enters the debris, it goes either into
either a decomposable or a resistant debris pool.

**More-Resistant Percentages**

The more-resistant percentage of a pool of resistant debris is the
percentage of the pool that goes to the *more-resistant plant mulch*
pool (the rest of the material entering the mulch goes to the
*less-resistant plant mulch* pool). All the resistant litter pools are
assumed to have the same more-resistant percentage, so FullCAM only
requires a single more-resistant percentage.

**Breakdown Percentages**

The breakdown percentage of a debris pool is the percentage of the pool
that breaks down each year.

Breakdown is the process by which debris becomes a combination of:

1.  *Atmospheric breakdown products* - Goes to the atmosphere. Consist
    mainly of CO~2~.
2.  *Solid breakdown products* - Goes to the soil (if mulch is not
    modelled) or the mulch (if mulch is modelled).

The breakdown percentage of a debris pool determines how long it takes
material to pass through the debris pool. Setting a breakdown percentage
to 0 means that none of the material in the debris pool ever leaves the
pool. Setting a high breakdown percentage means that in each simulation
step most of the debris pool at the beginning of the step moves either
to the atmosphere, soil, or mulch. It assumes exponential decay at
constant decay rate.

The chopped wood pools only have material in them due to a [Chopper
Roller](52_Chopper%20Roller.htm) event, which can only occur in a forest
with no trees.

Typical values for a crop would be for complete breakdown of litter
annually. Table 13 of the report *Greenhouse Gas Emissions from Land Use
Change in Australia: An Integrated Application of the National Carbon
Accounting System* provides some typical rates for native forests:

\

Litter Decomposition Rates for Tree Components.

  Plant Component             Litter Decomposition Rate (1/yr)
  -------------------------- ----------------------------------
  Decomposable Leaf                         1.0
  Resistant Leaf                            1.0
  Decomposable Deadwood                     0.1
  Resistant Deadwood                        0.1
  Decomposable Bark                         0.5
  Resistant Bark                            0.5
  Decomposable Coarse Root                  0.4
  Resistant Coarse Root                     0.1
  Decomposable Fine Root                    0.3
  Resistant Fine Root                       0.4

**Atmospheric Percentages of Breakdown Products**

The atmospheric percentage of the breakdown product of a debris pool is
the percentage of the breakdown products of the debris pool that moves
to the atmosphere (the rest moves to the soil or the mulch).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 046. Soil for the Whole Plot 2020

**Soil for the Whole Plot**

\[[Soil](203_Soil.htm) page : *Whole Plot* panel\]

Enter properties of the soil shared by both the forest and agricultural
soil.

**Clay Percentage**

Percentage of the soil that is clay. *[NCAS Technical Report No
12](reps/TR12%20Pre-Clearing%20Soil%20Carbon%20Levels%20in%20Australia.pdf){target="_blank"}*
provides clay percentage values for major soil types.

Affects the parameters for decomposition of organic soil pools (the
[RothC](114_RothC.htm) pools), and the parameters for the water content
of the soil (the topsoil moisture deficit or TSMD).

**Bulk Density**

Soil consists of:

- Particles --- either clay or quartz (in this context "quartz" just
  means "not-clay")
- Pore space --- the voids between the particles, usually filled with
  air or water.

The bulk density of the soil is the particle mass divided by its bulk
volume, where the bulk volume is the volume of the particles and pores
together in soil. Thus the bulk density is just the density of the soil
as it exists in the ground, treated as a bulk object (that is, a solid
object where we ignore the tiny holes / pores, so its boundary is as we
would normally see it from a couple of meters away). Units: tonnes per
cubic meter.

Used to compute the amount of water required to saturate the shallow
soil (namely the mm of water added from the point at which the TSMD is
zero until draining starts to occur), that is, the total porosity of the
soil expressed in mm of water.

By the way:

  ---------- --------------------------------------------------------------------------------
  Porosity   = pore space / bulk volume \[a fraction\]
             = (bulk volume - particle volume) / bulk volume
             = 1 - \[ particle volume \* particle mass) / (bulk volume \* particle mass) \]
             = 1 - (bulk density) / (particle mass / particle volume)
             = 1 - (bulk density) / (particle density)
  WFPS       = water filled pore space fraction
             = water-filled-pore-space / total-pore-space \[a fraction\]
  ---------- --------------------------------------------------------------------------------

Water is always measured in mm of clear water, a 1-D measurement that
suffices for volumes in soils.

See [Soil Water](44_Soil%20Water.htm).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 047. Product Properties 2020

**Product Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Products* button\]

Specify the properties of the products produced by the current species
([Select a Species](56_Select%20a%20Species.htm)).

*Products* are any plant material that is moved offsite from the plot.
Products from separate species is treated entirely separately by
FullCAM.

**Decomposition Percentages**

The decomposition percentage of a product pool (either "in use" or "in
landfill") is the average percentage of carbon mass lost to
decomposition (and thus as CO~2~ to the atmosphere) each year. The
higher the decomposition percentage, the faster the product returns its
carbon to the atmosphere.

A decomposition percentage of 0 means that none of the pool decomposes
(so no carbon returns to the atmosphere from the product). A
decomposition percentage of 100% means that in each simulation step all
of the pool decomposes, thereby returning all of its carbon to the
atmosphere.

The decomposition percentage of a debris pool is the percentage lost per
year due to decomposition (that is, 100% less the percentage of the
original material that is still there a year later, if decomposition is
the only process removing material from the pool). It assumes
exponential decay at constant decay rate. Click the exponential decay
button for alternative expressions, a graph, and a fuller explanation.

**Bio-energy, Move-to-Landfill**

Forest products may be burnt for bio-energy or moved to landfill after
being used.

Once in a landfill, material just decomposes --- thereby returning its
carbon to the atmosphere eventually. For a given species and product
type, the decomposition percentage for a product in use will generally
be higher than the decomposition percentage for the product in landfill.
Agricultural products may be burnt for bio-energy after being used, but
may not be moved to a landfill.

Material burnt for bio-energy is burnt immediately (it is NOT added to
the biofuel), thereby returning its carbon to the atmosphere. The
"biofuel" product category is there for a different purpose: the biofuel
product pool consists of biofuel stocks awaiting burning for bio-energy.
Setting the *Percentage Burnt for Bio-Energy Each Year* to 100% causes
all the biofuel in the pool at the beginning of a simulation step to be
burnt in that step. For completeness, you have the option of sending
forest biofuel to landfill instead of burning it for bio-energy.

**Product Categories**

The names of the wood products here do NOT define the products: the
behaviour of the various wood product categories are defined solely by
the product decomposition fractions. The only things of significance to
FullCAM are that a hectare of forest produces X tonnes of a wood product
that decomposes at a given rate, and so on.

Suppose a forest product is being used to produce fence palings for
suburban back yards. There is no category here called "fence palings".
The only thing relevant to carbon accounting is how fast those fence
palings decompose. Suppose you find that 1/20 of the carbon in the fence
palings returns to the atmosphere each year. Then the decomposition
percentage of the fence palings is 5%. Make sure that one of the wood
product decomposition fractions is about 5%, and add the fence palings
to that category. For instance, suppose you enter the decomposition rate
of packing wood as 5.2%. Add the fence palings to the category labelled
"packing wood".

The 0.2% difference in decomposition rate may be negligible but if not
allocate your decomposition rates as best as possible.

The wood product names used here are suggestive only (terms such as
"very long lived wood", "long lived wood", \..., "short lived wood" or
may be "wood life 7", \..., "wood life 1" could also have been used.

Crop product names can be taken more literally, but the same applies as
with the wood products --- the names do not matter per se, as only the
decomposition fractions define the behaviour of the plant products for
carbon accounting purposes.

The rationale behind the wood products life cycle pools used by the NCAS
can be found in the NCAS Technical Reports [No.
8](reps/TR8%20Usage%20and%20Life%20Cycle%20of%20Wood%20Products.pdf){target="_blank"}
and [No.
24](reps/TR24%20Analysis%20of%20Wood%20Product%20Accounting%20Options%20for%20the%20National%20Carbon%20Accounting%20System.pdf){target="_blank"}
([Contact Us](190_Contact%20Us.htm)).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 048. Research Edition 2020

Research Edition

Standard and Research Editions

Each version of FullCAM comes in two editions, the standard edition and
the research edition.

The research edition of FullCAM is intended only for professional
researchers in carbon accounting and plant modelling. The research
edition is available upon reasonable request.

**Differences in Function**

Functionally, the research edition differs from the standard edition in
that:

- It includes the
  [3PG](http://www.fullcam.au/FullCAMServer2020/Help/115_3PG.htm) tree
  growth model. (Both editions contain the 3PG-lite model for computing
  the [Forest Productivity Index
  (FPI)](188_Forest%20Productivity%20Index.htm).)
- It can calculate the Forest Productivity Index from scratch (see
  [Configure Tree Production](108_Configure%20Tree%20Production.htm))
- It can do [Nitrogen
  Simulation](http://www.fullcam.au/FullCAMServer2020/Help/55_Nitrogen%20Simulation.htm)
  (other than just in the mulch, as part of
  [GENDEC](http://www.fullcam.au/FullCAMServer2020/Help/109_GENDEC.htm)).
- It includes version 26.5 of [RothC](114_RothC.htm).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 049. Further Documentation 2020

**Further Documentation**

This topic discusses available documentation beyond this Help system.

**Diagrams**

Press the *Diagrams* button on the
[Configuration](150_Configuration.htm) page to open the [Diagrams
Window](50_Diagrams%20Window.htm), which shows diagrams of your plot
model.

**Papers and Methodology**

See the National Inventory Report for further discussion of the
methodologies and literature drawn upon by FullCAM:

**National Carbon Accounting System Technical Reports**

Supporting technical documentation is provided in the National Carbon
Accounting System Technical Reports (see "Technical Reports" in the
FullCAM Help [Table of Contents](index.htm)).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 050. Diagrams Window 2020

**Diagrams Window**

\[[Configuration](150_Configuration.htm) page : *Diagrams* button\]

Selecting the \'Diagrams\...\' button shows diagrams of the FullCAM
model, for the current configuration. The diagrams show the pools,
layers, and systems in your plot (see [Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm)), and the flows
of material that occur.

**Diagrams**

Press the Diagrams button to see diagrams of the chosen configuration
(when the Configuration page is complete)

**Current limitations**

The diagrams show:

1.  Processes --- Processes are the continuous actions that occur all
    the time, such as production or decomposition.
2.  Carbon flows..
3.  Layers --- A layer is a collection of similar pools, such as trees,
    crops, debris, mulch, soil, or products.

**Use**

Choose the layer or system from the menu to the left of the toolbar. You
may need to resize the window or scroll to see all of the diagram.

The options button to the right of the diagram menu controls some
options on how the diagrams are displayed. In particular, the *Show
Names* option switches on the display of programming names on the
diagrams, which is useful when reading the FullCAM technical
documentation.

**Legend**

The smallish coloured rectangles are pools. The grey rectangles around
them are the layers. Some of the pools in a layer may be grouped by
function with a coloured rectangle within their layer, for example the
aboveground debris pools form the "litter".

The black lines show carbon flow. There is always an arrow at the end of
the flow, to indicate the direction of flow. Where two carbon flows
merge to become a single flow (like the flow of water at the junction of
two rivers), the black lines have a black dot. If two black lines cross
over one another without a black dot then the two flows are separate
(they do not join).

The small light blue circles are splitters, which are where a carbon
flow splits into more several flows. The proportions of material that
flow each way out of a splitter are controlled by inputs that you set in
the FullCAM inputs.

The names of the processes causing each flow are in blue. The names of
the inputs and outputs to each layer are in purple.

**Printing**

You may print the diagrams by clicking the *Page setup* and *Print*
icons. General Help regarding these functions is available from within
the dialog boxes. Specific options for the *Print what* option in the
*Page setup* dialog are as follows:

1.  **Displayed diagram**. In this case FullCAM will just print the
    diagram that is currently displayed.
2.  **All diagrams**. All diagrams are printed in sequence. Each diagram
    commences on a new page. When using *Print preview*, repeated
    clicking of the *Close* button moves on to the next diagram until
    the last one is reached.

To cancel the preview at the currently displayed diagram, close the
*Print preview* window by clicking the Close icon that is located on the
window title bar.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
