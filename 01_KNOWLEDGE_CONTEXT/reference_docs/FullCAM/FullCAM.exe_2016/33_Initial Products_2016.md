+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Initial Products**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page : *Initial
Products* button\]

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest* or
*Agricultural* panel : *Products* button\]

Describe the plot products existing at the start of the simulation.

**Introduction**

All of the initial forest products belong to the initial tree species,
which is specified in the [Initial Trees](185_Initial%20Trees.htm)
window (regardless of whether or not there are trees initially growing
on the plot).

All of the initial agricultural products belong to the initial crop
species, which is specified in the [Initial
Crops](184_Initial%20Crops.htm) window (regardless of whether or not
there is a crop initially growing on the plot).

If different species are planted later in the simulation, the products
of each species are treated separately because each species may have
different product decomposition rates (see [Product
Properties](47_Product%20Properties.htm)).

Forest products can start the simulation either in use as products or in
the landfill. Agricultural products can only start the simulation in use
as products (in FullCAM, agricultural products cannot go to landfill).

**Carbon Masses**

Enter the mass of carbon in the various product pools, in tonnes per
hectare as a time-series.

The names of the products are only indicative: the various product
categories are effectively defined by their decomposition fractions
(entered as species inputs). All CAMFor cares about is that a hectare of
plot produces X tonnes of a product that decomposes at a given rate.

Suppose the plot is a forest that produces fence palings for suburban
back yards. There is no category here called "fence palings", so what do
you do? The only thing that matters to carbon accounting is how fast
those fence palings decompose. Suppose you find that 1/20 of the carbon
in the fence palings returns to the atmosphere each year. Then the
decomposition fraction of the fence palings is 0.05 / year. Make sure
that one of the wood product decomposition fractions is about 0.05 /
year, and add the fence palings to that category. For instance, suppose
you enter the decomposition rate of packing wood as 0.052. Close enough.
Add the fence palings to the category labelled "packing wood".

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
product values. The button is disabled if the standard initial product
information for that species is not ready (incomplete or has invalid
values).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
