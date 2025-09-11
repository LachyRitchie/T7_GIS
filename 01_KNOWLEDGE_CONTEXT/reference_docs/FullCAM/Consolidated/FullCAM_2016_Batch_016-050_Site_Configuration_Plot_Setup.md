---
version: 2016
batch_range: 016-050
batch_name: Site_Configuration_Plot_Setup
creation_date: 2025-08-28
total_files: 22
---

# FullCAM 2016 - Batch 016-050: Site Configuration Plot Setup

## Table of Contents

- [017. Site Displacement 2016](#017-site-displacement-2016)
- [019. Stem Loss and Stalk Loss 2016](#019-stem-loss-and-stalk-loss-2016)
- [020. General Features 2016](#020-general-features-2016)
- [021. 3PG Leaves 2016](#021-3pg-leaves-2016)
- [023. Table Window 2016](#023-table-window-2016)
- [025. Output Windows 2016](#025-output-windows-2016)
- [026. Start and End of Simulation 2016](#026-start-and-end-of-simulation-2016)
- [027. Output Steps 2016](#027-output-steps-2016)
- [031. Initial Debris 2016](#031-initial-debris-2016)
- [032. Initial Soil 2016](#032-initial-soil-2016)
- [033. Initial Products 2016](#033-initial-products-2016)
- [036. Site Maximum Aboveground Biomass 2016](#036-site-maximum-aboveground-biomass-2016)
- [039. Site Growth Multipliers 2016](#039-site-growth-multipliers-2016)
- [042. Growth Properties 2016](#042-growth-properties-2016)
- [043. Plant Properties 2016](#043-plant-properties-2016)
- [044. Soil Water 2016](#044-soil-water-2016)
- [045. Debris Properties 2016](#045-debris-properties-2016)
- [046. Soil for the Whole Plot 2016](#046-soil-for-the-whole-plot-2016)
- [047. Product Properties 2016](#047-product-properties-2016)
- [048. Research Edition 2016](#048-research-edition-2016)
- [049. Further Documentation 2016](#049-further-documentation-2016)
- [050. Diagrams Window 2016](#050-diagrams-window-2016)

---

## 017. Site Displacement 2016

**No Help Available**

The Help Window shows this topic if there is no help in a context or
with certain sorts of errors.

Some windows (such as the [Main Window](217_Main%20Window.htm)) and some
pages have no help. When you are there, pressing "F1" leads you to here.

Otherwise, you may be here by error. If there was a help button (yellow
question mark on small green circle) on the window or page you had
selected, then you should have been lead to the help for that button ---
please [Contact Us](190_Contact%20Us.htm) so we know to fix the error.

Press the appropriate help button with the mouse if there are any
difficulties or ambiguity.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 019. Stem Loss and Stalk Loss 2016

**Stem Loss and Stalk Loss**

\[[Plant Properties](43_Plant%20Properties.htm) window : *Stem Loss*
button\]

This [time-series Window](135_time-series%20window.htm) is where enter
the stem loss rate of a tree species or the stalk loss rate of a crop
species. See [Mortality](121_Mortality.htm).

**Details**

  Vegetation Type   Definition of \'Plant Death\'
  ----------------- -------------------------------
  Forest            stem death
  Agricultural      stalk death

This time-series specifies plant mortality --- the percentage of stems
or stalks (and thus plants) that die per year. To make the mortality
rate a function of tree age, set the *Years are* in the *Timing* panel
to *Years since plants sprouted*.

The type of plant age to use in this time-series, if it is expressed in
years since the plants sprouted, is chosen in the *Properties of the
Species time-series* section in the [Growth
Properties](42_Growth%20Properties.htm) window.

The percentages in this time-series are limited to less than 100% ---
use one of the [Events](136_Events.htm) to kill the whole forest or
crop.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 020. General Features 2016

**General Features**

Some general features that every user of FullCAM should know.

**Readiness**

A FullCAM document (plot or estate) has many inputs, even in the simpler
configurations. When all the inputs have been filled with valid values,
and some outputs specified, then the document is *ready* to simulate. In
particular, you cannot simulate a plot until it is ready.

Parts of the document that are not ready are coloured red. Red writing
and colouring guide you to the parts that are not ready --- the bits you
need to complete before the plot can be simulated.

The status bar at the bottom of the document window says whether a
document is ready. When the document is ready the \'Run Plot
Simulation\' item in the \'Simulate\' menu and its corresponding icon on
the toolbar of the [Main Window](217_Main%20Window.htm) become enabled.

The interface will only let you enter valid values. It will immediately
reject an invalid value, such as a percentage that is greater than 100,
less than 0.0, or non-numeric. For a few inputs, the valid range depends
on other inputs --- so if those other inputs change then the input can
become invalid, in which case it is shown with a red background.

When a simulation is ready all tabs will not be in red, and the \'Run
Simulation\' icon on the toolbar of the [Main
Window](217_Main%20Window.htm) will be highlighted.

**Fractions and Percentages**

In FullCAM:

A *fraction* is a number from 0.0 to 1.0, inclusive.\
A *percentage* is a number from 0.0 to 100.0, inclusive.

The fraction *f* corresponds to the percentage (100 \* *f)*. For
example, the fraction 0.25 = 25% (recall that "%" just means "/100")
corresponds to the percentage 25.

We use fractions in FullCAM for computations, because it is easier to
calculate with fractions. But we use percentages in the user interface,
because it is quicker to type percentages than it is to type decimal
points or "%" symbols.

This also affects the terminology. For example, the "carbon percentage"
of leaves is the percentage of dry leaves by weight that is carbon, and
is approximately 50 (which we might write as 50%, if we regard the "%"
symbol in this instance like a unit), while the "carbon fraction" of
leaves is about 0.5, which is 50%.

**Timing**

The timing of land use actions can impact carbon levels. FullCAM has
been designed to be very flexible in relation to the timing of these
activities. Time is simulated as a series of equal-length steps. FullCAM
Standard Edition can run a simulation on anywhere from a yearly to a
daily basis. None of the other inputs depends on this time scale, so you
are free to run any model over any timescale. Timescales can be changed
by re-selecting the step length --- so you could run a plot model with
monthly time-steps, then change to weekly timescale.

Input time-series are always interpolated or extrapolated appropriately
to match the simulation steps. For example, if you enter annual rainfall
data but run the model daily, then the daily rainfall will simply be the
annual rainfall divided by 365 days.

The primary unit of time in FullCAM is the year. A year in FullCAM
always has 365 days (leap years are irrelevant to modelling with this
precision, but would just add significant complexity).

**Units**

- The unit of mass is the metric tonne, abbreviated "t", or kilogram,
  abbreviated to "kg". Masses are often measured in tonnes of dry mass
  (tdm) or tonnes of carbon (tC).
- The unit of time is the year, abbreviated "yr".
- The unit of area is the hectare, abbreviated "ha".
- The unit of distance is the meter, abbreviated "m", except when
  measuring water it is millimetres, "mm".
- The unit of temperature is the degree Celsius, abbreviated "deg C".

The expression "a/b/c" means "(a / b) / c" or equivalently "a / (b \*
c)", because order of operations is implicitly left to right. For
example, "t/ha/yr" means "(tonnes per hectare) per year".

**Inputs**

An *input* is a numerical input that you enter into a FullCAM document.
There are two types of inputs:

1.  *Single number* inputs - A single number, other than a data point of
    a time-series.\
    Example: the initial mass of leaves in the forest.
2.  *time-series* inputs - A time-series is a single value that varies
    with time.\
    Example: the rainfall falling on a plot.

The *regular value* of an input is a value specified by the user and
used in a normal plot simulation. You can perform a risk analysis by
attaching a probability distribution to an input (which then becomes a
*risk input*). Double-click on any input (if a time-series, on its
multiplier) to get information about it, or to edit its associated risk
properties (if a risk analysis is turned on). Alternatively, press F2
while the input is selected.

**Compatibility with Previous Versions of FullCAM**

FullCAM is under continual development; features are being added, and
occasionally removed.

Often a new version of FullCAM will have a unique file format. However,
newer versions of FullCAM can read many files that were created with
older formats. Generally, it is a good idea to use files in the latest
format. To do so, download the latest version of FullCAM and when you
open a file, if the file format can be updated, FullCAM will ask if you
wish to overwrite the file with the latest format. If you do not wish to
overwrite the file, you can also use the File menu to save a version of
the plot or estate with the latest format using an alternate name.

**Windows**

The main window is the thin window across the top of your screen with a
menu and toolbar, entitled "FullCAM X.X", where X.X is the version
number of the FullCAM program.

The main window is open whenever FullCAM is open. Individual FullCAM
documents or windows do not appear separately on the Windows taskbar. If
you close the main window (by clicking its close box) then you exit
FullCAM. You cannot resize the main window, but you can move it.

All FullCAM windows can be moved, and most can be resized. Move a window
by dragging it by its title bar; resize a window by dragging an edge or
a corner with the mouse. All FullCAM windows remember their positions
and sizes from when you last moved or resized them.

Quit FullCAM by choosing *Exit* from the *Program* menu of the main
window, or by closing the main window.

**Special Keys**

The following keys have special meanings that are not necessarily
apparent from looking through the menus. You do not need to know any of
these meanings to use FullCAM with a mouse and the usual keys, but these
meanings can speed you up.

- *Enter ---* If you are in a number entry box, FullCAM immediately
  process the number.

- *Tab* --- Jumps to the next data entry control (box, menu, button, and
  so on).

- *Shift-Tab* --- Jumps to the previous data entry control (box, menu,
  button, and so on).

- *Space* --- If a button is selected, pressing the *Space* bar presses
  the button.

- *Home, End, Page Up, Page Down* --- Move between pages in tabbed
  windows (such as the document input windows), move between help topics
  in the *Help* window, and move between records in the table windows.

- *Delete* --- Deletes selected items from lists.

- *F1* --- Opens the *Help* window at the help topic for the current
  window. If there are several help buttons on the window, pressing F1
  opens the Help at the topic for the first of the buttons --- you can
  then move to other topics using control-N (next) and control-B (back).
  However, in general we recommend you press the help button with the
  mouse to move straight to the topic you want.

- *F2* --- Opens the *Input Properties* window for the current input
  control (box, menu, and so on). If *Risk Analysis* is on, it instead
  opens the *Risk Properties* window for the input.

- *F9* --- Simulates a plot or estate document (refer [Introduction to
  Using FullCAM](1_Introduction%20to%20Using%20FullCAM.htm) for further
  details).

- *F12* --- Closes the window, automatically pressing any *OK* or *Done*
  button on the window.

- *Escape* --- Closes the window, automatically pressing any *Cancel*
  button on the window. Same as if the close-window box was clicked.

- *Alt* --- Shifts focus to the [Main Window](217_Main%20Window.htm),
  ready for a letter to choose a menu. A second *Alt* key press returns
  you to the previous window.

**Underlines on buttons** --- If there is a button in the current window
with an underlined letter, pressing that "Alt-" and that letter on the
keyboard presses that button (if there is no ambiguity due to currently
being in a text box and so on, just pressing the letter on the keyboard
has the same effect).

Most keyboard shortcuts are noted in the menus or in the tool tips of
toolbar buttons.

Most buttons have an *accelerator* key so you can activate it using the
keyboard instead of clicking it with the mouse. In the button's label,
its accelerator key is underlined. You can always activate the
accelerator key by holding down the *Alt* key while pressing the
underlined key. However if the cursor is not currently in an object that
accepts keyboard input (not in a text box or drop-down list box), you
can omit the *Alt* key and simply press the underlined key.

**Example.** A button labelled "Delete", where the "D" is underlined,
can be activated by pressing either "d" or "D" on the keyboard, or if
you are currently entering text or in a drop-down list box, press
"Alt-d" or "Alt-D".

**Entering Numbers**

FullCAM often requests information in the form of numbers. You enter
most numbers into text boxes, which are white against the grey
background of the window.

If you enter a number that is outside the allowed range of numbers, or
enter text that is not a number, FullCAM will ask you to re-enter the
number immediately you either try to leave the text box (move the focus
elsewhere) or you press the *Enter* key.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 021. 3PG Leaves 2016

**No Help Available**

The Help Window shows this topic if there is no help in a context or
with certain sorts of errors.

Some windows (such as the [Main Window](217_Main%20Window.htm)) and some
pages have no help. When you are there, pressing "F1" leads you to here.

Otherwise, you may be here by error. If there was a help button (yellow
question mark on small green circle) on the window or page you had
selected, then you should have been lead to the help for that button ---
please [Contact Us](190_Contact%20Us.htm) so we know to fix the error.

Press the appropriate help button with the mouse if there are any
difficulties or ambiguity.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 023. Table Window 2016

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
Density](9_Stem%20Density.htm)\]\
\[[Crops](216_Crops.htm) page of a database document : *any Table
button*\]

This window is for viewing and editing a table. See also [Find Request
in a Table](59_Find%20Request%20in%20a%20Table.htm).

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 025. Output Windows 2016

**Output Windows**

\[*Output Windows* page of the input window of a plot or estate
document\]

Control the output windows of the document.

Note that the **contents** of an [Output
Window](168_Output%20Window.htm), such as which simulation outputs to
display, are controlled from the output window itself.

**List**

This page lists the output windows, by name. A check beside the name
means that the output window will open after you run a simulation. You
cannot delete the last output window, but you can uncheck it.

An output window is listed in red if it is not ready and black if its
data is complete and ready to simulate. An output window is ready if it
has one or more available outputs selected. Make an unready output
window ready by showing the output window then selecting one or more
outputs to show in the window.

**Estate Outputs**

You may obtain any non-timing FullCAM outputs in the output windows of
an estate, because an estate consists of plot files with configurations
that may vary, and these configurations are not necessarily known when
you specify the estate outputs.

If an output is not possible for a plot (due to the configuration of the
plot file) that is simulated during an estate simulation, then the plot
will not contribute (or will contribute zeroes) to that estate output.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 026. Start and End of Simulation 2016

**Start and End of Simulation**

\[[Timing](199_Timing.htm) page : *Start and End of Simulation* panel\]

Set the time period over which the simulation runs.

The simulation runs from the beginning of the start date to the end of
the end date.

A number with a red background is not ready. A date is not ready if the
start and end dates are the same or the start date is later than the end
date.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 027. Output Steps 2016

**Output Steps**

\[[Timing](199_Timing.htm) page : *Output Steps* panel\]

Choose which simulation steps produce outputs, that you can view on the
[Output Windows](168_Output%20Window.htm).

**Output Steps**

An *output step* is a simulation step in which the state of the
simulation is recorded in the outputs, for viewing in the output windows
(which show graphs and tables of results), for risk analysis, and so on.

The simulation state is recorded at the END of the output step, that is,
after the movements of material for that step have occurred.

FullCAM always records the simulation step at the beginning and the end
of the simulation, that is, the "step immediately before the simulation
starts" (as it were) is always an output step, and the last step of the
simulation is always an output step.

In a plot simulation, FullCAM typically spends more time displaying the
simulation results in a table or graph than it spends calculating the
results. Have as few output steps as possible, consistent with getting
enough output for your purposes. If you want to increase the underlying
resolution in the simulation, decrease the simulation step length
instead ([Simulation Steps](5_Simulation%20Steps.htm)).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 031. Initial Debris 2016

**Initial Debris**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Initial
Debris* button\]

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest*
panel : *Trees* button\]

Describe the debris present in the plot at the start of the simulation.

**Introduction**

All of the initial forest debris belongs to the initial tree species,
which is specified in the [Initial Trees](185_Initial%20Trees.htm)
window (regardless of whether or not there are trees initially growing
on the plot).

All of the initial agricultural debris belongs to the initial crop
species, which is specified in the [Initial
Crops](184_Initial%20Crops.htm) window (regardless of whether or not
there is a crop initially growing on the plot).

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
decomposable deadwood that is "debris" but not yet "soil", and so on.

The "chopped wood" pools only have material in them due to a [Chopper
Roller](52_Chopper%20Roller.htm) event, which can only occur in a forest
with no trees.

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
debris values of the initial species. The button is disabled if the
standard initial debris information for that species is not ready
(incomplete or has invalid values).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 032. Initial Soil 2016

**Initial Soil**

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest* or
*Agricultural* panel : *Soil* button\]

Describe the soil in the plot at the start of the simulation.

See the [RothC](114_RothC.htm) soil pool abbreviations.

**Carbon Masses**

Enter the mass of carbon in the various soil pools, in tonnes per
hectare as a time-series.

**Water**

The topsoil moisture deficit (TSMD) is the amount of rainfall, in mm,
required to saturate the topsoil with water. It is a moisture *deficit*,
so the number you enter is zero or positive. The TSMD is used by RothC
to simulate soil decomposition.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 033. Initial Products 2016

**Initial Products**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Initial
Products* button\]

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest* or
*Agricultural* panel : *Products* button\]

Describe the plot products existing at the start of the simulation.

**Introduction**

All of the initial forest products belong to the initial tree species,
which is specified in the [Initial Trees](185_Initial%20Trees.htm)
window (regardless of whether or not there are trees initially growing
on the plot).

All of the initial agricultural products belong to the initial crop
species, which is specified in the [Initial
Crops](184_Initial%20Crops.htm) window (regardless of whether or not
there is a crop initially growing on the plot).

If different species are planted later in the simulation, the products
of each species are treated separately because each species may have
different product decomposition rates (see [Product
Properties](47_Product%20Properties.htm)).

Forest products can start the simulation either in use as products or in
the landfill. Agricultural products can only start the simulation in use
as products (in FullCAM, agricultural products cannot go to landfill).

**Carbon Masses**

Enter the mass of carbon in the various product pools, in tonnes per
hectare as a time-series.

The names of the products are only indicative: the various product
categories are effectively defined by their decomposition fractions
(entered as species inputs). All CAMFor cares about is that a hectare of
plot produces X tonnes of a product that decomposes at a given rate.

Suppose the plot is a forest that produces fence palings for suburban
back yards. There is no category here called "fence palings", so what do
you do? The only thing that matters to carbon accounting is how fast
those fence palings decompose. Suppose you find that 1/20 of the carbon
in the fence palings returns to the atmosphere each year. Then the
decomposition fraction of the fence palings is 0.05 / year. Make sure
that one of the wood product decomposition fractions is about 0.05 /
year, and add the fence palings to that category. For instance, suppose
you enter the decomposition rate of packing wood as 0.052. Close enough.
Add the fence palings to the category labelled "packing wood".

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
product values. The button is disabled if the standard initial product
information for that species is not ready (incomplete or has invalid
values).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 036. Site Maximum Aboveground Biomass 2016

**Site : Maximum Aboveground Biomass**

\[[Site](200_Site.htm) page : *Maximum Aboveground Biomass* panel\]

Enter information about the maximum aboveground biomass that can be
supported by the plot.

The *aboveground biomass* is the combined mass (in tdm/ha) of the
aboveground plant components:

- For trees: Stems, branches, bark, and leaves
- For crops: Grains, buds, fruit, stalks, and leaves.

It does not include the roots, or any debris or soil matter. It is a
mass, measured in tonnes per hectare of dry matter, not carbon mass.

The maximum aboveground biomass limits place absolute limits on the
amount of aboveground trees and crops can exist of the plot during a
simulation.

The growth of plants is calculated as specified elsewhere (see [Growth
Properties](42_Growth%20Properties.htm)), without regard to the maximum
aboveground biomass (except in the tree yield formula which uses the
maximum site biomass as the value toward which growth will approach).
After growth and turnover has been calculated for the plant components,
if the aboveground biomass of the plants exceeds the maximum aboveground
biomass for the site, then the masses of all of the plant components are
reduced, in proportion to their pre-reduction masses.

The mass removed from the plant components becomes turnover and is
treated as turnover, except that aboveground-biomass-limit-reduction
mass is added to turnover after yield-versus-production has been
determined (yield measurements do include the effects of regular
turnover, but do not include the effects of mortality or site biomass
limits).

There are separate aboveground biomass limits for trees and for crops
--- that is, the site may support different aboveground biomasses of
trees or crops.

In a mixed plot, limits apply to trees and crops separately and
proportionally. For example, if the maximum aboveground biomass for
trees is entered here as 80 tdm/ha (if the whole plot is covered in
forest then it can support 80 tdm/ha of aboveground biomass) but
currently only 20% of the plot is forested, then the maximum aboveground
biomass of trees is 20% \* 80 tdm/ha = 16 tdm/ha (the plot can support a
maximum aboveground tree biomass of 16 tdm/ha while 20% of it is
forested).

If the aboveground biomass of the plants never exceeds the maximum
aboveground biomass, then the maximum aboveground biomass has no effect
on the simulation --- except if the tree yield formula is used, in which
case the maximum forest aboveground biomass affects the tree growth rate
at all times (see [Growth Properties](42_Growth%20Properties.htm)).

If you do not wish there to be any upper limit on growth, simply set the
maximum aboveground biomass to a number high enough so as not to act as
a limiting effect (such as 999) --- effectively rendering it
inoperative.

The maximum aboveground biomass limit is intended to simulate
self-thinning and depends on the site, but not on the species.

**Trees**

The maximum aboveground tree biomass is also used to calculate tree
growth, if the option to use the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) is used (see [Configure Tree
Production](108_Configure%20Tree%20Production.htm)). Basically, the
aboveground tree mass asymptotically approaches the maximum aboveground
biomass.

If any tree species uses the tree yield formula then the maximum
aboveground biomass of the trees cannot exceed 764 tdm/ha (which
corresponds to the maximum possible aboveground biomass under the tree
yield formula). If you choose to use the tree yield formula when the
maximum aboveground biomass of the trees exceeds this amount, the input
here is coloured red to indicate it needs changing.

Information on aboveground biomass estimates can be found in [NCAS
Technical Report
No.44](reps/TR44%20Spatial%20Estimates%20of%20Biomass%20in%20'Mature'%20Native%20Vegetation.pdf){target="reps44"}.
Values for *Maximum Aboveground Biomass* can be downloaded from the
FullCAM server using [Data Builder](132_Data%20Builder.htm).

**Crops**

There is no crop-growth-by-formula option; the maximum crop biomass is
only used to limit crop mass.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 039. Site Growth Multipliers 2016

**Site : Growth Multipliers**

\[[Site](200_Site.htm) page : *Growth Multipliers* button\]

Enter information about growth variations on the plot compared to the
standard site for which the plant growth information is intended.

**Use**

The growth multipliers multiply the growth rates of the trees and crops,
to reflect site variation from a standard site.

Each input multiplies the growth of its component in every step of the
simulation. A setting of 1.0 is neutral (no adjustment); a setting of
1.10 will cause the plant component to grow 10% faster than the amount
otherwise calculated; a setting of 0.0 cuts off growth altogether.
"Growth" here means NPP if the growth is calculated using NPPs, or yield
if the growth is calculated using yields. These multipliers are applied
after all other growth computations (such as allocations).

These inputs should generally remain neutral (that is, 1.0) when
developing a model, but may be used to model the effect of different
environmental conditions --- such as less allocation to roots with
better moisture and nutrient availability. These growth multipliers can
be used as a shortcut to altering the relative growth tables. They are
useful as risk inputs in a risk analysis.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 042. Growth Properties 2016

**Growth Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Growth* button\]

These two windows, the tree growth and crop growth windows, are where
you specify how the current species grows ([Select a
Species](56_Select%20a%20Species.htm)). The two windows are very
similar, so are discussed together.

**Growth**

"Growth" on this window can mean either "production and turnover" or
"production only", depending on the second setting in the *Properties*
section. See [Yield and
NPP](131_Yield%20and%20Net%20Primary%20Production.htm).

**Tree Growth Method**

The tree growth method is set in the [Configure Tree
Production](108_Configure%20Tree%20Production.htm) panel. The methods
are:

1.  *Increments* - Use one of the increment time-series on this window.
    Set whether the allocations and increments are in terms of NPP or
    yields.
2.  *Tree yield formula* - The increments are not used. The allocations,
    like the increments computed by the tree yield formula, are
    automatically in terms of yields.

**Crop Growth Method**

Crop growth is always specified by increment time-series, and you always
set whether the allocation and increment time-series are in terms of NPP
or yields.

**Properties of the Species time-series**

The *species time-series* are:

- [Tree Growth Allocations](112_Tree%20Growth%20Allocations.htm) (this
  window)
- [Crop Growth Allocations](124_Crop%20Growth%20Allocations.htm) (this
  window)
- [Tree Growth Increments](110_Tree%20Growth%20Increments.htm) (this
  window)
- [Crop Growth Increments](118_Crop%20Growth%20Increments.htm) (this
  window)
- [Mortality](121_Mortality.htm) ([Plant
  Properties](43_Plant%20Properties.htm) window)
- [Stem Density](9_Stem%20Density.htm) ([Plant
  Properties](43_Plant%20Properties.htm) window)

Specify here whether the plant age used in any species time-series is
the average or the maximum age of the plants. This input only applies to
species time-series that are expressed in terms of times since the
plants were sprouted (although it is always a required input, regardless
of whether or not any species time-series are in terms of times since
sprouting). The average and maximum plant age only differ if there have
been thinning or harvesting events that do not clear the plot, and thus
allow new plants to sprout alongside the older plants --- see the
[Thin](140_Thin.htm) and [Harvest](153_Harvest.htm) events. Note that
the term "sprouting" is used to specify the time of germination. The
time of planting is when the plant is moved in site to the plot. The age
of planting will be the same or less than the age of sprouting (such as
to account for nursery time).

Specify whether the allocations and increases are for yields (measured
mass increments) or NPP flows. Most people will choose yields; the NPP
option is mainly for academic researchers. If the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) is being used, this choice has
been made for you (yields).

**Allocations**

The allocation time-series specify the growth of the plant components
relative to each other. We need one allocation time-series for each
plant component.

The numbers in the allocation time-series are the

*relative* allocations of yield or NPP to the various plant components.
Use any non-negative numbers; they are only meaningful in relation to
one another (for example, 1.0 for leaves and 0.2 for coarse roots is the
same as 1000 for leaves and 200 for coarse roots).

**Increments**

An increment time-series specifies the increase in one or a combination
of plant components. Only one increment time-series is used by the
species --- select one by clicking on the radio button to the left of
the rectangular button displaying the name of the increment time-series.

**Parameters in the Tree Yield Formula**

See the [Tree Yield Formula](130_Tree%20Yield%20Formula.htm). Variation
in site, management, species and other factors greatly impact forest
growth and hence, vary growth curve characteristics

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

*Calculation of G and r on the Departmental Server*

When you use [Data Builder](132_Data%20Builder.htm) to download tree
species, the [Departmental Server](219_Departmental%20Server.htm)
calculates the values of *G* and *r* that it downloads to your plot as
follows. These calculations are based on statistically calibrated models
involving site and management factors.

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

> *r* = exp(*ar* + *br* \* ln(*Pavg*)) = exp(*ar*) \* (*Pavg* \^ *br*)

where

*Pavg* = Average annual site FPI (forest productivity index). *Pavg* is
calculated solely from *M*, as described in the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) topic.

*ar* = Constant, Depends on rotation length and region. *ar* is constant
for a given species, but varies between species.

*br* = Multiplier. Depends on the region. Constant for a given species,
but varies between species.

> *x* \^ *y* = *x* to the power of *y* (for example, 5 \^ 2 = 25).

This equation only applies within a range of *Pavg* values in which a
species is expected to occur; outside of this range *r* is set to 1.
Thus, for a given species and in the range of *Pavg* in which the
species is expected to occur, the downloaded *r* only varies with *M*.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 043. Plant Properties 2016

**Plant Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Plants* button\]

Specify the non-growth properties of the species, for the current
species ([Select a Species](56_Select%20a%20Species.htm)).

**Carbon Percentages**

The carbon percentage is the fraction of the dry mass that is carbon.

**Turnover Percentages**

Turnover represents the part of a plant component being shed by the
plant. Turnover material is dead and moves to the debris pool. All of
the parts of a plant except tree stems are subject to turnover,
including roots.

The turnover percentage of a plant pool determines how fast material is
turned over (how frequently it falls from the plant). Setting a turnover
percentage to 0 means that there is no turnover. A turnover percentage
of 100% means that in each simulation step all of the pool dies and
moves to debris (so the only material in the pool at the end of the step
is new material --- plant components --- that was produced during the
step).

In FullCAM, turnover rates are assumed to be constant throughout the
year --- that is, the same turnover fraction is used in every simulation
step.

The turnover percentage of a plant pool is the percentage lost per year
due to turnover (that is, 100% less the percentage of the original
material that is still there a year later, if turnover is the only
process removing material from the plant pool). It assumes exponential
decay at a constant decay rate. Click the exponential decay button for
alternative expressions, a graph, and a fuller explanation.

Typical turnover rates for trees are described in Table 10 of the report
*Land Use Change in Australia: In Integrated Application of the National
Carbon Accounting System*. Turnover rates for additional species can be
extracted from the FullCAM database.

TABLE -- Typical turnover rates for tree species, (taken from Table 10
of the *Land Use Change Methods* Report) :

  Tree component   Turnover Rate (Fraction)
  ---------------- --------------------------
  Leaf             0.0470
  Branch           0.0056
  Bark             0.0083
  Coarse Root      0.0560
  Fine Root        0.1042

Turnover rates for annual crops are typically set at 0.81/yr.

**Stem Density**

For trees only. See the [Stem Density](9_Stem%20Density.htm)
time-series.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 044. Soil Water 2016

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

The [RothC](114_RothC.htm) module uses rainfall and evapotranspiration
to calculate the topsoil moisture deficit (TSMD). The evapotranspiration
is calculated as the product of the open-pan evaporation and this ratio
(which is 0.75 for temperate soils).

Alternatively, obtain monthly evapotranspiration with adequate accuracy
from Muller\'s (1982) collection of meteorological data for sites around
the world, then enter the evapotranspiration data in the open-pan
evaporation time-series and set this ratio to one.

**Ratio of Bare-to-Covered Maximum TSMD**

The *ratio of maximum TSMD for bare soil to maximum TSMD for covered
soil* is the ratio of the maximum topsoil moisture deficit (TSMD) for
bare soil to the maximum TSMD for covered soil.

This input is generally taken to be 0.556 (= 5 / 9). It is used by
[RothC](114_RothC.htm).

**Water Info**

Opens a window of text information about the partition of the total
saturated water capability of the soil into:

- Inaccessible water.
- The maximum topsoil moisture deficit (TSMD) that is accessible by the
  plants.
- Water that drains off.

Water in excess of the amount to saturate the soil is excess, and runs
off.

Requires that nitrogen simulation be switched on in the
[Configuration](150_Configuration.htm) (which enables the bulk density
parameter on the [Soil for the Whole
Plot](46_Soil%20for%20the%20Whole%20Plot.htm) panel of the
[Soil](203_Soil.htm) page.)

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

[]{.high
title="these do not appear to be equations, how are they related here and how should they be formatted?"}

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

total porosity = drainage (soil cannot hold this water, it drains)

> \+ available water (measured by TSMD, varying from 0 to maximum TSMD)\
> + inaccessible water (always present, no matter how dry the weather).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 045. Debris Properties 2016

**Debris Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Debris* button\]

Specify the properties of the debris produced by the current species
([Select a Species](56_Select%20a%20Species.htm)). Debris from separate
species is treated entirely separately by FullCAM. See the discussion of
debris vs. mulch in [Configure the Plot](6_Configure%20the%20Plot.htm).

**Resistant Percentages**

The resistant percentage of a tree or crop pool is the percentage of the
mass of the pool that is resistant to decomposition. The interpretation
of "resistant" is left up to you; just be sure to interpret it
consistently as the material flows through the debris and soil.

More precisely, the resistant percentage of a tree or crop pool is the
percentage of material, by mass, that, should it get to the soil as
plant material, would go into the resistant plant material (RPM) pool
rather than the decomposable plant material (DPM) pool. The DPM and RPM
definitions are part of, and thus defined by, the [RothC](114_RothC.htm)
model.

The tree or crop material that is not resistant is decomposable. When
material from the trees and crops enters the debris, it goes either into
either a decomposable or a resistant debris pool.

**More-Resistant Percentages**

The more-resistant percentage of a pool of resistant debris is the
percentage of the pool, by mass, that, upon entering the mulch, goes to
the *more-resistant plant mulch* pool (the rest of the material entering
the mulch goes to the *less-resistant plant mulch* pool). All the
resistant litter pools are assumed to have the same more-resistant
percentage, so FullCAM only requires a single more-resistant percentage.

**Breakdown Percentages**

The breakdown percentage of a debris pool is the percentage of the pool
that breaks down each year.

Breakdown is the process by which debris becomes: *Atmospheric breakdown
products* - Goes to the atmosphere. Consist mainly of CO~2~.

The breakdown percentage of a debris pool determines how long it takes
material to pass through the debris pool. Setting a breakdown percentage
to 0 means that none of the material in the debris pool ever leaves the
pool (so no plant material reaches the soil). Setting a breakdown
percentage to 100% means that in each simulation step all of the mass in
the debris pool at the beginning of the step moves either to the
atmosphere or to the soil or mulch (thus, no material builds up in the
debris pool).

The breakdown percentage of a debris pool is the percentage lost per
year due to breakdown (that is, 100% less the percentage of the original
material that is still there a year later, if breakdown is the only
process removing material from the pool). It assumes exponential decay
at constant decay rate. Click the exponential decay button for
alternative expressions, a graph, and a fuller explanation.

The chopped wood pools only have material in them due to a [Chopper
Roller](52_Chopper%20Roller.htm) event, which can only occur in a forest
with no trees.

Typical values for a crop would be for complete breakdown of litter
annually. Table 13 of the report *Greenhouse Gas Emissions from Land Use
Change in Australia: An Integrated Application of the National Carbon
Accounting System* provides some typical rates for native forests:

TABLE --- Litter Decomposition Rates for Tree Components.

  Plant Component            Litter Decomposition Rate (1/yr)
  -------------------------- ----------------------------------
  Decomposable Leaf          1.0
  Resistant Leaf             1.0
  Decomposable Deadwood      0.1
  Resistant Deadwood         0.1
  Decomposable Bark          0.5
  Resistant Bark             0.5
  Decomposable Coarse Root   0.4
  Resistant Coarse Root      0.1
  Decomposable Fine Root     0.3
  Resistant Fine Root        0.4

**Atmospheric Percentages of Breakdown Products**

The atmospheric percentage of the breakdown product of a debris pool is
the percentage of the breakdown products of the debris pool that moves
to the atmosphere (the rest moves to the soil).

**Example.** Suppose that for the decomposable GBF litter pool,

> breakdown percentage = 80\
> atmospheric percentage of breakdown product = 60

Then the pool would lose 80% of its mass due to breakdown over a whole
year, if there were no inputs to the pool, and of the broken down
material, 60% goes to the atmosphere and 40% goes to the soil. Thus, if
no inputs were added to the pool for a year, 80% \* 60% = 48% of the
pool would go to the atmosphere over the year, 80% \* 40% = 32% would go
to the soil, and 20% would still be in the pool at the end of the year.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 046. Soil for the Whole Plot 2016

**Soil for the Whole Plot**

\[[Soil](203_Soil.htm) page : *Whole Plot* panel\]

Enter properties of the soil shared by both the forest and agricultural
soil.

**Clay Percentage**

Percentage of the soil that is clay. *[NCAS Technical Report No
12](reps/TR12%20Pre-Clearing%20Soil%20Carbon%20Levels%20in%20Australia.pdf){target="reps12"}*
provides clay percentage values for major soil types.

Affects the parameters for decomposition of organic soil pools (the
[RothC](114_RothC.htm) pools), and the parameters for the water content
of the soil (namely the topsoil moisture deficit or TSMD).

**Bulk Density**

Soil consists of:

- Particles --- either clay or quartz (in this context \"quartz\" just
  means \"not-clay\")
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

Clarifications:

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 047. Product Properties 2016

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

**Move-to-Landfill**

Forest products may be moved to landfill after being used.

Once in a landfill, material just decomposes --- thereby returning its
carbon to the atmosphere eventually. For a given species and product
type, the decomposition percentage for a product in use will generally
be higher than the decomposition percentage for the product in landfill.
Agricultural products may not be moved to a landfill.

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
8](reps/TR8%20Usage%20and%20Life%20Cycle%20of%20Wood%20Products.pdf){target="reps08"}
and [No.
24](reps/TR24%20Analysis%20of%20Wood%20Product%20Accounting%20Options%20for%20the%20National%20Carbon%20Accounting%20System.pdf){target="reps24"}
([Contact Us](190_Contact%20Us.htm)).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 048. Research Edition 2016

Research Edition

Standard and Research Editions

Each version of FullCAM comes in two editions, the standard edition and
the research edition. This edition of FullCAM is the standard edition.

The research edition of FullCAM is intended only for professional
researchers in carbon accounting and plant modelling, such as at the
Department of the Environment or Australia's CSIRO. The research edition
is available on request from the Department of the Environment on a
case-by-case basis.

**Differences in Appearance**

The research edition is distinguished from the standard edition by the
word "research" in:

- The version name on the *Startup* and *About* windows.
- The title bar of the [Main Window](217_Main%20Window.htm).

**Differences in Function**

Functionally, the research edition differs from the standard edition in
that:

- It includes the 3PG tree growth model. Both editions contain the
  3PG-lite model for computing the [Forest Productivity Index
  (FPI)](188_Forest%20Productivity%20Index.htm).
- It can calculate the Forest Productivity Index from scratch.
- It can do Nitrogen Simulation (other than just in the mulch, as part
  of [GENDEC](109_GENDEC.htm)).
- It includes version 26.5 of [RothC](114_RothC.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 049. Further Documentation 2016

**Further Documentation**

This topic discusses available documentation beyond this Help system.

**Diagrams**

Press the *Diagrams* button on the
[Configuration](150_Configuration.htm) page to open the [Diagrams
Window](50_Diagrams%20Window.htm), which shows diagrams of your plot
model (as specified by the settings on the *Configuration* page).

**Papers and Methodology**

See the National Inventory Report for further discussion of the
methodologies and literature drawn upon by FullCAM:

Department of the Environment (2015) National Inventory Report 2013
Volume 1. Commonwealth of Australia 2015.

Department of the Environment (2015) National Inventory Report 2013
Volume 2. Commonwealth of Australia 2015.

**National Carbon Accounting System Technical Reports**

Supporting technical documentation is provided in the National Carbon
Accounting System Technical Reports (see \"Technical Reports\" in the
FullCAM Help [Table of Contents](index.htm)).

A compendium of wood densities for Australian tree species can be found
in the [NCAS Technical Report No.
18](reps/TR18%20Woody%20Density%20Phase%201%20-%20State%20of%20Knowledge.pdf){target="reps18"}.

**Other**

The report *A Carbon Accounting Model (FullCAM) for the Australian
Continent* (Richards and Evans 2001)
([www.environment.gov.au]{.underline}) might be helpful in making
configuration choices, but FullCAM has changed significantly since 2001.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 050. Diagrams Window 2016

**Diagrams Window**

\[[Configuration](150_Configuration.htm) page : *Diagrams* button\]

Selecting the \'Diagrams\...\' button shows diagrams of the FullCAM
model, for the current configuration. The diagrams show the pools,
layers, and systems in your plot (see [Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm)), and the flows
of material that occur.

We recommend the diagrams as very useful in understanding how the
FullCAM model works.

**Diagrams**

Press the Diagrams button to see diagrams of the chosen configuration
(when the Configuration page is complete)

**Current limitations**

At this stage the diagrams only show:

1.  Processes --- Processes are the continuous actions that occur all
    the time, such as production or decomposition.
2.  Carbon -- The flow of carbon through the biomass, debris and soil
    pools, to and from the atmosphere.
3.  Layers --- A layer is a collection of similar pools, such as trees,
    crops, debris, soil, or products.

**Use**

Choose the layer or system from the menu to the left of the toolbar. You
may need to resize the window or scroll to see all of the diagram.

The options button to the right of the diagram menu controls some
options on how the diagrams are displayed. In particular, the *Show
Names* option switches on the display of programming names on the
diagrams, which is useful when reading the FullCAM technical
documentation or computer code.

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
(they do NOT join).

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
*Print preview* window by clicking the Close icon (the small cross) that
is located on the window title bar.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
