+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

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
