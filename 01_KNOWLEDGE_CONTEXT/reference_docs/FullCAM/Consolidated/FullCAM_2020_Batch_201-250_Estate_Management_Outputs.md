---
version: 2020
batch_range: 201-250
batch_name: Estate_Management_Outputs
creation_date: 2025-08-28
total_files: 19
---

# FullCAM 2020 - Batch 201-250: Estate Management Outputs

## Table of Contents

- [201. Plants 2020](#201-plants-2020)
- [203. Soil 2020](#203-soil-2020)
- [205. Initial Conditions 2020](#205-initial-conditions-2020)
- [206. Forest Percentage 2020](#206-forest-percentage-2020)
- [207. Downloading Spatial Data 2020](#207-downloading-spatial-data-2020)
- [215. Trees 2020](#215-trees-2020)
- [216. Crops 2020](#216-crops-2020)
- [217. Main Window 2020](#217-main-window-2020)
- [219. Departmental Server 2020](#219-departmental-server-2020)
- [228. Pasture to Plantation Forest 2020](#228-pasture-to-plantation-forest-2020)
- [229. Plantation Forest to Plantation Forest 2020](#229-plantation-forest-to-plantation-forest-2020)
- [230. Native Forest to Plantation Forest 2020](#230-native-forest-to-plantation-forest-2020)
- [231. Native Forest to Pasture 2020](#231-native-forest-to-pasture-2020)
- [232. Grazed Woodland 2020](#232-grazed-woodland-2020)
- [233. Crop and Pasture Management 2020](#233-crop-and-pasture-management-2020)
- [234. Explorer 2020](#234-explorer-2020)
- [235. Regimes 2020](#235-regimes-2020)
- [247. Proxy Settings 2020](#247-proxy-settings-2020)
- [248. Event Update 2020](#248-event-update-2020)

---

## 201. Plants 2020

**Plants**

\[*Trees* page or *Crops* page in the input window of a document\]

These two pages, the [Trees](215_Trees.htm) page and the
[Crops](216_Crops.htm) page, are where you describe the species on the
plot. They are each partitioned into three panels:

- [Select a Species](56_Select%20a%20Species.htm) panel
- [Properties of the Species](145_Properties%20of%20the%20Species.htm)
  panel
- [Standard Information for the
  Species](146_Standard%20Information%20for%20the%20Species.htm) panel

**About Species**

Crop and Trees are loaded into the
[species](56_Select%20a%20Species.htm) list via the
[DataBuilder](132_Data%20Builder.htm).

Default parameters which control the growth, root:shoot ratios, turnover
rates, debris decay, and so on, are also downloaded along with the
species. These may then be edited by hand via the windows opened from
this page.

If there are no plants growing and the system is clear, then planting
events, namely [Plant Trees](158_Plant%20Trees.htm) or [Plant
Crop](161_Plant%20Crop.htm), can set plants growing on the plot. A
planting event can plant any species listed on this panel.

Clearing events, such as a [Thin](140_Thin.htm),
[Harvest](153_Harvest.htm), [Forest Fire](144_Forest%20Fire.htm), or
[Agricultural Fire](149_Agricultural%20Fire.htm), can remove the plants
if there are plants growing.

By clearing one species then planting a different species, a plot can
have several different species growing during the plot simulation - but
only one species growing in a system at any one time.

The debris and products from each species are tracked separately,
because they have characteristics that may differ from species to
species. However, all species are treated the same with respect to the
mulch and soil - different species merely have different proportions of
decomposable or resistant material.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 203. Soil 2020

**Soil**

\[*Soil* page of the input window of a plot or spatial document\]

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
  atmosphere if it becomes non-inert, such as if plowing breaks up the
  clay particles.

[RothC](114_RothC.htm) is always used to model the active soil; only
[CAMFor](77_CAMFor.htm) and [CAMAg](78_CAMAg.htm) model the inert soil.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 205. Initial Conditions 2020

**Initial Conditions**

\[*Initial Conditions* page of the input window of a plot or spatial
document\]

Enter inputs that describe the situation on the plot at the beginning of
the simulation. It is partitioned into several windows and a panel:

- [Initial Trees](185_Initial%20Trees.htm)
- [Initial Crops](184_Initial%20Crops.htm)
- [Initial Debris](31_Initial%20Debris.htm)
- [Initial Standing Dead](284_Initial%20StandingDead.htm)
- [Initial Soil](32_Initial%20Soil.htm)
- [Initial Products](33_Initial%20Products.htm)
- [Initial Conditions For the Whole
  Plot](197_Initial%20Conditions%20For%20the%20Whole%20Plot.htm)

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 206. Forest Percentage 2020

**Forest Percentage**

The forest percentage specifies proportional allocations for a number of
parameters in forest and agricultural systems within a mixed plot (see
[Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm) and [Configure
the Plot](6_Configure%20the%20Plot.htm)).

**Introduction**

The concept of the "forest percentage" arises only in a mixed multilayer
plot. A mixed multilayer plot has a multilayer forest system and a
multilayer agricultural system. In such a system, the forest percentage
scales most initial conditions and agricultural behaviour in accordance
with this percentage. For example, if the forest percentage in 30%, then
the agricultural percentage is 70%.

**Definition**

The *forest percentage* is defined as the percentage of the plot covered
by the tree canopy.

For example, a plot with 10 ha of forest and 30 ha of agricultural
system has a forest percentage of 25% (because 10 / 40 = 25% of the plot
is forest).

**Discussion**

The forest percentage is the percentage of the sunlight going to the
trees and not to crop species. In the plot simulator, this requires that
the agricultural activity be limited but that forest growth be
unimpeded. This is because forest systems are calibrated to an endemic
canopy cover for their location where a continuous forest cover
definition applies (\>2m in height and \>20% canopy cover), but
agricultural systems are calibrated to 100% sunlight. If the forest
fraction is *f* then:

- Tree production (growth) is no different to if the plot were a forest
  plot.
- Crop production (growth) is (1 -- *f* ) times what it would be if the
  plot were wholly agricultural.
- The mass present due to initial conditions in the soil and debris
  layers are scaled down by *f* and (1 - *f*) for forest and
  agricultural systems respectively.

For example, suppose a mixed plot has the forest fraction equal to 30%.
Then the forest growth is the same as what it would be if the whole plot
were forest, but the agricultural growth is limited to 70% of what it
would be if the whole plot were agricultural. The initial soil and
debris levels in the forest system are 30% of what they would be if the
whole plot were forest, and in the agricultural system are 70% of what
they would be if the whole plot were agricultural. No non-growth
processes are affected by the forest percentage.

The forest percentage can vary with time in response to events. [Forest
Percentage Change](116_Forest%20Percentage%20Change.htm) events should
be created when land management practices change alongside other events
giving effect to that change, such as the removal or planting of trees.
If [3PG](http://www.fullcam.au/FullCAMServer2020/Help/115_3PG.htm) is in
use, the percentage can also change as the tree canopy grows.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 207. Downloading Spatial Data 2020

**Downloading Spatial Data**

\[[Data Builder](132_Data%20Builder.htm) page : *Spatial Data* panel\]

This panel is for downloading data that is specific to a location, using
Data Builder.

**Inputs**

Specify the plot\'s location by entering its [Latitude and
Longitude](180_Latitude%20and%20Longitude.htm). The default latitude and
longitude is for Uluru.

The *Forest category* drop-down list provides a filter to help with
choosing trees species from DataBuilder. Selecting \"All\" will provide
all species, but choosing any other option from the list will narrow
down the options presented to those which would generally be available
for that type of land management.

The *Spatial data averaged over* list is where you choose the area over
which to average downloaded data. The purpose of this averaging is so
that the downloaded data represent the average conditions in a broader
area, which can be set from 1 hectare up to 2500 hectares. The area from
which the data is averaged for download, is centred on the plot
latitude/longitude, with the data to be averaged being climate, and
other inputs such as initial soil carbon.

The *[Forest Percentage](206_Forest%20Percentage.htm)* is used to set
the initial masses in proportion between the forest and agricultural
systems, and it becomes the [Initial Conditions For the Whole
Plot](197_Initial%20Conditions%20For%20the%20Whole%20Plot.htm) value. It
has no direct effect on any simulation of this plot. For modelling
systems transitioning from pasture to plantation, the initial forest
percentage for downloading should be set to 0.

When you download a species and set it as the initial species, the value
of the forest percentage for downloading is used to compute the initial
masses of the species. So if you later change the forest percentage for
downloading, you will have to reset the initial species.

**Download Spatial Data**

Press the *Download Spatial Data* button to download the location
specific data from the [Departmental
Server](219_Departmental%20Server.htm). Text to the right of the window
will then become visible showing the state and SA2 region for that the
latitude and longitude resides within.

For [Tree](215_Trees.htm) species, also displayed is the National
Plantation Inventory Region (NPI), which are plantation regions
published by ABARES, and the Growth Region, which are regions
determining the availability of species for environmental and mallee
plantings.

The Data Builder will download data for any point for which data is
available within the extent used. The FullCAM Server has spatial data
based on grids of varying resolutions from 25m to 1km.

**Downloading Crops and Trees**

\[[Data Builder](132_Data%20Builder.htm) page : *Trees and Crops*
panel\]

This panel is for downloading crop and tree species.

**Basic Operation**

1.  After downloading spatial data, select a species from the lower
    *Available Crops / Available Trees* lists, and press the *Download
    Species* button. This will download the species data to the plot and
    update the upper *Crop Species / Tree Species* lists.
2.  Having the *Apply downloaded data* checkbox ticked will overwrite
    previously downloaded or manually entered species data within the
    plot.

**Details**

When downloading the first species to a plot, Data Builder will ask if
you wish to make the species the initial species. We recommend you
select "Yes". This will populate the initial conditions parameters. The
existence of and parameters for the initial species can be edited via
the [Initial Conditions](205_Initial%20Conditions.htm) tab. This is the
preferred method of entering data into the initial conditions as all
data points will contain required default data.

Once at least one crop or tree species has been downloaded, regimes and
events are now ready to be added to the [Event Queue](136_Events.htm).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 215. Trees 2020

**Trees**

\[*Trees* page in the input window of a document\]

Describe the tree species. This page is similar to the
[Crops](216_Crops.htm) page, so we describe both pages together --- see
[Plants](201_Plants.htm).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 216. Crops 2020

**Crops**

\[*Crops* page in the input window of a document\]

Describe the crop species. This page is similar to the
[Trees](215_Trees.htm) page, so we describe both pages together --- see
[Plants](201_Plants.htm).

GBF = Grains, buds, and fruit

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 217. Main Window 2020

**Main Window**

This window is the thin window across the top of your screen with a menu
and toolbar, entitled "FullCAM X.X \[PR 2020\]", where X.X is the
version number of the FullCAM program.

The main window is open whenever FullCAM is open. It is the window
called "FullCAM" in the Windows Taskbar. Individual FullCAM documents or
windows do not get their own buttons on the Windows Taskbar.

If you close the main window then you exit FullCAM.

The main window contains the only fixed menus.

You cannot resize the main window, although you can move it.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 219. Departmental Server 2020

**Departmental Server**

The FullCAM server is operated by the Department of Industry, Science,
Energy and Resources and from which you can download data for sites
using the [Data builder](132_Data%20Builder.htm)

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 228. Pasture to Plantation Forest 2020

Pasture to Plantation Forest

Details

Pasture to plantation forest management systems are created in FullCAM
by using a plot type of *Multilayer mixed system*.

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

- Plot Type : Multilayer mixed system.

*Timing*

- *Start simulation at beginning of* year should be set to 20 years
  prior to plantation establishment.

It is always prudent to 'run the model in' by setting the start year
earlier (up to 20 years) than the actual period of interest. This is
because the soil carbon data at initialisation represents a pristine
condition, a condition that does not reflect any prior management.

*Build the Event Queue*

- Set the *Forest percentage for downloading* to 0.\
  Select the required *Crop species* (refer [Downloading Spatial
  Data](207_Downloading%20Spatial%20Data.htm)).\
  Select the required *Trees species*.
- Select an initial *Crop Regime* (refer [Events](136_Events.htm)).
- Select a subsequent rotation *Tree-species plantation regime.*

Additional tree and crop species can be added to model transitions from
one plantation species to another.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 229. Plantation Forest to Plantation Forest 2020

Plantation Forest to Plantation Forest

Details

Plantation forest to plantation forest management systems are created in
FullCAM by using a plot type of *Multilayer forest system*.

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

- Plot Type : Multilayer forest system.

*Data Builder*

Select the required *Trees and Events* (refer [Downloading Spatial
Data](207_Downloading%20Spatial%20Data.htm)).

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 230. Native Forest to Plantation Forest 2020

Native Forest to Plantation Forest

Details

Native forest to plantation forest management systems are created in
FullCAM by using a plot type of *Multilayer forest system*.

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

- Plot Type : Multilayer forest system.

*Data Builder*

Select the required *Trees and Events* (refer [Downloading Spatial
Data](207_Downloading%20Spatial%20Data.htm)).

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 231. Native Forest to Pasture 2020

Native Forest to Pasture

Details

Native forest to pasture management systems are created in FullCAM by
using a plot type of *Multilayer mixed system*.

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

- Plot Type : Multilayer mixed system.

*Data Builder*

Set the *Forest percentage for downloading* to the initial tree crown
canopy cover.\
Select the required *Trees and Crops* (refer [Downloading Spatial
Data](207_Downloading%20Spatial%20Data.htm)).

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 232. Grazed Woodland 2020

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 233. Crop and Pasture Management 2020

Crop and Pasture Management

Details

Crop and pasture management systems are created in FullCAM by using a
plot type of *Agricultural system*.

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

- Plot Type : Agricultural system.

*Data Builder*

Select the required *Crops* (refer [Downloading Spatial
Data](207_Downloading%20Spatial%20Data.htm)).

- Select a crop species.
- Select an appropriate crop species regime and build the Event Queue.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 234. Explorer 2020

**Explorer**

\[*Explorer* page of the input window of a plot document\]

This page shows inputs required by the current configuration showing
names, programming names and values for FullCAM inputs.

The values are the current values in the document. If the value is blank
or the value is not a number or "On/Off", or if there is no such value
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
the values of the document.

Drag and drop via Explorer is also provided to other FullCAM plot
windows, functionality such as [Plot Digest](281_Plot%20Digest.htm) for
input selection, or external applications such as Microsoft Word and
Excel for exporting the selected document data.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 235. Regimes 2020

**Forest Regimes**

\[[Data Builder](132_Data%20Builder.htm) page : *Trees* panel\]

**Introduction**

The regime names aim to describe the types of management practices that
will occur at a location. The regimes are species, location and time
specific, being based on either National Plantation Inventory region or
State.

The following text and table describes the regime names in the order
they appear in the regime name. If more detailed information on a regime
is required, or if the name is not exactly clear, place the mouse over
the regime name. This will lead to a yellow text box appearing with a
more detailed description of the regime.

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
establishing the forest was pasture. The 'plantation' previous land use
is used to build multiple rotations and hence is only available after
downloading an initial regime.

  Code         Description
  ------------ --------------------------------------
  InitPlant    Plantation at start of simulation
  LocalSpp     Local species at start of simulation
  NativeFor    Native forest at start of simulation
  Pasture      Pasture at start of simulation
  Plantation   2^nd^ rotation plantation

**Site Productivity Estimate**

A broad estimate of how productive the site is for a certain region.
This generally determines factors such as timing of events and rotation
length. Regimes with "recommended" after them are those that fit with
the site productivity assessment of the National Carbon Accounting
System.

If you feel that your site quality is much higher (i.e. deep fertile
river flat with access to groundwater) or lower (rocky outcrops or badly
degraded land) than reflected in the national account, you may select
other options to suit your conditions. When doing this you may also need
to adjust some other parameters in the model. For more information
contact [Contact Us](190_Contact%20Us.htm).

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

Indicates the number of fertilisation events and when they occur (i.e.
at or near time of establishment, or later after thinning for example).

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 247. Proxy Settings 2020

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

This option allows you to connect directly to the [Departmental
Server](219_Departmental%20Server.htm) overriding any system default
proxy.

Please note that changes to your proxy settings will not take effect
until the next time that you connect.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 248. Event Update 2020

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

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
