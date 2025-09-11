---
version: 2020
batch_range: 001-015
batch_name: Getting_Started
creation_date: 2025-08-28
total_files: 11
---

# FullCAM 2020 - Batch 001-015: Getting Started

## Table of Contents

- [001. Introduction to Using FullCAM 2020](#001-introduction-to-using-fullcam-2020)
- [003. Soil Properties 2020](#003-soil-properties-2020)
- [005. Simulation Steps 2020](#005-simulation-steps-2020)
- [006. Configure the Plot 2020](#006-configure-the-plot-2020)
- [009. Stem Density 2020](#009-stem-density-2020)
- [010. Documents and Files 2020](#010-documents-and-files-2020)
- [011. About 2020](#011-about-2020)
- [012. Site Water 2020](#012-site-water-2020)
- [013. Site Temperature 2020](#013-site-temperature-2020)
- [014. Credits 2020](#014-credits-2020)
- [015. Special Keys 2020](#015-special-keys-2020)

---

## 001. Introduction to Using FullCAM 2020

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

Plot information is stored in a *plot file*, with extension ".plo".

A *plot* simulation tracks all the carbon (and optionally, nitrogen)
associated with a plot -- either on the plot or in the products produced
by the plot.

Typical use:

1.  Create a new plot:
    1.  Choose *New Plot* from the *Document* menu. A blank plot
        document is created, and its input window appears with tabbed
        pages for [About](11_About.htm),
        [Configuration](150_Configuration.htm) and
        [Timing](199_Timing.htm). The titles on the *Configuration* and
        *Timing* pages are coloured red, indicating that these tabs are
        incomplete and must be completed before the plot can be
        simulated.
    2.  As soon as you have entered the minimum required data for the
        *Configuration* and *Timing* pages, more tabbed pages appear on
        the plot input window. Exactly **which** pages appear depends on
        your particular configuration.
    3.  If your configuration includes any of the multi--layer options
        then the *Data Builder* page appears. You can use this to
        download data needed to run a simulation.
    4.  A list of inputs can be viewed using the 'Models and Inputs'
        function located in the 'About your Configuration' portion of
        the Configuration page. It is also possible to view flow
        diagrams of the configured model. This can be done using the
        'Diagrams' function.
2.  When all the data is ready (with no red tabs visible) choose
    'Simulate' from the FullCAM main menu and 'Run Plot Simulation' from
    the drop down menu or click on the 'Run Plot Simulation' button,
    located in the lower half of the FullCAM main menu bar.
3.  When you run your first simulation, a default output window will be
    displayed. Specify the outputs you want to look at, and create
    additional output windows if needed, then rerun the simulation.
4.  You can now alter any inputs and immediately rerun the simulation.

Save your work at any time by choosing *Save* from the *File* menu, or
click the floppy disk button on the toolbar underneath the menu (the red
dot means the document has been changed). The resulting `.plo` file
contains the plot document, which includes the input window and all the
associated output windows.

Plot simulation is the basic unit of simulation in FullCAM -- simulating
estates consists of simulating many plots.

**Estate Simulations**

A number of plots may be aggregated into an *estate* document (stored as
an ".est" file). An estate is a collection of plots, each of which has a
specified area and starting date for land use. As estate files are area
based, their masses are quoted in tonnes. Estate files may represent a
diverse area of forest with stands (trees) of different ages, types and
management systems, or similarly a diverse area of agricultural land.

When you create an estate document (choose *New Estate* from the
*Document* menu), you create any number of plots with area, each of
which has its own:

1.  Plot file, which contains the document describing the plot, and
    which may be shared by multiple estate--plots.
2.  Area.
3.  Start date (when the estate-plot started being used as described in
    its plot file). You do **not** specify the actual geographic
    location of a plot.

Estate files are useful for simulating larger or heterogeneous areas of
land. You can also test varying timing and management options. See
[Estate Simulation](72_Estate%20Simulation.htm).

### Databases

FullCAM stores tabular data in database documents. This data can be
downloaded into plot documents by [Data
Builder](132_Data%20Builder.htm).

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

### Material Flows

The main carbon flow is:

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

Nitrogen is more complex, due to its mobility. Simulating nitrogen
introduces the mineral nitrogen pool, which is assumed to be in contact
with all the other pools. Nitrogen flows through the same pools as
carbon, however several additional processes exist to consume or
generate nitrogen. The required or excess nitrogen associated with any
of the organic pools flow into, or out of the mineral pool. If there is
insufficient nitrogen in the mineral pool for all the processes to
consume the amount they wish, then *nitrogen rationing* occurs -- which
means that less of the processes occur (for example, slowing plant
growth).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 003. Soil Properties 2020

**Soil Properties**

\[[Soil](203_Soil.htm) page : *Forest* or *Agricultural* panel :
*Properties* button\]

Enter the general properties of the soil. See the [RothC](114_RothC.htm)
soil pool abbreviations.

**Assorted**

The *HUM encapsulation percentage* is the percentage of the HUM carbon
mass that is encapsulated by clay, and thus becomes inert, each year.
Encapsulation transfers carbon to the inert pool. The HUM encapsulation
percentage is defaulted to zero.

The *depth of soil sampled* is the maximum soil depth that is being
modelled, typically to 30 cm. Soil above the sample depth is considered
shallow and topsoil.

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
multipliers when the soil is bare are computed for you by RothC. When
the soil is covered, both of these multipliers are further multiplied by
the *BIO-F and BIO-S modifier*, which is typically about 3.25. Note that
the forest soil is always covered, but covering of the agricultural soil
depends whether a crop or pasture exists.

**Plant Material, Biomass, and Humus Destination Percentages**

This window is for any material in the active soil pools that undergoes
decomposition. In each step of the simulation, material moves to the
various active soil carbon pools and to the atmosphere. The fraction of
moving material that leaves the soil for the atmosphere as gas is
computed by a RothC formula from the clay content of the soil (a higher
clay content means that a lower fraction leaves as gas). The remainder
of the moving material, called the "solids", moves to another or the
same active soil pool.

Moving material that is not given off as gas moves to the BIO-F, BIO-S
and HUM pools. The percentages moving to these pools are the same for
each of the plant material (DPM and RPM) and biomass (BIO-F and BIO-S)
pools. In version 26.3 of RothC, no material moves from the plant
material or biomass pools to the BIO-S pool, or from the HUM pool to the
BIO-F pool. The destination percentages add to 100%; the HUM percentage
is automatically calculated from the other(s).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 005. Simulation Steps 2020

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

The minimum time length per step is an hour.

The shorter the steps, the longer a plot simulation takes.

If you are simulating carbon only, monthly time steps are usually
sufficient. If simulating nitrogen, we recommend daily time steps
because nitrogen often gets used and replenished in a few days.

### Choosing the Number of Simulation Steps Per Year

*Time Resolution of Input Data*

If you specify the rainfall to FullCAM as just the total rainfall each
year (that is, one number per year), then it is unrealistic to expect
FullCAM to accurately simulate monthly or weekly phenomena that are
influenced by rainfall. Monthly simulation steps might be appropriate,
but the results might have to be interpreted carefully.

*Computing Time and Memory*

In a lengthy simulation or one with many outputs, there may not be
enough computer memory to do a simulation with very short steps, or it
might take longer to compute than is convenient.

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
reach pool C. If the steps are yearly then it takes two years for any
carbon from pool A to reach pool C, while with daily steps some carbon
can get to pool C by the end of the second day!

In reality, the step length is vanishingly small: carbon moves between
pools continuously, rather than in discrete movements that occur once
every beat of our simulation clock. This dependence of the simulation
results on the step length is called *graininess*.

As you decrease the step length, you will find your simulated results
will gradually approach limiting values. The limiting values are
simulation results that stay the same, no matter how much you further
decrease the step length. From the perspective of graininess, an
appropriate step length is the step length that gets you close to the
limiting values. For example, if halving the step length does not change
the results much then there is no point in decreasing it further.

For negligible graininess use a step length of at most:

- A month if just modelling carbon.
- A day if modelling mulch or nitrogen.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 006. Configure the Plot 2020

**Configure the Plot**

\[[Configuration](150_Configuration.htm) page : *Plot* panel\]

Specify what systems and layers of the plot you want to model (see
[Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm)).

**Plot Type**

Choose the layers of the plot that you want modelled (that is, the type
of plot model you want):

*Trees*

- Just the trees
- Just the forest mulch
- Just the forest soil
- A multilayer forest system

Used to model forest systems moving from plantation to plantation
(rotations), from native forest to plantation, or from plantation to
native forest or environmental plantings. It should **not** be used to
model transitions from agricultural systems to plantations or other
forest-agricultural transitions (use the mixed multilayer system
instead).

*Agriculture*

- Just the agricultural mulch
- Just the agricultural soil
- A multilayer agricultural system

Used to model agricultural systems. Does not include forestry activities
or trees.

*Mixed System*

- A mixed multilayer system

Consists of a multilayer forest system and a multilayer agricultural
system. The relative mix of forest to agricultural system may vary with
time. Used to model woodland grazing and transitions between forest and
pasture (deforestation and reforestation). A multilayer model consists
of multiple layers --- plants (trees or crop), debris, mulch (optional),
soil (optional), minerals (optional), and products.

Modelling only a single layer of a system causes the relevant
constituent model of FullCAM to run by itself, in its original form and
giving the same simulation as the standalone version of that model:

  Plot Type            Model Used
  -------------------- -----------------------------------------------------------------------
  Forest mulch         [GENDEC](http://www.fullcam.au/FullCAMServer2020/Help/109_GENDEC.htm)
  Agricultural mulch   [GENDEC](http://www.fullcam.au/FullCAMServer2020/Help/109_GENDEC.htm)
  Forest soil          [RothC](114_RothC.htm)
  Agricultural soil    [RothC](114_RothC.htm)

The "soil-style sensitivity of debris breakdown to temperature and
water" is on in any tree or crop species. (Soil-style sensitivity is
automatically turned off if the soil is not included.)

The "mulch-style sensitivity of debris breakdown to temperature and
water" is on in any tree or crop species and conditional irrigation is
on. Mulch-style sensitivity requires water, but conditional irrigation
is automatically turned off if the soil is not included.

The "mulch-style sensitivity of debris breakdown to temperature and
water" is off in every species, the definite and conditional irrigation
is specified by events rather than time series, and there are irrigation
events. (The effects are limited to small second order effects because
they are only due to graininess --- see [Simulation
Steps](5_Simulation%20Steps.htm)) --- omitting the soil omits the need
to compute water, so the irrigation events are omitted, so there is a
minor graininess effect on the whole simulation due to cutting some
simulation steps into two parts with the irrigation events.)

*Debris* is the largely intact dead plant material that is not part of
the soil and that has not broken down to become mulch.

1.  Material flows from plants to the debris.
2.  Material flows from the debris to the soil.

Debris "breaks down". This breakdown is not nitrogen limited.

Note that if you choose the breakdown fractions of the debris as high as
possible (so all the material entering the debris layer almost
immediately leaves for the mulch or soil), you effectively make the
FullCAM debris layer vanish (because it has no effect).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 009. Stem Density 2020

**Stem Density**

\[[Plant Properties](43_Plant%20Properties.htm) window : *Stem Density*
button\]

This is a [Time Series Window](135_time-series%20window.htm) to
facilitate entering the stem density of a tree species.

**Details**

FullCAM uses masses for all its calculations, so stem density is only
used to convert between stem masses and stem volumes. Stem density is
required if:

- Modelling is of a multilayer forest and any of the following:
  - Tree growth is specified by stem volume increments;
  - The amount of stem material is specified by volume in the initial
    conditions; or
  - The amount of stem material in any tree planting is specified by
    volume.

See the *Properties of the Species Time Series* section of [Growth
Properties](42_Growth%20Properties.htm).

If only the trees are modelled, the plant age used in the stem density
time series is the maximum age of the plants (there are no events in
this configuration, so the maximum and average ages are the same).

Because the stem density is a time series, it may vary with the age of
the tree (set *Years are* to "Years since plants sprouted") or with the
year (set *Years are* to "Calendar years" or "Years since start of
simulation").

The stem density is of the whole stem at the time indicated, not of the
new stem growth in that year. The units are kilograms per cubic metre
(note: most other masses in FullCAM are in tonnes).

The density of stem wood is typically between 300--1,000 kgdm/m^3^. A
compendium of wood densities for Australian tree species can be found in
the NCAS Technical Report No. 18.

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 010. Documents and Files 2020

**Documents and Files**

This topic is about using documents and files in FullCAM.

**Document Types**

FullCAM has two document types:

**1. Plot document**\
Represents an area of land with uniform characteristics. Masses are in
tonnes per hectare if there is no area, or in tonnes if you input an
area. Saved in a file extension of ".plo". See [Plot
Simulation](177_Plot%20Simulation.htm).

**2. Estate document**\
Represents an "estate", which is arbitrary collection of plots each with
its own area. Masses are in tonnes. Saved in a file extension of ".est".
See [Estate Simulation](72_Estate%20Simulation.htm).

The main type of document are plots --- for modelling forests and
agriculture regions on a single homogeneous area. Estates add areas to
plots, allowing you to combine multiple plots to model an heterogeneous
area --- such as for modelling a series of plantation forest stands.

**A Document Can Have Multiple Windows**

A document may have more than one window:

- There is always one window active for entering your inputs (the *input
  window*).
- You may create as many output windows as you require.

In FullCAM, you can have multiple graphs or tables for a simulation all
visible at once.

In addition, FullCAM can open any number of documents at once. So you
might have multiple documents open, each with multiple windows open.

A list of all open FullCAM documents can be viewed at the bottom of the
drop down menu when the document item in the main menu is selected or
alternatively in the document drop down list in the toolbar of FullCAM
main window. By selecting a document from either of these locations.

The *Window* menu on the [Main Window](217_Main%20Window.htm) allows you
to manage the windows individually, on a window by window basis.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 011. About 2020

**About**

\[*About* page of the input window of a plot, estate document\]

This page is for your notes about the document. What you enter on this
page has no effect on simulations.

**Name**

Use this area of the 'About' tab to enter a descriptive name for the
Plot. The name has no significance outside this page. The name entered
is not the name by which the plot is saved nor is it used to label any
output.

**Notes**

Notes are purely for recording relevant aspects of a FullCAM simulation.
FullCAM completely disregards these notes for all computational
purposes; they have no effect on any simulation.

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

You will still be able to save the document to a different name using
*Save As*, so you will be able to use it as a template for other
documents.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 012. Site Water 2020

**Site : Water**

\[[Site](200_Site.htm) page : *Water* button\]

This window is where you enter water and moisture information for the
plot, except that the soil-water information is entered in the [Soil
Water](44_Soil%20Water.htm) window.

**Introduction**

Various constituent models need to know the rainfall:
[RothC](114_RothC.htm), [CAMFor](77_CAMFor.htm) (if the breakdown of the
debris of any tree species is sensitive to temperature and rainfall),
and [CAMAg](78_CAMAg.htm) (if the breakdown of the debris of any crop
species is sensitive to temperature and rainfall).

Rainfall can be supplemented by definite irrigation.

**Natural**

The soil model [RothC](114_RothC.htm) requires details of open-pan
evaporation, in order to work out the topsoil moisture deficit (TSMD).

**Irrigation**

The irrigation in the forest and agricultural systems of a plot are
entirely separate, and no water runs from one system to the other.

*Definite irrigation* is irrigation that definitely occurs, regardless
of conditions. If you have historical irrigation data, enter it as
definite irrigation and turn off conditional irrigation. See the
[Definite Irrigation](92_Definite%20Irrigation.htm) time series.

*Conditional irrigation* is irrigation whose occurrence depends on the
conditions. Specify a minimum percentage of the maximum soil water
capacity in the conditional irrigation time series, and FullCAM applies
just enough irrigation to guarantee that the soil water never drops
below this amount. Thus, conditional irrigation ensures a minimum level
of soil water - irrigation is used as conditions require. Use
conditional irrigation to simulate the effect of a management practice
that uses irrigation to ensure a minimum soil water level. Setting the
conditional irrigation percentage to 0% effectively turns off
conditional irrigation. See the [Conditional
Irrigation](91_Conditional%20Irrigation.htm) time series.

The forest and agricultural water simulations are separate (FullCAM
assumes no lateral water movement on the plot), except that they share
the same rainfall, open-pan evaporation, and VPD. The forest and
agricultural irrigations are entirely separate.

Irrigation levels can be specified either with events or with time
series (see [Configure Event Or Time
Series](195_Configure%20event%20or%20time-series.htm)). If using time
series, enter the time series via the buttons on this window. If using
events, enter the events on the [Events](136_Events.htm) page. In either
case, enter all information about irrigation (namely whether conditional
irrigation is on, and which model it uses to operate in the forest).

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 013. Site Temperature 2020

**Site : Temperature**

\[[Site](200_Site.htm) page : *Temperature* button\]

Enter temperature information for the plot.

**Use**

The [RothC](114_RothC.htm) model requires the mean daily average air
temperature and debris sensitivity to temperature.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 014. Credits 2020

**Credits**

**Component Models**

The development of FullCAM and its component models is described in
Australia\'s National Greenhouse Gas Inventory Report. FullCAM includes
the Rothamsted Soil Carbon Model (RothC) described in Jenkinson et. al
(1987), Jenkinson (1990), and Jenkinson et. al (1991).

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
organisations. To view the FullCAM institutional arrangements relating
to the collection and preparation of input data for FullCAM, please
refer to Australia\'s National Greenhouse Gas Inventory Report.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 015. Special Keys 2020

**Special Keys**

The following keys have special meanings that are not necessarily
apparent from looking through the menus. You do not need to know any of
these meanings to use FullCAM with a mouse and the usual keys, but these
meanings can speed you up.

**Enter** - If you are in a number entry box, FullCAM immediately
processes the number.

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
