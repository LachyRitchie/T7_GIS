---
version: 2016
batch_range: 151-200
batch_name: Simulation_Analysis_Tools
creation_date: 2025-08-28
total_files: 39
---

# FullCAM 2016 - Batch 151-200: Simulation Analysis Tools

## Table of Contents

- [153. Harvest 2016](#153-harvest-2016)
- [154. Post-Thin Period 2016](#154-post-thin-period-2016)
- [155. Percentage of Precipitation Intercepted by the Tree Canopy 2016](#155-percentage-of-precipitation-intercepted-by-the-tree-canopy-2016)
- [156. Equilibrium Evaporation 2016](#156-equilibrium-evaporation-2016)
- [157. Site Area 2016](#157-site-area-2016)
- [158. Plant Trees 2016](#158-plant-trees-2016)
- [159. Risk Inputs 2016](#159-risk-inputs-2016)
- [160. Sensitivity Analysis 2016](#160-sensitivity-analysis-2016)
- [161. Plant Crop 2016](#161-plant-crop-2016)
- [163. Herbicide 2016](#163-herbicide-2016)
- [164. Plough 2016](#164-plough-2016)
- [166. Plot Files 2016](#166-plot-files-2016)
- [167. Plots in the Estate 2016](#167-plots-in-the-estate-2016)
- [168. Output Window 2016](#168-output-window-2016)
- [169. Select Outputs 2016](#169-select-outputs-2016)
- [170. Graph Lines 2016](#170-graph-lines-2016)
- [171. Select A Standard Event 2016](#171-select-a-standard-event-2016)
- [172. Overview of FullCAM 2016](#172-overview-of-fullcam-2016)
- [174. Autoqueue 2016](#174-autoqueue-2016)
- [175. Graph Axes 2016](#175-graph-axes-2016)
- [177. Plot Simulation 2016](#177-plot-simulation-2016)
- [178. Frost Modifier 2016](#178-frost-modifier-2016)
- [180. Latitude and Longitude 2016](#180-latitude-and-longitude-2016)
- [181. Soil Nutrition Modifier 2016](#181-soil-nutrition-modifier-2016)
- [182. Risk Properties of an Input 2016](#182-risk-properties-of-an-input-2016)
- [183. Soil Water Modifier 2016](#183-soil-water-modifier-2016)
- [184. Initial Crops 2016](#184-initial-crops-2016)
- [185. Initial Trees 2016](#185-initial-trees-2016)
- [186. One Plot in the Estate 2016](#186-one-plot-in-the-estate-2016)
- [188. Forest Productivity Index 2016](#188-forest-productivity-index-2016)
- [190. Contact Us 2016](#190-contact-us-2016)
- [193. Soil Inputs 2016](#193-soil-inputs-2016)
- [194. Vapour Pressure Deficit Modifier 2016](#194-vapour-pressure-deficit-modifier-2016)
- [195. Configure Event Or time-series 2016](#195-configure-event-or-time-series-2016)
- [196. Grazing Change 2016](#196-grazing-change-2016)
- [197. Initial Conditions For the Whole Plot 2016](#197-initial-conditions-for-the-whole-plot-2016)
- [198. Constituent Models In FullCAM 2016](#198-constituent-models-in-fullcam-2016)
- [199. Timing 2016](#199-timing-2016)
- [200. Site 2016](#200-site-2016)

---

## 153. Harvest 2016

**Harvest**

\[[Event Window](137_Event%20Window.htm) : *Harvest* panel\]

Enter the inputs specific to a harvest event.

**Introduction**

The forest counterpart of a harvest is a [Thin](140_Thin.htm) event

A harvest is the only means of forming agricultural products (apart from
grazing, see [Grazing Change](196_Grazing%20Change.htm) events), and can
take some of the crop offsite. See the [Product
Properties](47_Product%20Properties.htm) of each species.

**Affected Portion**

The affected portion is the fraction of the agricultural system in which
the harvest takes place. It is typically the fraction of the plot area
that is harvested.

**Clearing Harvest**

For a harvest to be clearing (that is, to clear the agricultural system
of its crop), the affected portion must be 100% and the destination
percentages for each pool must sum to 100%.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 154. Post-Thin Period 2016

**Post-Thin Period**

\[[Event Window](137_Event%20Window.htm) : [Thin](140_Thin.htm) panel :
*Post-Thin Period* section\]

Specify the relative allocations of new growth to the tree components in
the period immediately after a thin.

**Details**

Tree growth is often different for a period after a thin, due to the
response of the trees to the thin. Leaves and branches especially tend
to grow with extra vigour after a thin.

FullCAM models the post-growth differences using relative allocation
multipliers. Each multiplier multiplies the relative allocation that
would otherwise occur, for the whole length of the post thin period
(except that the boost period ends immediately if there is another
thin). That is, the relative multiplication multipliers here allow you
to modify the relative allocations for the period after a thin. No extra
growth occurs, just the allocation of any growth to the various
components can be changed.

For example, a leaf multiplier of 1.2 (while the multipliers for all the
other components are 1.0), and a post thin period of 0.5 years, would
mean that the relative allocation of growth to leaves would be 20% more
than otherwise for whole of the half year following the thin (assuming
there is no other thin in those six months).

Note that relative allocations are relative to each other, so
multiplying all the relative allocations by the same amount has no
effect.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 155. Percentage of Precipitation Intercepted by the Tree Canopy 2016

**Percentage of Precipitation Intercepted by the Tree Canopy**

\[[3PG Leaves](21_3PG%20Leaves.htm) window: *Percentage of Precipitation
Intercepted by the Tree Canopy* button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the percentage of precipitation ([Rainfall](88_Rainfall.htm),
[Definite Irrigation](92_Definite%20Irrigation.htm), and [Conditional
Irrigation](91_Conditional%20Irrigation.htm)) that does not get to the
soil because it is intercepted by the tree canopy, for the current
species ([Select a Species](56_Select%20a%20Species.htm)).

**Details**

The percentage will vary by season (especially if the trees are
deciduous) and by the age of the trees.

This time-series is used by [3PG](115_3PG.htm), and also by 3PG-lite to
compute the soil water modifier --- see [Configure Tree
Production](108_Configure%20Tree%20Production.htm).

The intercept percentage is typically from 0 to 20%. Higher values
result in lower amounts of available soil water, and thus to lower
growth.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 156. Equilibrium Evaporation 2016

**Equilibrium Evaporation**

\[[Site : Water](12_Site_Water.htm) window : *Equilibrium Evaporation*
button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the equilibrium evaporation for the plot, in millimetres (100 mm
= 1 megalitre per hectare).

Higher values result in less available soil water and thus less NPP
being produced by the trees.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 157. Site Area 2016

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

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 158. Plant Trees 2016

**Plant Trees**

\[[Event Window](137_Event%20Window.htm) : *Plant Trees* panel\]

Enter the inputs specific to a tree-planting event.

**Age**

Enter here the age of the trees when planted, in years. For example, if
planting six months old seedlings, enter "0.5" years, or, if planting
seeds, enter "0.0" years.

**Volume**

The volume of the stems of the trees when planted, in cubic metres per
hectare.

This volume will be converted to a mass in the FullCAM simulation by
multiplying it by the stem density.

**Mass**

If the \'masses\' option was selected from the \'Specify Tree Size By\'
list, enter the mass of all tree components when the trees were planted.
If the \'Volume for stems, masses for other components\' option was
selected, enter the mass of the non-stem tree components when planted,
in tonnes per hectare and the volume of stems of the trees at planting.
This volume will be converted to a mass in the FullCAM simulation by
multiplying it by the stem density.

**Species**

Select the species of tree to be planted from the drop down list of
available species.

If the species required is not available a new species must be entered
using the [Select a Species](56_Select%20a%20Species.htm) list on the
[Trees](215_Trees.htm) Tab.

**Specify Tree Size**

Select the method of specifying tree size by selecting one of the
options in the drop down list.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 159. Risk Inputs 2016

**Risk Inputs**

\[*Risk Inputs* page of the input window of a plot or spatial document\]

Manage all the risk inputs for a plot document --- see [Risk
Analysis](218_Risk%20Analysis.htm). It is only accessible if the plot is
configured for sensitivity analysis --- [Configure Risk
Analysis](8_configure%20risk%20analysis.htm).

**Use**

The list shows all the current risk inputs, using colour to show their
status:

  Colour         Status
  -------------- -----------------------------------------------------------
  Solid yellow   required by document and on
  Pale yellow    required by document and off
  Orange         not required by document (not used in this configuration)
  Red            not ready (refers to a non-existent species or event )

Only the risk inputs that are required by the document and on are used
in an analysis involving risk inputs; the rest are treated as ordinary
inputs (that is, always have the same value).

The risk input for a time-series is a single number that is the
multiplier for the data in the time-series (see [Time-series
Window](135_time-series%20window.htm)).

This page is always ready, because the risk inputs do not affect whether
or not the document can simulate. However, if there are any risk inputs
that are not ready then the sensitivity analyses cannot be run.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 160. Sensitivity Analysis 2016

**Sensitivity Analysis**

\[*Sensitivity Analysis* page of the input window of a plot document\]

This page is for performing a sensitivity analysis on the plot. It is
only accessible if the plot is configured for sensitivity analysis ---
[Configure Risk Analysis](8_configure%20risk%20analysis.htm).

The \@Risk software that is used to perform the risk analysis (see
below) currently has some practical issues which are described at the
bottom of this page.

**Overview**

Choose the analysis outputs and the analysis properties, then press the
*Run Sensitivity Analysis* button to do the analysis. FullCAM and \@Risk
then jointly perform the risk analysis, after which you can view the
results in \@Risk (as prompted by FullCAM).

To complete the sensitivity analysis requires the RDK version of the
\@Risk software from Palisade to be purchased and installed on the
computer being used to run FullCAM.

During a sensitivity analysis, the risk inputs replace their
corresponding (ordinary) inputs. In each simulation during the
sensitivity analysis, for each risk input FullCAM randomly generates one
number from the probability distribution of the risk input, and that
value is used as the input for that simulation.

**Analysis Inputs**

Analysis inputs are the risk inputs (showing on the [Risk
Inputs](159_Risk%20Inputs.htm) page) that are both available (relevant
to this plot configuration) and on (not switched off in their [Risk
Properties of an Input](182_Risk%20Properties%20of%20an%20Input.htm)
window).

**Analysis Outputs**

The analysis outputs are the FullCAM outputs that you choose in the
[Select Outputs](169_Select%20Outputs.htm) window you get to by pressing
the *FullCAM Outputs* button.

Also choose whether the sensitivity analysis outputs should be:

1.  The values of the chosen outputs for all the simulation steps
2.  Just the values of the chosen outputs for the last step in the
    simulation.

If you choose the outputs for all the simulation steps, the sensitivity
analysis can take a long while to compute, your computer may run low of
memory and thus run very slowly, and you may be overwhelmed by the
number of outputs in the analysis results. Choosing just the
end-of-simulation values of the FullCAM outputs is often sufficient, and
will mean that the analysis runs much faster.

**Analysis Properties**

The sampling types are:

- Traditional Monte Carlo. Each risk input is sampled independently of
  the others.
- Latin hypercube. The risk inputs samples are all chosen together, in a
  manner designed to explore the space of possibilities faster. Latin
  hypercube tends to get better results for a given number of plot
  simulations (iterations).
- Distribution means. Each risk input sample is always equal to the mean
  of its probability distribution. Only use this for checking.

Typically we use Latin hypercube.

The maximum number of iterations is the maximum number of iterations
(plot simulations) that will be performed in a sensitivity analysis,
regardless of whether or not convergence-stopping is on. If
convergence-stopping is off, the analysis will perform the maximum
number of iterations. A typical value is 1,000.

Often a sensitivity analysis will converge before the maximum number of
iterations. Convergence is where doing more iterations (plot
simulations) does not significantly change the results. Typically you
should check for convergence to save unnecessary computation; typically
define convergence as less than 1.5% changes, and check every 100
iterations.

**Running the Sensitivity Analysis**

Select the \'Sensitivity Analysis\' tab and perform the following steps:

1.  Select the desired output variables using the \'FullCAM Outputs\'
    button in the Analysis Outputs window. The outputs are selected in
    the same manner as described previously for the normal Output window
    (item 22, section B). Define whether results are required for every
    simulation step or just for the last step only.
2.  In the \'Analysis Properties\' window select the sampling type,
    define the maximum number of iterations to be used in the
    simulations and define the convergence conditions.
3.  Once all parameters for the simulation have been defined click on
    the \'Run Sensitivity Analysis\' button. This button will be
    disabled if the plot file is not ready. You will then be prompted on
    how to view the results in \@Risk.

Each iteration is a complete plot simulation, and a sensitivity analysis
will perform hundreds or thousands of them. Thus, the analysis can take
a while. If you have a lot of analysis outputs, or the analysis outputs
are every FullCAM output step, the analysis will take longer than
otherwise.

For a plot with a thousand steps (for example, 80 years of monthly
steps) and just a couple of outputs, a thousand iterations will
generally finish in less than a minute on most computers.

After the sensitivity analysis is finished according to the progress
window, \@Risk can take a while to open the \@Risk *Results* window. For
complex sensitivity analyses, the delay here can be minutes!

We recommend you start with a simple plot and a simple sensitivity
analysis to get a feel for the computation times on your computer.

Ignore the "simulations" in the \@Risk window that tells you the
progress of the sensitivity analysis --- \@Risk uses the word
"simulation" to mean something other than a plot simulation. Both
FullCAM and \@Risk mean an "iteration" to be a FullCAM plot simulation.

**Practical Issues**

Observing a few simple rules should help you avoid some pitfalls that
have been identified in the way FullCAM and \@Risk interact.

\@Risk output is displayed in a separate process with its own window
that is labelled "@Risk - Results" on the Windows Task Bar. It will be
referred to here simply as the "@Risk" window. If no \@Risk windows are
present then FullCAM automatically creates one when the first \@Risk
function (such as a sensitivity analysis) is run.

When FullCAM is running, do not close all \@Risk windows. If you do then
either restart FullCAM, or manually create an \@Risk window by choosing
the appropriate command from the Palisade group in the Windows Start
menu.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 161. Plant Crop 2016

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 163. Herbicide 2016

**Herbicide**

\[[Event Window](137_Event%20Window.htm) : *Herbicide* panel\]

Enter the inputs specific to a herbicide event.

**Details**

A herbicide event moves all crop material into the debris (as if there
were instant, 100% turnover).

The only input specific to this event is the percentage of the area
being modelled that is affected.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 164. Plough 2016

**Plough**

\[[Event Window](137_Event%20Window.htm) : *Plough* panel\]

Enter the inputs specific to a plough event.

**Details**

A plough event moves all crop, debris, and mulch material into the soil,
as either decomposable or resistant plant matter.

The only input specific to this event is the percentage of the area
being modelled that is affected.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 166. Plot Files 2016

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
the estate as described, but are available for selection in the \'Plots
in the Estate\...\' tab.

To add a new plot to the list of plot files, first ensure that the
desired new plot file is located in the appropriate folder specified
using the \'Choose folder\...\' button. Then press \'New\...\' select
the desired plot from the dialog box and press \'open\...\' (or
double-click the desired plot file). To replace a plot file currently
within the plot files list select the plot file to be replaced, press
\'Edit\...\', select the files list, select the new desired plot fie,
and press \'Open\...\' (or double-click the desired plot file). This
will update all plots in the estate that used the old plot file to use
the new plot file (thereby substituting one plot file for another
throughout the entire estate). Press the \'Sort\...\' button to arrange
all plot files in the plot file list alphabetically. To delete a plot
file from the list, select the file name and press the \'Delete\...\'
button. The plot file will be removed from the estate but is not deleted
from the folder containing the various plot files.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 167. Plots in the Estate 2016

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
are coloured light-blue. Plots whose starting time is after the estate
simulation ends are coloured dull orange.

Plots that are not ready for simulation are shown in red: edit them to
correct missing or invalid data.

To add a plot to the estate use the \'New\...\' button. After pressing
the \'New\...\', a dialog box opens in which a Start Time for the plot
is specified by entering the Calender year and simulation step within
that year when the plot was initiated. The Area of the plot is entered.
The Plot File is selected from the drop down list. Press \'OK\...\' to
accept the clause and enter the Plot file, its area and start time into
the estate.

To alter the Area or Start Time of a plot file within the estate, press
the \'Edit\...\' button and alter the values that appear in the dialog
box as required.

The \'Clone\...\' button can be used to enter an exact copy of the plot
file into the estate. This is useful when multiple plots of the same
tree or crop type with different areas or start times need to be
specified within the estate.

To remove a plot from the estate, select the plot and then press the
\'Delete\...\' button.

The All Plots and Selected Plots boxes to the right of the list provide
a summary of the number of plots and area of plots in the estate or
selected.

**The Estate Simulation**

Simulate the estate by choosing *Run Simulation* from the *Simulate*
menu (if that menu choice is greyed-out then the estate is not ready ---
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
the 'Plots in the Estate' window, right clicking on the selected plots
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

**Times: Growth time-series and Events**

A single plot file can be used many times in an estate, and each of
these plots may have a different start time. If any of the species
time-series (see [Growth Properties](42_Growth%20Properties.htm)) or
events (such as planting or thinning) are specified in terms of calendar
years then the plot file might become invalid (and thus not ready for
simulation) for some plot start times. If this occurs, FullCAM will
notify you and then abandon the estate simulation.

To avoid this possibility, in your plot files you should specify:

- The species time-series using times since planting
- Events in terms of time since the start of the simulation.

Use species or event timing in terms of calendar years with caution,
because they must make sense in terms of how the plot file is used in
the estate simulation.

**Example**. Suppose you have a plot file for a plantation forest, in
which all the time-series data (such as rainfall) and events (such as
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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 168. Output Window 2016

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

*Whole* means the whole of the land under consideration. The "whole
land" consists of the forest land and the agricultural land (one of
which may be missing, depending on the configuration). The land under
consideration is a plot in a plot simulation and an estate in an estate
simulation.

The *complete* mass of some land (whole, forest, or agricultural) is the
mass on and due to that land. It includes the plants, debris and soil.

The *onsite* mass of some land (whole, forest, or agricultural) is the
mass on that land. It includes the plants, debris and soil.

*Yield rates* are the combined rates of production and turnover, and are
what is observed by simply measuring the plants periodically.

*Emit* and *sequester* refer to emissions to the atmosphere and removal
from the atmosphere. That is, emissions and sequestrations/removals are
always to and from the atmosphere respectively.

Any moves of material between pools comprise a net movement, that is, it
is the combined effect of movement one way and the other way. In most
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

When you have a selection, you can copy it (look on the mouse menu that
pops up when you click on the secondary menu button --- the right
button, if you hold the mouse in your right hand). From there you can
paste it into other programs, such as Microsoft Excel.

**Notes on Specific Outputs**

"Production rates", "turnover rates" and "yield rates" are for the END
of the step. Consider using more simulation steps per year. For example:
if you have yearly steps, clear the forest in day 365 of a year (thus,
the clearing occurs at noon on day 365 of the year), and plant trees on
day 1 of the next year (the trees are planted at noon of day 1), then
the reported production rate for the year (step) with the clearing will
be zero because the rate is for the last part of the year --- from noon
until midnight on day 365, when there were no trees!

The conditional irrigation output is only accurate in simulation steps
with no events (it is calculated from the conditional irrigation in the
period from the latter of the beginning of the step or the last event in
the step to the end of the step).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 169. Select Outputs 2016

**Select Outputs**

\[[Output Window](168_Output%20Window.htm) : *Select Which Outputs to
Show* toolbar button\]\
\[[Sensitivity Analysis](160_Sensitivity%20Analysis.htm) window :
*FullCAM Outputs* button\]

Specify a set of FullCAM outputs, for display by the accompanying output
window or for use in a risk analysis.

**Use**

There are about 800 possible outputs, but this window shows only those
outputs that are available in the configuration of the current document.
Hover the mouse over the name of an output and you see a description of
the output that has been tailored to your configuration. Sometimes the
description is merely the same as the name.

Single-click on the icon or name of an output to select or deselect it.
Selected outputs are marked with a red tick.

The outputs are organised into folders, just like files are organised
into folders in Windows Explorer. Click on the plus (+) and minus (--)
buttons to expand and collapse the folders. A single-click on the icon
or name of a folder selects or deselects everything within the folder.

The number of outputs is shown in a message at the bottom of the window.
Hover the mouse over the message with the number of outputs to find out
how many outputs are chosen but that are unavailable in this
configuration (they were chosen previously, while the plot was in a
different configuration).

Choosing flows and leaks as outputs slows down the simulation a little.
This slowness is only likely to be significant in spatial simulations or
simulations of large estates.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 170. Graph Lines 2016

**Graph Lines**

\[[Output Window](168_Output%20Window.htm) : Double-click on graph to
open the *Graph Settings* window : *Lines* page\]

Choose the properties of an output line in the graph of an *Output
Window*.

**Details**

The line width is in points, for precise control over printed output.
However the resolution of the computer screen is much less than that of
a printer, so the width of the line in screen pixels is shown in
brackets after the line width in points. (Beware: for a given number of
points, the number of pixels depends on whether or not you are using
"small fonts".)

If the line width on the screen is not equal to one pixel, then the dash
and dotted styles are drawn on the screen as solid. (This is a
limitation of *Windows*).

Note the buttons for automatically assigning colours and for making all
line widths the same as the first (in the legend) on the output window
toolbar.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 171. Select A Standard Event 2016

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 172. Overview of FullCAM 2016

### Overview of FullCAM

An overview of what FullCAM can do.

### Introduction

FullCAM is a model for tracking the greenhouse gas emissions and changes
in stocks of carbon associated with land use and management. FullCAM is
a fully integrated Carbon Accounting Model (CAM) for estimating and
predicting all biomass, litter and soil carbon pools in forest and
agricultural systems. In addition, it accounts for changes in major
greenhouse gases and human-induced land use practices.

FullCAM is the model used to construct Australia's national greenhouse
gas emissions account for the land sector. Users of the model can
determine project-based results on a similar basis to Australia's
official recording of greenhouse emissions trends for land use and land
use change.

FullCAM was developed under the National Carbon Accounting System (NCAS)
at the former Australian Greenhouse Office (AGO) to integrate data on
land cover change, land use and management, climate, plant productivity,
and soil carbon over time -- to provide a dynamic account of the
changing stock of carbon in Australia's land systems since 1970.

FullCAM incorporates a suite of verifiable component models, adapted for
use at a fine spatial (25 m) and temporal (monthly) resolution for the
Australian continent, including:

- [CAMFor](77_CAMFor.htm) -- for forest systems
- [CAMAg](78_CAMAg.htm) -- for cropping and grazing systems
- [RothC](114_RothC.htm) -- for agricultural soil carbon

FullCAM can run each of these sub-models in isolation or in any sensible
combination. See [Constituent Models In
FullCAM](198_Constituent%20Models%20In%20FullCAM.htm).

The sub-models used within FullCAM can be integrated into various
combinations to suit the data available and outputs required. Whilst it
may be used for tracking of carbon stocks and flows in different forest
and agricultural systems, it may also be used more simply to review
project-based results for small land holdings.

Specifically, FullCAM calculates the carbon flows associated with:

- Forests. It calculates the carbon in the trees, debris, soil,
  products, and the carbon exchanged with the atmosphere, due to
  thinnings, multiple rotations, and fires.
- Agricultural systems, which can be cropped or grazed systems. FullCAM
  calculates the carbon in the plants, debris, soil, and products, and
  the carbon exchanged with the atmosphere, while including the effects
  of harvest, ploughing, fire, herbicides, and grazing.
- Afforestation and reforestation systems, which are represented and
  modelled as transitions from agricultural systems to forests.
- Deforestation systems, which are represented and modelled as
  transitions from forests to agricultural systems.
- Mixed systems (such as in agroforestry) -- assorted combinations of
  the systems above.

FullCAM calculates the carbon stocks and flows for land subject to
different land use and management activities.

Sensitivity analysis of the data (via Monte Carlo methods) can also be
used to assess the relative effects of uncertainty in model inputs.

FullCAM can also be used to review project-based results for small land
holdings.

### Main Function

The main function of FullCAM is to model the stocks and flows of carbon
in mixed forest and agricultural systems. This includes tracking carbon
within pure agricultural and forestry systems, as well as within
transitions from an agricultural activity to a forestry activity or
agroforestry system (and vice versa), and taking into account how these
systems and their proportional contributions change over time. FullCAM
models all carbon pools, plus interchanges and fluxes within the:

- Plants
- Debris
- Soil
- Products
- Atmosphere

FullCAM tracks the movement of carbon removal from the atmosphere,
through the growth of plants, all the way through to its return to the
atmosphere -- after potentially passing through plants, debris, soil,
grazing animals, or wood or agricultural products.

FullCAM can model carbon in up to:

- Six tree components
- Five crop components
- Twelve forest debris and ten agricultural debris components
- Six forest soil and six agricultural soil components
- Forest products
- Forest landfill pools
- agricultural products

FullCAM can be configured into many different models, and there are
hundreds of outputs to chose from. FullCAM can model different tree and
crop species, and also can account for changes in carbon due to
management events such as plantings, thinning, harvest, fire, grazing,
and ploughing.

**Capabilities**

FullCAM simulates carbon on a *plot* (an homogeneous region of land):

- [Plot Simulation](177_Plot%20Simulation.htm) tracks all the carbon
  associated with a plot, both on the plot and in the products produced
  by the plot.

FullCAM can also simulate:

- [Estate Simulation](72_Estate%20Simulation.htm). An estate is an
  arbitrary collection of plots, each with its own area.
- [Sensitivity Analysis](160_Sensitivity%20Analysis.htm), which assess
  the relative effects of uncertainty in inputs.

### Downloading Data and Benchmark Plots

You can streamline the process of setting up your plot document by
downloading data, including the default data and management regimes for
key species -- see [Data Builder](132_Data%20Builder.htm).

FullCAM may be used simply to investigate changes in carbon pools given
default inputs, or to determine emissions estimates for specific sites
with more complex land use histories. Download default data from the
FullCAM server via Data Builder and use it without modification to track
changes in carbon pools, or change it to suit your own management
practices.

### Resources

There is no initial setup data , so you must make your own choices about
what data to enter. There are several resources which may assist you:

- The Help system.
- Downloaded data.
- Supporting technical documentation including the National Carbon
  Accounting System Technical Reports (see [Help Index](index.htm)).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 174. Autoqueue 2016

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

## 175. Graph Axes 2016

**Graph Axes**

\[[Output Window](168_Output%20Window.htm) : Double-click on graph to
open the *Graph Settings* window : *Axes* page\]

Choose the properties of the graph axes of an *Output Window*.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 177. Plot Simulation 2016

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

An input is *species-dependent* if it depends on the species of plant
(that is, it describes a characteristic of material unique to that
particular species). Species dependency extends down to and includes the
debris layer, and across to the product layer, but extends no further:

- Most of the inputs for the plant, debris and product layers are
  species dependent.
- None of the inputs for the mulch, soil, mineral or atmosphere layers
  are species dependent. Once in the mulch or soil, it is sufficient
  just to classify the plant material as either *resistant* or
  *decomposable* (and if mulch is being simulated, the resistant
  material as either *less resistant* or *more resistant*).

**Rationing of Scarce Resources**

If a resource is scarce, the processes that use that resource compete
for it. During each time period:

1.  At the beginning of the time period, we compute all the *non-limited
    moves* of material from pool to pool due to each process (the moves
    that would occur if there were no scarcity of resources).
2.  The resources are rationed to each process on either a pro-rata or
    sequential basis (the choice is a plot input).
    - Pro rata: Each actual move (exchange of material) is equal to the
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

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 178. Frost Modifier 2016

**Frost Modifier**

\[[Site : Temperature](13_Site_Temperature.htm) window : *Frost
Modifier* button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the frost modifier (modFrost).

**Details**

This time-series is only used if the forest productivity index is
computed from scratch **and** the frost modifier is input directly ---
see [Configure Tree Production](108_Configure%20Tree%20Production.htm).

The frost modifier is dimensionless, and between 0 and 1. Higher values
result in more NPP being produced by the trees. A value of 1 implies no
frost, and 0 implies no NPP is produced.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 180. Latitude and Longitude 2016

**Latitude and Longitude**

The use of latitude and longitude in FullCAM.

**Decimal Degrees**

Always enter latitude and longitude in FullCAM in decimal degrees. All
spatial measurements in FullCAM are defined and exact in terms of
degrees, although we commonly speak of length approximations in
kilometres or meters.

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

**Example.** 12 degrees, 15 minutes and 1 second (12 deg 15\' 1\") is
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
  a meter).

**Example.** To move about 1 km west from 131.08123 deg E, move to
131.07123 deg E.

The size of a degree of longitude varies with latitude. For Australia, a
degree of longitude at the tip of Cape York corresponds to approximately
109km, while at southern Tasmania it is approximately 80km.

We use these length approximations often when talking about spatial
grids and cells, but the size of the cells and grids is defined in terms
of degrees. For example, when we talk about a woodiness cell of "25
meters" or "25 m resolution" what we mean is the cell of the woodiness
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
earth's surface).

**Australia**

Latitude and longitude coordinates must be from the Geographic Datum of
Australia (GDA) system, not from the Australian Map Grid (AMG) system.

Mainland Australia and Tasmania extend approximately from latitude
--10.6 deg N (Cape York, Queensland) to --43.6 deg N (South-east Cape,
Tasmania), and longitude 113.2 deg E (Steep Point, Western Australia) to
153.6 deg E (Cape Byron, NSW).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 181. Soil Nutrition Modifier 2016

**Soil Nutrition Modifier**

\[[Site : Productivity](64_Site_Productivity.htm) window : *Soil
Nutrition Modifier* button\]

This [time-series Window](135_time-series%20window.htm) is where enter
the soil nutrition modifier rating for the plot.

**Details**

The soil nutrition modifier is required to calculate the [Forest
Productivity Index (FPI)](188_Forest%20Productivity%20Index.htm).

The soil nutrition modifier is dimensionless, and typically between 0.75
and 1.25. Higher values result in more NPP being produced by the trees.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 182. Risk Properties of an Input 2016

**Risk Properties of an Input**

\[Press F6 on any input in a plot document where either type of risk
analyses is turned on (see [Configure Risk
Analysis](8_configure%20risk%20analysis.htm))\]

This window is where you create, edit, and delete a risk input. See
[Risk Analysis](218_Risk%20Analysis.htm).

**Making a Risk Input**

To make the input into a risk input, press the *Create Risk Properties*
button, enter the probability distribution, and edit any correlations
with other risk inputs.

Un-checking the *Risk properties are 'on'* checkbox turns the risk
properties off and effectively turns the input back into an ordinary
input, but retains the risk properties in case you want to turn them
back on.

The usual range for an input constrains the probability distribution of
the corresponding risk input. For example, the carbon percentage of bark
is a number from 0.0 to 100.0 (being a percentage), so the minimum and
maximum of the distribution cannot be outside 0.0 to 100.0.

You cannot choose the *OK* button unless the information in the window
is all valid. If a distribution parameter is invalid then it has a red
background --- so enter a new value for that parameter.

**Probability Distributions**

Only bounded distributions are allowed, to help ensure that the values
of the risk input always fall within their allowed range in FullCAM.

In all the distributions here, there is no possibility of a sampled
value less than the minimum or more than the maximum. When sampling the
distribution, the distribution is re-sampled as required until we get a
value that is in the min-max range.

The ranges of some inputs depend on other inputs. If those other inputs
are also risk inputs, then the situation can arise during a risk
analysis where the risk input is within its distribution range but is
out of the range allowed by FullCAM. If this happens, that simulation
within the risk analysis is discarded and another performed in its
place.

**Uniform Distribution**

Equal probability for every value from the minimum to the maximum.

**Triangular Distribution**

The probability density rises in a straight line from zero at the
minimum value to a peak at the most likely value, then declines in a
straight line to zero at the maximum value.

This is the simplest way to specify a distribution that is lumped around
the most likely value. Unless you know that the shape of that lumpiness
is definitely not triangular, this is generally the most suitable
distribution.

**Truncated Normal Distribution**

The normal (Gaussian) distribution has the classic, common, bell-shaped
probability distribution.

The mean must be between the minimum and the maximum.

Use this distribution where there are multiple independent sources of
error in factors that add to form the estimated value of the input.

**Truncated LogNormal Distribution**

The distribution of X when log(X) has a normal distribution (log =
logarithm, to any base).

The minimum must be greater than zero, and the mean must be between the
minimum and the maximum.

Use this distribution where there are multiple independent sources of
error in factors that are multiplied to form the estimated value of the
input.

**Correlations with Other Risk Inputs**

Risk inputs can be chosen to be correlated with one another --- choose
another risk input and edit its correlation (see [Correlation Between
Two Risk Inputs](65_Correlation%20Between%20Two%20Risk%20Inputs.htm)).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 183. Soil Water Modifier 2016

**Soil Water Modifier**

\[[Site : Water](12_Site_Water.htm) window : *Soil Water Modifier*
button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the soil water modifier (modASW).

**Details**

This time-series is only used if the forest productivity index is
computed from scratch **and** the soil water modifier is input directly
--- see [Configure Tree
Production](108_Configure%20Tree%20Production.htm).

The soil water modifier is dimensionless, greater than 0, and usually
less than 1. Higher values result in more NPP being produced by the
trees.

The soil water modifier is restricted to values between 0 and 1.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 184. Initial Crops 2016

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
[Initial Debris](31_Initial%20Debris.htm), so you **must** specify an
initial species.

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

Crop ages are used to access the crop time-series.

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
crop values. The button is disabled if the standard initial crop
information for the species is not ready (incomplete or has invalid
values).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 185. Initial Trees 2016

**Initial Trees**

\[[Trees](215_Trees.htm) page : *Initial Trees* button\]\
\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest*
panel : *Trees* button\]

Describe the trees growing in the forest system at the start of the
simulation.

**Species**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Even if there are no trees growing, there may be tree material in the
[Initial Debris](31_Initial%20Debris.htm), so you **must** specify an
initial species.

Enter the initial tree species. Only one tree species can grow in the
forest at any one time (see the [Select a
Species](56_Select%20a%20Species.htm) panel), so there can only be one
initial tree species. The species listed on the pull down on the menu
are those on the *Trees* page. The menu contains only a blank line if
there are no tree species, in which case you need to create a new
species on the *Trees* page.

The initial tree species is the (only) species of any trees growing in
the forest. Also, any debris in the forest, or any forest products in
use or in the landfill, are assumed to all belong to that species.

**Existence**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Specify whether there are trees growing in the forest at the beginning
of the simulation. If there are not, then the forest is clear and the
other inputs need not be entered.

**Specify Tree Size By**

Choose the method by which you are going to specify the initial size of
the tree components.

Stems may be specified by either volume or mass; all the other
components must be specified by mass. (The [Stem
Density](9_Stem%20Density.htm) needs to be specified as an input,
regardless of what you choose here.)

Alternatively, you can specify all the tree component sizes as
percentages of the maximum tree biomass (presumed to only occur in a
mature, undisturbed states). Thus, if the percentages of the components
add to 100%, the trees will be at their maximum biomass limit. The
maximum tree biomass *T* is computed from the maximum aboveground
biomass of the trees *A*, by:

> +-------+--------+-----------------------------------------------------+
> | *T* = | *A* \* | [(*stem%* + *branch%* + *bark%* + *leaf%* +         |
> |       |        | *coarse-root%* + *fine-root%*)]{.underline}         |
> |       +--------+-----------------------------------------------------+
> |       |        | (*stem%* + *branch%* + *bark%* + *leaf%*)           |
> +-------+--------+-----------------------------------------------------+

**Masses**

The masses of the various tree components at the start of the
simulation, in tonnes of dry matter per hectare.

Note that these are true masses, not carbon masses as in some other
inputs. The "mass" of some material is the weight of all of the
material; the "carbon mass" of the material is the weight of the carbon
in the material. The carbon masses of most tree components are about
half of their masses.

Convert between the masses and carbon masses using the carbon
percentages (see [Plant Properties](43_Plant%20Properties.htm)).

If CAMFor is on, enter the six CAMFor tree components: stem, branches,
bark, leaves, coarse roots, fine roots.

**Volumes**

The stem volume is the total volume of stems in the forest, in cubic
meters per hectare. This volume will be converted to a mass in the
FullCAM simulation by multiplying it by the stem density. Please be sure
that the stem-density time-series for the initial tree species is
correct!

**Ages**

Tree ages are used to access the tree time-series.

The age of the oldest trees in the forest is the age of the forest ---
the number of years since the current forest was planted, plus the age
of the trees when they were planted.

The average age of the trees in the forest reflects the new trees that
are assumed to have grown after removal of tree stems in past thinnings.
The average tree age must be less than the age of the oldest trees. (The
average age is also used as initial value of the growth-age for the
yield formula, if the yield formula is used for the initial tree
species.)

The average age must not exceed the age of the oldest trees, or both
boxes are coloured red to indicate that the data is incomplete.

Unless there are thinning events that thin some but not all of the tree
stems, the age of the oldest trees will equal the average age of the
trees.

**Numbers of Trees**

Enter the number of stems per hectare, which is the stand stocking
level.

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
tree values. The button is disabled if the standard initial trees
information for the species is not ready (incomplete or has invalid
values).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 186. One Plot in the Estate 2016

**One Plot in the Estate**

\[[Plots in the Estate](167_Plots%20in%20the%20Estate.htm) : *New* or
*Edit* button\]

This window specifies the properties of one of the [Plots in the
Estate](167_Plots%20in%20the%20Estate.htm).

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

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 188. Forest Productivity Index 2016

**Forest Productivity Index**

\[[Site : Productivity](64_Site_Productivity.htm) window : *Forest
Productivity Index* button\]\
This [time-series Window](135_time-series%20window.htm) is where enter
the forest productivity index (FPI) for the plot.

**Forest Productivity Index**

This window provides options for computing the forest productivity
index, which is required if the tree yield formula is used to compute
tree growth. It is a simplified variant of the 3PG model and produces an
index (equivalent to a site class) as either a long-term average (as
will life affect the life of a forest/plantation rotation) or as a
time-series (monthly or annual dataset) to consider the variability in
the site class over time.

As an alternative to calculating the forest productivity index, a value
can be obtained for the specified latitude and longitude in the [Data
Builder](132_Data%20Builder.htm).

**Details**

The forest productivity index is used if the tree production method is
the [Tree Yield Formula](130_Tree%20Yield%20Formula.htm) and the forest
productivity index is not calculated from scratch (see [Configure Tree
Production](108_Configure%20Tree%20Production.htm)).

The forest productivity index is a dimensionless measure of site
productivity due to soil, sunlight, rainfall, evaporation, and frost.
The forest productivity index varies during the year. Higher values of
forest productivity index result in more NPP produced by the trees.

The forest productivity index is described by the Australian Greenhouse
Office in [Report 27 of the National Carbon Accounting
Reports](reps/TR27%20Biomass%20Estimation%20Approaches%20for%20Assessment%20of%20Stocks%20and%20Stock%20Change.pdf){target="reps23"}
series.

The forest productivity index is an annualised rate, and is entered as a
single value that it would be if it continued at that rate for a whole
year.

Forest productivity index values can range from 0 to 100.

If actual site data is available, enter it in this time-series. If not,
use [Data Builder](132_Data%20Builder.htm) to download estimated monthly
forest productivity index (annualised). The derivation of this data is
described in [NCAS Technical Report
No.23](reps/TR23%20Developing%20a%20National%20Forest%20Productivity%20Model.pdf){target="reps23"}.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 190. Contact Us 2016

**Contact Us**

For further information about FullCAM, please consult the [FullCAM
website](http://www.environment.gov.au/climate-change/greenhouse-gas-measurement/land-sector){target="_blank"}.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 193. Soil Inputs 2016

**Soil Inputs**

\[[Soil](203_Soil.htm) page : *Forest* or *Agricultural* panel :
*Inputs* button\]

Specify the material that enters the soil. See the
[RothC](114_RothC.htm) soil pool abbreviations.

**Soil Input Percentages of Broken-Down Litter**

Specify where the broken-down litter goes to within the active soil.

The material in each litter pool breaks down, thereby transporting
material from the litter to the soil. This material, the broken-down
litter, can enter the DPM, RPM or HUM pools within the soil. Here, you
specify, for each type of broken down litter, which of these soil pools
the broken-down litter enters.

The decomposable (resistant) broken-down litter always goes to either
the DPM (RPM) or the HUM.

Naturally, the sum of each pair of percentages is 100%. Therefore the
HUM percentage is calculated automatically from the DPM/RPM value.

TABLE -- Typical values used are:

  Variable              To DPM or RPM   To HUM
  --------------------- --------------- --------
  Decomposable Litter   90              10
  Resistant Litter      90              10

**Manure from Offsite**

Manure from offsite (from outside the plot) may be added to the forest
or agricultural soil. Offsite manure inputs are only available if RothC
is used to model the soil.

Enter the time-series of manure carbon additions or add manure
application events to the \'Events\' tab depending on how manure
additions were configured in the \'Events\' or time-series window of the
\'Configuration Tab\'

Manure from offsite may be added to the forest or agricultural soil.
Enter the carbon mass in the manure, in tonnes per hectare, over time.

\'Offsite\' means \'from outside the plot\'. Offsite manure inputs are
only available if Roth C is used to model the soil.

In an agricultural system, manure from animals on the plot is dealt with
by grazing events (plant material eaten by grazing animals becomes
fodder, which may move to destinations including the DPM an RPM pools of
the soil). The offsite manure is the only explicit treatment of manure
by FullCAM.

Specify the percentages of the carbon in any offsite manure added to the
soil that move to the various organic soil components. That is, specify
the percentages of the carbon in the manure that are in the form of the
various soil components, when added to the soil. The percentages add to
100%; the HUM percentage is automatically calculated from the others.

Note that manure from offsite and grazing are entirely separate. The
manure inputs entered here have no effect on any grazing manure, and
vice versa.

TABLE --- Typical values used are:

Percentage of Manure

  Variable   Carbon that goes to
  ---------- ---------------------
  DPM        49
  RPM        49
  BIO-F      0
  BIO-S      0

**Plant Residues**

Plant residue inputs are plant material from the debris that enters the
soil. The material enters the DPM soil pool if it is decomposable, or
the RPM soil pool if it is resistant. Specify the total amount of plant
material entering the soil over time.

Plant residues can only be specified here if you are simulating the
[Soil](203_Soil.htm) by itself. If you are simulating a multi-layer
system, then the plant residues from the debris are automatically
calculated, so an explicit input for plant residues is neither required
nor desired.

The ratio of DPM to RPM is the mass of DPM divided by the mass of RPM in
the plant matter added to the soil, and is also known as the "quality
factor for incoming plant debris". Typical values for the ratio of DPM
to RPM are:

1.44 - Most agricultural crops and improved grassland\
0.67 - Unimproved grassland and scrub (including savanna)\
0.25 - Deciduous and tropical woodland.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 194. Vapour Pressure Deficit Modifier 2016

**Vapour Pressure Deficit Modifier**

\[[Site : Water](12_Site_Water.htm) window : *VPD Modifier* button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the VPD modifier (modVPD).

**Details**

This time-series is only used if the [Forest Productivity
Index](188_Forest%20Productivity%20Index.htm) is computed from scratch
and the [Soil Water Modifier](183_Soil%20Water%20Modifier.htm) is
computed --- see [Configure Tree
Production](108_Configure%20Tree%20Production.htm).

The vapour pressure deficit modifier is dimensionless, greater than 0,
and usually less than 1. Higher values result in more NPP being produced
by the trees.

The vapour pressure deficit modifier is restricted to values between 0
and 1.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 195. Configure Event Or time-series 2016

**Configure Event Or time-series**

\[[Configuration](150_Configuration.htm) page: *Events or time-series*
button\]

Specify certain inputs as either by time-series or by events.

Press the \'Events\' or \'time-series\' button to access the window
where you decide where various sorts of inputs are treated as event or
as time-series data.

**Introduction**

FullCAM only allows events if a multi-layer plot is modelled (see
[Configure the Plot](6_Configure%20the%20Plot.htm)), so if modelling a
plot that is not multi-layer then time-series data will always be used.

You can change these settings at any time without losing any of the
time-series or event data you may have entered.

If you do not want any of a particular input (for example, there is no
irrigation in your simulation), it is easiest to set its input type to
*Events*, but do not create any events of that type. This way you will
not be asked for the time-series input.

Some inputs, such as irrigation, can be specified either as events or as
time-series. This is where you configure how they are to be specified.

Unless the complete forest (CAMFor) or complete agricultural system
(CAMAg) or both are modelled then FullCAM does no allow (or process)
event and thus time-series data will always be used.

**Irrigation**

For a discussion of irrigation, see [Site : Water](12_Site_Water.htm).

Set the irrigation:

- As time-series: The [Definite
  Irrigation](92_Definite%20Irrigation.htm) and [Conditional
  Irrigation](91_Conditional%20Irrigation.htm) time-series
- As events: [Irrigation Change](54_Irrigation%20Change.htm) events.

**Manure-From-Offsite Added to the Soil**

Manure from offsite can be added to the soil whenever the soil is
modeled.

Set the manure additions:

- As time-series: The [Manure Inputs to Soil from
  Offsite](101_Manure%20Inputs%20to%20Soil%20from%20Offsite.htm)
  time-series
- As events: [Manure-From-Offsite
  Change](62_Manure-From-Offsite%20Change.htm) events.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 196. Grazing Change 2016

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

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 197. Initial Conditions For the Whole Plot 2016

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 198. Constituent Models In FullCAM 2016

**Constituent Models In FullCAM**

This topic is about the constituent models ("sub-models") within
FullCAM.

**Introduction**

FullCAM integrates these models into a single cohesive model. FullCAM
has since been expanded with capabilities that go well beyond just the
constituent models.

**FullCAM Consists of Three Constituent Models**

FullCAM is a flexible and highly integrated system of three existing
models, each of which deals with particular aspects of the carbon and
nitrogen cycling and greenhouse emissions accounting. The models can be
used in various configurations, depending on your requirements.

1.  [CAMFor](77_CAMFor.htm) --- **C**arbon **A**ccounting **M**odel for
    **For**estry Models carbon cycling in a forest, including the trees,
    debris and soil. Forest growth can be included as yield curves,
    empirical growth formula, or process modelling.
2.  [CAMAg](78_CAMAg.htm) --- **C**arbon **A**ccounting **M**odel for
    **Ag**riculture Models carbon cycling in an agricultural system,
    including the crops, debris, soil, minerals, and agricultural
    products. Includes both cropping and grazing.
3.  [RothC](114_RothC.htm) --- **Roth**amsted Institute active soil
    **C**arbon model Models carbon cycling in the active soil.

**Seamless Integration Into a Single Model**

FullCAM always uses the constituent models appropriately, combining them
as required into what appears as a single model of your specified plot.

CAMFor and CAMAg are framework models --- they model multiple layers of
a forest or an agricultural system respectively, and provide frameworks
into which the other models can be embedded. RothC is a specialist model
--- it only simulates a single layer of a forest or agricultural system,
but does so in more detail than CAMFor or CAMAg.

When you configure FullCAM, the constituent models are switched on and
off as required by the configuration. The FullCAM
[Configuration](150_Configuration.htm) page only allows you to enter
configurations that makes physical sense.

**Types of Plot That Can Be Modelled**

FullCAM allows you to run all sensible combinations of these models, to
model any of the following:

1.  A forest
2.  An agricultural system
3.  A mixed forest and agricultural system
4.  Soil only (either forest or agricultural).

FullCAM can model one forest and one agricultural system simultaneously.
Forests and agricultural systems both have debris and both have soil, so
RothC has both forest and agricultural versions. There are thus four
distinct model-instances:

1.  CAMFor
2.  CAMAg
3.  Forest RothC
4.  Agricultural RothC

Forest RothC and agricultural RothC are identical except that the soil
is always covered in forest RothC but may be either bare or covered in
agricultural RothC.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 199. Timing 2016

**Timing**

\[*Timing* page of the input window of a plot or estate document\]

This page is where you set the timing for the simulation:

- [Simulation Steps](5_Simulation%20Steps.htm)
- [Start and End of
  Simulation](26_Start%20and%20End%20of%20Simulation.htm)
- [Output Steps](27_Output%20Steps.htm)

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 200. Site 2016

**Site**

\[*Site* page of the input window of a plot or estate document\]

Enter site information for the plot. The page is partitioned into
several windows and panels:

- [Site : Water](12_Site_Water.htm)
- [Site : Temperature](13_Site_Temperature.htm)
- [Site : Productivity](64_Site_Productivity.htm)
- [Site : Growth Multipliers](39_Site_Growth%20Multipliers.htm)
- [Site : Displacement](17_Site_Displacement.htm)
- [Site : Area](157_Site_Area.htm)
- [Site : Maximum Aboveground
  Biomass](36_Site_Maximum%20Aboveground%20Biomass.htm)

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
