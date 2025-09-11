---
version: 2016
batch_range: 001-015
batch_name: Getting_Started
creation_date: 2025-08-28
total_files: 14
---

# FullCAM 2016 - Batch 001-015: Getting Started

## Table of Contents

- [001. Introduction to Using FullCAM 2016](#001-introduction-to-using-fullcam-2016)
- [002. Downloading Crops and Events 2016](#002-downloading-crops-and-events-2016)
- [003. Soil Properties 2016](#003-soil-properties-2016)
- [005. Simulation Steps 2016](#005-simulation-steps-2016)
- [006. Configure the Plot 2016](#006-configure-the-plot-2016)
- [007. Startup Window 2016](#007-startup-window-2016)
- [008. Configure Risk Analysis 2016](#008-configure-risk-analysis-2016)
- [009. Stem Density 2016](#009-stem-density-2016)
- [010. Documents and Files 2016](#010-documents-and-files-2016)
- [011. About 2016](#011-about-2016)
- [012. Site Water 2016](#012-site-water-2016)
- [013. Site Temperature 2016](#013-site-temperature-2016)
- [014. Credits 2016](#014-credits-2016)
- [015. Special Keys 2016](#015-special-keys-2016)

---

## 001. Introduction to Using FullCAM 2016

### Introduction to Using FullCAM

An introduction to the sorts of things you might do with FullCAM.

### Simulations

**Plot Simulations**

A *plot* is a piece of land with uniform characteristics, such as a
forest stand or a paddock. A plot can have either:

1.  No area -- the plot is a *point* model, and its output masses are in
    tonnes per hectare.
2.  A specified area -- the plot has an area, so its output masses are
    in tonnes.

Plot information is stored in a *plot file*, whose extension ".plo".

A *plot* simulation tracks the carbon associated with a plot -- either
on the plot or in the products produced by the plot.

Typical use:

1.  Create a new plot:
    - Choose *New Plot* from the *File : New* menu. A blank plot
      document is created, and its input window appears with tabbed
      pages for [About](11_About.htm),
      [Configuration](150_Configuration.htm) and
      [Timing](199_Timing.htm). The titles on the *Configuration* and
      *Timing* pages are the colour red, indicating that you **must**
      complete these pages before you can simulate the plot.
    - As soon as you have entered the minimum required data for the
      *Configuration* and *Timing* pages, more tabbed pages appear on
      the plot input window. Exactly **which** pages appear depends on
      your particular configuration.
    - A list of inputs can be viewed using the 'Models and Inputs'
      function located in the 'About your Configuration' portion of the
      Configuration page. It is also possible to view flow diagrams of
      the configured model. This can be done using the 'Diagrams'
      function.
2.  When all the data is ready (with no red tabs visible) choose
    'Simulate' from the FullCAM main menu and 'Run Plot Simulation' from
    the drop--down menu or click on the 'Run Plot Simulation' button,
    located in the lower half of the FullCAM main menu bar.
3.  When you run your first simulation, a default output window will be
    displayed. Specify the outputs you want to look at, and create
    additional output windows if needed, then rerun the simulation.
4.  You can now alter any inputs and immediately rerun the simulation,
    as often as required.

Save your work at any time by choosing *Save* from the *File* menu, or
click the save button on the toolbar underneath the menu (the red dot
means the document has been changed). The resulting .plo file contains
the plot document, which includes the input window and all the
associated output windows.

Plot simulation is the basic unit of simulation in FullCAM -- simulating
estates just consists of simulating many plots.

**Estate Simulations**

A number of plots may be aggregated into an *estate* document (stored as
an ".est" file). An estate is a collection of plots, each of which has a
specified area and starting date for land use. As estate files are area
based, their masses are quoted in tonnes. Estate files may represent a
diverse area of forest with stands (trees) of different ages, types and
management systems, or similarly a diverse area of agricultural land.

When you create an estate document (choose *New Estate* from the *File :
New* menu), you create any number of plots with area, each of which has
its own:

1.  Plot file, which contains the document describing the plot, and
    which may be shared by multiple estate--plots.
2.  Area.
3.  Start date (when the estate--plot started being used as described in
    its plot file). You do **not** specify the actual geographic
    location of a plot.

Estate files are useful for simulating larger or heterogeneous areas of
land. You can also test varying timing and management options. See
[Estate Simulation](72_Estate%20Simulation.htm).

### List of Inputs

In configuring data for analysis by any model within FullCAM, users are
presented with a specific list of input data needed to support each
configuration. The list of required input data can be viewed using the
'Models and Inputs' button in the 'About your Configuration' section of
the Configuration page (tab). Various options can be selected to display
the model configuration, the variable names used by FullCAM and the
values assigned to the variables. This information can also be saved in
a spreadsheet or text format. This capacity allows users to find a
balance between the data they have available, the sophistication of the
model configuration and the type and accuracy (certainty) of the outputs
required.

### Sensitivity Analysis

Monte Carlo analyses are a useful way to assess the relative effects of
model parameters. More specifically, they allow users to determine both
model sensitivity and the probability based distribution of potential
outputs, inherent uncertainties in each of the data inputs. FullCAM
links to the \@Risk RDK software by Palisade
([palisade.com](http://www.palisade.com){target="_blank"}) to provide
this capability. This capability is accessed by 'Sensitivity' check box
in the Risk Analysis section of the Configuration page. However,
completing a sensitivity analysis requires the presence of a licenced
version of the \@Risk RDK software on the computer used to run FullCAM.

### Material Flows

The main carbon flow is

Atmosphere → plants → debris → mulch → soil.

At this level the flow is unidirectional. There are only two carbon
feedback loops:

1.  Within the mulch, due to microbes eating and dying.
2.  Within the soil, due to microbes eating and dying.

Each of these loops is strictly confined to its layer (mulch and soil
respectively).

The other large carbon flows are:

- Carbon moves from the debris, mulch, soil, and products to the
  atmosphere due to decomposition.
- Carbon moves directly from the root debris to the soil, bypassing the
  mulch.
- In a thinning or harvest event, carbon moves from the plants and
  debris to the products.
- In a fire, carbon moves from the plants, debris and mulch to the
  atmosphere and soil.

To get your simulation working realistically, you may need to alter the
FullCAM inputs that determine the flows. Work back from where the
simulation appears to be giving unrealistic results to where the carbon
is coming from, and so on back until realism is achieved.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 002. Downloading Crops and Events 2016

**Downloading Crops and Events**

\[[Data Builder](132_Data%20Builder.htm) page : *Crops and Events*
panel\]

This panel is for downloading crop species and agricultural event data,
using Data Builder.

**Basic Operation**

1.  Select a crop species from the upper list, and press the *Download
    This Species* button. This will populate the list of regimes in the
    second drop-down list.
2.  Select a regime from the regime list and press the *Download Events
    for This Regime* button. This loads the events for the selected
    regime into the events list on the [Events](136_Events.htm) page.

**Details**

When downloading a species, the Data Builder will ask if you wish to
make the species the initial species. We recommend you select "Yes",
unless you wish to apply a different species as the initial species.
Selecting "Yes" does not necessarily mean that the species exists at the
start of the simulation, only that the initial conditions for the
agricultural system (mainly the debris) will be set using that species.

The agricultural portion of the plot should now be ready to simulate (so
the *Crops* tab should not be red, and the buttons in the *Agricultural*
panel of the *Initial Conditions* page will not be red).

Agricultural regimes cycle through time for the length of the
simulation. Choosing and downloading another agricultural regime will
replace the events of the old regime with those of the new regime.

Clicking the *Clear Agricultural Events* button clears all the events
downloaded as part of the agricultural regimes.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 003. Soil Properties 2016

**Soil Properties**

\[[Soil](203_Soil.htm) page : *Forest* or *Agricultural* panel :
*Properties* button\]

Enter the general properties of the soil. See the [RothC](114_RothC.htm)
soil pool abbreviations.

**Soil Properties**

The *HUM encapsulation percentage* is the percentage of the HUM carbon
mass that is encapsulated by clay, and thus becomes inert, each year.
Encapsulation transfers carbon to the inert pool, which is very
sensitive to build-up over time, so the encapsulation percentage is
typically pretty low. In sandy soils the HUM encapsulation percentage is
typically zero, and the inert pool only builds up due to fires.

The *Depth of soil sampled* is the maximum depth soil, in centimetres,
that is being modelled. Typically equal to 30 cm. Soil above the sample
depth is considered shallow and topsoil. Soil below the sample depth is
ignored, except that if nitrogen simulation is switched on in the
[Configuration](150_Configuration.htm) then there is a deep ammonium
pool and a deep nitrate pool --- see [Mineral Nitrogen
Model](253_Mineral%20Nitrogen%20Model.htm)).

The *pH of sampled soil* is the pH of the shallow soil, which is used to
compute nitrification rates if nitrogen simulation is switched on. A
soil that is neither acidic not alkaline (or basic) has a pH of 7.0,
less if it is acidic (minimum 0), more if it is alkaline (maximum 14).

**Decomposition Rate Multipliers**

The quantity of carbon in each [RothC](114_RothC.htm) soil pool (DPM,
RPM, BIO-F, BIO-S, HUM) decays exponentially with time if there is no
new carbon flowing into the pool: After a time *t* (in years), the
fraction of the original carbon still in the pool is

> [y]{style="font-size:large;"} = [x]{style="font-size:large"}
> ^(--*abct*)^
>
> where
>
> *a* = rate modifier for temperature\
> *b* = rate modifier for topsoil moisture\
> *c* = rate modifier for soil cover\
> *k* = decomposition rate multiplier \[1/y\].

*a*, *b* and *c* are the same for all pools, but *k* can be different
for different pools.

In a step of *T* years (*T* \<= 1), the fraction of the carbon that is
in the pool at the beginning of the step and that leaves the pool during
the step (the "decomposition fraction" of the pool for that step) is
thus

> [y]{style="font-size:large;"} = [x]{style="font-size:large"}
> ^(--*abckT*)^
>
> Typically, the decomposition rate multipliers are approximately:
>
> *k*
>
>   ------- -----------------------------------------------
>   10.00   DPM
>   0.30    RPM
>   0.66    BIO-F (only entered in version 26.3 of RothC)
>   0.66    BIO-S (only entered in version 26.3 of RothC)
>   0.02    HUM
>   ------- -----------------------------------------------

In version 26.5 of RothC: The BIO-F and BIO-S decomposition rate
multipliers when the soil is bare are computed by RothC. When the soil
is covered, both of these multipliers are further multiplied by the
*BIO-F and BIO-S modifier*, which is typically about 3.25. Note that the
forest soil is always covered, but covering of the agricultural soil
depends on a time-series that is entered.

**Plant Material, Biomass, and Humus Destination Percentages**

Any material in the active soil pools that undergoes decomposition
moves. In each step of the simulation, material moves to the various
active soil carbon pools and to the atmosphere. The fraction of moving
material that leaves the soil for the atmosphere as gas is computed by a
RothC formula from the clay content of the soil (a higher clay content
means that a lower fraction leaves as gas). The remainder of the moving
material, called the "solids", moves to another or the same active soil
pool.

Moving material that is not given off as gas moves to the BIO-F, BIO-S
and HUM pools. The percentages moving to these pools are the same for
each of the plant material (DPM and RPM) and biomass (BIO-F and BIO-S)
pools. In version 26.3 of RothC, no material moves from the plant
material or biomass pools to the BIO-S pool, or from the HUM pool to the
BIO-F pool. The destination percentages add to 100%; the HUM percentage
is automatically calculated.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 005. Simulation Steps 2016

**Simulation Steps**

\[[Timing](199_Timing.htm) page : *Simulation Steps* panel\]

Set the amount of time in a simulation step (all simulation steps
simulate the same amount of time).

A (simulation) *step* is the unit of time considered by a FullCAM
simulation. In each step, there is exactly one material movement from
one pool to the next pool due to processes (see [Processes and
Events](58_Processes%20and%20Events.htm)). Each step always simulates
the same amount of time. Steps are like the heartbeats of the model:
material moves from pool to adjoining pool once per step (exception:
more than once if the step is interrupted by an event).

The shorter the steps, the longer a plot simulation takes.

### Choosing the Length of Simulation Steps

*Time Resolution of Input Data*

If you specify the rainfall to FullCAM as just the total rainfall each
year (that is, one number per year), then it is unrealistic to expect
FullCAM to accurately simulate monthly or weekly phenomena that are
influenced by rainfall. Monthly simulation steps might be appropriate,
but the results might have to be interpreted carefully.

*Computing Time and Memory*

In a lengthy simulation or one with many outputs, there may not be
enough computer memory to do a simulation with very short steps, or it
might take longer to compute than is convenient. This problem will
probably only arise when simulating estates.

*Graininess*

In FullCAM, each atom of material belongs to one pool (such as trees
leaves), and carbon moves between the various pools once per step (at
the end of the step). While the rate of circulation of material among
the pools is mainly governed by the various physiological and empirical
rate inputs, it is subtly influenced by the length of step and
occasionally this is significant.

Consider carbon that flows from pool A to pool B to pool C (for example,
tree leaves to leaf litter to soluble mulch). It takes one step for any
carbon from pool A to reach pool B, and a second step for any of it to
reach pool C. If the steps are yearly then it takes two years for ANY
carbon from pool A to reach pool C, while with daily steps some carbon
can get to pool C by the end of the second day!

In reality, the step length is vanishingly small: carbon moves between
pools continuously, rather than in discrete movements that occur once
every beat of our simulation clock. Now, we want to model the essential
nature of the system with as little computing effort as possible. If we
decrease the step length then we get a more realistic simulation, but we
do more computing. This dependence of the simulation results on the step
length is called *graininess*.

FullCAM performs its calculations efficiently. It runs near the maximum
possible speed on your computer --- and your computer is probably a
supercomputer by the standards of a decade ago. So speed of computation
is not much of a limiting factor. The precision of the quantities in
FullCAM is relatively low so round-off error is almost insignificant ---
but there is little point in using more steps than necessary in case the
round off error begins to affect your results. FullCAM's speed of
computation and flexibility in its treatment of time allows you to
overcome the artificial barriers set by arbitrary and fixed frequencies
of simulations steps that are present in many other models.

What is a sensible amount of time per step? As you decrease the step
length, you will find your simulated results will gradually approach
limiting values. The limiting values are simulation results that stay
the same, no matter how much you further decrease the step length. From
the perspective of graininess, an appropriate step length is the step
length that gets you close to the limiting values. For example, if
halving the step length does not change the results much then there is
no point in decreasing it further.

As a rough rule of thumb, for negligible graininess use a step length of
at most a month unless modelling for detailed results (such as in an
academic or scientific situation).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 006. Configure the Plot 2016

**Configure the Plot**

\[[Configuration](150_Configuration.htm) page : *Plot* panel\]

Specify what systems and layers of the plot you want to model (see
[Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm)).

**Plot Type**

Choose the systems and layers of the plot that you want modelled:

- Just Forest Soil (Forest soil)
- Just Agricultural Soil (Agricultural soil)
- A multilayer Forest system (Forest system)
- A multilayer Agricultural system (Agricultural system)
- A multilayer mixed system (Mixed system)

**Forest soil or Forest system**

Used to model forest systems moving from plantation to plantation
(rotations), from native forest to plantation, or from plantation to
native forest or environmental plantings. It should not be used to model
transitions from agricultural systems to plantations or other
forest-agricultural transitions (use the mixed multilayer system
instead).

**Agricultural soil or Agricultural system**

Used to model agricultural systems. Does not include forestry activities
or trees.

**Mixed system**

Consists of a multilayer forest system and a multilayer agricultural
system. The relative mix of forest to agricultural system may vary with
time. Used to model woodland grazing and transitions between forest and
pasture (deforestation and reforestation).

A *multilayer* model consists of multiple layers --- plants (trees or
crop), debris, soil (optional), minerals (optional), and products.

Modelling only a single layer of a system causes the relevant
constituent model of FullCAM to run by itself, in its original form.

Aboveground material flows from the debris to the soil.

1.  Material flows from plants to the debris.
2.  Material flows from the debris to the soil.

Debris "breaks down".

Mulch "decomposes" by the action of an explicit live microbe pool.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 007. Startup Window 2016

**Startup Window**

\[Start FullCAM (after you start, but before you can use FullCAM)\]

\[*Program* menu : *About FullCAM* menu item\]

This window introduces the FullCAM program.

**Use**

- Informational only

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 008. Configure Risk Analysis 2016

**Configure Risk Analysis**

\[[Configuration](150_Configuration.htm) page : *Risk Analysis* panel\]

Specify whether you want to do [Risk Analyses](218_Risk%20Analysis.htm).

**Use**

The plot document is "configured for risk analyses" if you check the box
for [Sensitivity Analysis](160_Sensitivity%20Analysis.htm), in which
case the [Risk Inputs](159_Risk%20Inputs.htm) page becomes accessible.

Turning on risk analyses has no effect on regular plot simulations; it
merely allows the possibility of risk analyses.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 009. Stem Density 2016

**Stem Density**

\[[Plant Properties](43_Plant%20Properties.htm) window : *Stem Density*
button\]

This [time-series Window](135_time-series%20window.htm) is where enter
the stem density (also known as the \"basic density\") of a tree
species.

**Details**

FullCAM uses masses for all its calculations, so stem density is only
used to convert between stem masses and stem volumes. You require stem
density if:

- Modelling a multilayer forest and any of the following:
  - Tree growth is specified by stem volume increments
  - The amount of stem material is specified by volume in the initial
    conditions
  - The amount of stem material in any tree planting is specified by
    volume.

If stem density is not required for any of the above then it is not used
(that is, it will not affect FullCAM calculations), even though you are
free to enter it into the document.

See the *Properties of the Species time-series* section of [Growth
Properties](42_Growth%20Properties.htm).

If only the trees are modelled, the plant age used in the stem density
time-series is the maximum age of the plants (there are no events in
this configuration, so the maximum and average ages are the same).

Because the stem density is a time-series, it may vary with the age of
the tree (set *Years are* to \"Years since plants sprouted\") or with
the year (set *Years are* to \"Calendar years\" or \"Years since start
of simulation\").

The stem density is of the whole stem at the time indicated, not of the
new stem growth in that year. The units are kilograms per cubic metre
(note: most other masses in FullCAM are in tonnes).

The density of stem wood is typically about 300 -- 1,000 kgdm/m^3^. A
compendium of wood densities for Australian tree species can be found in
the [NCAS Technical Report No.
18](reps/TR18%20Woody%20Density%20Phase%201%20-%20State%20of%20Knowledge.pdf){target="reps18"}.

If you have only a single number for stem density, just use that. (Set
*Years of data* to 1, *Data points per year* to 1, resize the
time-series, and enter the stem density in the single cell of the
time-series. *Years are* and *Extrapolation* can be set to anything.)

Typical values for native forest communities are described in Table 7 of
*Greenhouse Gas Emissions from Land Use Change in Australia: An
Integrated Application of the National Carbon Accounting System*.
Additional species specific values can be extracted from the FullCAM
database.

  Major Vegetation Group (MVG) Class            Wood Density (Basic, kg dry matter/m^3^)
  --------------------------------------------- ------------------------------------------
  Rainforest and Vine Thickets                  500
  Eucalyptus Tall Open Forests                  550
  Eucalyptus Open Forest                        625
  Eucalypt Low Open Forest                      550
  Eucalyptus Woodland                           890
  Acacia Forest and Woodland                    940
  Callitris Forest and Woodland                 650
  Casuarina Forest and Woodland                 860
  Melaleuca Forest and Woodland                 660
  Other Forests and Woodland                    800
  Tropical Eucalyptus Woodland/Grassland        830
  Eucalyptus Open Woodland                      890
  Acacia Open Woodland                          940
  Mallee Woodland and Shrubland                 1060
  Low Closed Forest and Closed Shrubland        1000
  Acacia Shrubland                              940
  Other Shrublands                              940
  Heath                                         900
  Chenopod Shrub, Samphire Shrub and Forbland   900
  Unclassified Native Vegetation                780

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 010. Documents and Files 2016

**Documents and Files**

This topic is about using documents and files in FullCAM.

**Definitions**

A *document* in FullCAM is a set of information about a plot or estate
simulation and is represented as an input window and other optional
windows (output windows, diagrams window, and so on). A document exists
only in computer memory --- fast electronic memory that **is erased**
when you exit FullCAM or turn off your computer.

A *file* is a set of information stored as a single entity on a
computer's hard disk. A file **is not erased** when you exit FullCAM or
turn off your computer --- the file will still be there when you turn
the computer back on.

**Document Types**

FullCAM Standard Edition has two document types:

*Plot document*\
Represents a "plot", an area of land with uniform characteristics.
Masses are in tonnes per hectare if there is no area, or in tonnes if
you input an area. Saved in a "plot file", whose file extension is
".plo". See [Plot Simulation](177_Plot%20Simulation.htm).

*Estate document*\
Represents an "estate", which is arbitrary collection of plots each with
its own area. Masses are in tonnes. Saved in an "estate file", whose
file extension is ".est". See [Estate
Simulation](72_Estate%20Simulation.htm).

You will probably mainly use plot documents --- for modelling forests,
crops, carbon emissions and so on, on a single homogeneous area. Estates
add areas to plots, allowing you to combine separate plots to model an
heterogeneous area --- such as for modelling a series of plantation
forest stands.

Typically, spatial and database documents are used only by Department of
the Environment to compute Australia's national carbon account. However,
if you have the appropriate data you can simulate any landscape.

**Opening Multiple Documents**

FullCAM can open any number of documents at once. A list of all open
FullCAM documents can be viewed in the drop down list on the main
window.

The *Windows* menu on the [Main Window](217_Main%20Window.htm) allows
you to manage the windows individually, on a window by window basis.

You must use one of the Save commands from the File menu to save a
document as a file before exiting FullCAM. It is also wise to save your
document periodically while you are working, to guard against unexpected
program termination such as might be caused by a power failure.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 011. About 2016

**About**

\[*About* page of the input window of a plot or estate document\]

This page is for your notes about the document. What you enter on this
page has no effect on simulations.

**Name**

Use this area of the \'About\' tab to enter a descriptive name for the
Plot. The name has no significance outside this page. The name entered
is not the name by which the plot is saved nor is it used to label any
output. It is solely provided to allow the user to include extra detail
about the Plot and simulation.

**Notes**

Notes are purely for recording relevant aspects of a FullCAM simulation.
FullCAM completely disregards these notes for all computational
purposes; they have no effect on any simulation. However, it is
recommended that users enter detail about plot and estate documents in
the Notes. The Notes will be saved along with the rest of the document.
The content of the Notes should contain information on data sources, any
unusual characteristics of the document or its simulation results, the
location of any external output files (e.g. those saved to Excel on
other programs), any key decisions or uncertainties in preparing the
document etc. The Notes act as a metadata statement on simulation,
reminding the user of the simulation attributes, and informing others
about important aspects of the simulation.

Consider including:

- Purpose of the document
- Data sources
- Unusual characteristics of the document or simulation result
- Key assumptions made in preparing the document
- Uncertainties inherent in the document.

**Lock Document**

Checking the *Lock Document* checkbox will immediately lock the
document, which will:

1.  Replace the *Lock Document* checkbox with a notice that includes:
    - Notice that the document is locked
    - The time of locking
    - A security identifier that uniquely identifies this locking
      action.
2.  Save the document immediately.
3.  Prevent the document from ever being saved again.

While working with a locked document, changes can be made and simulation
completed using the changed run parameters; however, the changes cannot
be saved under the original name of the locked document.

You will still be able to save the document to a different name (using
*Save As*), so you will be able to use it as a template for other
documents.

Locking effectively prevents the document from ever being altered and
saved. If the document is:

1.  Saved to a different name
2.  Altered
3.  Renamed to the original name
4.  Locked

then the second locking will be at a different time and the security
identifier will very likely be different, so it will be obvious that it
is not the original locked document.

Suppose you lock a document and send it out into the world, and that a
new document later comes back. If the new document is locked and has the
same lock-time and security identifier as your original, you can be
confident that the contents of the returned document are the same as
your original.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 012. Site Water 2016

**Site : Water**

\[[Site](200_Site.htm) page : *Water* button\]

This window is where you enter water and moisture information for the
plot, except that the soil-water information is entered in the [Soil
Water](44_Soil%20Water.htm) window.

**Introduction**

On occasion, constituent models ([RothC](114_RothC.htm) and
[CAMFor](77_CAMFor.htm)) will need to know the rainfall if the breakdown
of the debris of any tree species is sensitive to temperature and
rainfall, and for [CAMAg](78_CAMAg.htm) if the breakdown of the debris
of any crop species is sensitive to temperature and rainfall. Rainfall
can be supplemented by definite irrigation.

**Natural**

The soil model [RothC](114_RothC.htm) requires details of open-pan
evaporation, in order to work out the topsoil moisture deficit (TSMD).

**Irrigation**

The irrigation in the forest and agricultural systems of a plot are
entirely separate, and no water runs from one system to the other.

*Definite irrigation* is irrigation that definitely occurs, regardless
of conditions. If you have historical irrigation data, enter it as
definite irrigation and turn off conditional irrigation. See the
[Definite Irrigation](92_Definite%20Irrigation.htm) time-series.

*Conditional irrigation* is irrigation whose occurrence depends on the
conditions. Specify a minimum percentage of the maximum soil water
capacity in the conditional irrigation time-series, and FullCAM applies
just enough irrigation to guarantee that the soil water never drops
below this amount. Thus, conditional irrigation ensures a minimum level
of soil water - irrigation is used as conditions require. Use
conditional irrigation to simulate the effect of a management practice
that uses irrigation to ensure a minimum soil water level. Setting the
conditional irrigation percentage to 0% effectively turns off
conditional irrigation. See the [Conditional
Irrigation](91_Conditional%20Irrigation.htm) time-series.

The forest and agricultural water simulations are separate (FullCAM
assumes no lateral water movement on the plot), except that they share
the same rainfall, open-pan evaporation, and [Vapour Pressure
Deficit](97_Vapour%20Presser%20Deficit.htm). The forest and agricultural
irrigations are entirely separate.

Irrigation levels can be specified either with events or with
time-series (see [Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm)). If using
time-series, enter the time-series via the buttons on this window. If
using events, enter the events on the [Events](136_Events.htm) page. In
either case, enter all information about irrigation (namely whether
conditional irrigation is on, and which model it uses to operate in the
forest).

**Forest Irrigation**

RothC calculates soil water as a deficit, as the *topsoil moisture
deficit* (TSMD). The RothC soil water capacity (corresponds to a TSMD of
zero when the soil is at its wettest, but equal to the maximum TSMD when
the soil is at its driest) is calculated by RothC from the soil sample
depth, the ratio of bare-to-covered maximum TSMD, and the clay fraction
--- input these in the [Soil Water](44_Soil%20Water.htm) window and
[Soil for the Whole Plot](46_Soil%20for%20the%20Whole%20Plot.htm) panel,
respectively.

**Agricultural Irrigation**

Only the [RothC](114_RothC.htm) model runs an agricultural soil water
model. You can use conditional irrigation whenever the soil is included
in the plot. See the remarks on RothC in the forest irrigation section
above.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 013. Site Temperature 2016

**Site : Temperature**

\[[Site](200_Site.htm) page : *Temperature* button\]

Enter temperature information for the plot.

**Use**

The simulator requires the mean daily average air temperature and debris
sensitivity to temperature.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 014. Credits 2016

**Credits**

**Component Models**

The development of FullCAM and its component models is described in
Volume 2 of the 2013 National Inventory Report (Appendix 6B). FullCAM
includes the Rothamsted Soil Carbon Model (RothC) described in Jenkinson
et. al (1987) Jenkinson (1990) and Jenkinson et. al (1991).

- Jenkinson, D.S., Hart P.B.S, Rayner, J.H. and Parry, L.C. (1987)
  Modelling the turnover of organic matter in long-term experiments at
  Rothamsted. INTECOL Bulletin. 15:1-8; and
- Jenkinson, D.S. (1990) The turnover of organic carbon and nitrogen in
  soil. Philosophical Transactions of the Royal Society. 329:361-368.
- Jenkinson, D.S., Adams, D.E. and Wild, A. (1991) Model Estimates of
  CO2 Emissions from Soil in Response to Global Warming. Nature.
  351:304-306.

**Contributors**

FullCAM is a result of continuous work and contributions from a range of
organisations, made up of both data providers and IT service providers.
To view the FullCAM institutional arrangements relating to the
collection and preparation of input data for FullCAM, please refer
Volume 1 of the 2013 National Inventory Report (Section 1.2).

**Citations**

Department of the Environment (2015) National Inventory Report 2013
Volume 1. Commonwealth of Australia 2015.

Department of the Environment (2015) National Inventory Report 2013
Volume 2. Commonwealth of Australia 2015.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 015. Special Keys 2016

**Special Keys**

The following keys have special meanings that are not necessarily
apparent from looking through the menus. You do not need to know any of
these meanings to use FullCAM with a mouse and the usual keys, but these
meanings can speed you up.

**Enter ---** If you are in a number entry box, FullCAM immediately
process the number.

**Tab** --- Jumps to the next data entry control (box, menu, button, and
so on).

**Shift-Tab** --- Jumps to the previous data entry control (box, menu,
button, and so on).

**Space** --- If a button is selected, pressing the *Space* bar presses
the button.

**Home, End, Page Up, Page Down** --- Move between pages in tabbed
windows (such as the document input windows), move between help topics
in the *Help* window, and move between records in the table windows.

**Delete** --- Deletes selected items from lists.

**F1** --- Opens the *Help* window at the help topic for the current
window. If there are several help buttons on the window, pressing F1
opens the Help at the topic for the first of the buttons --- you can
then move to other topics using control-N (next) and control-B (back).
However, in general we recommend you press the help button with the
mouse to move straight to the topic you want.

**F2** --- Opens the *Input Properties* window for the current input
control (box, menu, and so on). If analysis is on, it instead opens the
*Risk Properties* window for the input. If in a spatial document, it
instead opens the *Spatial Properties* window for the [No Help
Available](148_No%20Help%20Available.htm) window.

**F9** --- Simulates a plot or estate document (refer [Introduction to
Using FullCAM](1_Introduction%20to%20Using%20FullCAM.htm) for further
details).

**F12** --- Closes the window, automatically pressing any *OK* or *Done*
button on the window.

**Escape** --- Closes the window, automatically pressing any *Cancel*
button on the window. Same as if the close-window box was clicked.

**Alt** --- Shifts focus to the [Main Window](217_Main%20Window.htm),
ready for a letter to choose a menu. A second *Alt* key press returns
you to the previous window.

**Underlines on buttons** --- If there is a button in the current window
with an underlined letter, pressing that "Alt-" and that letter on the
keyboard presses that button (if there is no ambiguity due to currently
being in a text box and so on, just pressing the letter on the keyboard
has the same effect).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
