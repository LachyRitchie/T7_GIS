---
version: 2016
batch_range: 051-100
batch_name: Species_Events_Management
creation_date: 2025-08-28
total_files: 27
---

# FullCAM 2016 - Batch 051-100: Species Events Management

## Table of Contents

- [051. Forest Treatment 2016](#051-forest-treatment-2016)
- [052. Chopper Roller 2016](#052-chopper-roller-2016)
- [053. Termite Change 2016](#053-termite-change-2016)
- [054. Irrigation Change 2016](#054-irrigation-change-2016)
- [056. Select a Species 2016](#056-select-a-species-2016)
- [057. Plots, Systems, Layers, and Pools 2016](#057-plots,-systems,-layers,-and-pools-2016)
- [058. Processes and Events 2016](#058-processes-and-events-2016)
- [059. Find Request in a Table 2016](#059-find-request-in-a-table-2016)
- [062. Manure-From-Offsite Change 2016](#062-manure-from-offsite-change-2016)
- [064. Site Productivity 2016](#064-site-productivity-2016)
- [065. Correlation Between Two Risk Inputs 2016](#065-correlation-between-two-risk-inputs-2016)
- [072. Estate Simulation 2016](#072-estate-simulation-2016)
- [077. CAMFor 2016](#077-camfor-2016)
- [078. CAMAg 2016](#078-camag-2016)
- [086. Decay Rate Window 2016](#086-decay-rate-window-2016)
- [088. Rainfall 2016](#088-rainfall-2016)
- [089. Average Air Temperature 2016](#089-average-air-temperature-2016)
- [090. Soil Fertility Rating 2016](#090-soil-fertility-rating-2016)
- [091. Conditional Irrigation 2016](#091-conditional-irrigation-2016)
- [092. Definite Irrigation 2016](#092-definite-irrigation-2016)
- [093. Solar Radiation 2016](#093-solar-radiation-2016)
- [094. Frost Nights 2016](#094-frost-nights-2016)
- [096. Air Temperature 2016](#096-air-temperature-2016)
- [097. Vapour Pressure Deficit 2016](#097-vapour-pressure-deficit-2016)
- [097. Vapour Presser Deficit 2016](#097-vapour-presser-deficit-2016)
- [098. Open-Pan Evaporation 2016](#098-open-pan-evaporation-2016)
- [099. Plant Residue Inputs to Soil 2016](#099-plant-residue-inputs-to-soil-2016)

---

## 051. Forest Treatment 2016

**Forest Treatment**

\[[Event Window](137_Event%20Window.htm) : *Forest Treatment* panel\]

Enter the inputs specific to a forest treatment event.

**Details**

A forest treatment can be applied to a forest whose growth is being
determined by the tree yield formula [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm). The treatment alters the
growth characteristics of the trees onward from that point in time.

Each treatment has a Type 1 and a Type 2 effect as described in
*Snowden, P (2002) Modelling Type 1 and Type 2 Growth Responses in
Plantations after Application of Fertilizer or Other Silvicultural
Treatments. Forest Ecology and Management 163:229--244*.

Put simply, a Type 1 event occurs during the life of a rotation and has
an effect for a specified period (generally to advance the rate of
growth) in a way that would likely shorten overall rotation length. A
Type 2 event is an increase in site productivity (possibly due to
species change) over the entire rotation period.

**Type 1: Age Advance**

A type 1 treatment moves the forest back (or forth) along the growth-age
curve determined by the tree yield formula, by advancing (or retarding)
the adjusted age of the trees used in the formula. See [Growth
Properties](42_Growth%20Properties.htm).

The tree age used in the tree yield formula is advanced by the *Age
advance due to treatment*, phased in steadily over the years in the
*Advancement period* (which begins starting with the event).

**Example**

Suppose that in May 2004 a pine plantation gets a nitrogen fertiliser
dose, whose effect is to speed up growth by moving the trees six years
along the growth-age curve over the next five years. Suppose that you
are modelling the plantation's growth using the tree yield formula. Then
you would create a forest treatment event in May 2004 whose "Age advance
due to treatment" is 1.00 (because the total extra advance due to the
treatment is +1.00 years --- six years growth in five real years is an
advance of one year) and whose "Advancement period" is 5 years (because
the advance is phased in over five real years).

The effects of multiple treatments ARE cumulative. For example, the
effect of an age advance of 1.0 years over five years starting 2004 and
another age advance of 1.5 years over 3 years starting 2005 would be an
age advance of 2.5 years from 2009 and onward (when both advances are
fully applied).

The effect of age advances persist for the life of the forest, but are
cancelled when the forest is cleared or a coppice created (that is, when
all the aboveground mass of the trees is removed).

The effect of the forest treatments is directly visible in the "Age of
trees used in tree yield formula" output (Element-independent : Timing).

A forest treatment with an age advance of zero should have no effect. In
practice, however, it may have a slight effect if the number of
simulation steps per year is low enough to cause significant graininess
(see [Simulation Steps](5_Simulation%20Steps.htm)) --- because the
forest treatment event breaks a step into two parts.

**Type 2: Tree Yields**

When the tree yield formula is in use, the maximum aboveground biomass
is equal to the maximum aboveground biomass entered in the *Site* window
(*M* in the tree yield formula, see [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm)) multiplied by the current tree
yield multiplier (*y*).

Thus the "tree yield multiplier" multiplies the tree yield that would
otherwise be computed by the tree yield formula (because the tree yield
is proportional to the maximum aboveground biomass in the tree yield
formula), and likewise multiplies the maximum aboveground forest biomass
allowed on the site.

The tree yield multiplier always starts a simulation at 1.0, and only
changes due to forest treatments. Each type 2 forest treatment replaces
the previous treatment --- the effects of type 2 forest treatments are
NOT cumulative.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 052. Chopper Roller 2016

**Chopper Roller**

\[[Event Window](137_Event%20Window.htm) : *Chopper Roller* panel\]

Enter the inputs specific to a chopper roller event.

**Details**

A chopper roller event is where machines run over post-harvest slash
(residue) of a forest breaking up the coarse woody litter (that is,
coarse aboveground debris). This typically only occurs after thinning
100% of forest plantations, and its goal is to accelerate the breakdown
of the coarse litter.

A chopper roller event can only occur in a forest when there are no
trees.

In a chopper roller event in FullCAM:

- The specified percentages of material in the deadwood and bark pools
  are moved to the chopped wood pools.
- The distinction between decomposable and resistant material is
  maintained: there is a decomposable chopped wood pool and a resistant
  chopped wood pool.

The chopped wood pools have their own breakdown inputs, set in the
[Debris Properties](45_Debris%20Properties.htm) window for each tree
species. The breakdown percentages of the chopped wood (that is, the
percentages that breakdown per year) are typically higher than the
breakdown percentages of the deadwood or bark pools.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 053. Termite Change 2016

**Termite Change**

\[[Event Window](137_Event%20Window.htm) : *Termite Change* panel\]

Enter the inputs specific to a termite change event.

**Details**

Enter the inputs that describe the level of termite activity from now
until the next termite change event.

There is no termite activity at the beginning of a simulation. Termite
action begins with the first termite event. Turn off future termite
activity again by setting all the inputs of a termite event to zero.

In FullCAM, termites only eat deadwood and coarse dead roots in forests.
The eaten material goes immediately to the atmosphere.

A "percentage eaten by termites" is the percentage of the material in
the pool at the beginning of each simulation step that does not break
down during the step but that is eaten by termites. Material added to
the debris during a step cannot be eaten by termites --- so even with
100% termite percentages there may be a little coarse woody debris
present at the end of each step.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 054. Irrigation Change 2016

**Irrigation Change**

\[[Event Window](137_Event%20Window.htm) : *Irrigation Change* panel\]

Enter the inputs specific to an irrigation change event.

**Details**

Enter the inputs that describe the level of forest or agricultural
irrigation from now until the next irrigation event (of the same kind,
forest or agricultural).

There is no irrigation at the beginning of a simulation. Irrigation
begins with the first irrigation event. Turn off future irrigation again
by setting all the inputs of an irrigation event to zero.

This time-series is only used when the *Irrigation* setting on the
[Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm) window is set
to *Events*.

See [Site : Water](12_Site_Water.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 056. Select a Species 2016

**Select a Species**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Select a
Species* panel\]

Choose the tree or crop species to edit in the remainder of the page.

**Details**

A species is *in use* in the simulation either because it is the initial
species or because it is planted in a planting event.

The plot is only ready for simulation if every species that is used in
the simulation is ready. Species that are not ready to simulate are
shown in red.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 057. Plots, Systems, Layers, and Pools 2016

**Plots, Systems, Layers, and Pools**

An overview of the things that are modelled in FullCAM, and defines the
terms used in FullCAM for those things.

**Plots**

A *plot* is a piece of land with uniform characteristics. There are
three kinds of plot:

1.  *Forest plot* - The plants are trees.
2.  *Agricultural plot* - The plants are crops.
3.  *Mixed plot* - A mixed plot is partly forest and partly agricultural
    (such as grazed woodland or agroforestry areas). The fraction of the
    plot that is forest (the [Forest
    Percentage](206_Forest%20Percentage.htm); the rest is agricultural)
    may vary with time. Mixed plots allow FullCAM to model transitional
    systems such as deforestation to an agricultural use or
    reforestation of pasture.

The area of the plot is irrelevant within a FullCAM plot simulation,
because all quantities are processed by the program on a "per hectare"
basis. In particular, masses are measured in tonnes per hectare (so when
we say "mass", we often really mean "mass per unit area"). If you prefer
to work in "tonnes" rather than "tonnes per hectare" then you can
specify an area for the plot ([Site : Area](157_Site_Area.htm)).

Estate and spatial simulations work by simulating each plot in the area
under consideration then multiplying the results by the area (in
hectares) of the relevant plots.

**Systems**

A system is an independent ecosystem on a plot. There are two types of
*system*:

1.  *Forest (system)* - A forest has trees, and the characteristics we
    associate with trees.
2.  *Agricultural system* - An agricultural system has crops, and the
    characteristics we associate with crops.

A plot consists of one or both systems:

1.  A forest plot consists of one system, namely a forest system.
2.  An agricultural plot consists of one system, namely an agricultural
    system.
3.  A mixed plot consists of two systems, namely a forest system and an
    agricultural system.

*Plants* are either trees or crops. A *species* is either a "tree
species" or a "crop species":

- A tree species grows in a forest
- A crop species grows in an agricultural system.

In a FullCAM simulation:

- Only one tree species can be growing in the forest at any one time
- Only one crop species can be growing in the agricultural system at any
  one time.

Either system may be *clear*, which means it has no plants growing in
it.

**Layers**

A *layer* is a part of a system with similar characteristics. Each
system is partitioned into six layers:

*Plants* - Either *trees* or *crops*. The plants remove carbon from the
atmosphere by production (the combination of photosynthesis and
respiration). Plant material moves to the debris via turnover, and to
the products by thinning or harvesting. Crop material also moves to the
atmosphere.

*Debris* Dead plant material that has not reached the soil or (if the
mulch is simulated) the mulch. Debris is further partitioned into:

1.  *Litter* --- Aboveground debris. Material moves to the atmosphere
    and to either the mulch (if the mulch is simulated) or the active
    soil (if not) by breakdown.
2.  *Dead roots* --- Belowground debris. Material moves to the
    atmosphere and to the active soil by breakdown.

*Mulch* - An optional aboveground layer between the litter and the soil,
in which microbial action is modelled. Material moves to the atmosphere
and within the mulch by decomposition, within the mulch by microbial
death, and to the soil and atmosphere by humification.

*Soil* - The soil is further partitioned into:

*Active* --- For material that can be moved elsewhere in the model.
Material moves to the atmosphere and within the active soil by
decomposition, and to the inert soil by encapsulation.

*Inert* --- For material in the soil that does not move anywhere else in
the model (that is, it stays in the inert soil forever). Carbon that is
encapsulated physically (usually in clay) or chemically (usually as
char) may be considered inert. Fires can move carbon from all of the
above layers into the inert soil.

In addition, the atmosphere is treated by the model as an infinite
reservoir of carbon.

**Pools**

Each layer (except for the minerals) is further partitioned into several
pools. A *pool* is a collection of material that is homogeneous and not
further subdivided in FullCAM. From a mechanical point of view, a
FullCAM simulation consists of moving material between pools.

For example, in a forest the plant layer (that is, the trees) consists
of the stem, branch, bark, leaf, coarse root, and fine root pools.

A layer is a collection of neighbouring pools with similar
characteristics.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 058. Processes and Events 2016

**Processes and Events**

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

Moves material from a plant pool to a debris pool as the material dies
(and possibly drops off the plant).

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

An "event" is a particular management action that occurs occasionally or
irregularly. An event is applied immediately, generally perturbing the
biological processes involved. Events are usually human management
actions.

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
thereby forming an "event queue", on the [Events](136_Events.htm) page
on the input window of a plot document. During a simulation, FullCAM
simply applies the events at the times they are specified to occur.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 059. Find Request in a Table 2016

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

## 062. Manure-From-Offsite Change 2016

**Manure-From-Offsite Change**

\[[Event Window](137_Event%20Window.htm) : *Manure-From-Offsite Change*
panel\]

Enter the inputs specific to a manure-from-offsite change event.

**Details**

Enter the yearly level of application of manure from offsite to the
forest or agricultural soil, from now until the next manure-from-offsite
event (of the same kind, forest or agricultural).

There is no application of manure from offsite at the beginning of a
simulation. Application of manure to the soil begins with the first
manure-from-offsite event. Turn off future application of manure from
offsite again by setting the input of a manure-from-offsite event to
zero.

Manure from offsite is in addition to and separate from the manure due
to grazing animals in an agricultural system.

This event is only used when the *Nitrogen Fertiliser Application*
setting on the [Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm) window is set
to *Events*.

Set the properties of the manure in [Soil
Inputs](193_Soil%20Inputs.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 064. Site Productivity 2016

**Site : Productivity**

\[[Site](200_Site.htm) page : *Productivity* button\]

Enter information about the productivity of the plot.

**Use**

"Soil fertility rating" and "Soil nutrition modifier" (which are very
closely related) are on this window in the [Site](200_Site.htm) page
rather than on the [Soil](203_Soil.htm) page because they represent
general properties of the site and its soil, rather than properties due
entirely to soil characteristics.

The forest productivity index (FPI) is required when the tree yield
formula is used to compute tree production, and the FPI is not computed
from scratch by FullCAM --- see [Configure Tree
Production](108_Configure%20Tree%20Production.htm).

Only one of these three measures of productivity is required at any one
time.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 065. Correlation Between Two Risk Inputs 2016

**Correlation Between Two Risk Inputs**

\[[Risk Properties of an
Input](182_Risk%20Properties%20of%20an%20Input.htm) window : *Edit
Correlation* button\]

Enter the correlation between two risk inputs.

**Use**

Enter a number from --1.0 to +1.0.

A value of 0.0 indicates that the two risk inputs are not correlated:
when one rises, the other is just as likely to fall as to rise.
Uncorrelated inputs are not necessarily independent (they can be related
in a non-linear way, such as x and y in x = y \* y).

A value of +1.0 indicates that the risk inputs are fully positively
linearly correlated: whenever one increases by a certain amount, the
other increases by a proportional amount.

A value of --1.0 indicates that the risk inputs are fully negatively
linearly correlated: whenever one increases by a certain amount, the
other decreases by a proportional amount.

A value between 0.0 and +1.0 indicates that the risk inputs are somewhat
positively linearly correlated: when one increases by a certain amount,
the other is more likely to rise than to fall, and tends to do so by a
proportional amount.

A value between 0.0 and --1.0 indicates that the risk inputs are
somewhat negatively linearly correlated: when one increases by a certain
amount, the other is more likely to fall than to rise, and tends to do
so by a proportional amount.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 072. Estate Simulation 2016

**Estate Simulation**

Some general aspects of simulating an estate in FullCAM.

**Estates**

An estate is an arbitrary collection of plots, where each plot is
assigned an area.

A FullCAM plot is a model of what is happening at a particular point (a
position with no area), and is limited to one tree species and one crop
species and the interplay between them. An estate provides the mechanism
for combining FullCAM plots into an area.

For example, to model a few hectares of plantation containing five
species of trees, you would create:

1.  Five FullCAM plots, one for each of the tree species.
2.  One FullCAM estate that defines the appropriate area for each plot,
    multiples plot results by plot areas and adds the resultant values
    together to give a single estate value for each output variable
    selected.

**Estate Documents**

An estate document specifies a list of plots, where each plot also has:

1.  An area (in hectares);
2.  A starting date for simulation of the plot.

The estate represents the sum of the individual areas assigned to each
plot. Each plot and its associated area is entered into the estate
simulation on the basis of the starting time specified. See [Plots in
the Estate](167_Plots%20in%20the%20Estate.htm).

**What Happens in an Estate Simulation**

An estate simulation performs a plot simulation for each plot in the
estate. The results (typically in t/ha) are multiplied by the plot area
(so the results are, typically, in tonnes). The results for all plots
are added together, to give the results for the entire estate.

1.  FullCAM creates a plot document in memory, called the *working
    plot*. The working plot is blank, but copies the timing and output
    information from the estate document.
2.  FullCAM zeroes the outputs in the estate document.
3.  For each plot in the estate FullCAM:
    - Reads the plot file into the working plot, except for the timing
      and output information.
    - Performs a plot simulation on the working plot.
    - Multiplies the working plot outputs by the area of the plot (for
      appropriate outputs) and add them to the outputs in the estate
      document.
4.  Scales the outputs in the estate document to allow for additive
    (such as carbon mass) or average (such as rainfall) outputs.
5.  Destroys the working plot.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 077. CAMFor 2016

**CAMFor**

The CAMFor model is one of the [Constituent Models In
FullCAM](198_Constituent%20Models%20In%20FullCAM.htm).

**Description**

CAMFor is a model of a forest ecosystem --- trees, debris, soil,
minerals, and products. It models all movements of carbon between a
forest system and the atmosphere.

CAMFor is a straightforward calculation tool, moving material around the
forest system with simple inputs such as ratios, rate constants, and
growth tables. It models processes such as growth, turnover, and
decomposition that occur continuously. It models events, such as
planting, thinning, and fires. It always tracks the carbon in each part
of the system, and optionally tracks the nitrogen as well. It can
operate at various timescales.

The name "CAMFor" comes from *C*arbon *A*ccounting *M*odel for
*FOR*ests.

CAMFor is a framework model. A tree growth model, a mulch model, and a
soil model can be plugged into it to provide more detailed modelling of
these layers. CAMFor does not model the soil itself (although it used
to); it requires a specialist soil model to model the soil for it.

CAMFor is very similar to [CAMAg](78_CAMAg.htm).

**Credits**

The CAMFor model within FullCAM finds its conceptual foundations in a
public domain FORTRAN program called *CO~2~Fix*, published in October
1990 by Frits Mohren, Kees Klein Goldewik, "De Dorrchamp", Wageningen.
It was enhanced and otherwise designed at the Australian Greenhouse
Office by Gary Richards, with modelling and programming by David Evans .

CAMFor should be cited as Richards, GP; Evans, DMW; (2000) Carbon
Accounting Model for Forests (CAMFor v3.35) User Manual, National Carbon
Accounting System [Technical Report No.
26](reps/TR26%20Carbon%20Accounting%20Model%20for%20Forests%20(CAMFor)%20User%20Manual%20Version%203.35.pdf){target="reps26"},
Australian Greenhouse Office.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 078. CAMAg 2016

**CAMAg**

The CAMAg model is one of the [Constituent Models In
FullCAM](198_Constituent%20Models%20In%20FullCAM.htm).

**Description**

CAMAg is a model of an agricultural (cropped land) ecosystem --- crop,
debris, soil, minerals, and products. It models all movements of carbon
between an agricultural system and the atmosphere.

CAMAg is a straightforward calculation tool, moving material around the
agricultural system with simple inputs such as ratios, rate constants,
and growth tables. It models processes such as growth, turnover, and
decomposition that occur continuously. It models events, such as
planting, harvest, and fires. It always tracks the carbon in each part
of the system. It can operate at various timescales.

The name "CAMAg" comes from *C*arbon *A*ccounting *M*odel for
*AG*riculture.

CAMAg is a framework model. A mulch model and a soil model can be
plugged into it to provide more detailed modelling of these layers.
CAMAg does not model the soil itself; it requires a specialist soil
model to model the soil for it.

CAMAg is very similar to [CAMFor](77_CAMFor.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 086. Decay Rate Window 2016

**Decay Rate Window**

\[[Plant Properties](43_Plant%20Properties.htm) window : any *Decay
Rate* button\]\
\[[Debris Properties](45_Debris%20Properties.htm) window : any *Decay
Rate* button\]

This window is for entering a single number that describes the rate of
decay of a pool due to some process.

Enter the decay rate using any of the nine equivalent expressions (the
FullCAM interface only ever shows rate as the percentage lost after a
year).

**Definition**

Consider a pool of material where:

1.  Material leaves the pool at a rate that is proportional to the
    amount of material in the pool
2.  No material enters the pool.

The *decay rate* is the number that describes how fast the material in
the pool leaves the pool. This window is for entering the decay rate for
a decay process in FullCAM.

**Example**. A decay rate of 10% per year means that:

- After the first year only 90% of the pool remains
- After two years only 90% \* 90% = 81% of the original pool remains
- In the third year another 10% of the material present at the beginning
  of the third year is lost, so after three years only 90% \* 90% \* 90%
  = 72.9% of the original pool remains,

and so on.

The simple model above occurs in many places in FullCAM, for example
when describing the turnover of plant components, the breakdown of
debris, or the decomposition of product pools.

Although the rate of outflow can be measured more easily if there is no
inflow into the pool, there can be inflows to the pool at the same time
as the decay process is causing material to leave the pool. The decay
rate simply measures the rate of the outflow due to the decay process.

(The process by which material leaves the pool above is *exponential*,
because the rate at which material leaves is proportional to the amount
of material present. An exponential decay model is widely used in
FullCAM because it is a reasonably accurate representation of a wide
range of biological processes, while being mathematically simple).

(The process by which material leaves the pool above is *exponential*,
because the rate at which material leaves is proportional to the amount
of material present. An exponential decay model is widely used in
FullCAM because it is a reasonably accurate representation of a wide
range of biological processes, while being mathematically simple).

**Equivalent Expressions**

In the FullCAM interface, the rate asked for is the percentage lost per
year (for example the percentage of coarse roots turnover per year, or
the percentage of product decomposed each year). The "percentage lost
per year" is the way that FullCAM stores a decay rate and the way it
uses it in the simulation calculations.

However, some rates are not suitably expressed as the percentage lost
per year. For example, 99.999% lost per year is better expressed as
61.7% lost per month, or 3.1% lost per day, or a half life of 22 days.
There is no single way for specifying the rates that is suitable over
the wide range that might be used in FullCAM. Hence this window.

By clicking on the button next to the rate box in the FullCAM interface,
you opened this window, the decay rate window. The only purpose of this
window is to enter a single number, the decay rate. The use of this
window is optional --- the single number in the regular FullCAM
interface (which is always the percentage lost after a year) is usually
enough.

There are nine equivalent expressions for the decay rate. Click on a
radio button to enter the rate in that form. Press the *Insert* key to
enter the number you type into FullCAM (as in the FullCAM interface),
and have the rate translated into the other eight expressions.

**Graph**

The graph shows the amount left in the pool as a percentage of the
original amount in the pool (red), and the half life of the decay
process (orange).

**Decay Equation**

The equation for exponential decay, shown in the graph, is that after a
time *T*:

  ----------------------------------------- -- ------------------------------------------
  The fraction lost from the pool is           1 -- \[(1 -- *f*) \^*T*\]
  The fraction remaining in the pool is        (1 -- *f*) \^*T*
  The percentage lost from the pool is         100 \* 1 -- \[(1 -- 0.01 \* *p*) \^*T*\]
  The percentage remaining in the pool is      100 \* (1 -- 0.01 \* *p*) \^*T*
  ----------------------------------------- -- ------------------------------------------

where *f* is the fraction lost per year and *p* is the percentage lost
per year (*p* = 100 \* *f*). Note that "\^" means "to the power of", for
example 3\^2 = 3 to the power of 2 = 3 squared = 9.

**Limits**

The decay rate shown in this window cannot be:

- Higher than 99.999 999 998% lost per year (equivalent to 6.5% lost per
  day and to a half life of 0.028 years)
- Lower than 0.0001% lost per year (equivalent to 0.000000274% lost per
  day and to a half life of 693,146 years)

Above and below these limits not all the nine equivalent expressions can
be shown, because of limits in the numerical representation used in
FullCAM (64-bit floating point numbers). Near these limits, some of the
equivalent expressions may be slightly different to what you type in.
This phenomenon is intrinsic to the equivalent expressions, and of no
concern. The expression stored by FullCAM is the percentage lost after a
year. A number typed into another expression is converted to this form
in FullCAM, and then displayed by converting back to the appropriate
equivalent expression. So, when you type in a number in one of the
equivalent expressions, the number is converted to a percentage lost
after a year and then converted back before being displayed. These
conversions are slightly inaccurate at extreme values, due to numerical
roundoff. Any conversion errors are insignificant compared to
experimental error, so, while slightly annoying, are of no concern.

If this decay rate window is used to edit a decay rate outside the
limits, the decay rate is first changed to fit just within the limits.

If you want to enter a decay rate of zero, you have to do so in the
FullCAM interface rather than in this decay rate window.

**Window Navigation**

Although it is possible to navigate the screen with tabs and up-down
arrow keys, we recommend selecting the type of description (the radio
buttons) with the mouse. Because you have to use the mouse in this
window anyway, you can only use the mouse to click the buttons that open
the decay rate window (rather than being able to tab to those buttons).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 088. Rainfall 2016

**Rainfall**

\[[Site : Water](12_Site_Water.htm) window : *Rainfall* button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the total rain falling onto the plot, in millimetres (100 mm = 1
megalitre per hectare).

**Details**

If actual site data is available, enter it in this time-series. If not,
use [Data Builder](132_Data%20Builder.htm) to download estimated monthly
rainfall data (the derivation of this data is described in [NCAS
Technical Report
No.23](reps/TR23%20Developing%20a%20National%20Forest%20Productivity%20Model.pdf){target="reps23"}).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 089. Average Air Temperature 2016

**Average Air Temperature**

\[[Site : Temperature](13_Site_Temperature.htm) window : *Average Air
Temperature* button\]

This [time-series Window](135_time-series%20window.htm) is where you
enter the daily average air temperature, in degrees Celsius.

**Details**

If actual site data is available, enter it in this time-series. If not,
use [Data Builder](132_Data%20Builder.htm) to download estimated monthly
average air temperature data (the derivation of this data is described
in [NCAS Technical Report
No.23](reps/TR23%20Developing%20a%20National%20Forest%20Productivity%20Model.pdf){target="reps23"}).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 090. Soil Fertility Rating 2016

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

## 091. Conditional Irrigation 2016

**Conditional Irrigation**

\[[Site : Water](12_Site_Water.htm) window : *Conditional Irrigation*
button (*Forest* or *Agricultural*)\]

This [time-series Window](135_time-series%20window.htm) is where you
enter the percentage of the soil water capacity that is guaranteed by
conditional irrigation.

**Details**

In every simulation step, FullCAM applies just enough conditional
irrigation to bring the soil water level up to this specified percentage
of the maximum soil water level. All other water (namely rainfall and
definite irrigation) is applied first, and if the soil water level is
still below this guaranteed percentage then FullCAM applies the
conditional irrigation required to bring the water level up this
percentage. This window is a typical time-series window provided that
irrigation was specified to occur as a time-series in the \'Events or
time-series\' window of the \'Configuration\' Tab. If irrigation was
specified as events then irrigation events need to be added to the
\'Events\' Tab.

This time-series is only used when the *Irrigation* setting on the
[Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm) window is set
to *time-series*.

See [Site : Water](12_Site_Water.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 092. Definite Irrigation 2016

**Definite Irrigation**

\[[Site : Water](12_Site_Water.htm) window : *Definite Irrigation*
button (*Forest* or *Agricultural*)\]

This [time-series Window](135_time-series%20window.htm) is where you
enter irrigation that definitely occurs (does not depend on conditions),
in millimetres (100 mm = 1 megalitre per hectare).

The window is also a typical time-series window provided that irrigation
was specified to occur as a time-series in the \'Events or time-series\'
window of the \'Configuration

Tab\'. If irrigation was specified as events, then irrigation events
need to be added to the \'Events\' Tab.

**Details**

This time-series is only used when the *Irrigation* setting on the
[Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm) window is set
to *time-series*.

See [Site : Water](12_Site_Water.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 093. Solar Radiation 2016

**Solar Radiation**

\[Site : Light window : Solar Radiation button\]

This [time-series Window](135_time-series%20window.htm) is where you
enter the mean daily solar radiation incident on the plot, in megajoules
per square metre.

If actual site data is available, then it may be entered on this table.
Should such data not be available, use the [Data
Builder](132_Data%20Builder.htm) function to obtain estimated solar
radiation data. The derivation of this data is described in [NCAS
Technical Report No.
23](reps/TR23%20Developing%20a%20National%20Forest%20Productivity%20Model.pdf){target="reps23"}.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 094. Frost Nights 2016

**Frost Nights**

\[[Site : Temperature](13_Site_Temperature.htm) window : *Frost Nights*
button\]

This [time-series Window](135_time-series%20window.htm) is where you
enter the number of nights in which any frost occurs. For example, if
there were frosts on the nights of March 12, 14 and 16 (only) in March
1963 then the time-series value for March 1963 would be "3".

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 096. Air Temperature 2016

**Air Temperature**

The source of air temperature data must first be specific. Choose either
average or if actual site data is available, enter it in the
time-series.

\'Air Temperature time-series\' or \'Estimate from min and range of air
temperatures\' from the drop down menu to select the type of air
temperature data that is available. If \'Average Air Temperature
time-series\' is selected, then click on the \'Average Air Temperature\'
button to input average daily air temperature values in degrees Celsius
as a time-series using the typical time-series window.

If average air temperature data is not available, but minimum and
maximum air temperature data are, then select the \'Estimate from min.
and range of air temperature\' menu item. The input the daily minimum
air temperature data in degrees Celsius and the daily temperature range
in degrees Celsius by clicking on the \'Minimum Air Temperature\...\'
and \'Air Temperature Daily Range\...\' buttons.

If the average daily temperature, minimum temperature or temperature
range data are not available, use the [Data
Builder](132_Data%20Builder.htm) to obtain estimated values. The
derivation of this data is described in [NCAS Technical Report No.
23](reps/TR23%20Developing%20a%20National%20Forest%20Productivity%20Model.pdf){target="reps23"}.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 097. Vapour Pressure Deficit 2016

**Vapour Pressure Deficit**

\[[Site : Water](12_Site_Water.htm) window : *Vapour Pressure Deficit*
button \]

This [time-series Window](135_time-series%20window.htm) is where you
enter the mean daily vapour pressure deficit (VPD), in Kilopascals.

**Details**

If actual site data is available, enter it in this time-series. If not,
use [Data Builder](132_Data%20Builder.htm) to download estimated monthly
vapour pressure deficit data (the derivation of this data is described
in [NCAS Technical Report
No.23](reps/TR23%20Developing%20a%20National%20Forest%20Productivity%20Model.pdf){target="reps23"}).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 097. Vapour Presser Deficit 2016

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

## 098. Open-Pan Evaporation 2016

**Open-Pan Evaporation**

\[[Site : Water](12_Site_Water.htm) window : *Open-pan Evaporation*
button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the open-pan evaporation for the plot, in millimetres (100 mm =
1 megalitre per hectare).

**Details**

If actual site data is available, enter it in this time-series. If not,
use [Data Builder](132_Data%20Builder.htm) to download estimated monthly
open-pan evaporation data (the derivation of this data is described in
[NCAS Technical Report
No.23](reps/TR23%20Developing%20a%20National%20Forest%20Productivity%20Model.pdf){target="reps23"}).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 099. Plant Residue Inputs to Soil 2016

**Plant Residue Inputs to Soil**

\[[Soil Inputs](193_Soil%20Inputs.htm) window : *Plant Residues*
button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the carbon mass of plant residues from the debris and mulch that
enter the soil, in tonnes per hectare.

**Details**

FullCAM automatically calculates these inputs in multi-layer plot models
that include the soil ([Configure the
Plot](6_Configure%20the%20Plot.htm)), so this input is only required
when the soil is being modelled on its own.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
