---
version: 2016
batch_range: 101-150
batch_name: Advanced_Configuration_Modeling
creation_date: 2025-08-28
total_files: 33
---

# FullCAM 2016 - Batch 101-150: Advanced Configuration Modeling

## Table of Contents

- [101. Manure Inputs to Soil from Offsite 2016](#101-manure-inputs-to-soil-from-offsite-2016)
- [102. Soil Cover 2016](#102-soil-cover-2016)
- [108. Configure Tree Production 2016](#108-configure-tree-production-2016)
- [109. GENDEC 2016](#109-gendec-2016)
- [110. Tree Growth Increments 2016](#110-tree-growth-increments-2016)
- [112. Tree Growth Allocations 2016](#112-tree-growth-allocations-2016)
- [113. Crop Yields Table 2016](#113-crop-yields-table-2016)
- [114. RothC 2016](#114-rothc-2016)
- [115. 3PG 2016](#115-3pg-2016)
- [116. Forest Percentage Change 2016](#116-forest-percentage-change-2016)
- [118. Crop Growth Increments 2016](#118-crop-growth-increments-2016)
- [120. Plant Removal and Replacement 2016](#120-plant-removal-and-replacement-2016)
- [121. Mortality 2016](#121-mortality-2016)
- [122. Sensitivity of Debris Breakdown to Temperature and Water 2016](#122-sensitivity-of-debris-breakdown-to-temperature-and-water-2016)
- [123. Notes on a Plant Species 2016](#123-notes-on-a-plant-species-2016)
- [124. Crop Growth Allocations 2016](#124-crop-growth-allocations-2016)
- [127. Simulate Menu 2016](#127-simulate-menu-2016)
- [130. Tree Yield Formula 2016](#130-tree-yield-formula-2016)
- [131. Yield and Net Primary Production 2016](#131-yield-and-net-primary-production-2016)
- [132. Data Builder 2016](#132-data-builder-2016)
- [135. Time-Series Window 2016](#135-time-series-window-2016)
- [136. Events 2016](#136-events-2016)
- [137. Event Window 2016](#137-event-window-2016)
- [138. Configure Other Options 2016](#138-configure-other-options-2016)
- [140. Thin 2016](#140-thin-2016)
- [141. Models and Inputs Window 2016](#141-models-and-inputs-window-2016)
- [142. Standard Events of a Species 2016](#142-standard-events-of-a-species-2016)
- [143. Event Timing 2016](#143-event-timing-2016)
- [144. Forest Fire 2016](#144-forest-fire-2016)
- [145. Properties of the Species 2016](#145-properties-of-the-species-2016)
- [148. No Help Available 2016](#148-no-help-available-2016)
- [149. Agricultural Fire 2016](#149-agricultural-fire-2016)
- [150. Configuration 2016](#150-configuration-2016)

---

## 101. Manure Inputs to Soil from Offsite 2016

**Manure Inputs to Soil from Offsite**

\[[Soil Inputs](193_Soil%20Inputs.htm) window : *Manure from Offsite*
button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify the carbon mass (and maybe also the nitrogen mass) entering the
soil from outside the plot, in tonnes per hectare.

**Details**

Manure from offsite (that is, from outside the plot) may be added to the
forest or agricultural soil.

In an agricultural system, manure from animals on the plot is dealt with
by grazing --- see the [Grazing Change](196_Grazing%20Change.htm)
events: plant material eaten by grazing animals becomes fodder, which
may go to destinations including the DPM an RPM pools of the soil. This
manure-from-offsite time-series is the only explicit treatment of manure
by FullCAM.

This time-series is only used when the *Manure-From-Offsite Added to the
Soil* setting on the [Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm) window is set
to *time-series*.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 102. Soil Cover 2016

**Soil Cover**

\[[Soil](203_Soil.htm) page : *Agricultural* panel : *Soil Cover*
button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify whether or not the agricultural soil is covered, in plot models
that only model the agricultural soil (see [Configure the
Plot](6_Configure%20the%20Plot.htm)).

**Agricultural Soil**

If you are modelling the soil but not the whole agricultural system,
then you have to tell FullCAM when the soil is covered or not. Soil
cover consists of debris and plants, and it affects the rate of moisture
loss from the soil and thus the agricultural soil water levels (more
precisely, the topsoil moisture deficit computed by the
[RothC](114_RothC.htm) model).

Enter the soil cover time-series to tell FullCAM when there is enough
soil cover to slow down the rate of water loss from the soil. If the
agricultural soil is covered by vegetation or debris (and thus less
prone to drying out) for the whole of the relevant period, then enter 1.
If it is bare for the whole period, enter 0. If it is partly covered for
all of the period, or covered for only part of the period, enter a
number between 0 and 1.

After interpolation and extrapolation to get a soil cover value in each
simulation step, a soil cover value of 0.5 or greater is treated as
covered and a soil over value of less than 0.5 is treated as bare.

When the soil cover is automatically calculated by FullCAM (that is,
when the soil is modelled as part of a multi-layer agricultural system),
the agricultural soil is considered to be always covered except during:

- The period between ploughing and the subsequent planting
- The period between an agricultural fire that immediately follows a
  herbicide, and the subsequent planting

The herbicides, ploughs and fires mentioned here are ignored if they
affect less than 50% of the plot.

**Forest Soil**

Forest soil is considered to be always covered.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 108. Configure Tree Production 2016

**Configure Tree Production**

\[[Configuration](150_Configuration.htm) page : *Tree Production*
panel\]

Specify how the production of new tree material should be calculated.

**Introduction**

The amount of new tree material is called the *net primary production*
(NPP) of the trees, and is the combined outcome of photosynthesis and
respiration.

**Method**

Choose a tree growth method:

- *Increments* - FullCAM will use time-series of volume or mass
  increments of new growth, by calendar year or by tree age. You have to
  supply that data, in the [Growth
  Properties](42_Growth%20Properties.htm) window.
- *Tree yield formula* Uses an equation, the [Tree Yield
  Formula](130_Tree%20Yield%20Formula.htm), to calculate tree growth.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 109. GENDEC 2016

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

## 110. Tree Growth Increments 2016

**Tree Growth Increments**

\[[Growth Properties](42_Growth%20Properties.htm) window (for trees) :
Any of the *Increments* buttons\]

This [time-series Window](135_time-series%20window.htm) is one of the
tree increment time-series windows, where you specify the growth of the
trees as either:

- Volume increments of stems \[m^3^/ha\]
- Mass increments of various tree components \[tdm/ha\]
- NPP flows to various tree components \[tdm/ha\].

**Details**

Stems have no turnover, so NPP flows to the stems are equal to the yield
increments of the stems.

Stem volume increments are converted to stem mass increments by
multiplying by the [Stem Density](9_Stem%20Density.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 112. Tree Growth Allocations 2016

**Tree Growth Allocations**

\[[Growth Properties](42_Growth%20Properties.htm) window (for trees) :
Any of the *Allocations* buttons\]

This [time-series Window](135_time-series%20window.htm) is one of the
tree allocation time-series windows, where you specify the relative
allocations of yield or NPP (see [Yield and
NPP](131_Yield%20and%20Net%20Primary%20Production.htm)) to the six tree
components: stems, branches, bark, leaves, coarse roots, or fine roots.

**Introduction**

The allocations determine the growth of the component, relative to the
other tree components. A high allocation means more growth of the
component compared to the other components, a low allocation means the
component grows slower than the other components. The tree components
all grow in certain proportions to one another at various stages in the
tree's life; these allocations are the mechanism for determining those
proportions in FullCAM.

Enter an allocation for each period in the time-series. The allocations
are purely relative: it is not the size of the numbers by themselves
that matters, only the ratios between the allocations to the various
tree components.

**Examples**

In these examples we will assume yield allocations. Thus we are
concerned only with the mass increases of the tree components, relative
to one another.

Typically the stem (or bole) growth is your reference, and the mass
increases of the other components relative to the stems are noted. In
this case, set the relative stem growth to 1.0 and set the other
relative growths accordingly. For example, if leaf mass increment is a
half of the stem mass increment (in tdm/ha, over the relevant time
period) then set the stem allocation to 1.0 and the leaf allocation to
0.5.

**Example 1**. Suppose that, in a given year of tree growth, the mass of
the stems in a hectare of trees increases by 15 tonnes, while the mass
of bark on the same hectare increases by 5 tonnes. Then the ratio of
stem growth to bark growth is 15 / 5 = 3. Thus the relative growth
factors of stems and bark are respectively 3x and x, where x is any
non-negative number. You might choose any of the following as the
relative growths for that year:

- Stem allocation is 1.0 and bark allocation is 0.33 (the obvious
  choice).
- Stem allocation is 3.0 and bark allocation is 1.0
- Stem allocation is 6.0 and bark allocation is 2.0.

And so on.

**Example 2**. Suppose that in a given three month period of tree growth
that, in a hectare of trees, the mass increases in the components over
the period were as follows:

> 
>   Vegetation Component   Value in tdm/ha
>   ---------------------- -----------------
>   Stems                  0.25
>   Branches               0.50
>   Bark                   0.125
>   Leaves                 0.75
>   Coarse roots           0.25
>   Fine roots             0.125

The typical choice of yield allocations (namely, all relative to the
stems) for this period would be:

> 
>   Vegetation Component   Yield Allocation
>   ---------------------- ------------------
>   Stems                  1.0
>   Branches               2.0
>   Bark                   0.5
>   Leaves                 3.0
>   Coarse roots           1.0
>   Fine roots             0.5

Another choice (branches as reference) would be:

> 
>   Vegetation Component   Yield Allocation
>   ---------------------- ------------------
>   Stems                  0.5
>   Branches               1.0
>   Bark                   0.25
>   Leaves                 1.5
>   Coarse roots           0.5
>   Fine roots             0.25

And so on.

Data on allocations to various tree components can be found in the NCAS
Technical Reports
[5a](reps/TR5A%20Review%20of%20Allometric%20Relationships%20for%20Estimating%20Woody%20Biomass%20for%20Queensland,%20the%20Northern%20Territory%20and%20Western%20Australia.pdf){target="reps5a"},
[5b](reps/TR5B%20Review%20of%20Allometric%20Relationships%20for%20Estimating%20Woody%20Biomass%20for%20New%20South%20Wales,%20the%20Australian%20Capital%20Territory,%20Victoria,%20Tasmania%20and%20South%20Australia.pdf){target="reps5b"},
[17](reps/TR17%20Synthesis%20of%20Allometrics,%20Review%20of%20Root%20Biomass%20and%20Design%20of%20Future%20Woody%20Biomass%20Sampling%20Strategies.pdf){target="reps17"},
[25](reps/TR25%20Review%20of%20Unpublished%20Biomass-Related%20Information%20Western%20Australia,%20South%20Australia,%20New%20South%20Wales%20and%20Queensland.pdf){target="reps25"}
and
[44](reps/TR44%20Spatial%20Estimates%20of%20Biomass%20in%20'Mature'%20Native%20Vegetation.pdf){target="reps44"}
([17](reps/TR17%20Synthesis%20of%20Allometrics,%20Review%20of%20Root%20Biomass%20and%20Design%20of%20Future%20Woody%20Biomass%20Sampling%20Strategies.pdf){target="_blank"}
is the synthesis report).

General values for major vegetation types can be found in Table 3 of the
report *Greenhouse Gas Emissions from Land Use Change in Australia:
Results of the National Carbon Accounting System 1988--2001*. Additional
species specific allocations can be extracted from the FullCAM database.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 113. Crop Yields Table 2016

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

## 114. RothC 2016

**RothC**

The RothC [Soil](203_Soil.htm) model is one of the [Constituent Models
In FullCAM](198_Constituent%20Models%20In%20FullCAM.htm).

**Description**

The [Rothamsted Carbon
Model](http://www.rothamsted.ac.uk/ssgs/RothC/RothC.php){target="_new"}
(RothC) model is a soil carbon model. RothC models the turnover of
organic carbon in non-waterlogged soils, taking into account clay
content, temperature, moisture content, plant and manure inputs, and
plant cover. RothC tracks the amount of microbes and several soil pools
containing active carbon.

The name "RothC" comes from
[*ROTH*amsted-Institute](http://www.rothamsted.ac.uk){target="_new"}
active soil *C*arbon model.

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
website](http://www.rothamsted.ac.uk){target="_new"}.

The DPM pool tends to small and transient, because material moves
quickly from DPM to BIO-F, BIO-S, and HUM (because it decomposes
easily).

The RPM pool is sometimes called "particulate organic matter" (POM)
elsewhere.

Typically the fraction of total soil carbon in the BIO-F and BIO-S pools
is very small --- these are small but very active pools of microbes. In
practice it is often difficult to impossible to measure BIO-F and BIO-S.

**RothC Version**

If the plot model includes the soil then the [RothC](114_RothC.htm)
model will be used to simulate the soil (RothC version **26.3**; fully
calibrated for Australian conditions).

If you model a mixed forest and agricultural system and model the soil,
then FullCAM will always use the same version of RothC for both the
forest soil and the agricultural soil.

**Inert Soil**

The inert (or "inactive") soil is all in the inert pool in FullCAM (see
[Soil](203_Soil.htm)). The inert material is sometimes called "charcoal
and charred plant material" (CHAR) elsewhere. In FullCAM the inert pool
is outside of RothC --- it is instead managed by [CAMFor](77_CAMFor.htm)
or [CAMAg](78_CAMAg.htm) --- even though the RothC model elsewhere has
an inert pool. The inert pool is simply a reservoir of soil material
that is very unlikely to move to any other pool in the foreseeable
future. It mainly consists of charcoal or material that is physically
encapsulated (perhaps by clay).

**Credits**

The RothC model within FullCAM implements the FORTRAN programs
"ROTHC-26.3" and "ROTHC-26.5_32" by K.W. Coleman, D.S Jenkinson, L.C.
Parry and J.H. Rayner. It draws on papers by Jenkinson and Coleman,
amongst others.

The model was enhanced by the CSIRO in Adelaide (Jan Skjemstad, +618
8303 8427) and the Australian Greenhouse Office. Enhancements include
the ability to use the historical weather time-series rather than
average weather (including the topsoil moisture deficit (TSMD)
computations). Equilibrium and radiocarbon dating computations were
omitted.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 115. 3PG 2016

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

## 116. Forest Percentage Change 2016

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

Set the forest percentage manually here. It will not change until the
next forest change event. This is a reasonable approach to use for
activities such as the thinning of trees in a grazed woodland. Note that
the Forest Percentage Change does not automatically respond to a
[Thin](140_Thin.htm) event that removes a prescribed portion of trees.
If the thin event is being used to alter the tree canopy cover to
promote pasture growth, then the thin and forest percentage change
events should be manually aligned.

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

This field may be used with or without the tree yield formula.

**Note**: Under this option, in simulation steps where the tree yield
formula happens to not be in use, the forest percentage is equal to the
constant forest percentage entered in the initial conditions. This is
similar to the linking of canopy closure and age of maximum growth in
the previous option but lets you set the age of canopy closure manually.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 118. Crop Growth Increments 2016

**Crop Growth Increments**

\[[Growth Properties](42_Growth%20Properties.htm) window (for crops) :
Any of the *Increments* buttons\]

This [time-series Window](135_time-series%20window.htm) is one of the
crop increment time-series windows, where you specify the growth of the
crop as either:

- Mass increments of various crop components \[tdm/ha\]
- NPP flows to various crop components \[tdm/ha\].

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 120. Plant Removal and Replacement 2016

**Thin or Harvest : Plant Removal and Replacement**

\[[Event Window](137_Event%20Window.htm) : *Thin* panel : *Tree/Plant
removal and replacement* section\]

Specify how the [Thin](140_Thin.htm) or [Harvest](153_Harvest.htm)
affects the average age of the plants.

**Introduction**

In this topic:

  ---------- -- --------------------------------------------------------
  Thins         \"Plants\" are trees; the \"event\" is a thin
  Harvests      \"Plants\" are crop plants; the \"event\" is a harvest
  ---------- -- --------------------------------------------------------

The only effect of this section is to specify how the average age of the
plants changes due to the event. By specifying the average age of the
plants that are removed from the plot, and whether or not new plants
spring up to replace them, you can control the change in the average age
of the plants.

This is only of interest if you are using the average age of the plants
to determine relative allocations or growth (see the [Growth
Properties](42_Growth%20Properties.htm) windows), in which case you can
control how the event moves the plants along their growth curves.

These settings are only relevant (and thus enabled) for thinnings that
leave some stems or stalks (that is, the fraction of plants removed is
less than 100%).

**Default Setting**

Most people will want the default setting:

1.0 in the top box\
0.0 in the middle\
0.0 in the bottom box,\
Do not check the *Replace removed plants\...* box.

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 121. Mortality 2016

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
Loss and Stalk Loss](19_Stem%20Loss%20and%20Stalk%20Loss.htm)
time-series.

**Ratios of Component Losses to Stem Loss**

When a given percentage of the stems or stalks die, the percentages of
other plant components on the plot that die may be different. Specify
these differences in the "Ratio\..." fields. For example, if the *ratio
of leaf loss to stem loss* is 0.3 and 2% of the tree stems die in a
given year, then the percentage of leaves on the plot that are lost is
only 2% \* 0.3 = 0.6% (perhaps the trees close to death have fewer
leaves than the other trees?)

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
- a constant mortality in the Stem Loss or Stalk Loss time-series and
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
time-series. If the average age of the plants after mortality is applied
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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 122. Sensitivity of Debris Breakdown to Temperature and Water 2016

**Sensitivity of Debris Breakdown to Temperature and Water**

\[[Debris Properties](45_Debris%20Properties.htm) window : *Sensitivity*
section\]

Specify how the breakdown rates of the debris increase with increasing
temperature and water.

**Introduction**

You can choose either of both of two styles of sensitivity:

Mulch style\
[Soil](203_Soil.htm) style (as in [RothC](114_RothC.htm))

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 123. Notes on a Plant Species 2016

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 124. Crop Growth Allocations 2016

**Crop Growth Allocations**

\[[Growth Properties](42_Growth%20Properties.htm) window (for crops) :
Any of the *Allocations* buttons\]

This [time-series Window](135_time-series%20window.htm) is one of the
crop allocation time-series windows, where you specify the relative
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

Enter an allocation for each period in the time-series. The allocations
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

And so on.

**Example 2**. Suppose that in a given one month period of crop growth
that, in a hectare of crop, the mass increases in the components over
the period were as follows:

> 
>   Vegetation Component   tdm/ha value
>   ---------------------- --------------
>   GBF                    2.0
>   Stalks                 5.0
>   Leaves                 20.0
>   Coarse roots           10.0
>   Fine roots             1.0

One choice of relative yield allocations (all relative to the GBF
allocation) for this period would be:

> 
>   Vegetation Component   Relative Yield
>   ---------------------- ----------------
>   GBF                    1.0
>   Stalks                 2.5
>   Leaves                 10.0
>   Coarse roots           5.0
>   Fine roots             0.5

Another choice (stalk growth as reference) would be:

> 
>   Vegetation Component   Relative Yield
>   ---------------------- ----------------
>   GBF                    0.4
>   Stalks                 1.0
>   Leaves                 4.0
>   Coarse roots           2.0
>   Fine roots             0.2

And so on.

Typical values can be found in Table 2 (Appendix A) of *Greenhouse Gas
Emissions from Land Use Change in Australia: Results of the National
Carbon Accounting System 1988--2001*.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 127. Simulate Menu 2016

**Simulate Menu**

\[*Simulate* menu, on the [Main Window](217_Main%20Window.htm)\]

This topic is about the items on the *Simulate* menu.

**Run Simulation**

Select \'Run Plot Simulation\' to run a simulation on the current
document. The type of simulation depends on the current document type:

  Document Type   Simulation Type
  --------------- -------------------
  Plot            plot simulation
  Estate          estate simulation

If multiple plots and /or estates are open when \'Run Plot Simulation\'
is selected only the active (front most) plot estate is simulated.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 130. Tree Yield Formula 2016

**Tree Yield Formula**

The tree yield formula is one of the tree production methods in a
multi-layer forest (see [Configure Tree
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

= *A* + sum over each treatment of

  --------------------- -- --------------------------------
  0                        if *A \<= W*
  *v \* (A -- W) / U*      if *A \>= W* and *A \<= W + U*
  *v*                      if *A \> W + U*
  --------------------- -- --------------------------------

where, for each treatment undergone by the forest, specified by the type
1 parameters in the forest treatment events,

*v* = the age advance due to the treatment, either positive or negative,
in years\
*U* = the advancement period, in years\
*W* = the age (of same type as *A*) at which the treatment was applied,
in years.

**Notes**

Thus *T* asymptotically approaches *r \* M \* y* from below as *d*
increases. Note that exp(0) = 1, exp(negative) *\<* 1, and exp(any) *\>*
0. The maximum aboveground biomass for trees when the tree yield formula
is in use is *r \* M \* y*. The forest treatment events move the forest
back and forth along the growth-age curve described by the tree yield
formula, where each age advance is phased in linearly over the
advancement period. When the tree yield formula is in use (that is, the
current tree species uses the tree yield formula to determine its
growth), all age-based properties of the trees use the adjusted age of
the trees (*d*), including the [Tree Growth
Allocations](112_Tree%20Growth%20Allocations.htm),
[Mortality](121_Mortality.htm), and [Stem Density](9_Stem%20Density.htm)
time-series.

**Non-Constant Productivity**

The tree yield formula above gives the growth-age curve of the tree if
the productivity of the site remains constant. Site productivity is
specified by the [Forest Productivity Index
(FPI)](188_Forest%20Productivity%20Index.htm) time-series. In practice
the FPI can vary substantially over time in some environments, which can
have a very marked effect on tree growth.

The relationship between *M* and the average annual FPI *Pavg* over the
life of the tree is taken to be (from observations in experiments)

> *M =* \[ 6.0109 \* sqrt(*Pavg*) *--* 5.2912 \] *\^* 2.
>
> Notation: *x \^* 2 = *x \* x*, and *x* = sqrt(*x \* x*).

Thus, we calculate *Pavg* from *M*. We assume a linear relationship
between FPI and aboveground tree mass in the short term, so the
aboveground mass increment from adjusted age *a1* to *a2* is

> *r \* M \** \[ *y2 \** exp(*--k / a2*) *- y1 \** exp(*--k / a1*) \] \*
> (*P / Pavg*)

where

*P* = the actual FPI over the period *a1* to *a2* (so if using monthly
time steps, *P* will be about *Pavg*/12 on average) (*Site :
Productivity* window),

*y1* = the value of *y* at age *a1*,

*y2* = the value of *y* at age *a2*.

If the maximum annual FPI of 30 was present during the whole life of the
trees, the average annual FPI *Pavg* would be 30 and thus the maximum
aboveground biomass *M* would be 764 tdm/ha (which is the maximum *M*
value you can enter for trees on the *Site* page) (note that (6.0109 \*
sqrt(30) -- 5.2912)\^2 = 764).

**Data Inputs to the Formula**

Thus the data inputs to the tree yield formula are:

1.  *M*, the maximum aboveground biomass
2.  *r*, the species-multiplier of the maximum aboveground biomass
3.  *G*, the tree age of maximum growth
4.  *P*, the time-series of the forest productivity index
5.  *y*, the tree yield multiplier (which can be changed by type 2
    forest treatment events)
6.  The age advances specified by the type 1 forest treatment events.

On the [Departmental Server](219_Departmental%20Server.htm), *r* and *G*
are calculated from other inputs. See [Growth
Properties](42_Growth%20Properties.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 131. Yield and Net Primary Production 2016

**Yield and Net Primary Production**

Yield and net primary production are related concepts and you will need
to know how they are defined in order to understand plant growth in
FullCAM.

**Turnover**

A plant is normally "turning over" or shedding material, producing
"litterfall\" aboveground and "root slough" belowground.

**Net Primary Production**

The net increase in plant mass due to the addition of new plant material
is called the *net primary production* (NPP), which includes the effects
of both photosynthesis and respiration. net primary production is
difficult to measure due to the confounding effect of *turnover* (in
which all plant components except tree stems lose portions via
turnover), and is of interest mainly to people tracking tree physiology.

net primary production is due to the combined effects of photosynthesis
and respiration. The mass added by photosynthesis is called *gross
primary production* (GPP). It is photosynthesis that removes carbon from
the atmosphere and adds it to the plant. However, much of the GPP is
promptly lost (and carbon returned to the atmosphere) due to
respiration. In trees, net primary production is typically about half of
GPP. In FullCAM, net primary production is measured in tonnes per
hectare.

Thus, in normal growth, a plant is simultaneously adding to its mass by
the process of production (which adds net primary production to the
plant) and losing mass by the process of turnover (which loses material
from the plant).

**Yield**

Due to the turnover of plant components, when we measure the change in
component mass over a period of time we actually measure the *yield*,
which is the net primary production less the turnover. Yield is
relatively easy to measure and is of interest to anyone who measures
plant masses.

The yield of a plant is the net primary production produced less the
material shed by turnover: in any given period,

*Yield = Net Primary Production -- Turnover*.

**Use Net Primary Production or Yield?**

Net primary production is due to production, material-turned-over is due
to turnover, and yield is due to the combined effects of production and
turnover.

There are two fundamentally different ways of specifying or measuring
plant growth:

1.  By yield changes --- changes in yield with time.
2.  By net primary production flows --- amounts of net primary
    production added to the plant component.

In practice, the material-turned-over is hard to measure precisely
(because material moving to debris via turnover is quickly dispersed
into the environment), while yields are relatively easy to measure
precisely (just measures the plant mass).

The yield is what you get if you simply measure the mass of the
specified plant component(s), and a "mass increment" (or "yield
increment") is the difference in measurements of mass over the period of
the increment.

For example, if you measure the leaves of the trees of a forest as 20
tdm/ha on June 1 then the yield of the tree leaves on June 1 is 20
tdm/ha. If you then measure the leaves of the trees as 26 tdm/ha on
August 1, the mass increment of the tree leaves is 6 tdm/ha over those
two months. If your increment time-series contained monthly leaf mass
increments, then it might have 3 tdm/ha in June and another 3 tdm/ha in
July.

A net primary production flow to a tree or crop component in a given
period is the mass of net primary production that is added to the
component in the period.

For example, continuing the previous example, suppose that the trees
shed 1 tdm/ha of leaves during June and a further 2 tdm/ha of leaves in
July. Then the net primary production flowing to the leaves in June must
have been 4 tdm/ha (the leaf mass increment was 3 tdm/ha in June, which
included shedding 1 tdm/ha of leaves) and in July must have been 5
tdm/ha (3 tdm/ha net gain, including a 2 tdm/ha loss). If your increment
time-series contained monthly leaf net primary production flows, then it
would have 4 tdm/ha in June and another 5 tdm/ha in July.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 132. Data Builder 2016

**Data Builder**

\[*Data Builder* page of the input window of a plot document\]

Use the Data Builder to download data from the [Departmental
Server](219_Departmental%20Server.htm) into your plot document. For help
on the three panels on this page, see:

- [Downloading Spatial Data](207_Downloading%20Spatial%20Data.htm)
- [Downloading Trees and
  Events](208_Downloading%20Trees%20and%20Events.htm)
- [Downloading Crops and
  Events](2_Downloading%20Crops%20and%20Events.htm)

**Introduction**

The Data Builder allows you to easily build ready-to-run plots by
downloading the input data for your plot from the [Departmental
Server](219_Departmental%20Server.htm).

Although the Data Builder has been designed for ease of use, it is
"open" enough for experienced users to build complex systems. Take care
when downloading complex data or modifying downloaded data, or modelling
errors can result.

**Internet Connection to the FullCAM Server**

Using the Data Builder requires that your computer be connected to the
Internet. The Data Builder will automatically connect as required.

Check the *Data Builder on* box to acknowledge that you are connected to
the Internet and thus ready to proceed.

**Plot Configuration**

The Data Builder is only available for the multi-layer plot types (see
[Configure the Plot](6_Configure%20the%20Plot.htm)), namely multi-layer
forest systems, multi-layer agricultural systems, and mixed multi-layer
systems. Your choice of plot type will affect the species and regime
data offered for downloading. For example, [Regimes](235_Regimes.htm)
including a transition from pasture to plantation are not available for
a multi-layer forest system because a pasture is modelled by an
agricultural system.

**Download Tree and Crop Species Required by the Event Queue**

Downloading tree and crop regimes puts events on the
[Events](136_Events.htm) page but does not download the species
mentioned by those events. This button (the \"Download Events for This
Regime\" button) is only enabled if there are species required by the
event queue that have not been downloaded yet, and it downloads all of
those species at once. Pressing this button is often more convenient
than downloading the required species individually.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 135. Time-Series Window 2016

**Time-Series Window**

\[[Site : Water](12_Site_Water.htm) window : any *time-series* button\]\
\[[Site : Temperature](13_Site_Temperature.htm) window : any
*time-series* button\]\
\[[Site : Productivity](64_Site_Productivity.htm) window : any
*time-series* button\]\
\[[Growth Properties](42_Growth%20Properties.htm) window : any
*time-series* button\]\
\[[Plant Properties](43_Plant%20Properties.htm) window : any
*time-series* button\]\
\[[Soil Inputs](193_Soil%20Inputs.htm) window : any *time-series*
button\]\
\[[Crop Yields Table](113_Crop%20Yields%20Table.htm) window : any
*time-series* button\]

This window is for entering, editing, viewing, and exporting a
time-series.

This topic is displayed when you click the *Window* help icon in any
time-series window; when you press the *Data* help icon you open the
topic about that particular time-series.

**Time-Series Data**

A time-series is a sequence of numbers, one for each point in time,
spaced at regular intervals in time. For example, the 12 monthly
rainfalls for a year constitute a time-series.

In FullCAM, the data points in a year are assumed to be equally spaced
throughout the year. The exact way in which they are used depends on the
'Timing' and 'Amount of data' settings, as described below.

FullCAM will make the best possible use of the time-series data you
enter, regardless of the amount of time-series data and the number and
frequency of simulation steps. At the beginning of a simulation, FullCAM
interpolates and extrapolates the given time-series into a *full*
time-series, which consists of one data point per simulation step.

**Interpolation**

The interpolation is linear, between the nearest two given data points.

If there is any missing data in a time-series FullCAM interpolates the
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
interpolate data values \-- the time-series window will not be ready to
simulate, and the window button will be red.

*Timing \-- Start year, Years are*

The year that the time-series is to start from. \'Start year\' and
\'Years are\' together determine the years that the data in the
time-series table applies to.

**Example 1.** Calendar time

If \'Start year\' is 2006 and \'Years are\' is \'Calendar time\', then
the time-series data will be applied from 2006 onwards.

**Example 2.** Time since start of simulation

If \'Start year\' is 2007 and \'Years are\' is \'Time since start of
simulation\', then the time-series data will be applied from *2007 years
after the simulation start time*. It may be more appropriate to instead
set the \'Start Year\' to 0.

**Example 3.** Years since plants sprouted

If \'Start year\' is 2007 and \'Years are\' is \'Years since plants
sprouted\', then the time-series data will be applied from *2007 years
after the plant event*. It may be more appropriate to instead set the
\'Years are\' to 0.

It should be noted that if this option is selected, the time-series
headings are always entitled \'Data\'. This is the case even if there
are 12 Data points per year (in which case the column headings would be
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

Unless the time-series is a spatial input (see below), the time-series
data will be shown as a table of numbers.

Each row of the table has the data for one year. For example, if the
start year is 1962 and the years are calendar years, then the first row
in the table is for 1962, the next row for 1963, and so on.

You can cut, copy, and paste rectangular blocks of numbers from the
table (which allows you to transfer data to other programs, such as
Microsoft Excel). When pasting more than one number from the table at
the same time, you need only select the upper left cell of the
rectangular block you are pasting into (such as in Microsoft Excel) to
paste the entire selection.

**Amount of Data**

Change the size of the time-series data by entering values in the *Years
of data* and the *Data points per year* boxes. A change will take effect
when the insertion point leaves a box or the *Update Data Size* button
is clicked.

If the *Years are* value is set to \'Calendar time\' and *Data points
per year* (see below) is a multiple of 12, then data points will apply
to specific months. For example, if there are 12 data points for the
year then the first data point is for January, the next for February,
and so on. Similarly, if there are 24 data points for the year then the
first two data points are for the first and second halves of January,
the next two for February, and so on.

Change the size of the window, and thus the area available to the
visible part of the table, by dragging its lower right corner with the
mouse.

**Multiplier**

The *multiplier* simply multiplies every value in the table when FullCAM
uses the value in a simulation. If the multiplier is 1.0, then FullCAM
will use the values in the table. If the multiplier is 2.0, then FullCAM
will use 2.0 times the values in the table, and so on. The multiplier is
useful for quickly changing the whole time-series to see what would
happen if\...

**Risk Input**

The only part of a time-series that can be a risk input (that is, is
subject to change during a [Sensitivity
Analysis](160_Sensitivity%20Analysis.htm) is the multiplier. Thus an
analysis can scale the whole time-series by a random multiplier during
an analysis, but cannot change the ratios between pairs of data points
in the time-series.

If an analysis involving risk is turned on ([Configure Risk
Analysis](8_configure%20risk%20analysis.htm)), open the risk inputs
window for the time-series multiplier by pressing the F2 key or
double-clicking in the multiplier box.

The risk input is given the same name as the time-series (for example,
"Rainfall"), even though the risk input is the multiplier in the
time-series (for example, "Rainfall - time-series multiplier"). This is
to simplify naming procedures.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 136. Events 2016

**Events**

\[*Events* page of the input window of a plot document\]

This page shows the regimes and events that can occur during a
simulation.

Each simulation step consists of continuous processes (such as growth or
decomposition) punctuated by any events that occur during that step ---
see [Processes and Events](58_Processes%20and%20Events.htm).

**Regime and Event Queue**

The events are presented on the page in a list, one event per line.

To view or edit an individual event, open it in the [Event
Window](137_Event%20Window.htm) by double-clicking on it or selecting it
then pressing the *Edit* button. Click the list section headers to sort
the queue --- sort by *Year* to sort them by time, that is, to show the
events in chronological sequence.

The sequence of events that occur during the simulation is called the
*event queue*. If the list of events is sorted by time, then the
simulating events on the list, in the order presented, constitute the
event queue. In most circumstances the terms "event list" and "event
queue" are used interchangeably.

  Event Name     Description
  -------------- ----------------------------------------------------------------------------------
  Forest         Only affects the forest system, such as plant trees, forest fire
  Agricultural   Only affects the agricultural system, such as plant crops, harvest
  Mixed          Affects both the forest and agricultural systems, such as forest fraction change

**Populating the Event List**

Events are loaded into the Event List by one of three methods:

Using the "[Data Builder"](132_Data%20Builder.htm)

Cloning an existing item

Using the "New\..." button

**Editing Event Timing**

The timing of events can be edited using the [event order
editing](274_Editing%20Event%20List%20Order.htm) functions.

**Simulating Events**

An event is *simulating* if it will occur in a simulation. All events
are simulating, except:

- Events that occur outside the period of the simulation (too early or
  too late)
- Events that have been switched off (see [Event
  Timing](143_Event%20Timing.htm)). Events can be switched off on the
  [Event Window](137_Event%20Window.htm), or on the Events page by the
  secondary mouse button and selecting either *Simulate Events* or *Do
  Not Simulate Events*.

Non-simulating events have no effect on the simulation.

**Initial Conditions**

The initial conditions panel lists the [Initial
Trees](185_Initial%20Trees.htm) and [Initial
Crops](184_Initial%20Crops.htm) species names that are growing in the
system at the start of the simulation.

The [Initial Trees](185_Initial%20Trees.htm) is always displayed first.
If there are no initial tree or crop species growing at the start of the
simulation then `No trees` or `No crops` are displayed accordingly.

Due to screen width restrictions the species name(s) may be truncated.

**Event Colour-Coding**

The timing fields on the event list (*Year*, *Day*, *Step in Year*) are
colour-coded to indicate the method used to specify the time of the
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

Finally, the events you select with the mouse are coloured in the usual
highlight colour.

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
of all plants. Depending on their extent, thins, harvests and fires
might be clearing. Ploughs and herbicides are always clearing. Once a
system is cleared, it needs to be planted before there is any more plant
growth.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 137. Event Window 2016

**Event Window**

\[[Events](136_Events.htm) page : *New* or *Edit* button\]\
\[[Standard Events of a
Species](142_Standard%20Events%20of%20a%20Species.htm) window : *New* or
*Edit* button\]

This window is for viewing and editing an individual event. See

[Event Timing](143_Event%20Timing.htm)\
[Autoqueue](174_Autoqueue.htm)

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

- If you are modelling a forest, the forest events are available
  (written in green).
- If you are modelling an agricultural system, the agricultural events
  are available (yellow).
- If you are modelling a mixed plot, both forest and agricultural events
  are available (brown).

Only events that are possible with the current configuration and current
species inputs can be created or edited (if they are not possible then
they are also not shown in the *Events* page in the input window). Note
that:

- Forest treatments are possible if and only if [CAMFor](77_CAMFor.htm)
  is on and one or more tree species are using the tree yield formula.
- Forest irrigation change events are only possible if forest
  [RothC](114_RothC.htm) is on, or CAMFor is on and one of more tree
  species has debris whose breakdown is sensitive to temperature and
  rainfall.
- Agricultural irrigation change events are only possible if
  agricultural RothC is on, or CAMAg is on and one of more crop species
  has debris whose breakdown is sensitive to temperature and rainfall.
- The following events are only possible if they are used in preference
  to their corresponding time-series (see [Configure Event Or
  time-series](195_Configure%20Event%20Or%20time-series.htm)) :
  - Forest/Agricultural irrigation change
  - Forest/Agricultural manure-from-offsite change.

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 138. Configure Other Options 2016

**Configure Other Options**

\[[Configuration](150_Configuration.htm) page: *Other Options* panel\]

Assorted configuration options.

**Events or time-series**

See [Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 140. Thin 2016

**Thin**

\[[Event Window](137_Event%20Window.htm) : *Thin* panel\]

A thin event is where some or all of the forest is harvested.

**Introduction**

The agricultural counterpart of a thin is a [Harvest](153_Harvest.htm)
event

A thin is the only event that creates forest products, that is, takes
tree material offsite. See the [Product
Properties](47_Product%20Properties.htm) of each species.

**Affected Portion**

The *affected portion* is the fraction of the total forest area being
modelled in which the thin takes place. It is also the fraction of the
plot area that is thinned --- the proportion of an unspecified areas to
be reported on a per hectare basis. For most plantations this would
generally equate to the fraction of the proportion of trees that are
thinned.

**Clearing Thin**

For a thin to be clearing (that is, to clear the forest of trees), the
affected portion must be 100% and the destination percentages for each
pool must add to 100%.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 141. Models and Inputs Window 2016

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

*Plants (ex production)* is about modelling all the aspects of plants
other than production: partitioning of production to the various plant
components, turnover, thinning, harvesting, fire, and so on.

**Options Menu**

(The drop-down menu on the far left of the toolbar.)

**Show Values.** Show the current values in the document. If the value
belongs to a species, it shows the value in the species that is
currently chosen for editing (there may be multiple species). If the
value belongs to an event, the value shown comes from an arbitrarily
chosen event of that type. If there is no species or event or the value
is blank or the value is not a number or "On/Off", or if there is no
such value in that type of document, generally no value is shown.

**Show Programming Names.** The programming names are useful if you are
reading the FullCAM technical documentation or code. The configuration
is useful as a compact written reminder, especially if you copy the list
to put in another sort of document.

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

1.  **Copy** - Select all or part of the text in the usual manner and
    press control-C or use the mouse menu. This performs the usual copy,
    suitable for pasting into a word processor. Use an equi-spaced font,
    such as *Courier New*, in the word processor to preserve the exact
    layout of the list.
2.  **Spreadsheet Copy** - Press the *Copy All Text in Spreadsheet
    Format* button or use the mouse menu. This copies all of the text,
    using tabs to separate fields --- suitable for pasting into a
    spreadsheet.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 142. Standard Events of a Species 2016

**Standard Events**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Standard
Information for the Species* panel : *Events* button\]

Manage the standard events, for the current species ([Select a
Species](56_Select%20a%20Species.htm)).

The standard events are simply events which are made available for a
species for convenience. The standard events downloaded through
Databuilder are only available for convenience and may not be relevant
or applicable for the particular species of interest. The standard
events should not be confused with the event queue (on the
[Events](136_Events.htm) page). The event queue is the queue of events
that will be simulated during a plot simulation.

**Uses**

If you often use a particular event (such as a particular thinning or
harvest) on the *Events* page, you might want to store the event as a
standard event. Then, when you want another such event on the *Events*
page, you can load the input values from the standard event rather than
retyping them. Also, storing the events that are typical for a given
species is helpful when you give the species (as FullCAM data) to
others. This is just a convenience to save typing when creating events
on the event queue.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 143. Event Timing 2016

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

Enter the date in any unambiguous way, such as \"4 Sep 2010\", \"s4\",
\"au9 1999\", \"4s2000\", \"8/4/0\" or \"8.4.1999\", except that you
cannot use hyphens because they are interpreted as negative signs (for
example 8 4 -35 is 8 Apr -35).

2\. Calandar years and days since the start of the simulation\
Example: -10, 0, 2345.

A calendar year is from a date in one year to the same date in the next
year, and can contain either 365 or 366 days depending on leap years.
The number of days can also be huge. So if you mean the same date in two
years time, set the calendar years equal to two and the days to zero,
but if you mean exactly 730 days then set the calendar years to zero and
the days to 730.

Go back and forth between the date types to see how they compare -
changes in one are reflected in the other, that is, they both show the
same date.

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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 144. Forest Fire 2016

**Forest Fire**

\[[Event Window](137_Event%20Window.htm) : *Forest Fire* panel\]

Enter the inputs specific to a forest fire event.

**Affected Portion**

The affected portion is the fraction of the forest area being modelled
in which the fire takes place. It is typically the fraction of the plot
area that is burnt or partly burnt.

**Destination Percentages in the Affected Portion**

These destination percentages are applied to the portion of the forest
that is affected by the fire.

The tree material that is affected by the fire either goes to the
atmosphere, goes to the debris, or remains where it is. The debris and
mulch material either goes to the atmosphere, to the inert soil (as
charcoal), or remains where it is. The sum of the two destination
percentages for a single pool must, obviously, be less than or equal to
100%.

Material is moved from the trees to the debris after the amounts of
debris that move have been calculated (tree material cannot go
immediately to the inert soil as a result of a fire).

**Example**. The affected portion is 70%. The stem destination
percentages are 40 to the atmosphere and 10 to the debris --- for a
total stem destination percentage of 50. Then, of all the stem material
on the plot, in this fire 70% \* 40% = 28% goes to the atmosphere, 70%
\* 10% = 7% becomes deadwood, and the remaining (100% -- 70%) + 70% \*
(100% -- 50%) = 65% does not move (stays onsite).

Typically very little if any of the deep minerals will be lost to the
atmosphere, and only a small portion or none of the shallow minerals.

**Clearing Fire**

For a fire to be clearing (that is, to clear the forest of trees), the
affected portion must be 100% and the destination percentages for each
pool (the sum of the destination percentages to the atmosphere and to
the debris) must sum to 100%.

**Leaf Regrowth Percentage**

The leaf regrowth percentage is the percentage of the leaves lost in the
fire that grow back over the next year --- in addition to any other
(that is, regular) growth.

At any stage a tree has some growth potential stored within it that has
not yet been expressed. If a fire burns all the leaves off a tree then
the tree will use this stored growth potential to regrow some leaves so
that regular growth (that is, capturing energy via photosynthesis in the
leaves) can resume.

The leaf regrowth percentage multiplied by the mass of leaves lost in
the fire is added back to the trees, at a uniform rate over the next
year, in addition to any other growth (and regardless of any changes in
the [Forest Percentage](206_Forest%20Percentage.htm)). This ensures that
a forest that has lost all its leaves will continue to grow.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 145. Properties of the Species 2016

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

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 148. No Help Available 2016

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

## 149. Agricultural Fire 2016

**Agricultural Fire**

\[[Event Window](137_Event%20Window.htm) : *Agricultural Fire* panel\]

Enter the inputs specific to a agricultural fire event.

**Affected Portion**

The affected portion is the fraction of the agricultural system in which
the fire takes place. It is typically the fraction of the plot area that
is burnt or partly burnt.

**Destination Percentages in the Affected Portion**

These destination percentages are applied to the portion of the
agricultural system that is affected by the fire. GBF = grains, buds,
and fruit.

The crop material that is affected by the fire either moves to the
atmosphere, moves to the debris, or remains where it is. The debris and
mulch material either moves to the atmosphere, to the inert soil (as
charcoal), or remains where it is. The sum of the two destination
percentages for a single pool must be less than or equal to 100%.

Material is moved from the crop to the debris after the amounts of
debris that move have been calculated (crop material cannot go
immediately to the inert soil as a result of a fire).

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

For a fire to be clearing (that is, to clear the agricultural system
entirely of crop), the affected portion must be 100% and the destination
percentages for each pool (the sum of the destination percentages to the
atmosphere and to the debris) must sum to 100%.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 150. Configuration 2016

**Configuration**

\[*Configuration* page of the input window of a plot\]

This page is where you specify the configuration of your plot, that is,
choose which parts of the plot should be modelled. This topic describes
configuration issues in general terms; for more specifics see:

[Configure the Plot](6_Configure%20the%20Plot.htm)\
[Configure Tree Production](108_Configure%20Tree%20Production.htm)\
[Configure Risk Analysis](8_configure%20risk%20analysis.htm)\
[Configure Other Options](138_Configure%20Other%20Options.htm)

**About**

This window allows users to view a list of all inputs (click on the
\'Models and Inputs\'\... button) or a diagram showing all pools and
fluxes of C and N (click on the \'Diagrams\...\' button) for the model
configuration selected. Note that there is no capacity to model nitrogen
in this edition of FullCAM but the diagrams show the full theoretical
form of the model including nitrogen.

**Models and Inputs**

Clicking the \'Models and Inputs\' button brings up a new window which
lists a variety of information for the model configuration selected. The
level of detail of information presented in this window can be specified
using the \'Options\' button located at the far left of the menu bar for
this window. Additional menu bar buttons allow the user to copy and
select various components of the window, turn on word wrap if required,
export the information in the window to a text file, find text and view
help file.

Clicking the Options button and scrolling down to the \'Display\' menu
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
programming code for the variables in square brackets \[\] (e.g. Carbon
% of fine roots \[CFracFirtA\] = 38.4%). Programming names are useful if
you are reading and referring to the FullCAM Function Specification.

*Show configuration*: presents the user specified configuration for the
plot as the first item in the information displayed. If any
discrepancies exist between this list and the regular interface, the
regular interface is correct.

You can get help related to a specific input by placing the cursor in
the line in which the input is presented and clicking the \'Help for
Input on Selected Line\' button in the menu bar (Ctrl + i). General help
pertaining to this window can be obtained by clicking on the \'Help\'
button in the menu bar (F1)

**Configuration Determines Inputs**

The configuration you choose will affect which inputs are required. For
example, if you model a forest system only, then none of the
agricultural inputs will be required.

You might want to experiment with different configurations in order to
determine the most configuration that most suits your needs, given the
available inputs and your required outputs. To help in this process, for
each configuration you can see model diagrams ([Diagrams
Window](50_Diagrams%20Window.htm)) and a list of required inputs
([Models and Inputs Window](141_Models%20and%20Inputs%20Window.htm)).

**FullCAM Integrates Its Constituent Models**

The [Constituent Models In
FullCAM](198_Constituent%20Models%20In%20FullCAM.htm) models may be used
either independently or in combination. [CAMFor](77_CAMFor.htm) and
[CAMAg](78_CAMAg.htm) are multi-layer framework models, while
[RothC](114_RothC.htm) is a single-layer specialist model. FullCAM
allows you to run combinations of these models to simulate single or
multi-layer models (see [Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm)), as forest,
agricultural or mixed.

**Readiness**

When the *Configuration* page is unready (that is, incomplete --- as
when you create a new document):

- The writing on the tab of the page is red.
- Only the [About](11_About.htm), Configuration, and
  [Timing](199_Timing.htm) tabbed pages appear in the input window of
  the document.

When the *Configuration* page is ready (that is, complete):

- The writing on the tab of the page is black.
- If the *Timing* page is also ready then more than three tabbed pages
  appear in the input window. Exactly which pages appear depends on the
  configuration --- for example, the [Mulch](202_Mulch.htm) page only
  appears if mulch is modelled.

While all the input pages use the red or black tab to indicate
unreadiness (see [General Features](20_General%20Features.htm)), only
the *Configuration* page also controls which other tabbed pages appear
in the document input window.

**Simpler Is Usually Better**

The more layers and the more sophisticated features you choose in your
model, the more difficult it will be to find all the required input
data. We recommend:

- Only modelling those layers and simulating those elements that you
  need;
- Restrict model configurations to those for which data is available and
  for which the outputs are understandable.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
