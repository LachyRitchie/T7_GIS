---
version: 2016
batch_range: 201-250
batch_name: Estate_Management_Outputs
creation_date: 2025-08-28
total_files: 27
---

# FullCAM 2016 - Batch 201-250: Estate Management Outputs

## Table of Contents

- [201. Plants 2016](#201-plants-2016)
- [202. Mulch 2016](#202-mulch-2016)
- [203. Soil 2016](#203-soil-2016)
- [205. Initial Conditions 2016](#205-initial-conditions-2016)
- [206. Forest Percentage 2016](#206-forest-percentage-2016)
- [207. Downloading Spatial Data 2016](#207-downloading-spatial-data-2016)
- [208. Downloading Trees and Events 2016](#208-downloading-trees-and-events-2016)
- [215. Trees 2016](#215-trees-2016)
- [216. Crops 2016](#216-crops-2016)
- [217. Main Window 2016](#217-main-window-2016)
- [218. Risk analysis 2016](#218-risk-analysis-2016)
- [219. Departmental Server 2016](#219-departmental-server-2016)
- [223. Species or Regime Selection Text Match Filter 2016](#223-species-or-regime-selection-text-match-filter-2016)
- [224. Species or Regime Selection Tree or Crop Species Filter 2016](#224-species-or-regime-selection-tree-or-crop-species-filter-2016)
- [225. Species or Regime Selection 2016](#225-species-or-regime-selection-2016)
- [226. Species or Regime Selection Forest or Agricultural Regime Filter 2016](#226-species-or-regime-selection-forest-or-agricultural-regime-filter-2016)
- [228. Pasture to Plantation Forest 2016](#228-pasture-to-plantation-forest-2016)
- [229. Plantation Forest to Plantation Forest 2016](#229-plantation-forest-to-plantation-forest-2016)
- [230. Native Forest to Plantation Forest 2016](#230-native-forest-to-plantation-forest-2016)
- [231. Native Forest to Pasture 2016](#231-native-forest-to-pasture-2016)
- [232. Grazed Woodland 2016](#232-grazed-woodland-2016)
- [233. Crop and Pasture Management 2016](#233-crop-and-pasture-management-2016)
- [234. Explorer 2016](#234-explorer-2016)
- [235. Regimes 2016](#235-regimes-2016)
- [243. Generate Plot Files 2016](#243-generate-plot-files-2016)
- [247. Proxy Settings 2016](#247-proxy-settings-2016)
- [248. Event Update 2016](#248-event-update-2016)

---

## 201. Plants 2016

**Plants**

\[*Trees* page or *Crops* page in the input window of a plot document\]

These two pages, the [Trees](215_Trees.htm) page and the
[Crops](216_Crops.htm) page, are where you describe the species on the
plot. They are each partitioned into three panels:

- [Select a Species](56_Select%20a%20Species.htm) panel
- [Properties of the Species](145_Properties%20of%20the%20Species.htm)
  panel

**About Species**

Clearing events, such as a [Thin](140_Thin.htm),
[Harvest](153_Harvest.htm), [Forest Fire](144_Forest%20Fire.htm), or
[Agricultural Fire](149_Agricultural%20Fire.htm), can remove the plants
if there are plants growing.

If there are no plants growing (that is, the system is clear), then
planting events, namely [Plant Trees](158_Plant%20Trees.htm) or [Plant
Crop](161_Plant%20Crop.htm), can set plants growing on the plot. A
planting event can plant any species listed on this panel.

By clearing one species then planting a different species, a plot can
have several different species growing during the plot simulation - but
only one species growing in a system at any one time.

The debris and products of each species are tracked separately, because
they have characteristics that may differ from species to species.
However, all species are treated the same with respect to the mulch and
soil - different species merely have different proportions of
decomposable or resistant material, and different proportions of
\"more-resistant\" material in the resistant material.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 202. Mulch 2016

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

## 203. Soil 2016

**Soil**

\[*Soil* page of the input window of a plot document\]

Enter inputs that describe the organic soil on the plot. This page is
partitioned into several windows:

- [Soil Inputs](193_Soil%20Inputs.htm)
- [Soil Properties](3_Soil%20Properties.htm)
- [Soil Water](44_Soil%20Water.htm)
- [Soil Cover](102_Soil%20Cover.htm)
- [Soil for the Whole Plot](46_Soil%20for%20the%20Whole%20Plot.htm)

The soil is always modelled exclusively by the [RothC](114_RothC.htm)
model.

**Active vs. Inert**

Soil is either active or inert.

- *Active soil* is soil in which the carbon is accessible by microbes
  and so on, and is thus available to normal soil processes and thus
  return to the atmosphere.
- *Inert soil* is soil in which the carbon is inaccessible for return to
  the atmosphere, either physically (for example, the inert soil is
  surrounded by clay) or chemically (for example, in charcoal). Inert
  soil carbon may eventually react with oxygen and return to the
  atmosphere if it becomes non-inert, such as if ploughing breaks up the
  clay particles.

[RothC](114_RothC.htm) is always used to model the active soil; only
[CAMFor](77_CAMFor.htm) and [CAMAg](78_CAMAg.htm) model the inert soil.

**Other Soil Inputs**

Some soil related inputs are entered in the [Soil Fertility
Rating](90_Soil%20Fertility%20Rating.htm) and [Soil Nutrition
Modifier](181_Soil%20Nutrition%20Modifier.htm) time-series, on the
[Site](200_Site.htm) window.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 205. Initial Conditions 2016

**Initial Conditions**

\[*Initial Conditions* page of the input window of a plot\]

Enter inputs that describe the situation on the plot at the beginning of
the simulation. It is partitioned into several windows and a panel:

- [Initial Trees](185_Initial%20Trees.htm)
- [Initial Crops](184_Initial%20Crops.htm)
- [Initial Debris](31_Initial%20Debris.htm)
- [Initial Products](33_Initial%20Products.htm)
- [Initial Soil](32_Initial%20Soil.htm)
- [Initial Conditions For the Whole
  Plot](197_Initial%20Conditions%20For%20the%20Whole%20Plot.htm)

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 206. Forest Percentage 2016

**Forest Percentage**

The forest percentage specifies the mix of forest and agricultural
systems within a mixed plot (see [Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm) and [Configure
the Plot](6_Configure%20the%20Plot.htm)).

**Introduction**

The concept of the "forest percentage" arises only in a mixed
multi-layer plot. A mixed multi-layer plot has a multi-layer forest
system and a multi-layer agricultural system. The relative mix of the
two systems is expressed as the forest percentage --- the forest
percentage is the means of saying how much of the plot is covered by
forest, and the rest is agricultural. For example, if the forest
percentage is 30% then the agricultural percentage is 70%.

**Definition**

The *forest percentage* is defined as the percentage of the plot covered
by the tree canopy.

For example, a plot with 10 ha of forest and 30 ha of agricultural
system has a forest percentage of 25% (because 10 / 40 = 25% of the plot
is forest).

**Discussion**

The forest percentage is the percentage of the sunlight going to the
trees. In the plot simulator, if the forest fraction (100 times the
forest percentage) is *f* then:

- Tree production (growth) is *f* times what it would be if the plot
  were a forest plot.
- Crop production (growth) is (1 -- *f* ) times what it would be if the
  plot were wholly agricultural.

Thus the forest percentage partitions the total production in the two
systems (forest and agricultural).

For example, suppose a mixed plot has the forest fraction equal to 30%.
Then the forest growth is 30% of what it would be if the whole plot were
forest, and the agricultural growth is 70% of what it would be if the
whole plot were agricultural. No non-growth processes are affected by
the forest percentage.

The forest percentage can vary with time in response to events (see
[Forest Percentage Change](116_Forest%20Percentage%20Change.htm)).

Forest percentage change events are typically connected to land clearing
or revegetation. For example, clearing all of a mixed plot that is all
forest and planting a crop on all the land changes the forest percentage
of the plot from 100% to 0%.

Notice that the definition and the use of the forest percentage by the
plot simulator (which is **effectively** the definition of forest
percentage in the model) do not necessarily agree. This can lead to some
traps for the unwary modeller, because it is up to you to ensure that
they do agree at all times. For example, you could use a forest
percentage change event on a plot with trees to change from 100% to 10%.
The plot simulator now gives the trees only 10% of the plot production,
and potentially 90% of the plot production goes to any crop, so unless
the forest percentage change was accompanied by a thin event this would
not make any sense. Even worse, if the trees on the plot were near their
biomass limit before the forest percentage change then they would be
grossly over the biomass limit after the change (because the biomass
limit is a product of the maximum biomass per hectare and the forest
fraction) and so most of the forest would instantly turn to debris in
the model!

The amount of carbon in the forest trees, debris, soil, and products is
not affected by the forest percentage, so changing the forest percentage
does not change these. Even changing the forest percentage from 100% to
0% does not affect the forest soil or the forest products.

There is one exception to the above: The growth determined by the [Tree
Yield Formula](130_Tree%20Yield%20Formula.htm) is not affected by the
forest percentage: the tree growth is always exactly as specified by the
tree yield formula, regardless of the forest percentage. This exception
is because the tree yield formula predicts tree growth as linked to a
site\'s ability to grow trees, and is already limited by the potential
to achieve different levels of canopy cover.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 207. Downloading Spatial Data 2016

**Downloading Spatial Data**

\[[Data Builder](132_Data%20Builder.htm) page : *Spatial Data* panel\]

This panel is for downloading data that is specific to a location, using
Data Builder.

**Inputs**

Specify the plot's location by entering its [Latitude and
Longitude](180_Latitude%20and%20Longitude.htm). The default latitude and
longitude is for Uluru.

The *forest percentage for downloading* is the [Forest
Percentage](206_Forest%20Percentage.htm) used by the Data Builder to
determine what data to download. It is used to set the initial masses in
proportion between the forest and agricultural systems, and it becomes
the [Initial Conditions For the Whole
Plot](197_Initial%20Conditions%20For%20the%20Whole%20Plot.htm) value. It
has no direct effect on any simulation of this plot. For modelling
systems transitioning from pasture to plantation, the initial forest
percentage for downloading should be set to 0.

When you download a species and set it as the initial species, the value
of the forest percentage for downloading is used to compute the initial
masses of the species. So if you later change the forest percentage for
downloading, you will have to reset the initial species --- at which
point it is easiest to start a new plot and start over.

The start month simply reports the first month of the simulation, as per
the [Timing](199_Timing.htm) page. It is used to decide which initial
soil water level (topsoil moisture deficit, TSMD --- see [Initial
Soil](32_Initial%20Soil.htm)) to download.

**Download**

Press the *Download Spatial Data* button to download the location
specific data.

The Data Builder will download data for any point for which data is
available. The FullCAM Server has spatial data based on grids of varying
resolution --- from 250m to 1km. At these scales, many site specific
features which logically prevent tree and crop growth will be missed.
For example, the Data Builder will allow you to grow crops on major
roads, in minor rivers, and even on the top of Uluru. No tenure data is
known to the FullCAM Server.

You might receive an error message stating that the FullCAM Server was
unable to find some data. This usually occurs because the FullCAM Server
thinks that the plot is located in a large body of water, and the
missing data is typically for the soil. If the plot is within 100m of a
large water body such as the coast , the FullCAM Server is usually
unable to locate data. Try moving the plot away from the water body by
adjusting the [Latitude and
Longitude](180_Latitude%20and%20Longitude.htm) and try again.

**Soils**

The *regional soils* list contains the range of soil types known to
exist in the state and IBRA region. The soil type for which data has
been downloaded is displayed to the right of the *Download Spatial Data*
button.

Downloading another soil type (*Download Soil* button) discards the
previous soil data and replaces it with the new soil data. This will
also update the crop species list.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 208. Downloading Trees and Events 2016

**Downloading Trees and Events**

\[[Data Builder](132_Data%20Builder.htm) page : *Trees and Events*
panel\]

This panel is for downloading tree species and forest event data, using
Data Builder.

**Basic Operation**

1.  Select a tree-species group from the upper list, and press the
    *Download List of Tree-Species/Regimes for This Species-Group*
    button. This just updates the lower list.
2.  Select a species/regime from the lower list and press the *Download
    Events for This Regime* button. This puts the events for the
    selected species/regime onto the events list on the
    [Events](136_Events.htm) page.
3.  While still with the same species/regime selection on the lower
    list, press the *Download This Species* button. This will download
    the species information for the selected species/regime to the list
    of tree species on the [Trees](215_Trees.htm) page.

As an alternative to step 3, just be sure to press the *Download Tree
and Crop Species Required by the Event Queue* button (at the bottom of
the Data Builder page) before trying to run a simulation. See [Data
Builder](132_Data%20Builder.htm) for details.

**Details**

A tree regime and the tree species planted in that regime have the same
name. The regime names reflect the type of management applied to the
species.

When downloading a species, the Data Builder will ask if you wish make
the species the initial species. We recommend you select "Yes", unless
you wish to apply a different species as the initial species. Selecting
"Yes" does not necessarily mean that the species exists at the start of
the simulation, only that the initial conditions for the forest (mainly
the debris) will be set using that species.

The forest portion of the plot should now be ready to simulate (so the
*Trees* tab should not be red, and the buttons in the *Forest* panel of
the *Initial Conditions* page will not be red).

You can download subsequent [Regimes](235_Regimes.htm) after the first
forest regime. After downloading the first forest regime, the list of
tree-species/regimes available for download is updated to include only
those that are applicable for second and subsequent rotations. Forest
regimes which start from pasture or native forest will not be available
after the first regime is downloaded, because it is expected that you
will be moving from a plantation to another plantation. You can select
different species groups (for example, move from Pinus radiata to
Eucalyptus globulus) and apply different establishment techniques within
each species.

If you make a mistake in building the forest event queues, click the
*Clear Forest Events* button to clear all the events downloaded as part
of the [Regimes](235_Regimes.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 215. Trees 2016

**Trees**

\[*Trees* page in the input window of a plot document\]

Describe the tree species. This page is very similar to the
[Crops](216_Crops.htm) page, so we describe both pages together --- see
[Plants](201_Plants.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 216. Crops 2016

**Crops**

\[*Crops* page in the input window of a plot document\]

Describe the crop species. This page is very similar to the
[Trees](215_Trees.htm) page, so we describe both pages together --- see
[Plants](201_Plants.htm).

GBF = Grains, buds, and fruit

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 217. Main Window 2016

**Main Window**

This window is the thin window across the top of your screen with a menu
and toolbar, entitled "FullCAM X.X", where X.X is the version number of
the FullCAM program.

The main window is open whenever FullCAM is open. It is the window
called "FullCAM" in the Windows Taskbar down at the bottom of the
screen. Individual FullCAM documents or windows do not get their own
buttons on the Windows Taskbar.

If you close the main window (by clicking its close box) then you exit
FullCAM.

The main window contains the only fixed menus.

You cannot resize the main window. Although you can move it, we
recommend you always leave it in its original position.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 218. Risk analysis 2016

**Risk Analysis**

This topic explains some general aspects of risk analysis in FullCAM.

Performing risk analysis in FullCAM requires use of the \@Risk software
product (refer to the [\@Risk](271_At%20Risk.htm) help page for further
information).

**Introduction**

*Risk analysis* is where you replace the single value of an input by a
probability distribution. That is, in risk analysis we consider the
value of some inputs to be probability distributions instead of single
numbers. See risk input, below.

Risk analysis is useful for exploring the effects of uncertainty in our
inputs. For example, in a regular plot simulation the value of the clay
fraction of the soil might be 13%. But what effect does it have on the
simulation if all we know about the clay fraction is that it is between
10% and 20% and most likely around 13%?

The type of risk analysis performed in FullCAM is 'sensitivity analysis'
and is performed only on plot documents.

[Sensitivity Analysis](160_Sensitivity%20Analysis.htm) estimates how
sensitive an output is to each input. Used to explore the range of
probable outputs, given uncertainty in the inputs.

Risk analysis needs to be turned on in the configuration --- see
[Configure Risk Analysis](8_configure%20risk%20analysis.htm). All the
risk inputs can be viewed at once on the [Risk
Inputs](159_Risk%20Inputs.htm) page.

**Risk Inputs**

A *risk input* is a FullCAM input with risk properties attached to it.
Those properties are:

- A probability distribution
- Correlations with other risk inputs
- An on/off switch.

See the [Risk Properties of an
Input](182_Risk%20Properties%20of%20an%20Input.htm) window.

Almost any FullCAM input that is a single number can be a risk input
(others, such as the start time for the simulation, are too intrinsic to
the simulation to be allowed to vary during a risk analysis). Each
time-series has a multiplier that can be a risk input. Typically you
will want to focus on only a small number of risk inputs at once,
because the risk analysis slows down with each risk input added.

To create a risk input for a given plot input:

1.  Ensure that the plot is configured for risk analysis --- [Configure
    Risk Analysis](8_configure%20risk%20analysis.htm).
2.  Select the field where you would normally enter the input (so that
    if you pressed a key it would write into the field).
3.  Press the F6 key which will cause the [Risk Properties of an
    Input](182_Risk%20Properties%20of%20an%20Input.htm) window to open.
4.  Fill out the properties and close the window.

The input now appears in the plot window as per normal, but with a
yellow background to signal that it is also a risk input (the yellow is
faded when it has been switched off; the yellow is overridden by red if
the regular value of the input is invalid). The input continues to use
its normal single value in plot simulations, regardless of its risk
properties.

The current risk inputs in a document are listed in the [Risk
Inputs](159_Risk%20Inputs.htm) page.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 219. Departmental Server 2016

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

## 223. Species or Regime Selection Text Match Filter 2016

**Species or Regime Selection : Text Match Filter**

\[[Species or Regime
Selection](225_Species%20or%20Regime%20Selection.htm) : *Text match
filter* panel\]

Input text to filter the tree or crop species, or alternatively the
forest or agricultural regime list displayed.

**Details**

A text filter maybe used to filter a regime or species list. The text
filter to be applied is a single block of text, and can be a whole or
part word(s).

The text match filter is applied in conjunction with either the [Species
or Regime Selection : Tree or Crop Species
Filter](224_Species%20or%20Regime%20Selection_Tree%20or%20Crop%20Species%20Filter.htm),
or the [Species or Regime Selection : Forest or Agricultural Regime
Filter](226_Species%20or%20Regime%20Selection_Forest%20or%20Agricultural%20Regime%20Filter.htm)
(depending on the search window invoked).

If the text filter field is blank then no text filter is applied to the
list.

The text filter is *not* case sensitive.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 224. Species or Regime Selection Tree or Crop Species Filter 2016

**Species or Regime Selection : Tree or Crop Species Filter**

\[[Species or Regime
Selection](225_Species%20or%20Regime%20Selection.htm) : *Tree or Crop
species filter* panel\]

Select tree or crop species specific filters to filter the tree or crop
species list displayed.

**Details**

A tree or crop species filter may be used to filter a tree or crop
species list.

**Tree species filter**

Tree species may be filtered by any combination of tree species group,
in use status or species in group.

**Crop species filter**

Crop species may be filtered by their in use status.

The in use status for a tree or crop species is detailed in the [Select
a Species](56_Select%20a%20Species.htm) help page.

The Tree or Crop species filter is applied in conjunction with the
[Species or Regime Selection : Text Match
Filter](223_Species%20or%20Regime%20Selection_Text%20Match%20Filter.htm)
to display Tree or Crop species in the list.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 225. Species or Regime Selection 2016

**Species or Regime Selection**

\[[Data Builder](132_Data%20Builder.htm) page : *Trees and Events*
panel\]

This window is displayed when the tree or crop species search, or the
forest or agricultural regime search buttons are pressed.

**Details**

Species and regimes are selected by the Species or Regime selection
windows.

Filters may be used to restrict the number of entries in the list
displayed. Filters that may be used are:

[Species or Regime Selection : Text Match
Filter](223_Species%20or%20Regime%20Selection_Text%20Match%20Filter.htm)\
[Species or Regime Selection : Tree or Crop Species
Filter](224_Species%20or%20Regime%20Selection_Tree%20or%20Crop%20Species%20Filter.htm)\
[Species or Regime Selection : Forest or Agricultural Regime
Filter](226_Species%20or%20Regime%20Selection_Forest%20or%20Agricultural%20Regime%20Filter.htm)

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 226. Species or Regime Selection Forest or Agricultural Regime Filter 2016

**Species or Regime Selection : Forest or Agricultural Regime Filter**

\[[Species or Regime
Selection](225_Species%20or%20Regime%20Selection.htm) : *Forest or
Agricultrual regime filter* panel\]

Select forest or agricultural regime specific filters to filter the
forest or agricultural regimes list displayed.

**Details**

A forest or agricultural regime filter may be used to filter a forest or
agricultural regime list.

**Forest regime filter**

[Regimes](235_Regimes.htm) may be filtered by any combination of:

*State\
Previous land use\
Site preparation\
Post planting weed control\
NPI\
Cultivation\
Thinning Pruning*

If the [Species or Regime
Selection](225_Species%20or%20Regime%20Selection.htm) window has been
accessed from the [Data Builder](132_Data%20Builder.htm) page, then the
State and NPI filters are disabled as the list has already been filtered
by State and NPI region.

**Agricultural regime filter**

Agricultural regimes may be filtered by the Configuration option that
they apply to.

The forest or agricultural regime filter is applied in conjunction with
the [Species or Regime Selection : Text Match
Filter](223_Species%20or%20Regime%20Selection_Text%20Match%20Filter.htm)
to display forest or agricultural regimes in the list.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 228. Pasture to Plantation Forest 2016

Pasture to Plantation Forest

Details

Pasture to plantation forest management systems are created in FullCAM
by using a plot type of *Multi-layer mixed system*.

Other systems that may be created by FullCAM are:

[Plantation Forest to Plantation
Forest](229_Plantation%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Plantation
Forest](230_Native%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Pasture](231_Native%20Forest%20to%20Pasture.htm)\
[Grazed Woodland](232_Grazed%20Woodland.htm)\
[Crop and Pasture Management](233_Crop%20and%20Pasture%20Management.htm)

**Method**

*Configuration*

- Plot Type : Multi-layer mixed system.

*Timing*

- Set the timing. The *Start simulation at beginning of* year should be
  set to 20 years prior to plantation establishment.

It is always prudent to \'run the model in\' by setting the start year
earlier (up to 20 years) than the actual period of interest. This is
because the soil carbon data at initialisation represents a pristine
condition, a condition that does not reflect any prior management.

*Databuilder*

- Set the *Forest percentage for downloading* to 0.\
  Select the required *Trees and Events* (refer [Downloading Trees and
  Events](208_Downloading%20Trees%20and%20Events.htm)).
- Select an initial rotation *Tree-species/Regimes.* The initial list
  displayed will be ex-pasture plantation *Tree-species/Regimes* only.
- Select a subsequent rotation *Tree-species/Regimes.* Subsequent lists
  displayed will be subsequent rotation plantation
  *Tree-species/Regimes* only.

Subsequent rotation *Tree-species/Regimes* may be selected and
downloaded as often as required. Additional *Tree-species/Regimes* can
be added either within the same *Tree-species groups* or from other
groups to model transitions from one plantation species to another.

Select the required *Crops and Events* (refer [Downloading Crops and
Events](2_Downloading%20Crops%20and%20Events.htm)).

- Select *Download Tree and Crop Species Required By the Event Queue*.
  This will add crop species *Agriculture plantation weed species* and
  also relevant events.

The plot should now be ready to simulate. There is no need to
specifically download any crop information from *Crops and Events*.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 229. Plantation Forest to Plantation Forest 2016

Plantation Forest to Plantation Forest

Details

Plantation forest to plantation forest management systems are created in
FullCAM by using a plot type of *Multi-layer forest system*.

Other systems that may be created by FullCAM are:

[Pasture to Plantation
Forest](228_Pasture%20to%20Plantation%20Forest.htm)\
[Native Forest to Plantation
Forest](230_Native%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Pasture](231_Native%20Forest%20to%20Pasture.htm)\
[Grazed Woodland](232_Grazed%20Woodland.htm)\
[Crop and Pasture Management](233_Crop%20and%20Pasture%20Management.htm)

**Method**

*Configuration*

- Plot Type : Multi-layer forest system.

*Databuilder*

Select the required *Trees and Events* (refer [Downloading Trees and
Events](208_Downloading%20Trees%20and%20Events.htm)).

- Select an initial rotation *Tree-species/Regimes.* The initial list
  displayed will be initial rotation plantation *Tree-species/Regimes*
  only.
- Select a subsequent rotation *Tree-species/Regimes.* Subsequent lists
  displayed will be subsequent rotation plantation
  *Tree-species/Regimes* only.

Subsequent rotation *Tree-species/Regimes* may be selected and
downloaded as often as required. Additional *Tree-species/Regimes* can
be added either within the same *Tree-species groups* or from other
groups to model transitions from one plantation species to another.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 230. Native Forest to Plantation Forest 2016

Native Forest to Plantation Forest

Details

Native forest to plantation forest management systems are created in
FullCAM by using a plot type of *Multi-layer forest system*.

Other systems that may be created by FullCAM are:

[Pasture to Plantation
Forest](228_Pasture%20to%20Plantation%20Forest.htm)\
[Plantation Forest to Plantation
Forest](229_Plantation%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Pasture](231_Native%20Forest%20to%20Pasture.htm)\
[Grazed Woodland](232_Grazed%20Woodland.htm)\
[Crop and Pasture Management](233_Crop%20and%20Pasture%20Management.htm)

**Method**

*Configuration*

- Plot Type : Multi-layer forest system.

*Databuilder*

Select the required *Trees and Events* (refer [Downloading Trees and
Events](208_Downloading%20Trees%20and%20Events.htm)).

- Select Tree species group *Local species*.
- Select an initial rotation *Tree-species/Regimes.* The initial list
  displayed will be *Local species* only.
- Select a subsequent rotation *Tree-species/Regimes.* This will require
  you to select another Tree species group value. Subsequent lists
  displayed will be plantation *Tree-species/Regimes* only.

Subsequent rotation *Tree-species/Regimes* may be selected and
downloaded as often as required. Additional *Tree-species/Regimes* can
be added either within the same *Tree-species groups* or from other
groups to model transitions from one plantation species to another.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 231. Native Forest to Pasture 2016

Native Forest to Pasture

Details

Native forest to pasture management systems are created in FullCAM by
using a plot type of *Multi-layer mixed system*.

Other systems that may be created by FullCAM are:

[Pasture to Plantation
Forest](228_Pasture%20to%20Plantation%20Forest.htm)\
[Plantation Forest to Plantation
Forest](229_Plantation%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Plantation
Forest](230_Native%20Forest%20to%20Plantation%20Forest.htm)\
[Grazed Woodland](232_Grazed%20Woodland.htm)\
[Crop and Pasture Management](233_Crop%20and%20Pasture%20Management.htm)

**Method**

*Configuration*

- Plot Type : Multi-layer mixed system.

*Databuilder*

- Set the *Forest percentage for downloading* to the initial tree crown
  canopy cover.\
  Select the required *Trees and Events* (refer [Downloading Trees and
  Events](208_Downloading%20Trees%20and%20Events.htm)).
- Select Tree species group *Native Forest Groups*.\
  Select the required *Crops and Events* (refer [Downloading Crops and
  Events](2_Downloading%20Crops%20and%20Events.htm)).
- Select a pasture species that will replace the native forest.
- Select an appropriate pasture regime. This regime will cycle through
  time.

*Events*

To clear the forest, [Thin](140_Thin.htm) and [Forest Percentage
Change](116_Forest%20Percentage%20Change.htm) events must be created.

A [Thin](140_Thin.htm) event is created to clear the trees.

- Select *New\...*
- Set the *Type* drop down list value to *Thin*.
- Enter the *Timing* details of the clearing.
- Select *Insert Standard Values*.
- Select a standard event. This will populate all values for the *Thin*
  event.
- Enter an event name, or alternatively select the *Autoname* button.
- Select *OK*. The event will now be stored on the
  [Events](136_Events.htm) page*.*

A [Forest Percentage Change](116_Forest%20Percentage%20Change.htm) event
is created by repeating the previous procedure with the following
exceptions:

- Set the *Type* to *Forest Percentage Change*.
- Set the *Timing* details to 1 day after the clearing *Thin* event.

If you wish to burn the debris, repeat the previous procedure and set
the *Type* to [Forest Fire](144_Forest%20Fire.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 232. Grazed Woodland 2016

Grazed Woodland

Details

Grazed woodland systems are created in FullCAM by using a plot type of
*Multi-layer mixed system*.

Other systems that may be created by FullCAM are:

[Pasture to Plantation
Forest](228_Pasture%20to%20Plantation%20Forest.htm)\
[Plantation Forest to Plantation
Forest](229_Plantation%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Plantation
Forest](230_Native%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Pasture](231_Native%20Forest%20to%20Pasture.htm)\
[Crop and Pasture Management](233_Crop%20and%20Pasture%20Management.htm)

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 233. Crop and Pasture Management 2016

Crop and Pasture Management

Details

Crop and pasture management systems are created in FullCAM by using a
plot type of *Multi-layer agricultural system*.

Other systems that may be created by FullCAM are:

[Pasture to Plantation
Forest](228_Pasture%20to%20Plantation%20Forest.htm)\
[Plantation Forest to Plantation
Forest](229_Plantation%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Plantation
Forest](230_Native%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Pasture](231_Native%20Forest%20to%20Pasture.htm)\
[Grazed Woodland](232_Grazed%20Woodland.htm)

**Method**

*Configuration*

- Plot Type : Multi-layer agricultural system.

*Databuilder*

Select the required *Crops and Events* (refer [Downloading Crops and
Events](2_Downloading%20Crops%20and%20Events.htm)).

- Select a crop species.
- Select an appropriate crop species regime. This regime will cycle
  through time.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 234. Explorer 2016

**Explorer**

\[*Explorer* page of the input window of a plot document\]

This page shows inputs required by the current configuration showing
names, programming names and values for FullCAM inputs.

The values are the current values in the document. If the value is blank
or the value is not a number or \"On/Off\", or if there is no such value
in that type of document, generally no value is shown. It is possible
that some inputs will be shown that are not required because of other
(non-configuration) settings - for example, in a forest configuration
the tree mortality inputs will be shown as required regardless of
whether or not the *Tree mortality on* box is checked on the [Plant
Properties](43_Plant%20Properties.htm) window for any species.

The programming names are useful if you are reading the FullCAM
technical documentation.

**Use**

The Window can be used as an alternate view of a document to get the
feel for the data required for a simulation and to allow browsing of all
the values of the document. Drag and drop functionality is also provided
to external application such as Microsoft Word and Excel to provide the
export of document data.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 235. Regimes 2016

**Regimes**

\[[Data Builder](132_Data%20Builder.htm) page : *Trees and Events*
panel\]

**Introduction**

The regime names aim to describe the types of management practices that
will occur at a location. The regimes are species, location and time
specific, being based on either National Plantation Inventory region or
State.

The following text and table describes the regime names in the order
they appear in the regime name. If more detailed information on a regime
is required, or if the name is not exactly clear, place the mouse over
the regime name. This will lead to a text box appearing with a more
detailed description of the regime.

**National Plantation Inventory Region or State**

This indicates the area in which the management system applies. The Data
Builder automatically filters the available regimes for a species based
on location. This field simply indicates that you are in the correct
area. If the point falls within an NPI region, then this is reported,
otherwise the regimes are filtered on a state basis

  Code         Description
  ------------ ------------------------
  Bomb/EG      Bombala/East Gippsland
  CentGipp     Central Gippsland
  CentTab      Central Tablelands
  CentVic      Central Victoria
  GrnTri       Green Triangle
  Lofty        Lofty Block
  MurrayVall   Murray Valley
  NthCst       North Coast
  NthQld       Northern Queensland
  NthTab       Northern Tablelands
  SEQld        South East Queensland
  SthTab       Southern Tablelands
  Tas          Tasmania

**Previous Land Use**

The initial conditions of a site and the site establishment techniques
employed vary depending on the previous land use. The previous land use
indicates the land use at the start of the simulation. For example, a
previous land use of pasture means that the land use prior to
establishing the forest was pasture. The \'plantation\' previous land
use is used to build multiple rotations and hence is only available
after downloading an initial regime.

  Code         Description
  ------------ --------------------------------------
  InitPlant    Plantation at start of simulation
  LocalSpp     Local species at start of simulation
  NativeFor    Native forest at start of simulation
  Pasture      Pasture at start of simulation
  Plantation   2nd rotation plantation

**Site Productivity Estimate**

A broad estimate of how productive the site is for a certain region.
This generally determines factors such as timing of events and rotation
length. Regimes with "recommended" after them are those that fit with
the site productivity assessment of the National Carbon Accounting
System.

If you feel that your site quality is much higher (ie deep fertile river
flat with access to groundwater) or lower (rocky outcrops or badly
degraded land) than reflected in the national account, you may select
other options to suit your conditions. When doing this you may also need
to adjust some other parameters in the model.

**Timing**

Gives the year range in which the management practices were applied.
Management systems have varied considerably over the years as increased
knowledge has lead to significant advances in plantation establishment
and management.

The year range indicates the type of management that was common during
that time period.

**Site Preparation**

Gives a description of the site preparation methods. These will vary
with location, time and previous land-use. For example, StripWC means a
strip weed control prior to planting, as is common in ex-pasture
systems. BroadBurn indicates a broadcast burn, as may be applied after
clearing or felling of existing trees.

  Code              Description
  ----------------- --------------------------------------------------------------
  BlanketWC         Blanket weed control
  Broad,Wind        Broadcast burn followed by windrow and burn
  BroadBurn         Broadcast burn
  BurnGrass         Grass cover burnt
  ChopperRoll       Chopper rolling
  Graze,Blanket     Grazing of grass, followed by blanket weed control
  Graze,Strip       Grazing of grass, followed by strip weed control
  Graze             Intensive grazing of grass
  InterplantSlash   No site preparation, just clearing debris ready for planting
  NoSitePrep        No site preparation
  SpotWC            Spot weed control
  Strip&Blanket     Strip and blanket weed control
  StripWC           Strip weed control
  WindrowBurn       Windrow and burn

**Site Cultivation**

Gives a description of the site cultivation methods. This may vary
depending on the previous land use.

  Code             Description
  ---------------- ---------------------------------
  BroadCult        Broadcast cultivation
  NoCult           No Cultivation
  SpotCult         Spot cultivation
  StripBroadCult   Strip and broadcast cultivation
  StripCult        Strip cultivation

**Post Planting Weed Control (PPWC)**

Gives a brief description of the type of post planting weed control. The
naming is similar to weed control carried out during site preparation.

  Code              Description
  ----------------- -----------------------------------------------
  BlanketPPWC       Blanket post planting weed control
  Graze,StripPPWC   Grazing with strip post planting weed control
  Man,BlanketPPWC   Manual removal, with blanket weed control
  Man,StripPPWC     Manual removal, with strip weed control
  ManPPWC           Manual post planting weed control
  NoPPWC            No post planting weed control
  StripPPWC         Strip post planting weed control

**Thins**

Indicates the number of thins prior to final harvest. For example, a
pulpwood plantation will have no thins, just a final harvest.
Non-commercial plantings (such as environmental or amenities plantings)
have no harvesting and are listed as NoHarvest.

  Code        Description
  ----------- ---------------------------------------------
  1Thin       1 thin prior to final harvest
  2Thin       2 thin prior to final harvest
  3Thin       3 thin prior to final harvest
  4Thin       4 thin prior to final harvest
  5Thin       5 thin prior to final harvest
  Coppice     Coppice system (roots survive harvest)
  NoThin      No thin prior to final harvest
  NoHarvest   No harvesting (i.e. environmental planting)

**Prunes**

Indicates the number of prunes during a rotation. Typically these occur
around the time of thinning, but this is not always the case.

  Code      Description   
  --------- ------------- --
  1Prune    1 prune       
  2Prune    2 prune       
  3Prune    3 prune       
  4Prune    4 prune       
  NoPrune   No pruning    

**Fertilisation**

Indicates the number of fertilisation events and when they occur (ie at
or near time of establishment, or later after thinning for example).

  Code                 Description
  -------------------- ------------------------------------------------------------------------
  1LateAgeFert         1 late age fertilisation (normally after thinning)
  2LateAgeFert         2 late age fertilisation (normally after thinning)
  3LateAgeFert         3 late age fertilisation (normally after thinning)
  FertAtEst            Fertilisation at or just after planting
  AtEst,1LateAgeFert   Fertilisation at or just after planting, plus 1 late age fertilisation
  AtEst,2LateAgeFert   Fertilisation at or just after planting, plus 2 late age fertilisation
  AtEst,3LateAgeFert   Fertilisation at or just after planting, plus 3 late age fertilisation
  NoFert               No fertilisation

**Unique ID Number**

This gives a unique identifier to every regime in the NCAS databases. It
can be used to track which systems have been downloaded for later
verification. The unique ID number will match that of the related
species.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 243. Generate Plot Files 2016

**Generate Plot Files**

\[ Utilities Menu : *Generate Plot Files* \]

**Use**

The Generate Plot Files function enables the bulk creation or update of
plot files using a specially formatted text file to specify new variable
values for the derived plots.

Plots created by \"Generate plot files\" will be copies of a single base
plot.

Generate plot files will update existing plot files or create new ones
if they do not already exist.

**Base Plot**

All plots are created from a single *Base plot*, supplied as an input to
this process. The base plot contains all data that is not to be altered
by the process. Generated plots will be copies of the base plot, with
changes as specified in the text import file.

**Text Import File**

This file contains all the data to be altered for the new plots
generated. Data formatting rules are:

- 1 plot per row.
- Data is tab delimited.
- Spaces in the file will be treated as ordinary characters that are
  part of the input (e.g. the space in \"Pinus radiata\"), not as a
  delimiter between fields.
- The first field must be the new plot name (or existing plot name in
  the event that you want to update existing plots). The plot name
  specified should not include file path or extension details as these
  will be generated by the *Generate Plot Files* process.
- Inputs for a species must be preceded by the name of the species to
  which they apply.
- Note that any species used in the input text file must already exist
  in the template plot. This function will not add new species, it will
  only modify ones that already exist in the template plot.
- Each input field is identified by its [programming
  name](141_Models%20and%20Inputs%20Window.htm#ProgrammingName) (e.g.
  Max forest aboveground biomass is maxAbgMF) and then the data item(s).

*time-series Inputs*

time-series inputs must have the time-series name (e.g. avgAirTemp-
*Average Air Temperature*) followed by 6 mandatory inputs, being:

- Start year
- Years are
- Extrapolation
- Years of data
- Data points per year
- Multiplier

The times series inputs identifying the *Years are* and *Extrapolation*
are stored in FullCAM internally as integers. Valid values for these
inputs are detailed below.

*Years are*\
0 Calendar time\
1 Time since start of simulation\
2 Years since plants sprouted

*Extrapolation*\
0 Use nearest year in table\
1 Cycle table data across all time\
2 Use average year of data

**Processing rules**

- If an input is invalid then the process will cease and error details
  reported. Plot files successfully created up until the error is
  encountered will be stored in the results directory specified.
- Inputs for multiple species may be imported, but each input set must
  be preceded by the species name input (*nmSP*). Multiple inputs per
  species are permissible as all inputs will be attributed to the last
  recorded species on the input row.
- If you attempt to update a species that does not exist in your
  template plot the output log will show \"Error - species \'Xxxx
  yyyyy\' not found\" and the plot will not be created / updated.
- Time-series inputs must include all information for the time-series
  (e.g. Extrapolation method, Multiplier etc.).
- Programming name inputs are case sensitive.
- If a plot name already exists then this process will either update the
  existing plot, or create a new plot from the base plot and inputs in
  the txt file. This is determined by the prompt :\
  \"If a generated plot exists already should it be updated with the new
  inputs from the input file?\"\
  Yes- Existing plot files will be updated with the inputs from the file
  specified.\
  No- Existing plot files will be over written, based on the base plot
  and the inputs from the file specified.

### Examples

After creating your own Base Plot, you can use the downloadable example
text files (links below), to help you get started.

**Example 1.** Create 3 plot files, adding a single tree species input
for each plot. Txt import file for tree species inputs (exclude
Description field):

  ID      Description                                                                         Type   Species               Variable        Value
  ------- ----------------------------------------------------------------------------------- ------ --------------------- --------------- -----------------------
  Plot1   *Turnover % of branches* for tree species Eucalyptus globulus                       nmSP   Eucalyptus globulus   turnFracBranF   0.6
  Plot2   *Species note* for tree species Eucalyptus globulus                                 nmSP   Eucalyptus globulus   notesSP         Imported species note
  Plot3   *Tree age of max growth in tree yield formula (G)* for tree species Pinus radiata   nmSP   Pinus radiata         tyf_G           12.6

[(Download example 1)](Generate%20Plot%20Files%20-%20Example%201.txt)

**Example 2.** Txt import file for time-series inputs

Create 3 plot files, adding a time-series for each plot:

+-------+--------------+------------+------------+--------------+-------------------------------------------------------------------------------------------------------------------------+
| ID\>  | Description  | Type       | Species/Yr | Variable     | Data                                                                                                                    |
+=======+==============+============+============+==============+======+======+======+======+======+======+======+======+=======+=======+=======+======+======+======+======+======+======+
| Plot1 | 5 years of   | nmSP       | Eucalyptus | incrStemVolF | 0    | 2    | 1    | 5    | 1    | 1    | 41.1 | 98.8 | 128.9 | 175.1 | 219.5 |                                         |
|       | annual *Stem |            | globulus   |              |      |      |      |      |      |      |      |      |       |       |       |                                         |
|       | volume       |            |            |              |      |      |      |      |      |      |      |      |       |       |       |                                         |
|       | increments*  |            |            |              |      |      |      |      |      |      |      |      |       |       |       |                                         |
|       | data         |            |            |              |      |      |      |      |      |      |      |      |       |       |       |                                         |
+-------+--------------+------------+------------+--------------+------+------+------+------+------+------+------+------+-------+-------+-------+------+------+------+------+------+------+
| Plot2 | 1 year of    | avgAirTemp | 1985                      | 0    | 2    | 1    | 12   | 1    | 19.5 | 19.8 | 16.9 | 14.4  | 10.7  | 8.8   | 9.5  | 10.1 | 9.3  | 12.6 | 14.0 | 14.7 |
|       | monthly      |            |                           |      |      |      |      |      |      |      |      |       |       |       |      |      |      |      |      |      |
|       | *Average air |            |                           |      |      |      |      |      |      |      |      |       |       |       |      |      |      |      |      |      |
|       | temperature* |            |                           |      |      |      |      |      |      |      |      |       |       |       |      |      |      |      |      |      |
|       | data         |            |                           |      |      |      |      |      |      |      |      |       |       |       |      |      |      |      |      |      |
+-------+--------------+------------+---------------------------+------+------+------+------+------+------+------+------+-------+-------+-------+------+------+------+------+------+------+
| Plot3 | 1 year of    | rainfall   | 1995                      | 0    | 1    | 1    | 12   | 1    | 20   | 50   | 30   | 40    | 20    | 50    | 80   | 200  | 300  | 10   | 35   | 125  |
|       | monthly      |            |                           |      |      |      |      |      |      |      |      |       |       |       |      |      |      |      |      |      |
|       | *Rainfall*   |            |                           |      |      |      |      |      |      |      |      |       |       |       |      |      |      |      |      |      |
|       | data         |            |                           |      |      |      |      |      |      |      |      |       |       |       |      |      |      |      |      |      |
+-------+--------------+------------+---------------------------+------+------+------+------+------+------+------+------+-------+-------+-------+------+------+------+------+------+------+

[(Download example 2)](Generate%20Plot%20Files%20-%20Example%202.txt)

**Example 3.** Txt import file for multiple inputs per plot

Create 3 plot files, adding multiple inputs (including time-series) for
each plot:

  ID      Description
  ------- -------------------------------------------------------------------------------------------------------------------------
  Plot1   *Turnover % of branches, Species note, Tree age of max growth in tree yield formula (G)* for tree species Pinus radiata
  Plot2   *Stem volume increments, Tree age of max growth in tree yield formula (G)* for tree species Eucalyptus globulus
  Plot3   *Tree age of max growth in tree yield formula (G)*

  ID      Type   Species         Variable        Value   Variable   Value                   Variable   Value
  ------- ------ --------------- --------------- ------- ---------- ----------------------- ---------- -------
  Plot1   nmSP   Pinus radiata   turnFracBranF   0.6     notesSP    Imported species note   tyf_G      12.6

+-------+------+------------+--------------+--------------------------------------------------------------------------------------------------+----------+-------+
| ID    | Type | Species    | Variable     | Series                                                                                           | Variable | Value |
+=======+======+============+==============+========+========+========+========+========+========+========+========+========+========+========+==========+=======+
| Plot2 | nmSP | Eucalyptus | incrStemVolF | 0      | 2      | 1      | 5      | 1      | 1      | 41.1   | 98.8   | 128.9  | 175.1  | 219.5  | tyf_G    | 10.5  |
|       |      | globulus   |              |        |        |        |        |        |        |        |        |        |        |        |          |       |
+-------+------+------------+--------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+----------+-------+

  ID      Type   Species         Variable     Value   Variable     Value   Variable     Value   Variable     Value   Variable     Value   Variable     Value   Variable   Value
  ------- ------ --------------- ------------ ------- ------------ ------- ------------ ------- ------------ ------- ------------ ------- ------------ ------- ---------- -------
  Plot3   nmSP   Pinus radiata   rFracStemF   1       rFracBranF   1       rFracBarkF   1       rFracLeafF   0.85    rFracCortF   1       rFracFirtF   0.65    maxAbgMF   160

[(Download example 3)](Generate%20Plot%20Files%20-%20Example%203.txt)

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 247. Proxy Settings 2016

**Proxy Settings**

\[*Internet* menu : *Proxy Settings*\]

This window is for maintaining your FullCAM proxy settings.

**Use System Default Proxy**

This setting causes FullCAM to use the system default proxy which is
specified in Control Panel -\> Internet Options -\> Connections -\> LAN
Settings.

If your LAN uses automatic configuration to set the proxy server, you
must manually configure that proxy server in FullCAM.

This is the default setting for Proxy.

**Use a Manually Configured Proxy**

This option allows you to specify the address and port of the proxy that
should be used. Type the proxy server name in the Address text box and
the port number in the Port text box.

**Do Not Use a Proxy**

This option allows you to connect directly overriding any system default
proxy.

Please note that changes to your proxy settings will not take effect
until the next time that you connect.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 248. Event Update 2016

**Event Update**

\[*Events* page : *Clone Events* or *Event Update* dialogues\]

[Event Timing](143_Event%20Timing.htm) can be updated for multiple
events at once. This can be either a positive or negative offset from
the current timing, and is irrespective of the type (Calendar date or
Days since start of simulation).

When moving an event with a negative offset, the regime which the event
belongs to will reorganise itself by changing the year of events so that
the regime always begins after the last data of the previous regime.

[Event Timing](143_Event%20Timing.htm) may be updated for multiple
events by multi-selecting the events on the Event List, and then
selecting either of the right mouse options:

*Apply Offset to Events*- Updates the selected [Events](136_Events.htm)
timing details by the offset years and days specified.

*Clone Events*- Clones the selected events and applies an offset to the
original events of the years and days specified. This can be
particularly useful if you wish to clone [Regimes](235_Regimes.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
