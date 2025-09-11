+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

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
