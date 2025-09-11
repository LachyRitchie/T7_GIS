---
title: Configure the Plot
version: 2016
category: Configuration
original_file: 6_Configure the Plot_2016.md
---

[Configuration page : *Plot* panel]

Specify what systems and layers of the plot you want to model (see
Plots, Systems, Layers, and
Pools).

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