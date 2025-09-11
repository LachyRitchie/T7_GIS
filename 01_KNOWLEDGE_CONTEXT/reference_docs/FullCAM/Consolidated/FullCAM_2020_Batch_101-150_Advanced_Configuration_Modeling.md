---
version: 2020
batch_range: 101-150
batch_name: Advanced_Configuration_Modeling
creation_date: 2025-08-28
total_files: 30
---

# FullCAM 2020 - Batch 101-150: Advanced Configuration Modeling

## Table of Contents

- [101. Manure Inputs to Soil from Offsite 2020](#101-manure-inputs-to-soil-from-offsite-2020)
- [102. Soil Cover 2020](#102-soil-cover-2020)
- [108. Configure Tree Production 2020](#108-configure-tree-production-2020)
- [110. Tree Growth Increments 2020](#110-tree-growth-increments-2020)
- [112. Tree Growth Allocations 2020](#112-tree-growth-allocations-2020)
- [114. RothC 2020](#114-rothc-2020)
- [116. Forest Percentage Change 2020](#116-forest-percentage-change-2020)
- [118. Crop Growth Increments 2020](#118-crop-growth-increments-2020)
- [120. Plant Removal and Replacement 2020](#120-plant-removal-and-replacement-2020)
- [121. Mortality 2020](#121-mortality-2020)
- [122. Sensitivity of Debris Breakdown to Temperature and Water 2020](#122-sensitivity-of-debris-breakdown-to-temperature-and-water-2020)
- [123. Notes on a Plant Species 2020](#123-notes-on-a-plant-species-2020)
- [124. Crop Growth Allocations 2020](#124-crop-growth-allocations-2020)
- [127. Simulate Menu 2020](#127-simulate-menu-2020)
- [130. Tree Yield Formula 2020](#130-tree-yield-formula-2020)
- [131. Yield and Net Primary Production 2020](#131-yield-and-net-primary-production-2020)
- [132. Data Builder 2020](#132-data-builder-2020)
- [135. Time-Series Window 2020](#135-time-series-window-2020)
- [136. Events 2020](#136-events-2020)
- [137. Event Window 2020](#137-event-window-2020)
- [138. Configure Other Options 2020](#138-configure-other-options-2020)
- [140. Thin 2020](#140-thin-2020)
- [141. Models and Inputs Window 2020](#141-models-and-inputs-window-2020)
- [142. Standard Events of a Species 2020](#142-standard-events-of-a-species-2020)
- [143. Event Timing 2020](#143-event-timing-2020)
- [144. Forest Fire 2020](#144-forest-fire-2020)
- [145. Properties of the Species 2020](#145-properties-of-the-species-2020)
- [146. Standard Information for the Species 2020](#146-standard-information-for-the-species-2020)
- [149. Agricultural Fire 2020](#149-agricultural-fire-2020)
- [150. Configuration 2020](#150-configuration-2020)

---

## 101. Manure Inputs to Soil from Offsite 2020

**Manure Inputs to Soil from Offsite**

\[[Soil Inputs](193_Soil%20Inputs.htm) window : *Manure from Offsite*
button\]

This [Time Series Window](135_time-series%20window.htm) is where you
specify the carbon mass (and maybe also the nitrogen mass) entering the
soil from outside the plot, in tonnes per hectare.

**Details**

Manure from offsite (from outside the plot) may be added to the forest
or agricultural soil.

In an agricultural system, manure from animals on the plot is dealt with
by grazing --- see the [Grazing Change](196_Grazing%20Change.htm)
events: plant material eaten by grazing animals becomes fodder, which
may go to destinations including the DPM an RPM pools of the soil. This
manure-from-offsite time series is the only explicit treatment of manure
by FullCAM.

This time series is only used when the *Manure-From-Offsite Added to the
Soil* setting on the [Configure Event Or Time
Series](195_Configure%20event%20or%20time-series.htm) window is set to
*Time series*.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 102. Soil Cover 2020

**Soil Cover**

\[[Soil](203_Soil.htm) page : *Agricultural* panel : *Soil Cover*
button\]

This [Time Series Window](135_time-series%20window.htm) is where you
specify whether or not the agricultural soil is covered, in plot models
that only model the agricultural soil (see [Configure the
Plot](6_Configure%20the%20Plot.htm)).

**Agricultural Soil**

The soil cover factor is a rate modifier applied against soil decay as
computed by the [RothC](114_RothC.htm) model. It is set as covered
(default value of 0.6) when a plant exists, slowing down decay. When a
plot is uncovered the value is set to 1, speeding up decay.

When the soil cover is automatically calculated by FullCAM as part of a
multilayer agricultural system, the agricultural soil is considered to
be always covered except after clearing events where crop and pasture is
fully removed.

If you are modelling the soil but not the whole agricultural system,
then you have to tell FullCAM when the soil is covered or not. Soil
cover consists of debris and plants, and it affects the rate of moisture
loss from the soil and thus the agricultural soil water levels.

Enter the soil cover time series to tell FullCAM when there is enough
soil cover to slow down the rate of water loss from the soil. If the
agricultural soil is covered by vegetation or debris (and thus less
prone to drying out) for the whole of the relevant period, then enter 1.
If it is bare for the whole period, enter 0. If it is partly covered for
all of the period, or covered for only part of the period, enter a
number between 0 and 1.

After interpolation and extrapolation to get a soil cover value in each
simulation step, a soil cover value of 0.5 or greater is treated as
covered and a soil over value of less than 0.5 is treated as bare.

**Forest Soil**

Forest soil is considered to be always covered.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 108. Configure Tree Production 2020

**Configure Tree Production**

\[[Configuration](150_Configuration.htm) page : *Tree Production*
panel\]

Specify how the production of new tree material should be calculated.

**Method**

Choose a tree growth method:

- *Increments* - FullCAM will use time series of volume or mass
  increments of new growth, by calendar year or by tree age. Data must
  be supplied in the [Growth Properties](42_Growth%20Properties.htm)
  window.
- *Tree yield formula* - Uses an empirical biomass yield equation, the
  [Tree Yield Formula](130_Tree%20Yield%20Formula.htm), to calculate
  tree growth.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 110. Tree Growth Increments 2020

**Tree Growth Increments**

\[[Growth Properties](42_Growth%20Properties.htm) window (for trees) :
Any of the *Increments* buttons\]

This [Time Series Window](135_time-series%20window.htm) is one of the
tree increment time series windows, where growth of the trees is
specified as either:

- Volume increments of stems \[m3/ha\]
- Mass increments of various tree components \[tdm/ha\]
- NPP flows to various tree components \[tdm/ha\].

**Details**

Stems have no turnover, so NPP flows to the stems are equal to the yield
increments of the stems.

Stem volume increments are converted to stem mass increments by
multiplying by the [Stem Density](9_Stem%20Density.htm).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 112. Tree Growth Allocations 2020

**Tree Growth Allocations**

\[[Growth Properties](42_Growth%20Properties.htm) window (for trees) :
Any of the *Allocations* buttons\]

This [Time Series Window](135_time-series%20window.htm) is one of the
tree allocation time series windows, where you specify the relative
allocations of yield or NPP (see [Yield and
NPP](131_Yield%20and%20Net%20Primary%20Production.htm)) to the six tree
components: stems, branches, bark, leaves, coarse roots, or fine roots.

**Introduction**

The allocations determine the growth of a component, relative to the
other components. A high allocation means more growth of the component
compared to the other components, a low allocation means the component
grows slower than the other components. Hence, allocations are purely
relative: it is not the size of the numbers by themselves that matters,
only the ratios between the allocations to the various tree components.

Typically the stem (or bole) growth is the frame of reference, and the
mass increases of the other components relative to the stems are
recorded. If the relative stem growth is set to 1.0, then where the leaf
mass increment is a half of the stem mass increment it would be set to
0.5.

Data on allocations to various tree components can be found in the NCAS
Technical Reports
[5a](reps/TR5A%20Review%20of%20Allometric%20Relationships%20for%20Estimating%20Woody%20Biomass%20for%20Queensland,%20the%20Northern%20Territory%20and%20Western%20Australia.pdf){target="_blank"},
[5b](reps/TR5B%20Review%20of%20Allometric%20Relationships%20for%20Estimating%20Woody%20Biomass%20for%20New%20South%20Wales,%20the%20Australian%20Capital%20Territory,%20Victoria,%20Tasmania%20and%20South%20Australia.pdf){target="reps5b"},
[17](reps/TR17%20Synthesis%20of%20Allometrics,%20Review%20of%20Root%20Biomass%20and%20Design%20of%20Future%20Woody%20Biomass%20Sampling%20Strategies.pdf){target="reps17"},
[25](reps/TR25%20Review%20of%20Unpublished%20Biomass-Related%20Information%20Western%20Australia,%20South%20Australia,%20New%20South%20Wales%20and%20Queensland.pdf){target="reps25"}
and
[44](reps/TR44%20Spatial%20Estimates%20of%20Biomass%20in%20'Mature'%20Native%20Vegetation.pdf){target="reps44"}
([17](reps/TR17%20Synthesis%20of%20Allometrics,%20Review%20of%20Root%20Biomass%20and%20Design%20of%20Future%20Woody%20Biomass%20Sampling%20Strategies.pdf){target="_blank"}
is the synthesis report). Recent revisions are reported by Paul and
Roxburgh (2017 & 2019).

General values for major vegetation types can be found in Table 3 of the
report *Greenhouse Gas Emissions from Land Use Change in Australia:
Results of the National Carbon Accounting System 1988--2001*. Additional
species specific allocations can be extracted from the FullCAM database.

[]{.small}

Paul and Roxburgh (2017), *FullCAM: building capability via
data-informed parameters*. CSIRO report.

Paul and Roxburgh (2019), *Refining FullCAM: building capability via
data-informed parameters*. CSIRO report.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 114. RothC 2020

**RothC**

The RothC [Soil](203_Soil.htm) model is one of the [Constituent Models
In FullCAM](198_Constituent%20Models%20In%20FullCAM.htm).

**Description**

The [Rothamsted Carbon
Model](http://www.rothamsted.ac.uk/ssgs/RothC/RothC.php){target="_blank"}
(RothC) model is a soil carbon model. RothC models the turnover of
organic carbon in non-waterlogged soils, taking into account clay
content, temperature, moisture content, plant and manure inputs, and
plant cover. RothC tracks the amount of microbes and several soil pools
containing active carbon. In FullCAM it has been extended to also track
nitrogen by applying C:N ratios.

**Active Soil Pools**

RothC partitions the active soil into five components (soil pools):

  Component   Description
  ----------- ---------------------------
  DPM         decomposable plant matter
  RPM         resistant plant matter
  BIO-F       fast decomposing biomass
  BIO-S       slow decomposing biomass
  HUM         humified organic matter.

The definitions of these soil pools can be found through the [Rothamsted
website](http://www.rothamsted.ac.uk){target="_blank"} and manual.

The DPM pool tends to small and transient, decomposing easily, with
material moving quickly from DPM to BIO-F, BIO-S, and HUM.

The RPM pool is sometimes called *particulate organic matter* (POM)
elsewhere.

Typically the fraction of total soil carbon in the BIO-F and BIO-S pools
is very small --- these are small but very active pools of microbes. In
practice it is often difficult to measure BIO-F and BIO-S.

The RothC model is always version 26.3 of RothC in the standard edition
of FullCAM. In the [Research Edition](48_Research%20Edition.htm) of
FullCAM you have the option of using either version 26.3 or version 26.5
of RothC.

**Inert Soil**

The inert soil is all in the inert pool in FullCAM (see
[Soil](203_Soil.htm)). The inert material is sometimes called \"charcoal
and charred plant material\" (CHAR) elsewhere. In FullCAM the inert pool
is outside of RothC --- it is instead managed by [CAMFor](77_CAMFor.htm)
or [CAMAg](78_CAMAg.htm) --- even though the RothC model elsewhere has
an inert pool. The inert pool is simply a reservoir of soil material
that is very unlikely to move to any other pool in the foreseeable
future. It mainly consists of charcoal or material that is physically
encapsulated.

**Credits**

The RothC model within FullCAM implements the FORTRAN programs
"ROTHC-26.3" and "ROTHC-26.5_32" by K.W. Coleman, D.S Jenkinson, L.C.
Parry and J.H. Rayner. It draws on papers by Jenkinson and Coleman,
amongst others.

The model was enhanced by the CSIRO in Adelaide (Jan Skjemstad) and the
Department. Enhancements include the ability to use the historical
weather time series rather than average weather, including the topsoil
moisture deficit (TSMD) computations, and tracking nitrogen. Equilibrium
and radiocarbon dating computations were omitted.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 116. Forest Percentage Change 2020

**Forest Percentage Change**

\[[Event Window](137_Event%20Window.htm) : *Forest Percentage Change*
panel\]

Enter the inputs specific to a forest-percentage change event.

**Details**

Enter the [Forest Percentage](206_Forest%20Percentage.htm) that will
apply to the plot, until the next forest percentage change event. See
[Initial Conditions For the Whole
Plot](197_Initial%20Conditions%20For%20the%20Whole%20Plot.htm).

Forest percentage change events with no valid choice are shown as a
simulating event in the event list (so you can change their type), but
are shown as not ready and have no effect on the simulation.

**Equal to a Constant**

This is the recommended way to adjust the forest percentage when using
the default parameters available from downloaded data. The forest
percentage will be changed to the specified value and will not change
until a subsequent forest change event occurs.

Note that the Forest Percentage Change does not automatically respond to
events that plant or remove trees. A forest percentage change event
should always be created alongside another event that purports to change
land management practices and/or influence the presence of a forest,
consistent with the events created from [new
regimes](274_New%20Regime.htm).

**Determined by the Tree Yield Formula**

Under this option the forest percentage rises from 0% at planting to
100% at the age of maximum growth. This relies on the evidence that the
age of maximum growth is at or near the age of canopy closure. The
growth determined by the tree yield formula is not affected by the
forest percentage, but the tree growth affects how much room is left for
pasture between the trees.

**Note**: Under this option, in simulation steps where the tree yield
formula is not in use, the forest percentage is equal to the constant
forest percentage entered in the initial conditions.

**Determined by the Tree Age**

It may be used with or without the tree yield formula.

**Note**: Under this option, in simulation steps where the tree yield
formula happens to not be in use, the forest percentage is equal to the
constant forest percentage entered in the initial conditions. This is
similar to the linking of canopy closure and age of maximum growth in
the previous option but lets the user set the age of canopy closure
manually.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 118. Crop Growth Increments 2020

**Crop Growth Increments**

\[[Growth Properties](42_Growth%20Properties.htm) window (for crops and
pastures) : Any of the *Increments* buttons or the *Die Off* button\]

This [Time Series Window](135_time-series%20window.htm) is one of the
following two crop and pasture time series windows, where you specify
the:

**1. Growth** of the crop or pasture as either:

- Mass increments of the specified crop or pasture components \[tdm/ha\]
- NPP flows to various crop or pasture components \[tdm/ha\].

**2. Die off**, for perennial pastures only, as either:

- Mass decrements of leaf components \[tdm/ha\]
- NPP flows from leaf components \[tdm/ha\].

**Details**

Crops and pastures may be grown via three different methods:

*Sigmoidal* (for annual species) - growth will begin from the planting
event and proceed to the harvest event, tracking along a sigmoidal
curve. At the time of harvest, the plant will have reached optimal
growth, which is the amount specified within the increment growth
window. This value should normally be an annual value.

*Perennial growth* (for perennial/multi-year species) - growth will
begin at time of planting from an initial standing dry matter amount,
and proceed using monthly increments and decrements. Perennial growth
can be used to accurately model seasonal variations and climatic impacts
on pasture yields.

*Linear* - growth will begin from the planting event and proceed to the
harvest event, tracking linearly from planting to harvest. At the time
of harvest, the plant will have reached optimal growth, which is the
amount specified within the increment growth window. This value should
normally be an annual value. Linear growth is not recommended for
modelling plant growth as it produces unrealistic amounts of biomass at
any point along the growth time series.

Additional detail and reference material on sigmoidal and perennial
growth methods can be found within Australia\'s National Inventory
Report.

**Additional Comments**

Crop and pasture growth within FullCAM does not take into account
climatic variability. It will simply model growth along a set curve to
reach the optimal yield as entered. The yields that are entered into
FullCAM should include climatic impacts into their modelling or
measurement prior to insertion into FullCAM.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 120. Plant Removal and Replacement 2020

**Thin or Harvest : Plant Removal and Replacement**

\[[Event Window](137_Event%20Window.htm) : *Thin* panel : *Tree/Plant
removal and replacement* section\]

Specify how the [Thin](140_Thin.htm) or [Harvest](153_Harvest.htm)
affects the average age of the plants.

**Introduction**

  ---------- -- ----------------------------------------------------
  Thins         *Plants* are trees; the *event* is a thin
  Harvests      *Plants* are crop plants; the *event* is a harvest
  ---------- -- ----------------------------------------------------

The only effect of this section is to specify how the average age of the
plants changes due to the event. By specifying the average age of the
plants that are removed from the plot, and whether or not new plants
spring up to replace them, you can control the change in the average age
of the plants.

This is only of interest if you are using the average age of the plants
to determine relative allocations or growth (see the [Growth
Properties](42_Growth%20Properties.htm) windows), in which case you can
control how the event moves the plants along their growth curves.

These settings are only relevant and enabled for thinnings that leave
some stems or stalks (if the fraction of plants removed is less than
100%).

**Default Setting**

Most people will want the default setting:

1.0 in the top box\
0.0 in the middle\
0.0 in the bottom box,\
Do not check the *Replace removed plants* box.

Under this setting:

- The average age of the removed plants is equal to the average age of
  the existing plants
- The average age of the plants on the plot is not changed by the event
- No new plants grow to replace the removed plants.

**Removal-Age Formula**

Specify the average age (in years) of the plants that are removed by the
event by specifying the three coefficients in a formula:

1.  The multiplier for the current average age of the plants (*A*)
2.  The multiplier for the age of the oldest plants in the forest or
    crop (*B*)
3.  An additive constant, in years. (*C*)

The average age of the removed plants is

> *A* \* (average age of plants) + *B* \* (age of oldest plants) + *C*.

If this average age is less than zero it is changed to zero; if it is
greater than the age of the oldest plants it is changed to the age of
the oldest plants.

**Example 1**. If *A* = 0, *B* = 0, *C* = 15 then the average age of the
removed plants is 15 years. So if the average age of the plants at the
time of the event was 10 years, then the average age of the removed
plants would be 15 years. So if 50% of the stems or stalks were removed
and there was no replacement, then the average age of the plants after
the event would be 5 years.

**Example 2**. If *A* = 1.2, *B* = 0, *C* = --0.5 then the average age
of the removed plants is 20% greater than the average age of plants
(before the event) less half a year. So if the average age of the plants
at the time of the event was 10 years, then the average age of the
removed plants would be 1.2 \* 10 -- 0.5 = 11.5 years. So if 50% of the
stems or stalks were removed without replacement then the average age of
the plants after the event would be 8.5 years.

The average age of the removed plants is only used to calculate the
average age of the remaining plants. It is your responsibility to
specify the average age of the removed plants sensibly. If the average
age of the plants after the event is greater than the age of the oldest
plants then it is changed to the age of the oldest plants.

The age of the oldest plants is not affected by the event --- it is only
altered by planting or clearing events, and the passage of time.

**Replacement**

Check the *Replace removed plants with new plants (of age 0)* box if you
want new plants to grow spontaneously, starting from age zero at the
time of the event and without a planting event, in the spaces left
behind by the removed plants.

Checking this box is appropriate for a native forest, but usually not
appropriate for a plantation forest. If the thinned trees were
intermingled through the forest, the non-thinned trees may bulk up to
fill the space previously occupied by the thinned trees (so consider a
forest treatment event that lowers the effective age of the trees). If
the thinned trees all come from the same portion of the plot and that
portion is completely cleared by the thin, then it would be better to
model the forest with an [Estate
Simulation](72_Estate%20Simulation.htm), using multiple plot files to
reflect the different management, rather than as a single plot file.

**Coppices**

If there are no stems or stalks left after the event yet the event is
not a clearing event (so the affected portion is 100% but the sum of the
destination percentages for at least one pool is less than 100%), then
the average age of the plants is not changed by the event (thus, you can
create coppices).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 121. Mortality 2020

**Mortality**

\[[Plant Properties](43_Plant%20Properties.htm) window : *Mortality*
section\]

Specify mortality rates for the plant species.

**Introduction**

Specify what percentage of plants die, what percentage of the plant
components die, and the average age of the plants that die. By
specifying the average age of the plants that die, and whether or not
new plants replace them, you can control the change in the average age
of the plants. This is only of interest if you are using the average age
of the plants to determine relative allocations or growth (see the
[Growth Properties](42_Growth%20Properties.htm) window), in which case
you can control how mortality moves the plants along their growth
curves.

Plant mass that "dies due to mortality" becomes turnover and is treated
in all ways as turnover, except that mortality mass is added to turnover
after yield-versus-production has been determined. (Yield measurements
do include the effects of regular turnover, but do not include the
effects of mortality or site biomass limits.)

**Stem or Stalk Loss**

Specify the percentages of the plants that die each year in the [Stem
Loss and Stalk Loss](19_Stem%20Loss%20and%20Stalk%20Loss.htm) time
series.

**Ratios of Component Losses to Stem Loss**

When a given percentage of the stems or stalks die, the percentages of
other plant components on the plot that die may be different. Specify
these differences in the "Ratio\..." fields. For example, if the *ratio
of leaf loss to stem loss* is 0.3 and 2% of the tree stems die in a
given year, then the percentage of leaves on the plot that are lost is
only 2% \* 0.3 = 0.6% (perhaps the trees close to death have fewer
leaves than the other trees?).

**Effect on Average Age of Plants**

Specify the average age (in years) of the plants that die by specifying
the three coefficients in a formula:

1.  The multiplier for the current average age of the plants (A)
2.  The multiplier for the age of the oldest plants in the forest or
    crop (B)
3.  An additive constant, in years (C)

The average age of plants that die is

> A \* (average age of plants) + B \* (age of oldest plants) + C.

If this average age is less than zero or greater than the age of the
oldest plants, no plant mortality occurs (that is, no plants die in that
step due to "mortality"). This feature allows you to specify, for
example,

- a constant age of death
- a constant mortality in the Stem Loss or Stalk Loss time series and
  mortality losses will not start until the oldest plants reach the
  specified average age of death.

**Example 1**. If A = 0, B = 0, C = 50 then the average age of the dying
plants is 50 years. Thus there is no plant loss due to mortality unless
the age of the oldest plant exceeds 50 years. If the age of the oldest
plants is over 50, and the average age of the plants is 40 years and 10%
of the plants die, then the average age of the plants that die is 50
years and the average age after mortality is 38.89 years (assuming no
replacement).

**Example 2**. If A = 1.2, B = 0, C = --3 then the average age of the
dying plants is 20% greater than the average age of plants (before the
mortality is taken into account) less three years. So if the average age
of the plants was 10 years, then the average age of the dying plants
would be 1.2 \* 10 -- 3 = 9 years.

The average age of the dying plants is only used to calculate the
average age of the remaining plants. It is your responsibility to
specify the average age of the dying plants sensibly, and so that it
interacts properly with the times or ages in the Stem Loss or Stalk Loss
time series. If the average age of the plants after mortality is applied
is greater than the age of the oldest plants then it is changed to the
age of the oldest plants.

The age of the oldest plants is not affected by mortality --- it is only
altered by planting or clearing events, and the passage of time.

**Replacement**

Check the "Replace dying trees" or "Replace dying plants" field if you
want new plants to start up from age 0 in the spaces left behind by the
dead plants. The only effect of this choice is on the average age of the
forest or crop. In a plantation you will usually not check this field
(as established trees will expand to fill the space of the dying
(removed) trees, intermingled with the retained trees). In a native
forest, however, you should check this field (because there is usually a
constant regeneration of trees).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 122. Sensitivity of Debris Breakdown to Temperature and Water 2020

**Sensitivity of Debris Breakdown to Temperature and Water**

\[[Debris Properties](45_Debris%20Properties.htm) window : *Sensitivity*
section\]

Specify how the breakdown rates of the debris increase with increasing
temperature and water.

**Introduction**

You can choose either of both of two styles of sensitivity:

Mulch style.\
[Soil](203_Soil.htm) style (as in [RothC](114_RothC.htm)).

The mulch layer always has temperature and water sensitivity: the mulch
decomposition rates increase with increasing temperature and rainfall.
Turning on mulch-style sensitivity will cause the debris breakdown layer
to behave with mulch-like responses to conditions. Mulch-style
sensitivity can be used to provide a more mulch-like simulation, if
required.

The soil layer always has temperature and water sensitivity: the soil
decomposition rates increase with increasing temperature and decreasing
topsoil moisture deficit.

All debris pools are always affected in the same manner. The same
sensitivity factor applies to the breakdown rate of each debris pool.

**No Sensitivity To Temperature or Water**

If neither style of sensitivity is on, then the fraction of each debris
pool lost due to breakdown is equal to the breakdown percentage for the
pool (entered elsewhere on the window) adjusted to the relevant period
of time:

> *g* = *M \* L*,

where

*g* = mass of material lost from the pool due to breakdown in the time
period

*M* = mass of the pool at the beginning of the time period

*L* = fraction of mass in the pool at the beginning of the time period
that is lost due to breakdown

= 1 -- (1 -- *f*)\^*y*

*f* = breakdown fraction (fraction lost due to breakdown per year)

= breakdown percentage of pool / 100

*y* = number of years in time period.

Note that *g*, *M*, and *L* are independent of temperature and water. 0
\<= *f* \<= 1.

**Mulch-Style Sensitivity**

If mulch-style sensitivity is on and soil-style sensitivity is off, then
you must enter the sensitivity to temperature (*s*) and the sensitivity
to water (*v*), which determine how sensitive the breakdown rates are.

> *g* = *M \* L* \* \[ 1 -- exp(--*s \* T*) \] \* \[ 1 -- exp(--*v \*
> W*) \]

where

*s* = the sensitivity of breakdown to temperature (*s* \>= 0)

*T* = the average air temperature (in deg C, negative temperatures
treated as zero for this purpose) during the time period (*T* \>= 0),

*v* = the sensitivity of breakdown to water (*v* \>= 0)

*W* = the total rainfall and irrigation (in mm) during the time period
(*W* \>= 0). Notice that both the temperature factor

> 1 -- exp(--*s \* T*)
>
> and the water factor
>
> 1 -- exp(--*v \* W*)
>
> are:
>
> - Between 0 and 1
> - Nearer 0 (less breakdown) as *T* and *W* fall or as *s* and *v* fall
> - Nearer 1 (more breakdown) as *T* and W rise or as *s* and *v* rise.

The overall rate of breakdown is quite sensitive to *s* and *v*. If *s*
or *v* are too small then there is almost no breakdown; if *s* or *v*
are too large then sensitivity is lost. As a very rough guide:

- set *s* to about 1 / (average temperature in a simulation step)
- set *v* to about 1 / (average rainfall-plus-irrigation during a
  simulation step).

If mulch-style sensitivity is on, the rate of breakdown falls to zero
when the average air temperature is at or below freezing or there is no
rainfall or irrigation specified.

**Soil-Style Sensitivity**

This option is only possible when the soil is modelled, because it uses
the topsoil moisture deficit in the soil and various RothC soil inputs
to compute the rate of breakdown. If it is on then it will cause a
difference to aboveground results when the soil is and is not included
in the model --- because if the soil is included in the model then this
sensitivity is on but if the soil is not included then this sensitivity
is off.

If soil-style sensitivity is on and mulch-style sensitivity is off, then
you do not need to enter any inputs: FullCAM uses the sensitivity
defined in the soil model ([RothC](114_RothC.htm)), which does not have
any inputs exposed in the user-interface.

> *g* = *M* \* *L*,

where

*L* = fraction of mass in the pool at the beginning of the time period
that is lost due to breakdown

> = 1 -- (1 -- *f*)\^(*y* \* *a* \* *b*)
>
> *a* = rate modifier due to temperature
>
> = 47.91 / (1 + exp0(106.06 / (18.27 + *T*)) for *T* \> --5
>
> 0 for *T* \<= --5
>
> *b* = rate modifier due to water

= 0.2 + 0.8 \* (*e* -- TSMD) / (*h* \* \[(20 + 130 \* *c* -- 100 \* *c
\* c*) \* (*d* / 23)\])

if version 26.3 of RothC in use

1 / (1 + exp\[ (TSMD -- (0.688405334 + 4.4746369 \* *c* -- 3.44203 \* *c
\* c*) \* *d*)

/ ((0.082530817 + 0.5364083 \* *c* -- 0.41268 \* *c \* c*) \* *d*) \]

if version 26.5 of RothC in use

*c* = clay fraction of soil

*d* = sample depth of soil

*h* = Ratio of the maximum TSMD when soil is bare to the maximum TSMD
when soil is covered

TSMD = topsoil moisture deficit (as computed by RothC).

Increasing *a* or *b* increases the effective time of decomposition, or
effectively increases the rate of decomposition during a given time
period. Increasing *T* or *W* increases *a* and *b* respectively
(increasing *W* tends to increase the TSMD). 0 \<= *a* \<= 1 and 0 \<=
*b* \<= 1.

**Combined Mulch-Style and Soil-Style Sensitivity**

If soil-style sensitivity and mulch-style sensitivity are both on then
FullCAM combines both styles of sensitivity.

*g* = *M \* L* \* \[ 1 -- exp(--*s \* T*) \] \* \[ 1 -- exp(--*v \* W*)
\],

where

*L* = 1 -- (1 -- *f*)\^(*y* \* *a \* b*)

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 123. Notes on a Plant Species 2020

**Notes on a Plant Species**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Notes* button\]

Write any notes on the current species ([Select a
Species](56_Select%20a%20Species.htm)).

**Details**

Notes are purely for your own use. FullCAM completely disregards these
notes for all computational purposes; they have no effect on any
simulation.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 124. Crop Growth Allocations 2020

**Crop Growth Allocations**

\[[Growth Properties](42_Growth%20Properties.htm) window (for crops) :
Any of the *Allocations* buttons\]

This [Time Series Window](135_time-series%20window.htm) is one of the
crop allocation time series windows, where you specify the relative
allocations of yield or NPP (see [Yield and
NPP](131_Yield%20and%20Net%20Primary%20Production.htm)) to the five crop
components: GBF (grains, buds, and fruit), stalks, leaves, coarse roots,
or fine roots.

**Introduction**

The allocations determine the growth of the component, relative to the
other crop components. A high allocation means more growth of the
component compared to the other components, a low allocation means the
component grows slower than the other components. The crop components
all grow in certain proportions to one another at various stages in the
plant's life; these allocations are the mechanism for determining those
proportions in FullCAM.

Enter an allocation for each period in the time series. The allocations
are purely relative: it is not the size of the numbers by themselves
that matters, only the ratios between the allocations to the various
crop components.

**Examples**

In these examples we will assume yield allocations. Thus we are
concerned only with the mass increases of the crop components, relative
to one another.

**Example 1**. Suppose in a given period of crop growth that the mass of
the stalks in a hectare of crop increases by 2 tonnes, while the mass of
leaves on the same hectare increases by 3.5 tonnes. Then the ratio of
stalk growth to leaf growth is 3.5 / 2 or 1.75. Thus the relative yield
allocations factors of stalks and leaves are respectively x and 1.75*x*,
where *x* is any non-negative number. You might choose any of the
following as the relative yield allocations for that year:

- Stalk allocation is 1.0 and leaf allocation is 1.75 (stalks are the
  reference component).
- Stalk allocation is 0.5714 and leaf allocation is 1.0 (leaves are the
  reference component)
- Stalk allocation is 100 and leaf allocation is 175.

**Example 2**. Suppose that in a given one month period of crop growth
that, in a hectare of crop, the mass increases in the components over
the period were as follows:

> 
>   Vegetation Component    tdm/ha value
>   ---------------------- --------------
>   GBF                         2.0
>   Stalks                      5.0
>   Leaves                      20.0
>   Coarse roots                10.0
>   Fine roots                  1.0

One choice of relative yield allocations (all relative to the GBF
allocation) for this period would be:

> 
>   Vegetation Component    Relative Yield
>   ---------------------- ----------------
>   GBF                          1.0
>   Stalks                       2.5
>   Leaves                       10.0
>   Coarse roots                 5.0
>   Fine roots                   0.5

Another choice (stalk growth as reference) would be:

> 
>   Vegetation Component    Relative Yield
>   ---------------------- ----------------
>   GBF                          0.4
>   Stalks                       1.0
>   Leaves                       4.0
>   Coarse roots                 2.0
>   Fine roots                   0.2

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 127. Simulate Menu 2020

**Simulate Menu**

\[*Simulate* menu, on the [Main Window](217_Main%20Window.htm)\]

This topic is about the items on the *Simulate* menu.

**Run Simulation**

Select *Run Plot Simulation* to run a simulation on the current
document. The type of simulation depends on the current document type:

  Document Type   Simulation Type
  --------------- -------------------
  Plot            plot simulation
  Estate          estate simulation

If multiple plots and /or estates are open when *Run Plot Simulation* is
selected only the active (front most) plot estate is simulated.

**Simulation Reports**

These reports provide some statistics on the last simulation, and the
plot simulations since you last started FullCAM.

The *Report Subrule for Last Simulation* menu option creates a [Subrule
Report](http://www.fullcam.au/FullCAMServer2020/Help/227_Subrule%20Report.htm).
This menu option is only available when the [Subrule
Report](http://www.fullcam.au/FullCAMServer2020/Help/227_Subrule%20Report.htm)
conditions are satisfied.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 130. Tree Yield Formula 2020

**Tree Yield Formula**

The tree yield formula is one of the tree production methods in a
multilayer forest (see [Configure Tree
Production](108_Configure%20Tree%20Production.htm)). It is an equation
for calculating tree growth, whose main inputs are maximum aboveground
biomass, tree age, and productivity.

**The Tree Yield Formula**

The tree yield formula for tree growth is

> *T(A) = r \* M \* y \** exp(*--k / d*)

where

*T* = Aboveground mass of the trees, in tdm/ha, if there was constant
(and thus average) productivity

*A* = Age of the tree (either the age of the oldest trees, or the
average age of the trees --- see the [Growth
Properties](42_Growth%20Properties.htm) window), in years

*M* = Maximum aboveground biomass of trees, in tdm/ha
([Site](200_Site.htm) page)

*r* = Maximum aboveground biomass multiplier ([Growth
Properties](42_Growth%20Properties.htm) window), a species-dependent
modifier of *M* (thus the maximum aboveground biomass used is *r \* M*)

*y* = Tree yield multiplier. Initially equal to one in any plot
simulation, then changed to the type 2 growth multiplier of the latest
forest treatment event

*k* = *2 \* G* -- 1.25.

> *G* = Tree age of maximum growth, in years ([Growth
> Properties](42_Growth%20Properties.htm) window, expressed as a
> multiplier of the maximum aboveground biomass plus a constant). This
> is also usually the age at which the canopy closes.

*d* = Adjusted age of the trees, in years

> = *A* + sum over each treatment of
>
>   --------------------- -- --------------------------------
>   0                        if *A \<= W*
>   *v \* (A -- W) / U*      if *A \>= W* and *A \<= W + U*
>   *v*                      if *A \> W + U*
>   --------------------- -- --------------------------------
>
> where, for each treatment undergone by the forest, specified by the
> type 1 parameters in the forest treatment events,
>
> *v* = the age advance due to the treatment, either positive or
> negative, in years\
> *U* = the advancement period, in years\
> *W* = the age (of same type as *A*) at which the treatment was
> applied, in years.

**Notes**

*T* asymptotically approaches *r \* M \* y* from below as *d* increases.
Note that exp(0) = 1, exp(negative) \< 1, and exp(any) \> 0. The maximum
aboveground biomass for trees when the tree yield formula is in use is
*r \* M \* y*. The forest treatment events move the forest back and
forth along the growth-age curve described by the tree yield formula,
where each age advance is phased in linearly over the advancement
period. When the tree yield formula is in use (that is, the current tree
species uses the tree yield formula to determine its growth), all
age-based properties of the trees use the adjusted age of the trees
(*d*), including the [Tree Growth
Allocations](112_Tree%20Growth%20Allocations.htm),
[Mortality](121_Mortality.htm), and [Stem Density](9_Stem%20Density.htm)
time series.

**Non-Constant Productivity**

The tree yield formula above gives the generic biomass yield curve under
average climatic conditions. To account for year-to-year variations in
climatic data, the tree yield formula-predicted increment in aboveground
biomass is moderated up or down at annual time steps based on the ratio
of the forest productivity index to the average forest productivity
index. See [Forest Productivity
Index](188_Forest%20Productivity%20Index.htm).

**Data Inputs to the Formula**

Thus the data inputs to the tree yield formula are:

1.  *M*, the maximum aboveground biomass
2.  *r*, the species-multiplier of the maximum aboveground biomass
3.  *G*, the tree age of maximum growth
4.  *FPI*, the time series of the forest productivity index
5.  *y*, the tree yield multiplier (which can be changed by type 2
    forest treatment events)
6.  The age advances specified by the type 1 forest treatment events.

On the [Departmental Server](219_Departmental%20Server.htm), *r* and *G*
are calculated from other inputs. See [Growth
Properties](42_Growth%20Properties.htm).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 131. Yield and Net Primary Production 2020

**Yield and NPP**

Yield and NPP are related concepts and you will need to know how they
are defined in order to understand plant growth in FullCAM.

**Turnover**

A plant is normally "turning over" or shedding material, producing
"litterfall" aboveground and "root slough" belowground.

**NPP**

The net increase in plant mass due to the addition of new plant material
is called the *net primary production* (NPP), which includes the effects
of both photosynthesis and respiration. NPP is difficult to measure due
to the confounding effect of *turnover* (in which all plant components
except tree stems lose portions via turnover), and is of interest mainly
to people tracking tree physiology.

NPP is due to the combined effects of photosynthesis and respiration.
The mass added by photosynthesis is called *gross primary production*
(GPP). It is photosynthesis that removes carbon from the atmosphere and
adds it to the plant. However, much of the GPP is promptly lost (and
carbon returned to the atmosphere) due to respiration. In trees, NPP is
typically about half of GPP. In FullCAM, NPP is measured in tonnes per
hectare.

Thus, in normal growth, a plant is simultaneously adding to its mass by
the process of production (which adds NPP to the plant) and losing mass
by the process of turnover (which loses material from the plant).

**Yield**

Due to the turnover of plant components, when we measure the change in
component mass over a period of time we actually measure the *yield*,
which is the NPP less the turnover. Yield is relatively easy to measure
and is of interest to anyone who measures plant masses.

The yield of a plant is the NPP produced less the material shed by
turnover: in any given period,

*Yield = NPP -- Turnover*.

**Use NPP or Yield?**

NPP is due to production, material-turned-over is due to turnover, and
yield is due to the combined effects of production and turnover.

There are two fundamentally different ways of specifying or measuring
plant growth:

1.  By yield changes --- changes in yield with time.
2.  By NPP flows --- amounts of NPP added to the plant component.

In practice, the material-turned-over is hard to measure precisely as
material moving to debris via turnover is quickly dispersed into the
environment, while yields are relatively easy to measure precisely.

The yield is what you get if you simply measure the mass of the
specified plant component(s), and a "mass increment" (or "yield
increment") is the difference in measurements of mass over the period of
the increment.

For example, if you measure the leaves of the trees of a forest as 20
tdm/ha on June 1 then the yield of the tree leaves on June 1 is 20
tdm/ha. If you then measure the leaves of the trees as 26 tdm/ha on
August 1, the mass increment of the tree leaves is 6 tdm/ha over those
two months. If your increment time series contained monthly leaf mass
increments, then it might have 3 tdm/ha in June and another 3 tdm/ha in
July.

An NPP flow to a tree or crop component in a given period is the mass of
NPP that is added to the component in the period.

For example, continuing the previous example, suppose that the trees
shed 1 tdm/ha of leaves during June and a further 2 tdm/ha of leaves in
July. Then the NPP flowing to the leaves in June must have been 4 tdm/ha
(the leaf mass increment was 3 tdm/ha in June, which included shedding 1
tdm/ha of leaves) and in July must have been 5 tdm/ha (3 tdm/ha net
gain, including a 2 tdm/ha loss). If your increment time series
contained monthly leaf NPP flows, then it would have 4 tdm/ha in June
and another 5 tdm/ha in July.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 132. Data Builder 2020

**Data Builder**

\[*Data Builder* page of the input window of a plot document\]

Use the Data Builder to download data from the [Departmental
Server](219_Departmental%20Server.htm) into your plot document.

For help downloading data, see [Downloading Spatial
Data](207_Downloading%20Spatial%20Data.htm).

**Introduction**

The Data Builder allows you to easily build plots by downloading the
input data for your plot from the [Departmental
Server](219_Departmental%20Server.htm).

For further details and for assistance in building plots for complex
systems, such as managed forest and agricultural mixes (agroforestry),
please [Contact Us](190_Contact%20Us.htm).

Although the Data Builder has been designed for ease of use, it has
advanced functionality that allows experienced users to build complex
systems. Take care when downloading complex data or modifying downloaded
data, as modelling errors can result.

**Internet Connection to the FullCAM Server**

Using the Data Builder requires that your computer be connected to the
Internet. The Data Builder will automatically connect to the
[Departmental Server](219_Departmental%20Server.htm) as required.

**Plot Configuration**

Your choice of plot type and location will affect the species and regime
data offered for downloading. For example, [Regimes](235_Regimes.htm)
including a transition from pasture to plantation are not available for
a forest system because a pasture is modelled by an agricultural system.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 135. Time-Series Window 2020

**Time Series Window**

\[[Site : Water](12_Site_Water.htm) window : any *Time Series* button\]\
\[[Site : Temperature](13_Site_Temperature.htm) window : any *Time
Series* button\]\
\[[Site :
Light](http://www.fullcam.au/FullCAMServer2020/Help/35_Site_Light.htm)
window : any *Time Series* button\]\
\[[Site : Productivity](64_Site_Productivity.htm) window : any *Time
Series* button\]\
\[[Growth Properties](42_Growth%20Properties.htm) window : any *Time
Series* button\]\
\[[Plant Properties](43_Plant%20Properties.htm) window : any *Time
Series* button\]\
\[[Soil Inputs](193_Soil%20Inputs.htm) window : any *Time Series*
button\]\
\[[Crop Yields
Table](http://www.fullcam.au/FullCAMServer2020/Help/113_Crop%20Yields%20Table.htm)
window : any *Time Series* button\]

This window is for entering, editing, viewing, and exporting a time
series.

This topic is displayed when you click the *Window* help icon in any
time series window; when you press the *Data* help icon you open the
topic about that particular time series.

**Time Series Data**

In FullCAM, the data points in a year are assumed to be equally spaced
throughout the year. The exact way in which they are used depends on the
'Timing' and 'Amount of data' settings, as described below.

FullCAM will make the best possible use of the time series data you
enter, regardless of the amount of time series data and the number and
frequency of simulation steps. At the beginning of a simulation, FullCAM
interpolates and extrapolates the given time series into a full time
series, which consists of one data point per simulation step.

**Interpolation**

The interpolation is linear, between the nearest two given data points.

If there is any missing data in a time series FullCAM interpolates the
missing data values based on the average of the corresponding data
values from other years. For each column, the average for each data
column is calculated and used for all missing data values.

**Example 1.** Average value interpolation.

If there is annual rainfall data for 1994 - 1996 and July data is
missing for 1995, then the July 1995 value is calculated as the average
of the July 1994 and 1996 values.

  Year   Jan     Feb   Mar    Apr    May    Jun    Jul    Aug   Sep   Oct    Nov    Dec
  ------ ------- ----- ------ ------ ------ ------ ------ ----- ----- ------ ------ -----
  1994   105.9   2.7   5.9    36.3   14.8   10.9   23.1   6.6   2.5   0.8    19.7   9.5
  1995   1.6     6.1   25.4   6.0    2.6    5.7           1.9   9.2   8.2    0.8    7.6
  1996   0.4     1.0   0.3    28.9   0.3    0.6    0.1    0.3   6.7   10.9   9.2    2.2

The interpolated value for July 1995 is: (23.1 + 0.1) / 2 = 11.6

**Example 2.** Unable to interpolate data values.

If an entire column of values are missing then FullCAM is unable to
interpolate data values \-- the time series window will not be ready to
simulate, and the window button will be red.

*Timing: Start year, Years are*

The year that the time series is to start from. 'Start year' and 'Years
are' together determine the years that the data in the time series table
applies to.

**Example 1.** Calendar time

If 'Start year' is 2006 and 'Years are' is 'Calendar time', then the
time series data will be applied from 2006 onwards.

**Example 2.** Time since start of simulation

If 'Start year' is 2007 and 'Years are' is 'Time since start of
simulation', then the time series data will be applied from *2007 years
after the simulation start time*. It may be more appropriate to instead
set the 'Start Year' to 0.

**Example 3.** Years since plants sprouted

If 'Start year' is 2007 and 'Years are' is 'Years since plants
sprouted', then the time series data will be applied from *2007 years
after the plant event*. It may be more appropriate to instead set the
'Years are' to 0.

It should be noted that if this option is selected, the time series
headings are always entitled 'Data'. This is the case even if there are
12 Data points per year (in which case the column headings would be
months- Jan, Feb, Mar etc.). This is because the column values are
always relative from the plant event.

*Timing \-- Extrapolation*

You choose the extrapolation method (for generating data points outside
the range of given data): either use the data in the nearest year of
given data, or cycle the given data for all time. If you only enter one
year of data, it makes no difference which extrapolation method you use.

**Example 1.** Nearest year extrapolation method.

If you entered rainfall for the three years 1990 to 1992 and chose the
nearest year extrapolation for a simulation that went from 1980 to 2000,
then:

- In each year from 1980 to 1990 inclusive, FullCAM will use the 1990
  rainfall data.
- For 1991 FullCAM will use the 1991 data.
- For each year from 1992 to 2000 inclusive, FullCAM will use the 1992
  rainfall data.

**Example 2.** Nearest year extrapolation method.

If you enter rainfall data for just the one year 1990 and choose the
nearest year extrapolation, then in every year of the simulation FullCAM
will use the 1990 rainfall (even if the simulation is from 1950 to
1972).

**Example 3**. Cyclic extrapolation method.

If you entered rainfall for the three years 1990 to 1992 and choose the
cyclic extrapolation for a simulation that went from 1980 to 2000, then:

1980, 1983, 1986, 1989, 1992, 1995, and 1998 will use the 1992 rainfall
data.\
1981, 1984, 1987, 1990, 1993, 1996, and 1999 will use the 1990 rainfall
data.\
1982, 1985, 1988, 1991, 1994, 1997, and 2000 will use the 1991 rainfall
data.

**Example 4.** Cyclic extrapolation method.

If you enter rainfall data for just the one year 1990 and choose the
cyclic extrapolation, then in every year of the simulation FullCAM
(regardless of when the simulation starts or ends) will use the 1990
rainfall.

**Table**

Unless the time series is a spatial input (see below), the time series
data will be shown as a table of numbers.

Each row of the table has the data for one year. For example, if the
start year is 1962 and the years are calendar years, then the first row
in the table is for 1962, the next row for 1963, and so on.

You can cut, copy, and paste rectangular blocks of numbers from the
table. When pasting more than one number from the table at the same
time, you need only select the upper left cell of the rectangular block
you are pasting into to paste the entire selection.

**Amount of Data**

Change the size of the time series data by entering values in the *Years
of data* and the *Data points per year* boxes. A change will take effect
when the insertion point leaves a box or the *Update Data Siz*e button
is clicked.

If the *Years are* value is set to 'Calendar time' and *Data points per
year* (see below) is a multiple of 12, then data points will apply to
specific months. For example, if there are 12 data points for the year
then the first data point is for January, the next for February, and so
on. Similarly, if there are 24 data points for the year then the first
two data points are for the first and second halves of January, the next
two for February, and so on.

Change the size of the window, and thus the area available to the
visible part of the table, by dragging its lower right corner with the
mouse.

**Multiplier**

The *multiplier* simply multiplies every value in the table when FullCAM
uses the value in a simulation. For example, if the multiplier is 2.0,
then FullCAM will use 2.0 times the values in the table. The default
value of 1.0 (i.e. no multiplier imapct).

As the multiplier is species specific it cannot change over time.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 136. Events 2020

**Events**

\[*Events* page of the input window of a plot document\]

This page shows the regimes and events that can occur during a
simulation.

Each simulation step consists of continuous processes (such as growth or
decomposition) punctuated by any events that occur during that step ---
see [Processes and Events](58_Processes%20and%20Events.htm).

**Regime and Event Queue**

The regimes and their associated events are presented on the page in two
lists -- with one regime or event per line.

To view or edit an individual regime or event, open it by
double-clicking on it or selecting it then pressing the *Edit* button.
In the Event window you can click the list section headers to sort the
queue by that column.

The sequence of events that occur during the simulation is called the
*event queue*. If the list of events is sorted by time, then the
simulating events on the list, in the order presented, constitute the
event queue. The terms "event list" and "event queue" are used
interchangeably.

  Event Name     Description
  -------------- ----------------------------------------------------------------------------------
  Forest         Only affects the forest system, such as plant trees, forest fire
  Agricultural   Only affects the agricultural system, such as plant crops, harvest
  Mixed          Affects both the forest and agricultural systems, such as forest fraction change

**Populating the Regime and Event Lists**

Regimes and Events are loaded into their lists by one of the following
methods:

- *Cloning* an existing item (event or regime)
- Using the *New Regime / Event* buttons

**Editing Event Timing**

The timing of events can be edited using the [Event
Timing](143_Event%20Timing.htm) functions.

**Simulating Events**

An event is *simulating* if it will occur in a simulation. All events
are simulating, except:

- Events that occur outside the period of the simulation (too early or
  too late)
- Events that have been switched off (see [Event
  Timing](143_Event%20Timing.htm)). Events can be switched off in the
  [Event Window](137_Event%20Window.htm), or on the Events page by the
  secondary mouse button and selecting either *Simulate Events* or *Do
  Not Simulate Events*. Entire regimes of events can be switched off by
  right-clicking in the Regime Editing Panel and selecting *Do Not
  Simulate Regime*.

Non-simulating events have no effect on the simulation.

**Initial Conditions**

The initial conditions panel lists the [Initial
Trees](185_Initial%20Trees.htm) and [Initial
Crops](184_Initial%20Crops.htm) species names that are growing in the
system at the start of the simulation.

The [Initial Trees](185_Initial%20Trees.htm) is always displayed first.
If there is no initial tree or crop species growing at the start of the
simulation then `No trees` or `No crops` are displayed accordingly.

**Event Colour-Coding**

The timing fields on the event list (*Year*, *Day*, *Step in Year*) are
colour--coded to indicate the method used to specify the time of the
event:

  colour       Method
  ------------ ----------------------------------------------------------
  White        Calendar time (such as 1995 day 24)
  Light blue   Time since start of simulation (such as 3 years 24 days)

The names on the event list are colour coded to indicate whether they
are ready, whether they are simulating or not, and what system they
affect:

  colour   Status / System
  -------- ------------------------------------------------------------------------------
  Red      Event not ready (renders event queue not ready)
  Grey     Event non-simulating (outside simulation period, will not affect simulation)
  Green    Forest
  Yellow   Agricultural
  Brown    Mixed

Selected Events and Regimes are coloured in [light
blue]{style="background-color:lightcyan"}.

**Event Queue and Readiness**

If the event queue is not ready then the "Events" title on the tab of
the *Events* page is shown in red. Some event queues are not ready
because they do not make sense --- such as a tree planting when there
are already trees, or a tree thin when there are no trees. The first
event that causes the event queue to be unready is highlighted in red,
and the "Status" box describes the state of the event queue to help you
sort out any problems. You are responsible for entering a sequence of
events that is valid (that is, such that FullCAM considers that the
event queue is ready).

**Clearing Events**

A *clearing* event is one that clears a system (forest or agricultural)
of all plants. Depending on their extent, thins, harvests, fires,
ploughs and herbicides might be clearing. Generally an event must clear
100% of a plot to be deemed a clearing event. Once a system is cleared,
it needs to be planted before there is any more plant growth.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 137. Event Window 2020

**Event Window**

\[[Events](136_Events.htm) page : *New* or *Edit* button\]\
\[[Standard Events of a
Species](142_Standard%20Events%20of%20a%20Species.htm) window : *New* or
*Edit* button\]

This window is for viewing and editing an individual event. See

[Event Timing](143_Event%20Timing.htm)

For help on the event-specific panel at the bottom of the window, see:

[Plant Trees](158_Plant%20Trees.htm)\
[Plant Crop](161_Plant%20Crop.htm)\
[Thin](140_Thin.htm)\
[Harvest](153_Harvest.htm)\
[Forest Fire](144_Forest%20Fire.htm)\
[Agricultural Fire](149_Agricultural%20Fire.htm)\
[Plough](164_Plough.htm)\
[Herbicide](163_Herbicide.htm)\
[Grazing Change](196_Grazing%20Change.htm)\
[Forest Treatment](51_Forest%20Treatment.htm)\
[Chopper Roller](52_Chopper%20Roller.htm)\
[Termite Change](53_Termite%20Change.htm)\
[Irrigation Change](54_Irrigation%20Change.htm)\
[Manure-From-Offsite Change](62_Manure-From-Offsite%20Change.htm)\
[Forest Percentage Change](116_Forest%20Percentage%20Change.htm)

**Name**

Every event needs a (non-blank) name, and the name must be unique within
the event list (either the events for the plot, or the events for a
species). Press the *Auto Name* button and FullCAM will insert a unique
name based on the properties of the event.

**Type**

Select the type of event:

- If you are modelling a forest, the forest events are available.
- If you are modelling an agricultural system, the agricultural events
  are available.
- If you are modelling a mixed plot, both forest and agricultural events
  are available.

Only events that are possible with the current configuration and current
species inputs can be created or edited (if they are not possible then
they are also not shown in the *Events* page in the input window). Note
that:

**Notes**

Enter anything you like in this field. It will have no effect on
simulation but it may be useful for sorting events in the [Standard
Events of a Species](142_Standard%20Events%20of%20a%20Species.htm)
window.

**Add Days**

A offset may be applied to an event by entering a value in the *Days*
field and clicking *Add Days* button. This can be either positive or
negative and will move the event that number of days forward or back in
the event queue.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 138. Configure Other Options 2020

**Configure Other Options**

\[[Configuration](150_Configuration.htm) page: *Other Options* panel\]

Assorted configuration options.

**Economic Modelling**

Costs and incomes are added to various events, so that economic
calculations can be performed. All economic modelling is in constant
dollars.

If economic modelling is on then the site must have an area (see [Site :
Area](157_Site_Area.htm)), so that the per-hectare costs can be added to
the fixed costs and be presented as a single cost.

If economic modelling is on then thins and harvests must be specified by
log and crop grades, because only log and crop grades include pricing
information on logs and crops. Note that, even using log grades, a thin
event can specify a 0% log grade and still specify which material moves
to debris - so forest management activities like pruning can still be
achieved with economic modelling on (same for crops).

**Events or Time Series**

See [Configure Event Or Time
Series](195_Configure%20event%20or%20time-series.htm).

**RothC Version**

If the plot model includes the soil then the [RothC](114_RothC.htm)
model is will be used to simulate the soil. If you are running the
[Research Edition](48_Research%20Edition.htm) of FullCAM, then you can
then specify which version of RothC to use:

- RothC version **26.3**. Fully calibrated for Australian conditions
  with data available. This version is always used by the standard
  version of FullCAM.
- RothC version **26.5**. More sophisticated, but not calibrated. Only
  in the [Research Edition](48_Research%20Edition.htm) of FullCAM.

If you model a mixed forest and agricultural system and model the soil,
then FullCAM will always use the same version of RothC for both the
forest soil and the agricultural soil.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 140. Thin 2020

**Thin**

\[[Event Window](137_Event%20Window.htm) : *Thin* panel\]

A thin event is where some or all of the forest is harvested.

**Introduction**

The agricultural counterpart of a thin is a [Harvest](153_Harvest.htm)
event

A thin is the only event that creates forest products, taking tree
material offsite. See the [Product
Properties](47_Product%20Properties.htm) of each species.

**Affected Portion**

The *affected portion* is the fraction of the total forest area being
modelled in which the thin takes place. It is also the fraction of the
plot area that is thinned --- the proportion of an unspecified areas to
be reported on a per hectare basis. For most plantations this would
generally equate to the fraction of the proportion of trees that are
thinned.

**Destination Percentages in the Affected Portion**

These destination percentages are applied to the portion of the forest
that is affected by the thin.

The destination percentages of litter (deadwood, chopped wood, bark
litter, and leaf litter) apply to all species whose material is present
in the litter.

*Log Grades*

Specify the percentages of full log grade extractions, which are
specified in turn for the species on the [Log Grades or Crop
Grades](http://www.fullcam.au/FullCAMServer2020/Help/263_Log%20Grades%20or%20Crop%20Grades.htm)
page.

For example,

specifying 50% of grade 1 means applying a Grade 1 thin at 50%
intensity.\
specifying 100% of grade 3 and 0% for the other grades applies a grade 3
thinning.

You can mix and match, so long as the log grade percentages do not
exceed 100%. So if grade 1 took stems for construction and grade 2 was
mainly branches for pulp, you could do some of each in this thin.

The *Extra Percentages to Debris* are for moving material from the
plants to the debris independently of (and in addition to) the log grade
movements. Especially useful for management operations like pruning. The
total plant material moved to the debris is equal to the amounts
specified by the log grades, plus the extra movements specified here.
The extra amount moved to the debris (above and beyond that specified by
the log grades) is equal to or less than the extra amount specified here
(depending on whether or not the specified material is available after
the log grades).

Check the *Clear all remaining tree mass to debris* box for this to
become a clearing thin (all tree material not specified by the log
grades is moved into debris).

Click *Show Destinations Percentages\...* to see all the log grades for
the species, and the affect of the specified log grade percentages. You
can see the destination percentages for the affected forest, which are
equivalent of the manual percentage changes (see next).

The advantage of the log grades is that the detailed work of specifying
the destination percentages is done once in the species, then quickly
applied to many thins. Because mill gate prices, harvest costs, and
transport costs are specified by species on the [Log Grades or Crop
Grades](http://www.fullcam.au/FullCAMServer2020/Help/263_Log%20Grades%20or%20Crop%20Grades.htm)
page, you must use the log grade system if doing economic modelling (see
[Configure Other Options](138_Configure%20Other%20Options.htm)).

*Manual*

The destination percentages for each thinned pool (stems, branch, bark
or leaves) must add to less than or equal to 100%. If they add to less
than 100% then the material without a destination remains on the plot,
in the forest.

If the thin affects all the stems (the affected portion is 100% and the
stem destination percentages add to 100%) then the thin must clear all
of the other tree pools as well to be physically realistic (because
leaves die without stems or branches).

It is possible to retain root material on site to simulate a coppicing
effect.

**Example**. Suppose the affected portion is 70%. Let the bark
destination percentages be 20 to the bark litter, 10 to biofuel, 30 to
paper and pulp, and 5 to mill residue --- for a total bark destination
percentage of 65. Thus 35% of the bark stays on the trees in the portion
of the forest affected by the thin. Then, of all the bark on the plot,
in this thin 70% \* 20% = 14% goes to bark litter, 7% becomes biofuel,
21% becomes paper and pulp, 3.5% becomes mill residue, and the rest
stays on the remaining trees.

**Clearing Thin**

For a thin to clear the forest of trees, the affected portion must be
100% and the destination percentages for each pool must add to 100%.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 141. Models and Inputs Window 2020

**Models and Inputs Window**

\[[Configuration](150_Configuration.htm) page : *Models and Inputs*
button\]

This window shows information about the currently chosen configuration:

- The constituent models that will be used to simulate your
  configuration
- The data inputs required by your configuration.

You cannot change any aspect of the configuration or the document from
this window.

**Models**

See [Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm), [Yield and
NPP](131_Yield%20and%20Net%20Primary%20Production.htm), and [Constituent
Models In FullCAM](198_Constituent%20Models%20In%20FullCAM.htm).

*Plants* is about modelling all the aspects of plants other than
production: partitioning of production to the various plant components,
turnover, thinning, harvesting, fire, and so on.

**Options Menu**

**Show Values.** Show the current values in the document. If the value
belongs to a species, it shows the value in the species that is
currently chosen for editing. If the value belongs to an event, the
value shown comes from an arbitrarily chosen event of that type. If
there is no species or event or the value is blank or the value is not a
number or "On/Off", or if there is no such value in that type of
document, generally no value is shown.

**Show Programming Names.** Shows the internal FullCAM programming
names..

**Show Configuration.** Shows a record of the choices you made.

**Display.** Either:

1.  **All inputs** - Shows all inputs to FullCAM, ignoring the
    configuration and any other settings. Showing values is not
    generally possible because some inputs will not exist.
2.  **Inputs required by the current configuration** - Shows the inputs
    that could be required by the current configuration, but ignores the
    settings on other pages of the document. It is possible that some
    inputs will be shown that are not required because of other
    (non-configuration) settings --- for example, in a forest
    configuration the tree mortality inputs will be shown as required
    regardless of whether or not the *Tree mortality on* box is checked
    on the [Plant Properties](43_Plant%20Properties.htm) window for any
    species.
3.  **Inputs required by the current configuration and other
    settings** - Shows the inputs that could be required by the current
    configuration and the current settings on other pages of the
    document. Thus this option gives the smallest, most accurate picture
    of the data inputs required by FullCAM, but requires you to have
    entered all the input settings already (as would be the case if the
    document was ready to simulate).

These inputs are never shown:

- Names and note inputs
- Configuration settings (all the settings made on the
  [Configuration](150_Configuration.htm) page)
- Event type, timing, and name inputs.

**Copy**

There are two copy options on the toolbar. Either:

1.  **Copy** - Select all or part of the text and copy to clipboard.
2.  **Spreadsheet Copy** - Press the *Copy All Text in Spreadsheet
    Format* button or use the mouse menu. This copies all of the text,
    using tabs to separate fields --- suitable for pasting into a
    spreadsheet.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 142. Standard Events of a Species 2020

**Standard Events**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Standard
Information for the Species* panel : *Events* button\]

Manage the standard events, for the current species ([Select a
Species](56_Select%20a%20Species.htm)).

The standard events are simply events which are made available for a
species for convenience. The standard events downloaded through Data
Builder are only available for convenience and may not be relevant or
applicable for the particular species of interest. The standard events
should not be confused with the event queue (on the
[Events](136_Events.htm) page). The event queue is the queue of events
that will be simulated during a plot simulation.

**Uses**

1.  If you often use a particular event on the *Events* page, you might
    want to store the event as a standard event. Then, when you want
    another such event on the *Events* page, you can load the input
    values from the standard event rather than retyping them. Also,
    storing the events that are typical for a given species is helpful
    when you give the species to others.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 143. Event Timing 2020

**Event Timing**

\[[Event Window](137_Event%20Window.htm) (via the
[Events](136_Events.htm) page): *Timing* panel\]

Enter timing information for the event.

**"Simulate" Checkbox**

The *Simulate* checkbox specifies whether or not the event is to be
simulated. Uncheck this box to effectively turn the event off --- it
will still be on the event queue, but it will not be simulated (it will
have no effect on a simulation). This is useful for temporarily
suspending an event from the simulation.

The *Simulate* checkbox may be checked or unchecked on the [Event
Window](137_Event%20Window.htm), or on the [Events](136_Events.htm) page
by the secondary mouse button and selecting either *Simulate Events* or
*Do Not Simulate Events*.

**Type and Time**

Specify the event time, as either a:

1\. Calendar date\
Examples: 1 Jan 2001, 31 Dec 2010.

Enter the date in any unambiguous way, such as "4 Sep 2010", "s4", "au9
1999", "4s2000", "8/4/0" or "8.4.1999", except that you cannot use
hyphens because they are interpreted as negative signs (for example 8 4
-35 is 8 Apr -35).

2\. Calendar years and days since the start of the simulation\
Example: -10, 0, 2345.

A calendar year is from a date in one year to the same date in the next
year, and can contain either 365 or 366 days depending on leap years.
The number of days can also be huge. So if you mean the same date in two
years time, set the calendar years equal to two and the days to zero,
but if you mean exactly 730 days then set the calendar years to zero and
the days to 730.

Changes made in one format are reflected in the other upon format
change.

An event always occurs at noon of the day on which it is specified to
occur, even if that time is in the middle of a simulation step. FullCAM
computes the continuous processes for the partial step up to the event,
executes the event, then computes the continuous processes up to the
next event or the end of the step.

Each event occurs instantaneously --- it begins and ends at noon of the
same day.

Event timing may be updated for multiple events by multi-selecting the
events on the Event List, and then selecting the right mouse option
*Apply Offset to Events*. The timing may then be updated by the [Event
Update](248_Event%20Update.htm) dialog.

**Add Days**

A offset may be applied to an event by entering a value in the *Days*
field and clicking *Add Days* button. This can be either positive or
negative and will move the event that number of days forward or back in
the event queue.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 144. Forest Fire 2020

**Forest Fire**

\[[Event Window](137_Event%20Window.htm) : *Forest Fire* panel\]

Enter the inputs specific to a forest fire event.

**Affected Portion**

The affected portion is the fraction of the forest area that is burnt or
partly burnt.

**Age Adjustment**

The Age Adjustment allows for some additional growth of woody biomass
post-disturbance. This is achieved by effectively re-calculating the
stand age applied in the TYF such that it is less than the actual stand
age. The effective stand age applied in the TYF post Age Adjustment is
calculated from the biomass removed in the disturbance event. This
calculation is based on the TYF and its relationship between age and
above-ground biomass. The effective stand age is assumed to decline
backwards along the TYF such that the more biomass removed, the younger
the stand is assumed to be when growth resumes post-disturbance. Hence,
the impact of the Age Adjustment is dependent on both the amount of
biomass removed and also the stand age at the time of disturbance. For
relatively young stands, this will stimulate growth when the effective
stand age is moved back to be closer to the age of maximum biomass
increments (G years). However for mature stands, the Age Adjustment has
relatively little impact on growth.

It should be noted that the effective stand age used in the TYF may be
different to the actual stand age. Both of these stand ages are
available as outputs of the model.

**Destination Percentages in the Affected Portion**

These destination percentages are applied to the portion of the forest
that is affected by the fire.

The tree material that is affected by the fire can be transferred to the
atmosphere, to the standing dead pool, or to the debris pool. Standing
dead material created in an earlier event can be similarly transferred
to the atmosphere or to debris. Debris and mulch material can be
transferred to the atmosphere or to inert soil (as charcoal). Where the
sum of the destination percentages for a single pool does not sum to
100%, the remainder is taken to stay in its original pool.

Material transferred from one pool to another as a result of the fire
event will not be further affected by the fire event. For example, a
single forest fire event can move stems to debris, but not further to
inert soil.

**Years to Regrow Post-Fire**

If a forest fire event is applied to a forest layer where trees are
planted and growing (ie: not thinned), they will recover to their
previous level of growth within the time period specified. This behavior
should only be used to model fires that are not stand-replacing. If a
stand-replacing fire is being modelled, it should be accompanied by
other events for the thinning and re-planting of trees.

**Using Fire Events to Model Land Clearing**

Forest fire events can be applied following a [thinning](140_Thin.htm)
(forest removal) event to remove the debris created during thinning,
consistent with the concept of a *conversion burn*. When creating a [New
Regime](274_New%20Regime.htm) for tree species, such fire events will be
created alongside thinning events.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 145. Properties of the Species 2020

**Properties of the Species**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel\]

Enter the properties of the current species ([Select a
Species](56_Select%20a%20Species.htm)).

**Readiness**

The concept of readiness is described in general in [General
Features](20_General%20Features.htm).

Buttons for mandatory FullCAM properties are shown in black if they are
complete, red if not. Buttons for optional FullCAM properties are shown
in black if they are complete, orange if not. The Notes button is shown
in bold font if any notes have been entered for the species. The name of
the species must be completed, and it must be unique. If any of the
properties are not fully specified, then the species cannot be
simulated.

**Plantation type**

The Plantation type is editable in a database document and displayed in
a plot document. It is used in spatial simulations to differentiate
between *Other tree*, *Softwood* and *Hardwood* Plantation types.

**MVG and MNFG**

The MVG (Major Vegetation Group) and MNFG (Managed Native Forest Group)
numbers apply only to database documents.

MVG and MNFG are applicable only when the Plantation type is *Other
tree*. They are identification number for the species during a [Spatial
Simulation](http://www.fullcam.au/FullCAMServer2020/Help/73_Spatial%20Simulation.htm),
used by either the MVG or MNFG spatial files (see [Spatial-Only
Inputs](http://www.fullcam.au/FullCAMServer2020/Help/68_Spatial-Only%20Inputs.htm)).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 146. Standard Information for the Species 2020

**Standard Information for the Species**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Standard
Information for the Species* panel\]

Set standard information for the current species ([Select a
Species](56_Select%20a%20Species.htm)):

[Initial Trees](185_Initial%20Trees.htm)\
[Initial Crops](184_Initial%20Crops.htm)\
[Initial Debris](31_Initial%20Debris.htm)\
[Initial Products](33_Initial%20Products.htm)\
[Standard Events of a
Species](142_Standard%20Events%20of%20a%20Species.htm)

*Standard* initial conditions or events for a species may be considered
to be those typical for that species or conditions.

**Use in Plots**

Standard information is optional for plot documents - they may be
ignored.

The standard values may be automatically copied into the appropriate
initial conditions or events window by clicking the *Insert Standard
Values* button.

Standards that are not ready in a plot document are coloured orange
(optionally not ready).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 149. Agricultural Fire 2020

**Agricultural Fire**

\[[Event Window](137_Event%20Window.htm) : *Agricultural Fire* panel\]

Enter the inputs specific to a agricultural fire event.

**Affected Portion**

The affected portion is the fraction of the agricultural system in which
the fire takes place. It is typically the fraction of the plot area that
is burnt or partly burnt.

**Destination Percentages in the Affected Portion**

These destination percentages are applied to the portion of the
agricultural system that is affected by the fire.

The crop material that is affected by the fire either moves to the
atmosphere, moves to the debris, or remains where it is. The debris and
mulch material either moves to the atmosphere, to the inert soil (as
charcoal), or remains where it is. The sum of the two destination
percentages for a single pool must be less than or equal to 100%.

Material is moved from the crop to the debris after the amounts of
debris that move have been calculated. Crop material cannot go
immediately to the inert soil as a result of a fire.

**Example**. The portion of the agricultural system that is affected by
the fire is 90%. The GBF destination percentages are 80 to the
atmosphere and 10 to the debris --- for a total stem destination
percentage of 90. Then, of all the GBF material on the plot, in this
fire 90% \* 80% = 72% goes to the atmosphere, 90% \* 10% = 9% becomes
GBF litter, and the remaining (100% -- 90%) + 90% \* (100% -- 90%) = 19%
stays where it was.

Typically very little if any of the deep minerals will be lost to the
atmosphere, and only a small portion or none of the shallow minerals.

**Clearing Fire**

For a fire to clear the agricultural system entirely of crop, the
affected portion must be 100% and the destination percentages for each
pool (the sum of the destination percentages to the atmosphere and to
the debris) must sum to 100%.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 150. Configuration 2020

**Configuration**

\[*Configuration* page of the input window of a document\]

This page is where you specify the configuration of your plot, by
choosing which parts of the plot should be modelled. This topic
describes configuration issues in general terms; for more specifics see:

[Configure the Plot](6_Configure%20the%20Plot.htm)\
[Configure What To
Simulate](http://www.fullcam.au/FullCAMServer2020/Help/128_Configure%20What%20To%20Simulate.htm)\
[Configure Tree Production](108_Configure%20Tree%20Production.htm)\
[Configure Other Options](138_Configure%20Other%20Options.htm)

**About**

This window allows users to view a list of all inputs (click on the
'Models and Inputs'\... button) or a diagram showing all pools and
fluxes of C (click on the 'Diagrams\...' button) for the model
configuration selected.

**Models and Inputs**

Clicking the 'Models and Inputs' button brings up a new window which
lists a variety of information for the model configuration selected. The
level of detail of information presented in this window can be specified
using the 'Options' button located at the far left of the menu bar for
this window. Additional menu bar buttons allow the user to copy and
select various components of the window, turn on word wrap if required,
export the information in the window to a text file, find text and view
help file.

Clicking the Options button and scrolling down to the 'Display' menu
option allows the user to specify the inputs that will be displayed in
the window. Options include:

- All inputs: lists all inputs whether required or not for the current
  configuration settings.
- Inputs required by the current configuration: only displays inputs
  required by the current configuration.
- Inputs required by the current configuration and other settings:
  displays inputs required by the current configuration plus additional
  information pertaining to other events such as fire, plough,
  herbicide, grazing, irrigation, manure application, etc.

The other three menu items on the Options button allow the user to
specify the nature of the information presented:

*Show values*: presents the values entered into the various tabs and
windows to the right of the descriptor of each input (e.g. Carbon % of
fine roots = 38.4 %). If the value belongs to a species, it shows the
value of the species that is currently selected for editing in the
appropriate tab. If the value belongs to an event, the value shown comes
from the chosen event of that type. No value is shown if there is no
species or event or the value of the input is blank.

*Show programming names*: presents the name assigned by FullCAM
programming code for the variables in square brackets (e.g. Carbon % of
fine roots \[CFracFirtA\] = 38.4%). Programming names are useful if you
are reading and referring to the FullCAM Function Specification.

*Show configuration*: presents the user specified configuration for the
plot as the first item in the information displayed. If any
discrepancies exist between this list and the regular interface, the
regular interface is correct.

You can get help related to a specific input by placing the cursor in
the line in which the input is presented and clicking the 'Help for
Input on Selected Line' button in the menu bar (Ctrl + i). General help
pertaining to this window can be obtained by clicking on the 'Help'
button in the menu bar (F1)

**Configuration Determines Inputs**

The configuration you choose will affect which inputs are required. For
example, if you model a forest system only, then none of the
agricultural inputs will be required. Or if 3PG is not used to model
tree production, the inputs that describe the net primary productivity
of the forest are not required.

You might want to experiment with different configurations in order to
determine the most configuration that most suits your needs, given the
available inputs and your required outputs. To help in this process, for
each configuration you can see model diagrams ([Diagrams
Window](50_Diagrams%20Window.htm)) and a list of required inputs
([Models and Inputs Window](141_Models%20and%20Inputs%20Window.htm)).

The plot input window only shows tabs for pages that have required
inputs. On these pages, any inputs that are not required are dimmed
(unavailable). To see which models use which inputs, change the
configuration and any other relevant settings (such as turning
irrigation on or off) and see if the input is still enabled.

**FullCAM Integrates Its Constituent Models**

All of the [Constituent Models In
FullCAM](198_Constituent%20Models%20In%20FullCAM.htm) models are
available, either independently or in combination.
[CAMFor](77_CAMFor.htm) and [CAMAg](78_CAMAg.htm) are multilayer
framework models. FullCAM allows you to run combinations of these
models, to simulate single or multilayer models (see [Plots, Systems,
Layers, and Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm)),
either forest or agricultural or mixed.

**Readiness**

When the *Configuration* page is unready and requiring more information:

- The writing on the tab of the page is red.
- Only the [About](11_About.htm), Configuration, and
  [Timing](199_Timing.htm) tabbed pages appear in the input window of
  the document.

When the *Configuration* page is ready (that is, complete):

- The writing on the tab of the page is black.
- If the *Timing* page is also ready then more than three tabbed pages
  appear in the input window.

While all the input pages use the red or black tab to indicate
unreadiness (see [General Features](20_General%20Features.htm)), only
the *Configuration* page also controls which other tabbed pages appear
in the document input window.

**Simpler Is Usually Better**

The more layers and the more sophisticated features you choose in your
model, the more difficult it will be to find all the required input
data. We recommend:

- Only modelling those layers and simulating those elements that you
  need (in particular, do not model nitrogen unless necessary)
- Restrict model configurations to those for which data is available and
  for which the outputs are understandable.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
