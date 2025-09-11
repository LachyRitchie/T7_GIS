+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

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
because all quantities are processed by the program on a per hectare
basis. Masses are measured in tonnes per hectare. If you prefer to work
in "tonnes" rather than "tonnes per hectare" then you can specify an
area for the plot ([Site : Area](157_Site_Area.htm)).

Estate simulations work by simulating each plot in the area under
consideration then multiplying the results by the area (in hectares) of
the relevant plots.

**Systems**

A system is an independent ecosystem on a plot. There are two types of
*system*:

- *Forest (system)* - A forest has trees, and the characteristics
  associated with trees.
- *Agricultural system* - An agricultural system has crops, and the
  characteristics associated with crops.

A plot consists of one or both systems:

- A forest plot consists of one system, namely a forest system.
- An agricultural plot consists of one system, namely an agricultural
  system.
- A mixed plot consists of two systems, namely a forest system and an
  agricultural system.

*Plants* are either trees or crops. A *species* is either a tree or crop
species:

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

*Minerals* - Mineral store for nitrogen. If there is insufficient
nitrogen, the usual processes of production and decomposition moving
material around may be limited.

*Products* - Consists of plant material taken offsite such as wood or
agricultural products. Material may subsequently move to the atmosphere
by decomposition.

In addition, the atmosphere is modelled as an infinite reservoir of
carbon and nitrogen.

**Pools**

Each layer (except for the minerals) is further partitioned into several
pools. A *pool* is a collection of material that is homogeneous and not
further subdivided in FullCAM. From a mechanical point of view, a
FullCAM simulation consists of moving material between pools.

For example, in a forest the plant (tree) layer consists of the stem,
branch, bark, leaf, coarse root, and fine root pools.

A layer is a collection of neighbouring pools with similar
characteristics.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
