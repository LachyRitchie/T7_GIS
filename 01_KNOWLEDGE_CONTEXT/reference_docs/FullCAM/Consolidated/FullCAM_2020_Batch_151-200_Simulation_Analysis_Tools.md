---
version: 2020
batch_range: 151-200
batch_name: Simulation_Analysis_Tools
creation_date: 2025-08-28
total_files: 33
---

# FullCAM 2020 - Batch 151-200: Simulation Analysis Tools

## Table of Contents

- [153. Harvest 2020](#153-harvest-2020)
- [154. Post-Thin Period 2020](#154-post-thin-period-2020)
- [157. Site Area 2020](#157-site-area-2020)
- [158. Plant Trees 2020](#158-plant-trees-2020)
- [161. Plant Crop 2020](#161-plant-crop-2020)
- [163. Herbicide 2020](#163-herbicide-2020)
- [164. Plough 2020](#164-plough-2020)
- [166. Plot Files 2020](#166-plot-files-2020)
- [167. Plots in the Estate 2020](#167-plots-in-the-estate-2020)
- [168. Output Window 2020](#168-output-window-2020)
- [169. Select Outputs 2020](#169-select-outputs-2020)
- [170. Graph Lines 2020](#170-graph-lines-2020)
- [171. Select A Standard Event 2020](#171-select-a-standard-event-2020)
- [172. Overview of FullCAM 2020](#172-overview-of-fullcam-2020)
- [175. Graph Axes 2020](#175-graph-axes-2020)
- [177. Plot Simulation 2020](#177-plot-simulation-2020)
- [178. Frost Modifier 2020](#178-frost-modifier-2020)
- [180. Latitude and Longitude 2020](#180-latitude-and-longitude-2020)
- [181. Soil Nutrition Modifier 2020](#181-soil-nutrition-modifier-2020)
- [183. Soil Water Modifier 2020](#183-soil-water-modifier-2020)
- [184. Initial Crops 2020](#184-initial-crops-2020)
- [185. Initial Trees 2020](#185-initial-trees-2020)
- [186. One Plot in the Estate 2020](#186-one-plot-in-the-estate-2020)
- [188. Forest Productivity Index 2020](#188-forest-productivity-index-2020)
- [190. Contact Us 2020](#190-contact-us-2020)
- [193. Soil Inputs 2020](#193-soil-inputs-2020)
- [194. Vapour Pressure Deficit Modifier 2020](#194-vapour-pressure-deficit-modifier-2020)
- [195. Configure Event Or Time-Series 2020](#195-configure-event-or-time-series-2020)
- [196. Grazing Change 2020](#196-grazing-change-2020)
- [197. Initial Conditions For the Whole Plot 2020](#197-initial-conditions-for-the-whole-plot-2020)
- [198. Constituent Models In FullCAM 2020](#198-constituent-models-in-fullcam-2020)
- [199. Timing 2020](#199-timing-2020)
- [200. Site 2020](#200-site-2020)

---

## 153. Harvest 2020

**Harvest**

\[[Event Window](137_Event%20Window.htm) : *Harvest* panel\]

Enter the inputs specific to a harvest event.

**Introduction**

The forest counterpart of a harvest is a [Thin](140_Thin.htm) event

A harvest is the only means of forming agricultural products, apart from
grazing - see [Grazing Change](196_Grazing%20Change.htm) events, and can
take some of the crop offsite. See the [Product
Properties](47_Product%20Properties.htm) of each species.

GBF = Grains, buds, and fruit.

**Affected Portion**

The affected portion is the fraction of the agricultural system in which
the harvest takes place. It is typically the fraction of the plot area
that is harvested.

**Destination Percentages in the Affected Portion**

These destination percentages are applied to the portion of the
agricultural system that is affected by the harvest.

The destination percentages of litter (GBF litter, stalk litter, and
leaf litter) apply to all species whose material is present in the
litter.

*Crop Grades*

Specify the percentages of full crop grade harvests, which are specified
in turn for the species on the [Log Grades or Crop
Grades](http://www.fullcam.au/FullCAMServer2020/Help/263_Log%20Grades%20or%20Crop%20Grades.htm)
page.

For example

specifying 50% of grade 1 means applying a Grade 1 thin at 50%
intensity.\
specifying 100% of grade 3 and 0% for the other grades applies a grade 3
thinning.

You can mix and match, so long as the crop grade percentages do not
exceed 100%.

The *Extra Percentages to Debris* are for moving material from the
plants to the debris independently of (and in addition to) the crop
grade movements. Especially useful for management operations like
pruning. The total plant material moved to the debris is equal to the
amounts specified by the crop grades, plus the extra movements specified
here. The extra amount moved to the debris (above and beyond that
specified by the crop grades) is equal to or less than the extra amount
specified here (depending on whether or not the specified material is
available after the crop grades).

Check the *Clear all remaining crop mass to debris* box for this to
become a clearing harvest (all crop material not specified by the crop
grades is thrown into the debris).

Click *Show Destinations Percentages\...* to see all the crop grades for
the species, and the affect of the specified crop grade percentages. You
can see the destination percentages for the affected agricultural
system, which are equivalent ot the the manual percentage changes (see
next).

The advantage of the crop grades is that the detailed work of specifying
the destination percentages is done once in the species, then quickly
applied to many harvests, Because crop prices, harvest costs, and
transport costs are specified by species on the [Log Grades or Crop
Grades](http://www.fullcam.au/FullCAMServer2020/Help/263_Log%20Grades%20or%20Crop%20Grades.htm)
page, you must use the crop grade system if doing economic modelling
(see [Configure Other Options](138_Configure%20Other%20Options.htm)).

*Manual*

The destination percentages for each harvested pool (GBF, stalks,
leaves, coarse roots) must add to less than or equal to 100%. If they
add to less than 100% then the material without a destination remains on
the plot, in the agricultural system.

If the harvest affects all the stalks (the affected portion is 100% and
the stalk destination percentages add to 100%) then the harvest must
clear all of the other crop pools as well to be physically realistic
(because leaves die without stalks).

It is possible to retain root material on site to simulate a coppicing
effect.

**Example 1**. The portion of the agricultural system that is affected
by harvesting is 70%. The leaf destinations are 0% to biofuel, 40% to
leaf products, 30% to hay, straw and silage, and 20% to litter --- for a
total bark destination fraction of 90% (10% of the leaves stays on the
crops in the portion of the agricultural system affected by harvesting).
Then, of all the leaves on the plot, in this harvest 70% \* 40% = 28%
goes to leaf products, 21% becomes hay, straw or silage, 14% becomes
leaf litter, and the rest stays on the remaining crop plants.

**Example 2**. Suppose there is a harvest of an apple orchard in which
all of the orchard is harvested, 10% of the removed apple mass is left
on the plot, 60% is sent to the supermarket (as a GBF product), and the
rest is fed to pigs (thus qualifying as "hay, straw or silage"). Then
the affected portion of the agricultural system is 100%, the destination
percentage of GBF to GBF products is 60, the destination percentage to
hay, straw, and silage is 30, and the destination percentage to litter
is 10.

**Clearing Harvest**

For a harvest to be clearing and clear the agricultural system of its
crop, the affected portion must be 100% and the destination percentages
for each pool must sum to 100%.

**Volatisation Percentages of Nitrogen**

These are the percentages of the nitrogen from the material going to the
products that goes to the atmosphere.

For example, suppose that 20% of the leaves in the crop go to leaf
products. Then 20% of the nitrogen in the leaves would also go to the
leaf products --- except that some of that nitrogen is volatised (moves
to the atmosphere). Suppose that you specify the volatisation percentage
of nitrogen going to leaf products as 40. Then 20% \* 40% = 8% of the
nitrogen in the leaves of the crop moves to the atmosphere during a
harvest and 20% \* 60% = 12% of the nitrogen in the leaves of the crop
moves to the leaf products during a harvest.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 154. Post-Thin Period 2020

**Post-Thin Period**

\[[Event Window](137_Event%20Window.htm) : [Thin](140_Thin.htm) panel :
*Post-Thin Period* section\]

Specify the relative allocations of new growth to the tree components
not affected by a a thin in the period immediately after a thin.

**Details**

Tree growth can be modelled for modified behaviour for a period after a
thin, due to the response of the trees to the thin.

FullCAM models the post-growth differences using relative allocation
multipliers. Each multiplier multiplies the relative allocation that
would otherwise occur, for the whole length of the post-thin period. No
extra growth occurs, just the allocation of any growth to the various
components can be changed.

The modified behaviour during a post-thin period will be superceded by
the parameters in any sucsequent thinning event.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 157. Site Area 2020

**Site : Area**

\[[Site](200_Site.htm) page : *Area* panel\]

Enter information about the area of the plot.

**Use**

Choose either:

1.  No Area - The plot model is a *point* model --- it has no area, but
    represents a typical hectare. Output masses are reported in tonnes
    per hectare.
2.  Area - The plot is a piece of land with a specified area. Output
    masses are reported in tonnes.

The choice only affects the way the outputs are reported. Relative to
the *No area* choice, the outputs under the *Area* choice are multiplied
by the specified area in hectares (for appropriate outputs).

**Example**. Suppose that when you choose *No Area* the mass of carbon
in the trees after a simulation is 20 t/ ha. If you change your choice
to *Area* and specify the area as 7 hectares, when you rerun the
simulation the reported mass of carbon in the trees will be 140 t (20 t/
ha \* 7 ha = 140 t).

If economic modelling is on (see [Configure Other
Options](138_Configure%20Other%20Options.htm)), then the \"Area\" option
is automatically chosen and you will need to have a valid area (enter 1
hectare as the area if you effectively want the output masses to be
\"per hectare\").

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 158. Plant Trees 2020

**Plant Trees**

\[[Event Window](137_Event%20Window.htm) : *Plant Trees* panel\]

Enter the inputs specific to a tree-planting event.

**Species**

Select the species of tree to be planted from the drop-down list of
available species.

If the species required is not available, a new species must be entered
using the [Select a Species](56_Select%20a%20Species.htm) list on the
[Trees](215_Trees.htm) Tab.

**Specify Tree Size**

Select the method of specifying tree size by selecting one of the
options in the drop-down list.

**Age**

The age of the trees when planted, in years. 0 years represents planting
from seed

**Volume and Mass**

If the 'masses' option was selected from the 'Specify Tree Size By'
list, enter the mass of all tree components when the trees were planted.
If the 'Volume for stems, masses for other components' option was
selected, enter the mass of the non-stem tree components when planted,
in tonnes per hectare and the volume of stems of the trees at planting.
This volume will be converted to a mass in the FullCAM simulation by
multiplying it by the stem density.

**Tree Yield Formula: Growth Calibration**

Select whether the calibration used by tree yield formula consiiders the
application of grazing/browsing, is in a riparian/floodplain zone, or is
otherwise user-defined.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 161. Plant Crop 2020

**Plant Crop**

\[[Event Window](137_Event%20Window.htm) : *Plant Crop* panel\]

Enter the inputs specific to a crop-planting event.

**Age**

The age of the crop plants when planted, in years. For example, if
planting seedlings at six months, enter "0.5" years. For example, if
planting seeds enter "0.0" years.

**Masses**

The mass of the crop components when planted, in tonnes per hectare.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 163. Herbicide 2020

**Herbicide**

\[[Event Window](137_Event%20Window.htm) : *Herbicide* panel\]

Enter the inputs specific to a herbicide event.

**Details**

A herbicide event moves all crop material into the debris.

A herbicide event set at 100% coverage is classified as a clearing
event.

The only input specific to this event is the percentage of the area
being modelled that is affected.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 164. Plough 2020

**Plough**

\[[Event Window](137_Event%20Window.htm) : *Plough* panel\]

Enter the inputs specific to a plough event.

**Details**

A plough event moves all crop, debris, and mulch material into the soil,
as either decomposable or resistant plant matter.

The only input specific to this event is the percentage of the area
being modelled that is affected.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 166. Plot Files 2020

**Plot Files**

\[*Plot Files* page of the input window of an estate document\]

Specify the plot files that are used by the estate.

**Use**

An estate is a collection of plots. Each plot in the estate has a plot
file.

Details for a given plot file may be used by several plots in the
estate. For example, details of a typical pine plantation plot file
might be used for a 100 ha plot planted in 1982, a 20 ha plot planted in
1983, and so on. Therefore, the plot files are specified separately from
the plots in the estate (which saves users having to edit numerous plot
files).

All of the plot files in an estate must be in the same folder. Use the
Choose Folder button to specify the folder. Thus, you can move plot
files around on your computer as long as they remain within a single
specified folder.

Plot files are listed by name. Those coloured light blue are not used in
the estate as described, but are available for selection in the 'Plots
in the Estate\...' tab.

To add a new plot to the list of plot files, first ensure that the
desired new plot file is located in the appropriate folder specified
using the 'Choose folder\...' button. Then press 'New\...' select the
desired plot from the dialog box and press 'open\...' (or double-click
the desired plot file). To replace a plot file currently within the plot
files list select the plot file to be replaced, press 'Edit\...', select
the files list, select the new desired plot fie, and press 'Open\...'
(or double-click the desired plot file). This will update all plots in
the estate that used the old plot file to use the new plot file (thereby
substituting one plot file for another throughout the entire estate).
Press the 'Sort\...' button to arrange all plot files in the plot file
list alphabetically. To delete a plot file from the list, select the
file name and press the 'Delete\...' button. The plot file will be
removed from the estate but is not deleted from the folder containing
the various plot files.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 167. Plots in the Estate 2020

**Plots in the Estate**

\[*Plots in the estate* of the input window of an estate document\]

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

To add a plot to the estate use the 'New\...' button. After pressing the
'New\...', a dialog box opens in which a Start Time for the plot is
specified by entering the Calender year and simulation step within that
year when the plot was initiated. The Area of the plot is entered. The
Plot File is selected from the drop-down list. Press 'OK\...' to accept
the clause and enter the Plot file, its area and start time into the
estate.

To alter the Area or Start Time of a plot file within the estate, press
the 'Edit\...' button and alter the values that appear in the dialog box
as required.

The 'Clone\...&rdsquo; button can be used to enter an exact copy of the
plot file into the estate. This is useful when multiple plots of the
same tree or crop type with different areas or start times need to be
specified within the estate.

To remove a plot from the estate, select the plot and then press the
'Delete\...' button.

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

See [Estate Simulation](72_Estate%20Simulation.htm).

**Times: Growth Time Series and Events**

A single plot file can be used many times in an estate, and each of
these plots may have a different start time. If any of the species time
series (see [Growth Properties](42_Growth%20Properties.htm)) or events
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

1\. 10 ha, starting in 1940\
2. 20 ha, starting in 1950\
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

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 168. Output Window 2020

**Output Window**

\[[Output Windows](25_Output%20Windows.htm) : *Show Selected Output
Window* button\]

This window shows your selected outputs for the last simulation, either
in a graph or a table.

**Show Graph or Table, Choose Outputs**

To show the outputs as a graph, press the *View As Graph* button
(leftmost button in the toolbar in the Output window).

To show the outputs an a table of numbers, press the *View As Table*
button (second from the left in the toolbar in the Output window).

To change which outputs are showing in the graph and table, press the
*Choose Outputs* button (third from the left in the toolbar in the
Output window).

**Multiple Output Windows**

You may have more than one output window for a given document (plot or
estate). The outputs shown in each of the output windows can be
unrelated, which allows you to look at several different aspects of the
simulation simultaneously.

**Output Descriptions**

The *C mass* of X is the mass of carbon in X, that is, the mass of all
the carbon atoms in X.

The *N mass* of X is the mass of nitrogen in X, that is, the mass of all
the nitrogen atoms in X.

*Whole* means the whole of the land under consideration. The "whole
land" consists of the forest land and the agricultural land (one of
which may be missing, depending on the configuration). The land under
consideration is a plot in a plot simulation and an estate in an estate
simulation.

The *complete* mass of some land (either whole, forest, or agricultural)
is the mass on and due to that land. It includes the plants, debris,
mulch (if modelled), soil, any products from the land, and any fossil
fuels displaced by the burning or use of those products.

The *onsite* mass of some land (either whole, forest, or agricultural)
is the mass on that land. It includes the plants, debris, mulch (if
modelled), and soil.

*Yield rates* are the combined rates of production and turnover, and are
what is observed by simply measuring the plants periodically.

*Emit* and *sequester* refer to emissions to the atmosphere and removal
from the atmosphere.

Any moves of material between pools comprise a net movement. In most
cases a move is only possible in one direction, but moves involving the
minerals pools can often be bi-directional.

**Graph**

A few points to note when using the graphing feature:

- Double-clicking on a graph item opens the graph settings window at the
  appropriate place. Single-clicking an item selects it, whereupon you
  can drag it around the window, or resize it by dragging on a handle.
  Shift-select to select multiple items. For example, make the graph
  bigger by single-clicking on it, then dragging the lower-right handle
  of the graph.
- The content of the titles (graph, x-axis, and y-axis) can either be
  set automatically by FullCAM or entered manually. Double-click on the
  relevant title to open the graph settings window, and then choose
  either *Automatic* or *Manual*. If *Manual* is selected, type in the
  desired wording for the graph.
- The axis scales (that is, the starting number, ending number, and
  where the tick marks occur) can either be set automatically by FullCAM
  or chosen manually. Double-click on the axis numbers to open the graph
  settings window at the appropriate place. Choose either *Automatic* or
  *Manual*, and if *Manual* type in the desired parameters.
- The axis, line, and border widths are chosen in points. When they are
  shown on the screen they are rounded to the nearest whole number of
  pixels, but when printed they are shown as the correct number of
  points. Thus minor width changes will not show up on the screen, but
  will show up in a printed version.
- Change the order of the outputs in the legend by switching to the
  table and dragging the output columns to the desired order.

**Graphing Using an External Program**

The graph is very configurable and will satisfy most users. If you wish
to create a graph in a different program:

1.  Save the data to a file using the *Save to File* button
2.  Open the resulting `.csv` file in a graphing capable program.

Alternatively: go to the table view, select the data you want (see
selection shortcuts, below), copy it, then go to the other application
and paste it as needed.

**Table**

Each row shows the state of the simulation at the END of the simulation
step in the leftmost two columns. Thus, a table row shows the state of
the plot AFTER the simulation step labelled in the row. For example, if
there are 12 simulation steps per year then a row with *Step in Year*
equal to "Feb" shows the state of the simulation at the END of February.

The first row of results always shows the initial conditions of the
simulation. This row is coloured differently. Outputs that do not
describe the initial conditions in a non-trivial manner do not have an
entry in the initial conditions row.

Resize the columns by dragging the line separating the columns in the
header (the line between the names of adjoining columns). FullCAM
remembers your adjustments when it saves the plot.

Move a column by dragging its heading. FullCAM remembers the new
arrangement when it saves the plot. FullCAM uses the order of the
outputs in the table to make the graph legend (arrange the outputs in
the graph legend by moving the table columns around).

Change the mass units of a column (typically from t/ha to kg or Mt per
hectare) by selecting a cell in the column and using the mouse menu or
the *Increase/Decrease Mass Unit* buttons in the toolbar.

Change the size of the window, and thus the area available to the table,
by dragging a corner.

Select a column by double-clicking in the header or units rows of the
column (or, for the first two columns, in the units row only), and
select all the columns over to a second column by holding the shift key
down while double-clicking the second column.

Select a row (except the second) by double-clicking in the first two
columns of the row, and select all the rows down to a second row by
holding the shift key down while double-clicking the second row.

Select all the data by pressing the *Select All Data* button. Select
everything in the table by pressing the *Select All* button.

Make arbitrary selections of data and statistics by dragging the mouse.
Drags that start in the heading rows are ignored (because they change
the order of the columns instead), as are drags that start in the time
columns.

When you have a selection, you can copy it and can paste it into other
programs.

**Notes on Specific Outputs**

Production rates, turnover rates and yield rates are for the end of the
step. Consider using more simulation steps per year. For example: if you
have yearly steps, clear the forest in day 365 of a year (thus, the
clearing occurs at noon on day 365 of the year), and plant trees on day
1 of the next year (the trees are planted at noon of day 1), then the
reported production rate for the year (step) with the clearing will be
zero because the rate is for the last part of the year --- from noon
until midnight on day 365, when there were no trees.

The conditional irrigation output is only accurate in simulation steps
with no events (it is calculated from the conditional irrigation in the
period from the latter of the beginning of the step or the last event in
the step to the end of the step).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 169. Select Outputs 2020

**Select Outputs**

\[[Output Window](168_Output%20Window.htm) : *Select Which Outputs to
Show* toolbar button\]

Specify a set of FullCAM outputs for display by the accompanying output
window.

**Use**

There are about 800 possible outputs, but this window shows only those
outputs that are available in the configuration of the current document.

Single click on the icon or name of an output to select or deselect it.
Selected outputs are marked with a red tick.

The outputs are organised into folders, just like files are organised
into folders in Windows Explorer. Click on the plus (+) and minus (--)
buttons to expand and collapse the folders. A single click on the icon
or name of a folder selects or deselects everything within the folder.

The number of outputs is shown in a message at the bottom of the window.
Hover the mouse over the message with the number of outputs to find out
how many outputs are chosen but that are unavailable in this
configuration (they were chosen previously, while the plot was in a
different configuration).

Choosing flows and leaks as outputs slows down the simulation a little.
This slowness is only likely to be significant in simulations of large
estates.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 170. Graph Lines 2020

**Graph Lines**

\[[Output Window](168_Output%20Window.htm) : Double-click on graph to
open the *Graph Settings* window : *Lines* page\]

Choose the properties of an output line in the graph of an *Output
Window*.

**Details**

The line width is in points, for precise control over printed output.
For a given number of points the number of pixels depends on whether or
not you are using small fonts.

If the line width on the screen is not equal to one pixel, then the dash
and dotted styles are drawn on the screen as solid.

Note the buttons for automatically assigning colours and for making all
line widths the same as the first (in the legend) on the output window
toolbar.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 171. Select A Standard Event 2020

**Select A Standard Event**

\[[Event Window](137_Event%20Window.htm) : *Insert Standard Values*
button\]

This window is for choosing between the available standard events, when
inserting standard values into an event.

**Use**

Select a standard event then press the *OK* button, or double-click on
an event. The event thus chosen will be the one whose values replace the
event currently being edited.

The standard events all belong to a species. You can choose any one of
the events of the appropriate type, regardless of species.

Events in red are not ready.

See [Standard Events of a
Species](142_Standard%20Events%20of%20a%20Species.htm)

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 172. Overview of FullCAM 2020

### Overview of FullCAM

An overview of what FullCAM can do.

### Introduction

FullCAM is a model for tracking the greenhouse gas emissions and changes
in stocks of carbon and nitrogen associated with land use and
management. FullCAM is a fully integrated Carbon Accounting Model (CAM)
for estimating and predicting all biomass, litter and soil carbon pools
in forest and agricultural systems. In addition, it accounts for changes
in major greenhouse gases, nitrogen cycling and human-induced land use
practices.

FullCAM is the model used to construct Australia\'s national greenhouse
gas emissions account for the land sector. Users of the model can
determine project-based results on a similar basis to Australia\'s
official recording of greenhouse emissions trends for land use and land
use change.

FullCAM was developed to integrate data on land cover change, land use
and management, climate, plant productivity, and soil carbon over time
to provide a dynamic account of the changing stock of carbon in
Australia\'s land systems since 1970.

FullCAM incorporates a suite of verifiable component models, adapted for
use at a fine spatial (25 m) and temporal (monthly) resolution for the
Australian continent, including:

- [CAMFor](77_CAMFor.htm) -- for forest systems
- [CAMAg](78_CAMAg.htm) -- for cropping and grazing systems
- [RothC](114_RothC.htm) -- for agricultural soil carbon

FullCAM can run each of these sub-models in isolation or in combination.
See [Constituent Models In
FullCAM](198_Constituent%20Models%20In%20FullCAM.htm).

The sub-models used within FullCAM can be integrated into various
combinations to suit the data available and outputs required. FullCAM
may be used for tracking of carbon and nitrogen stocks and flows in
different forest and agricultural systems, and can also be used more
simply to review project-based results for small land holdings.

Specifically, FullCAM calculates the carbon and nitrogen flows
associated with:

- Forests, including the wood products made from wood harvested from the
  forest. It calculates the carbon in the trees, debris, mulch, soils,
  and wood products, and the carbon and nitrogen exchanged with the
  atmosphere, due to thinnings, multiple rotations, and fires.
- Agricultural systems, which can be cropped or grazed systems. FullCAM
  calculates the carbon and nitrogen in the plants, debris, mulch, soil,
  and products, and the carbon and nitrogen exchanged with the
  atmosphere, while including the effects of harvest, ploughing, fire,
  herbicides, and grazing.
- Afforestation and reforestation systems, which are represented and
  modelled as transitions from agricultural systems to forests.
- Deforestation systems, which are represented and modelled as
  transitions from forests to agricultural systems.
- Mixed systems (such as in agroforestry) -- assorted combinations of
  the systems above.

FullCAM calculates the carbon and nitrogen stocks and flows (including
the effect of nitrogen shortages on plant growth) for land subject to
different land use and management activities.

FullCAM also has the ability to calculate the fossil fuel displacement
values by use of wood or agricultural products (including bioenergy).
For instance, if forests or crops are used for bioenergy (energy derived
from burning them or their residues), FullCAM can calculate how much
fossil fuel based energy emissions this would equal (given 1 tonne of
biomass burned approximates to x kilojoules of fossil fuel emissions).
This gives users a better understanding of the relative impacts of their
land use practices on greenhouse emission levels.

FullCAM can also be used to review project-based results for small land
holdings.

### Main Function

The main function of FullCAM is to model the stocks and flows of carbon
and nitrogen in mixed forest and agricultural systems. This includes
tracking carbon and nitrogen within pure agricultural and forestry
systems, as well as within transitions from an agricultural activity to
a forestry activity or agroforestry system (and vice versa), and taking
into account how these systems and their proportional contributions
change over time. FullCAM models all carbon and nitrogen pools, plus
interchanges and fluxes within the:

- Plants
- Debris
- Soil
- Products
- Atmosphere

FullCAM tracks the movement of carbon, from its removal from the
atmosphere through the growth of plants, all the way through to its
return to the atmosphere -- after potentially passing through plants,
debris, soil, grazing animals or wood or agricultural products.

FullCAM can model carbon in up to:

- Six tree components
- Five crop components
- Twelve forest debris and ten agricultural debris components
- Six forest soil and six agricultural soil components
- Forest products
- Agricultural products.

FullCAM can be configured into many different models, and there are
hundreds of outputs to choose from. FullCAM can model different tree and
crop species, and also can account for changes in carbon due to
management events such as plantings, thinning, harvest, fire, grazing,
and ploughing.

**Capabilities**

- [Plot Simulation](177_Plot%20Simulation.htm) tracks all the carbon
  associated with a plot, both on the plot and in the products produced
  by the plot
- [Estate Simulation](72_Estate%20Simulation.htm). An estate is an
  arbitrary collection of plots, each with its own area.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 175. Graph Axes 2020

**Graph Axes**

\[[Output Window](168_Output%20Window.htm) : Double-click on graph to
open the *Graph Settings* window : *Axes* page\]

Choose the properties of the graph axes of an *Output Window*.

**Details**

*Major ticks* are the larger marks along the axis. Major ticks are
usually labelled with a number. Gridlines, which are lines across the
whole graph, can occur at major ticks.

*Minor ticks* are the smaller marks along the axis. Minor ticks are not
labelled and do not have gridlines.

To set the scale manually, choose the *Manual* button in the *Scale*
area, then enter numbers for the five scale parameters. You can copy the
current graph scale parameters to the editing boxes by pressing the
*Load Current Graph Values* button. The *Minimum* and *Maximum* values
are the starting and finishing values of the axis. The *Major tick unit*
is the change in value of the axis parameter between consecutive major
tick marks. Similarly for minor ticks. The *Ticks start at* value is the
value at which both the major and minor tick marks start (and continue
thereafter), and must be equal to or slightly less than the minimum
value.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 177. Plot Simulation 2020

**Plot Simulation**

Some general aspects of simulating a plot in FullCAM.

**Timing: Steps and Time Periods**

The simulated time is partitioned into equal-length *steps*. Each step
may be punctuated by one or more events, because an event may occur at
any time.

A *time period* is the period of time from an event or step boundary to
the next event or step boundary (whichever occurs first). During a time
period, the only things that happen are processes (because, by
definition, there are no events). Within each time period, all the
processes are simulated as a single calculation that computes the effect
of the processes for the whole time period.

**System Separation**

The forest and agricultural systems are completely separate in a FullCAM
simulation, except for interaction through the [Forest
Percentage](206_Forest%20Percentage.htm). The forest and agricultural
systems have no effect on each other, except that the forest percentage
partitions the production in the two systems.

**Species Dependency**

An input is *species-dependent* if it depends on the species of plant by
describing a characteristic of material unique to that particular
species. Species dependency extends down to and includes the debris
layer, and across to the product layer, but extends no further:

- Most of the inputs for the plant, debris and product layers are
  species dependent.
- None of the inputs for the mulch, soil, mineral or atmosphere layers
  are species dependent. Once in the mulch or soil, it is sufficient
  just to classify the plant material as either *resistant* or
  *decomposable* (and if mulch is being simulated, the resistant
  material as either *less resistant* or *more resistant*).

**Rationing of Scarce Resources**

If a resource is scarce (such as available nitrogen from the mineral
pool), the processes that use that resource compete for it. During each
time period:

1.  At the beginning of the time period, we compute all the *non-limited
    moves* of material from pool to pool due to each process (the moves
    that would occur if there were no scarcity of resources).
2.  The resources are rationed to each process on either a pro-rata or
    sequential basis (the choice is a plot input).
    - Pro-rata: Each actual move (exchange of material) is equal to the
      corresponding non-limited move multiplied by the *rationing
      fraction r*, where *r* is equal to the actual resource available
      divided by the sum of the amounts of the resource required by the
      non-limited moves.
    - Sequential: An order of processes that affect the resource that
      was specified in the plot input. For each process in turn, the
      moves (and exchanges of scarce resources) due to the process are
      recomputed --- and the remaining amount of scarce resource is
      updated after each process. Generally, early processes are
      allocated as much as they need and later processes (events)
      receive nothing.
3.  All the moves are applied.

The justification for pro-rata rationing is that each process is assumed
to use the scarce resource it requires at a constant rate over the time
period. Therefore, if there is not enough of the resource, then all of
the processes will be limited at the same time, having each received the
same fraction of its desired amount. Unless you are aware of the process
order for sequential rationing, it is recommended that resources be
rationed on a pro-rata basis.

Thus, for each time period, the processes are simulated as being
continuous and simultaneous.

The only scarce (potentially limiting) resource included in FullCAM at
this stage is available nitrogen.

**Example**. Suppose that in a given period of time:

- Process A requires 10 tN/ha of nitrogen (N) from the mineral pool.
- Process B requires 5 tN/ha.
- Process C requires 1 tN/ha.

Thus a total of 16 tN/ha of N is needed from the mineral pool. Suppose
there is only 7 tN/ha of N in the mineral pool. Then, under pro-rata
rationing, each process receives only 7/16 (the rationing fraction) of
what it requires:

- Process A gets (7/16) \* 10 tN/ha of N from the mineral pool
- Process B gets (7/16) \* 5 tN/ha
- Process C gets (7/16) \* 1 tN/ha.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 178. Frost Modifier 2020

**Frost Modifier**

\[[Site : Temperature](13_Site_Temperature.htm) window : *Frost
Modifier* button\]

**Details**

This time series is only used if the forest productivity index is
computed from scratch **and** the frost modifier is input directly (that
is, it is not computed by 3PG-lite) --- see [Configure Tree
Production](108_Configure%20Tree%20Production.htm).

The frost modifier is dimensionless, and between 0 and 1. Higher values
result in more NPP being produced by the trees. A value of 1 implies no
frost, and 0 implies no NPP is produced.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 180. Latitude and Longitude 2020

**Latitude and Longitude**

FullCAM\'s use of latitude and longitude.

**Decimal Degrees**

Always enter latitude and longitude in FullCAM in decimal degrees. All
spatial measurements in FullCAM are defined and exact in terms of
degrees, although we commonly speak of length approximations in
kilometres or metres.

Latitude measures degrees from the equator; positive latitudes are in
the northern hemisphere, negative latitudes are in the southern
hemisphere (Australia is at about --30 degrees latitude). Goes from --90
deg N to +90 deg N ("N" is for = "north").

Longitude measures degrees east of Greenwich, London. Goes from --180
deg E to +180 deg E ("E" is for "east").

**Conversion from Minutes and Seconds**

To convert between decimal degrees and minutes and seconds:

> 1 minute = 1/60 degree\
> 1 second = 1/ 60 minute = 1/3600 degree.

**Example.** 12 degrees, 15 minutes and 1 second (12 deg 15' 1") is
equal to

> 12 degrees + 15 / 60 degrees + 1/3600 degrees\
> = 12 + 0.25 + 0.000277777778 degrees\
> = 12.25028 degrees (to about 1m precision)

**Length Approximations**

One degree of latitude is roughly 100 km (closer to 110 km). Except near
the poles, a degree of latitude is roughly equal in length to a degree
of longitude. Thus:

- One hundredth of a degree (0.01 degrees) is about 1 km
- Five decimal places gives about 1m precision (0.00001 degrees is about
  a metre).

**Example.** To move about 1 km west from 131.08123 deg E, move to
131.07123 deg E.

The size of a degree of longitude varies with latitude. For Australia, a
degree of longitude at the tip of Cape York corresponds to approximately
109km, while at southern Tasmania it is approximately 80km.

We use these length approximations often when talking about spatial
grids and cells, but the size of the cells and grids is defined in terms
of degrees. For example, when we talk about a woodiness cell of "25
metres" or "25 m resolution" what we mean is the cell of the woodiness
grid is 0.00025 degrees square --- as drawn on the ground, such a the
cell has slightly curved edges, the northern and southern edges have
slightly different lengths, and the northern and eastern edges may have
quite different lengths.

**Curvature of the Earth**

Grids and their cells are specified as rectangles and squares
respectively, as measured in degrees of latitude and longitude. Due to
the curvature of the earth, the outline of the area of earth covered by
a grid is not quite rectangular. Likewise, the cells are not quite
square: the north-south side of each cell is not quite the same as the
length of the east-west sides, and the east-west side nearer the equator
is longer than the east-west side nearer the nearest pole.

FullCAM corrects for these effects when reporting areas, that is,
FullCAM always reports true areas (areas as you would measure on the
earth\'s surface).

**Australia**

Latitude and longitude coordinates must be from the Geographic Datum of
Australia (GDA) system, not from the Australian Map Grid (AMG) system.

Mainland Australia and Tasmania extend approximately from latitude
--10.6 deg N (Cape York, Queensland) to --43.6 deg N (South-east Cape,
Tasmania), and longitude 113.2 deg E (Steep Point, Western Australia) to
153.6 deg E (Cape Byron, NSW).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 181. Soil Nutrition Modifier 2020

**Soil Nutrition Modifier**

\[[Site : Productivity](64_Site_Productivity.htm) window : *Soil
Nutrition Modifier* button\]

This [Time Series Window](135_time-series%20window.htm) is where enter
the soil nutrition modifier rating for the plot.

**Details**

The soil nutrition modifier is dimensionless, and typically between 0.75
and 1.25. Higher values result in more NPP being produced by the trees.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 183. Soil Water Modifier 2020

**Soil Water Modifier**

\[[Site : Water](12_Site_Water.htm) window : *Soil Water Modifier*
button\]

**Details**

The soil water modifier is dimensionless, greater than 0, and usually
less than 1. Higher values result in more NPP being produced by the
trees.

The soil water modifier is restricted to values between 0 and 1.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 184. Initial Crops 2020

**Initial Crops**

\[[Crops](216_Crops.htm) page : *Initial Crops* button\]

\[[Initial Conditions](205_Initial%20Conditions.htm) page :
*Agricultural* panel : *Crops* button\]

Describe the crop growing in the agricultural system at the start of the
simulation.

**Species**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Even if there are no crops growing, there may be crop material in the
[Initial Debris](31_Initial%20Debris.htm) or [Initial
Products](33_Initial%20Products.htm) so you **must** specify an initial
species.

Enter the initial crop species. Only one crop species can grow in the
forest at once (see the [Select a Species](56_Select%20a%20Species.htm)
panel), so there can only be one initial crop species. The species on
the menu are those on the *Crops* page. The menu contains only a blank
line if there are no crop species, in which case you need to create a
new species on the *Crops* page.

The initial crop species is the (only) species of any crop plants
growing in the agricultural system. Also, any debris in the agricultural
system, or any agricultural products in use or in the landfill, are
assumed to belong to that species.

**Existence**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Specify whether there is a crop of plants growing in the agricultural
system at the beginning of the simulation. If there is not, then the
agricultural system is clear and the other inputs need not be entered.

**Ages**

Crop ages are used to access the crop time series.

The age of the oldest plants in the crop is the age of the crop --- the
number of years since the current crop was planted, plus the age of the
plants when they were planted.

The average age of the plants in the crop reflects the new plants that
are assumed to have grown after removal of plants in any past partial
harvestings. The average plant age must be less than the age of the
oldest plants.

The average age must not exceed the age of the oldest plants, or both
boxes go red.

Unless there are harvesting events that remove some but not all of the
crop, the age of the oldest plants will equal the average age of the
plants.

**Masses**

The masses of the various crop components at the start of the
simulation, in tonnes per hectare.

Note that these are true masses, not carbon masses as in some other
inputs. The "mass" of some material is the weight of all of the
material; the "carbon mass" of the material is the weight of the carbon
in the material. The carbon masses of most crop components are about
half of their masses.

Convert between the masses and carbon masses using the carbon fractions
(see [Plant Properties](43_Plant%20Properties.htm)).

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
crop values (set via the *Initial Crops* button on the *Standard
Information for the Species* panel of the *Crops* pages, see [Standard
Information for the
Species](146_Standard%20Information%20for%20the%20Species.htm)). The
button is disabled if the standard initial crop information for the
species is not ready (incomplete or has invalid values).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 185. Initial Trees 2020

**Initial Trees**

\[[Trees](215_Trees.htm) page : *Initial Trees* button\]\
\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest*
panel : *Trees* button\]

Describe the trees growing in the forest system at the start of the
simulation.

**Species**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Even if there are no trees growing, there may be carbon in the [Initial
Debris](31_Initial%20Debris.htm) or [Initial
Products](33_Initial%20Products.htm) to consider. This is only possible
if an initial species is specified to provide the conditions.

Only one tree species can grow in the forest at any one time (see the
[Select a Species](56_Select%20a%20Species.htm) panel). The species
listed on the pull down on the menu are those on the *Trees* page. If
there are no tree species available, a new species can be created on the
*Trees* page or downloaded by the [Data
Builder](132_Data%20Builder.htm).

**Existence**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Specify whether there are trees growing in the forest at the beginning
of the simulation. If there are not, then the forest is clear and the
other inputs need not be entered. Trees will not grow until a planting
event is created to establish them.

When using [Data Builder](132_Data%20Builder.htm), if a species is set
as the initial tree species then it shall by default set the existance,
but only if a crop species has not already been set as an initial
species.

**Specify Tree Size By**

The intial biomass of the forest can either be set on the basis of mass
or volume, on in relation to the [Maximum Aboveground
Biomass](36_Site_Maximum%20Aboveground%20Biomass.htm). The method chosen
should be appropriate to the configuration of tree production.

If the selection is as a percentage of maximum tree biomass, then the
initial conditions for the forest will be set at their site maximum
scaled to the [Forest Percentage](206_Forest%20Percentage.htm). Bear in
mind that trees will still grow relative to their age, and so this
option should generally only be used when modelling the removal of
forest at the start of the simulation.

If the selection is as a percentage of tree-age biomass, then the intial
conditions for the forest will be set as a proportion of their site
maximum based on the age profile of the trees, and scaled to the [Forest
Percentage](206_Forest%20Percentage.htm). This is the recommended choice
for modelling a forest in most circumstances and is used by the [Data
Builder](132_Data%20Builder.htm).

**Masses**

Available when specifying tree size by mass or volume.

The masses of the various tree components at the start of the
simulation, in tonnes of dry matter per hectare. Note that these are
true masses, not carbon masses as in some other inputs.

**Volumes**

Available when specifying tree size by volume for stems.

The stem volume is the total volume of stems in the forest, in cubic
meters per hectare. This volume will be converted to a mass in the
FullCAM simulation by multiplying it by the stem density.

**Percentage of biomass**

Available when specifying tree size by percentages of maximum biomass or
tree-age biomass

The proportions of biomass in each pool are determined here. The
resulting biomass and carbon in each pool is calculated relative to the
Site [Maximum Aboveground
Biomass](36_Site_Maximum%20Aboveground%20Biomass.htm), and if selecting
tree-age biomass then the Age.

**Ages**

Tree ages are used to access the tree time series.

The age of the oldest trees in the forest is the age of the forest. The
average age of the trees in the forest reflects the new trees that are
assumed to have grown after removal of tree stems in past thinnings. The
average tree age must be less than the age of the oldest trees.

Unless there are thinning events that thin some but not all of the tree
stems, the age of the oldest trees will equal the average age of the
trees. Setting both ages to a very large number will approximate
maturity.

**Numbers of Trees**

Enter the number of stems per hectare, which is the stand stocking
level.

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
tree values (set via the *Initial Trees* button on the *Standard
Information for the Species* panel of the *Trees* pages, see [Standard
Information for the
Species](146_Standard%20Information%20for%20the%20Species.htm)). The
button is disabled if the standard initial trees information for the
species is not ready (incomplete or has invalid values).

**Tree Yield Formula: Growth Calibrations**

The [Tree Yield Formula](42_Growth%20Properties.htm) may have
alternative empirical calibrations available for a given tree species.
Options are listed here in the drop down menu. The Tree Yield Formula
parameters applied under these alternative options are listed under the
Trees-Growth tab.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 186. One Plot in the Estate 2020

**One Plot in the Estate**

\[[Plots in the Estate](167_Plots%20in%20the%20Estate.htm) : *New* or
*Edit* button\]

This window specifies the properties of one of the [Plots in the
Estate](167_Plots%20in%20the%20Estate.htm).

**Details**

Simulation of the plot begins in the year and step of the start time
specified here. For example, if a plot start year is set to 1985 and its
start step to 6 (which would be June, if the estate timing was 12 steps
per year), then the plot will be simulated starting with step 6 in 1985
of the estate simulation.

If the estate simulation starts before the plot simulation (the estate
simulation start time is before the plots start time), then the plot
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

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 188. Forest Productivity Index 2020

**Forest Productivity Index (FPI)**

\[[Site : Productivity](64_Site_Productivity.htm) window : *Forest
Productivity Index* button\]\
This [Time Series Window](135_time-series%20window.htm) is where enter
the forest productivity index (FPI) for the plot.

**Forest Productivity Index (FPI)**

This window provides options for computing the FPI, which is required if
the tree yield formula is used to compute tree growth. It is a
simplified variant of the 3PG model and produces a time-series (monthly
or annual) index that is equivalent to a site class.

As an alternative to calculating the FPI, a value from the NCAS
modelling can be obtained for the latitude and longitude specified in
the [Data Builder](132_Data%20Builder.htm) window.

**Details**

The FPI is used if the tree production method is the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) and the FPI is not calculated
from scratch (see [Configure Tree
Production](108_Configure%20Tree%20Production.htm)).

The FPI is a dimensionless measure of site productivity due to soil,
sunlight, rainfall, evaporation, and frost. The FPI varies during the
year. The FPI is described in [NCAS Technical Report
No.27](reps/TR27%20Biomass%20Estimation%20Approaches%20for%20Assessment%20of%20Stocks%20and%20Stock%20Change.pdf),
with recent updates being described by Paul and Roxburgh (2019).
Improved FullCAM-prediction of woody growth increments. Report prepared
for the Department of the Environment and Energy. CSIRO Land and Water,
Canberra.

Enter the FPI as an "annualised rate", which is what the FPI would be if
it continued at that rate for a whole year. Thus the FPI is like
temperature (if only the annual figure is given, the annual figure
applies in each month), rather than like rainfall (if only the annual
figure is given, one twelfth of the annual figure in each month). In
FullCAM, the FPI is always reported as an annualised rate.

FPI values range from 0 to 100, but the average FPI over a year rarely
exceeds 25. On a good site the FPI might vary between 6 in a poor month
to 60 in the best month. However the average of the FPI over a year is
rarely more than 25. Thus the yearly average of the numbers you enter
should only exceed 25 for exceptionally productive sites.

If actual site data is available, enter it in this time series. If not,
use [Data Builder](132_Data%20Builder.htm) to download estimated monthly
FPI. The derivation of this data is described in [NCAS Technical Report
No.23](reps/TR23%20Developing%20a%20National%20Forest%20Productivity%20Model.pdf).

The FullCAM model utilises the Tree Yield Formula (Eq. 1, Waterworth et
al. 2007) to predict increments in above-ground biomass (AGB) within
forests, woodlands, shrublands and plantations.

AGB = M x *y* x \[exp(-k / A2) - exp(-k / A1) \] x (FPIt / FPIave)   
**Eq. 1**

where, AGB = Current annual increment in above-ground biomass (AGB, Mg
DM ha-1 year-1) M is the maximum AGB in undisturbed native vegetation
(Mg DM ha-1), and for Australian vegetation is estimated as:       M =
(6.011 sqrt(FPIave) - 5.291)^2^ (Waterworth et al. 2007). *y* = value of
the Type 2 multiplier to account for factors that increase growth
potential at a given site (e.g. planting configuration, Snowdon 2002)
A1, A2 = age (years) in year 1 and 2, respectively, etc. k = 2 x G -
1.25, where G = tree age of maximum growth rate (years), FPIt = Annual
Forest Productivity Index over the period A1 to A2, and is the sum of
site factors (soil type, fertility and climate) driving growth,
regardless of the type of planting or its age (Kesteven and Landsberg
2004); and FPIave = mean long-term average annual forest productivity
index, which is independent of age (Kesteven and Landsberg 2004).

In FullCAM, inter-annual variation in climatic conditions (e.g.
intermittent droughts) are accounted for by annually adjusting the TYF
predicted increment in woody growth by the fraction:

FPIt / FPIave    **Eq. 2**

Hence, in a drought year where FPIt \< FPIave, the growth increments are
adjusted down.

Across the period of simulation, the average increment multiplier given
in Eq. 2 needs to be close to 1.0 to enable the default TYF curve to
attain the expected long-term maximum above-ground biomass of the stand
(M) is attained. Due to the formulation of FullCAM\'s TYF, M will not be
achieved if FPIave is less than the mean of the FPIt values for the
years across which the simulation is run. Running a simulation over a
period across which the average of the FPIt values are x% lower (or
higher) than the FPIave will, for all years, result in biomass
predictions that are x% lower (or higher than) the default TYF curve
with a maximum AGB equal to M. Care is therefore required when
considering the definition of FPIave. The definition of FPIave applied
in the TYF is the average of the FPIt values between the years 1970 and
2017. This definition of FPIave is what is downloaded automatically from
the [Data Builder](132_Data%20Builder.htm). However, for years for which
there is no FPI data available, and where the user has selected to
extrapolate FPI data based on the average, FPIt is taken to be the
average of the FPIt values observed over the period of simulation. To
enable this, an exception is applied in the first year without an
observed value for FPIt. For that year, an adjustment is applied to
prevent the last year with an observed FPIt from having undue influence
on estimates over time.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 190. Contact Us 2020

**Contact Us**

For further information about FullCAM, please consult the [FullCAM
website](http://fullcam.com){target="_blank"}.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 193. Soil Inputs 2020

**Soil Inputs**

\[[Soil](203_Soil.htm) page : *Forest* or *Agricultural* panel :
*Inputs* button\]

Specify the material that enters the soil. See the
[RothC](114_RothC.htm) soil pool abbreviations.

**Soil Input Percentages of Humified Mulch**

Specify where the humified mulch goes to within the active soil. FullCAM
only includes mulch if you have configured
[GENDEC](http://www.fullcam.au/FullCAMServer2020/Help/109_GENDEC.htm) to
model the mulch, and this section is only on if RothC models the active
soil.

With such a configuration, each pool in the mulch undergoes
humification, the process whereby material is transported from the mulch
down to the soil. This material, the humified mulch, can enter the DPM,
RPM or HUM pools within the soil. Specify, for each mulch pool, which of
these soil pools the humified mulch enters.

Humified mulch from the soluble mulch pools, being decomposable, can
only go to the DPM or HUM pools. Humified mulch from the more-resistant
and less-resistant mulch pools, being resistant , can only go to the RPM
or HUM pools. Humified mulch from the live microbes pools contains both
decomposable and resistant material, so specify the percentage that goes
to DPM and RPM versus HUM.

Naturally, the sum of each pair of percentages is 100%. Therefore the
HUM percentage is calculated automatically from the DPM/RPM value.

**Typical values used are:**

  Variable                    To DPM or RPM   To HUM
  -------------------------- --------------- --------
  Plant Soluble litter             100          0
  Plant Less Resistant             80           20
  Plant More Resistant             50           50
  Microbial Soluble Litter         100          0
  Microbial Less Resistant         60           40
  Microbial More Resistant         40           60
  Live Microbes                    75           25

**Soil Input Percentages of Broken-Down Litter**

Specify where the broken-down litter goes to within the active soil.

The material in each litter pool breaks down, thereby transporting
material from the litter to the soil. This material, the broken-down
litter, can enter the DPM, RPM or HUM pools within the soil. Here, you
specify, for each type of broken down litter, which of these soil pools
the broken-down litter enters.

The decomposable and resistant broken-down litter always goes to either
the DPM, RPM or HUM.

Naturally, the sum of each pair of percentages is 100%. Therefore the
HUM percentage is calculated automatically from the DPM/RPM value.

**Typical values used are:**

  Variable               To DPM or RPM   To HUM
  --------------------- --------------- --------
  Decomposable Litter         90           10
  Resistant Litter            90           10

**Manure from Offsite**

Manure from offsite (from outside the plot) may be added to the forest
or agricultural soil. Offsite manure inputs are only available if RothC
is used to model the soil.

Enter the time series of manure carbon additions or add manure
application events to the 'Events' tab depending on how manure additions
were configured in the 'Events' or time series window of the
'Configuration tab'

Manure from offsite may be added to the forest or agricultural soil.
Enter the carbon mass in the manure, in tonnes per hectare, over time.

'Offsite' means 'from outside the plot'. Offsite manure inputs are only
available if Roth-C is used to model the soil.

In an agricultural system, manure from animals on the plot is dealt with
by grazing events (plant material eaten by grazing animals becomes
fodder, which may move to destinations including the DPM an RPM pools of
the soil). The offsite manure is the only explicit treatment of manure
by FullCAM.

Specify the percentages of the carbon in any offsite manure added to the
soil that move to the various organic soil components. The percentages
add to 100%; the HUM percentage is automatically calculated from the
others.

Note that manure from offsite and grazing are entirely separate. The
manure inputs entered here have no effect on any grazing manure, and
vice versa.

**Typical values used are:**

Variable

Percentage of Manure

DPM

49

RPM

49

BIO-F

0

BIO-S

0

**Plant Residues**

Plant residue inputs are plant material from the debris or mulch that
enters the soil. The material enters the DPM soil pool if it is
decomposable, or the RPM soil pool if it is resistant. Specify the total
amount of plant material entering the soil over time.

Plant residues can only be specified here if you are simulating the
[Soil](203_Soil.htm) by itself. If you are simulating a multilayer
system, then the plant residues from the debris or mulch are
automatically calculated, so an explicit input for plant residues is
neither required nor desired.

The ratio of DPM to RPM is the mass of DPM divided by the mass of RPM in
the plant matter added to the soil, and is also known as the "quality
factor for incoming plant debris". Typical values for the ratio of DPM
to RPM are:

1.44 - Most agricultural crops and improved grassland\
0.67 - Unimproved grassland and scrub (including savanna)\
0.25 - Deciduous and tropical woodland.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 194. Vapour Pressure Deficit Modifier 2020

**Vapour Pressure Deficit (VPD) Modifier**

\[[Site : Water](12_Site_Water.htm) window : *VPD Modifier* button\]

This [Time Series Window](135_time-series%20window.htm) is where you
specify the VPD modifier (modVPD) used by
[3PG](http://www.fullcam.au/FullCAMServer2020/Help/115_3PG.htm)-lite.

**Details**

This time series is only used if the [Forest Productivity Index
(FPI)](188_Forest%20Productivity%20Index.htm) is computed from scratch
and the [Soil Water Modifier](183_Soil%20Water%20Modifier.htm) is
computed by
[3PG](http://www.fullcam.au/FullCAMServer2020/Help/115_3PG.htm)-lite ---
see [Configure Tree Production](108_Configure%20Tree%20Production.htm).

The VPD modifier is dimensionless, greater than 0, and usually less
than 1. Higher values result in more NPP being produced by the trees.

The VPD modifier is restricted to values between 0 and 1.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 195. Configure Event Or Time-Series 2020

**Configure Event Or Time Series**

\[[Configuration](150_Configuration.htm) page: *Events or Time Series*
button\]

Specify certain inputs as either by time series or by events.

Press the 'Events' or 'Time Series' button to access the window where
you decide where various sorts of inputs are treated as event or as time
series data.

**Introduction**

FullCAM only allows events if a multilayer plot is modelled (see
[Configure the Plot](6_Configure%20the%20Plot.htm)), so if modelling a
plot that is not multilayer then time series data will always be used.

You can change these settings at any time without losing any of the time
series or event data you may have entered.

If you do not want any of a particular input (for example, there is no
irrigation in your simulation), it is easiest to set its input type to
*Events*, but do not create any events of that type. This way you will
not be asked for the time series input.

Some inputs, such as irrigation, can be specified either as events or as
time series. This is where you configure how they are to be specified.

Unless a forest, agricultural or mixed system are modelled then FullCAM
does no allow events and thus time series data will always be used.

**Irrigation**

For a discussion of irrigation, see [Site : Water](12_Site_Water.htm).

Set the irrigation:

- As time series: The [Definite
  Irrigation](92_Definite%20Irrigation.htm) and [Conditional
  Irrigation](91_Conditional%20Irrigation.htm) time series
- As events: [Irrigation Change](54_Irrigation%20Change.htm) events.

**Manure-From-Offsite Added to the Soil**

Manure from offsite can be added to the soil whenever the soil is
modelled.

Set the manure additions:

- As time series: The [Manure Inputs to Soil from
  Offsite](101_Manure%20Inputs%20to%20Soil%20from%20Offsite.htm) time
  series
- As events: [Manure-From-Offsite
  Change](62_Manure-From-Offsite%20Change.htm) events.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 196. Grazing Change 2020

**Grazing Change**

\[[Event Window](137_Event%20Window.htm) : *Grazing Change* panel\]

Enter the grazing inputs that apply from this event until the next
grazing event. A plot simulation always starts with grazing switched
off. Grazing occurs to plants after production and turnover; it does not
affect either production or turnover.

**New Grazing Levels**

Specify the new level of grazing, to apply from this event until the
next grazing event.

In any aboveground plant or litter pool, if the amount of specified
grazing exceeds the amount of material in the pool then the grazing is
reduced such that all of that pool is eaten away (that is, the pool mass
is prevented from going negative).

Like all inputs in FullCAM, the grazing inputs apply to the crop or
litter as it is at the beginning of each processing time period (at the
later of the beginning of the last step or after the last event).

**New Root Slough**

Root sloughing keeps the root mass in proportion to the aboveground
plant mass.

Example: Suppose grazers remove 90% of the aboveground plant mass . If
root sloughing is on, the plant will turn over 90% of its roots to
debris --- except that if the maximum root slough percentage is less
than 90%, the percentage of roots sloughed off is the maximum root
slough percentage. But if root sloughing is off, then the plants will
keep all their roots regardless of how fiercely their aboveground mass
is grazed.

**New Fodder Destination Percentages**

*Fodder* is the plant material eaten by any grazing animals. The fodder
destination percentages specify where the carbon and nitrogen in the
fodder moves to after passing through the grazing animals.

Material gets to the DPM and RPM (see [RothC](114_RothC.htm)) via manure
(typically around 30%) and urine; it gets to the mineral pool via urine;
it gets to the atmosphere via urine, manure and enteric fermentation.

Typically all N from manure and urine goes into shallow ammonium.

The sum of the destination percentages for each of carbon and nitrogen
is always 100%; the last destination percentage in each column (animal
products) is calculated automatically for you.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 197. Initial Conditions For the Whole Plot 2020

**Initial Conditions For the Whole Plot**

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Whole Plot*
panel\]

Describe inputs that apply to the whole plot at the beginning of the
simulation.

**Details**

A plot simulation starts with the [Forest
Percentage](206_Forest%20Percentage.htm) as set here. Use a [Forest
Percentage Change](116_Forest%20Percentage%20Change.htm) event on the
[Events](136_Events.htm) page to change the forest percentage during the
plot simulation. Otherwise the percentage will remain at this initial
setting.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 198. Constituent Models In FullCAM 2020

**Constituent Models In FullCAM**

This topic is about the constituent models ("submodels") within FullCAM.

**Introduction**

FullCAM was initially formed by integrating these models into a single
cohesive model. FullCAM has since been expanded with capabilities that
go well beyond just the constituent models.

**FullCAM Consists of Constituent Models**

FullCAM is a flexible and highly integrated system of the following
models, each of which deals with particular aspects of the carbon
cycling and greenhouse emissions accounting. The models can be used in
various configurations, depending on your requirements.

1.  [CAMFor](77_CAMFor.htm) --- **C**arbon **A**ccounting **M**odel for
    **For**ests models carbon cycling in a forest, including the trees,
    debris, soil, minerals, and wood products. Forest growth can be
    included as yield curves, empirical growth formula, or process
    modelling.
2.  [CAMAg](78_CAMAg.htm) --- **C**arbon **A**ccounting **M**odel for
    **Ag**riculture models carbon cycling in an agricultural system,
    including the crops, debris, soil, minerals, and agricultural
    products. Includes both cropping and grazing.
3.  [RothC](114_RothC.htm) --- **Roth**amsted Institute active soil
    **C**arbon Model models carbon cycling in the active soil.

**Seamless Integration Into a Single Model**

FullCAM always uses the constituent models appropriately, combining them
as required into what appears as a single model of your specified plot.

CAMFor and CAMAg are framework models --- they model multiple layers of
a forest or an agricultural system respectively, and provide frameworks
into which the other models can be embedded. GENDEC, RothC and 3PG are
specialist models --- they only simulate a single layer of a forest or
agricultural system, but do so in more detail than CAMFor or CAMAg.

When you configure FullCAM, the constituent models are switched on and
off as required by the configuration. The FullCAM
[Configuration](150_Configuration.htm) page only allows you to enter
configurations that makes physical sense.

For each of the constituent models, there is a configuration that allows
the model to be run on its own --- which is useful for verifying that
FullCAM properly incorporates that model.

**Types of Plot That Can Be Modelled**

FullCAM allows you to run all sensible combinations of these models, to
model any of the following:

1.  A forest
2.  An agricultural system
3.  A mixed forest and agricultural system
4.  Trees only

FullCAM can model one forest and one agricultural system simultaneously.
Forests and agricultural systems both have debris and both have soil, so
both GENDEC and RothC have both forest and agricultural versions.
Forests have trees but agricultural systems do not. There are the
following model-instances:

1.  CAMFor
2.  CAMAg
3.  Forest RothC
4.  Agricultural RothC

Forest RothC and agricultural RothC are identical except that the soil
is always covered in forest RothC but may be either bare or covered in
agricultural RothC.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 199. Timing 2020

**Timing**

\[*Timing* page of the input window of a plot, or estate document\]

This page is where you set the timing for the simulation:

- [Simulation Steps](5_Simulation%20Steps.htm)
- [Start and End of
  Simulation](26_Start%20and%20End%20of%20Simulation.htm)
- [Output Steps](27_Output%20Steps.htm)

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 200. Site 2020

**Site**

\[*Site* page of the input window of a plot or spatial document\]

Enter site information for the plot. The page is partitioned into
several windows and panels:

- [Site : Water](12_Site_Water.htm)
- [Site : Temperature](13_Site_Temperature.htm)
- [Site :
  Light](http://www.fullcam.au/FullCAMServer2020/Help/35_Site_Light.htm)
- [Site : Productivity](64_Site_Productivity.htm)
- [Site : Growth Multipliers](39_Site_Growth%20Multipliers.htm)
- [Site : Area](157_Site_Area.htm)
- [Site : Maximum Aboveground
  Biomass](36_Site_Maximum%20Aboveground%20Biomass.htm)

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
