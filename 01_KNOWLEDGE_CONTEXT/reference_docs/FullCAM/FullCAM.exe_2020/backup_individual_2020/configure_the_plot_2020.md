---
title: Configure the Plot
version: 2020
category: Configuration
original_file: 6_Configure the Plot_2020.md
---

Specify what systems and layers of the plot you want to model (see
Plots, Systems, Layers, and
Pools).

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
  Forest mulch         GENDEC
  Agricultural mulch   GENDEC
  Forest soil          RothC
  Agricultural soil    RothC

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
they are only due to graininess --- see Simulation
Steps) --- omitting the soil omits the need
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
