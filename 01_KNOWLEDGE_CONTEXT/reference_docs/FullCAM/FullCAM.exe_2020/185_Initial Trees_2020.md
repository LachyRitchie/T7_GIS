+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Initial Trees**

\[[Trees](215_Trees.htm) page : *Initial Trees* button\]\
\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest*
panel : *Trees* button\]

Describe the trees growing in the forest system at the start of the
simulation.

**Species**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Even if there are no trees growing, there may be carbon in the [Initial
Debris](31_Initial%20Debris.htm) or [Initial
Products](33_Initial%20Products.htm) to consider. This is only possible
if an initial species is specified to provide the conditions.

Only one tree species can grow in the forest at any one time (see the
[Select a Species](56_Select%20a%20Species.htm) panel). The species
listed on the pull down on the menu are those on the *Trees* page. If
there are no tree species available, a new species can be created on the
*Trees* page or downloaded by the [Data
Builder](132_Data%20Builder.htm).

**Existence**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Specify whether there are trees growing in the forest at the beginning
of the simulation. If there are not, then the forest is clear and the
other inputs need not be entered. Trees will not grow until a planting
event is created to establish them.

When using [Data Builder](132_Data%20Builder.htm), if a species is set
as the initial tree species then it shall by default set the existance,
but only if a crop species has not already been set as an initial
species.

**Specify Tree Size By**

The intial biomass of the forest can either be set on the basis of mass
or volume, on in relation to the [Maximum Aboveground
Biomass](36_Site_Maximum%20Aboveground%20Biomass.htm). The method chosen
should be appropriate to the configuration of tree production.

If the selection is as a percentage of maximum tree biomass, then the
initial conditions for the forest will be set at their site maximum
scaled to the [Forest Percentage](206_Forest%20Percentage.htm). Bear in
mind that trees will still grow relative to their age, and so this
option should generally only be used when modelling the removal of
forest at the start of the simulation.

If the selection is as a percentage of tree-age biomass, then the intial
conditions for the forest will be set as a proportion of their site
maximum based on the age profile of the trees, and scaled to the [Forest
Percentage](206_Forest%20Percentage.htm). This is the recommended choice
for modelling a forest in most circumstances and is used by the [Data
Builder](132_Data%20Builder.htm).

**Masses**

Available when specifying tree size by mass or volume.

The masses of the various tree components at the start of the
simulation, in tonnes of dry matter per hectare. Note that these are
true masses, not carbon masses as in some other inputs.

**Volumes**

Available when specifying tree size by volume for stems.

The stem volume is the total volume of stems in the forest, in cubic
meters per hectare. This volume will be converted to a mass in the
FullCAM simulation by multiplying it by the stem density.

**Percentage of biomass**

Available when specifying tree size by percentages of maximum biomass or
tree-age biomass

The proportions of biomass in each pool are determined here. The
resulting biomass and carbon in each pool is calculated relative to the
Site [Maximum Aboveground
Biomass](36_Site_Maximum%20Aboveground%20Biomass.htm), and if selecting
tree-age biomass then the Age.

**Ages**

Tree ages are used to access the tree time series.

The age of the oldest trees in the forest is the age of the forest. The
average age of the trees in the forest reflects the new trees that are
assumed to have grown after removal of tree stems in past thinnings. The
average tree age must be less than the age of the oldest trees.

Unless there are thinning events that thin some but not all of the tree
stems, the age of the oldest trees will equal the average age of the
trees. Setting both ages to a very large number will approximate
maturity.

**Numbers of Trees**

Enter the number of stems per hectare, which is the stand stocking
level.

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
tree values (set via the *Initial Trees* button on the *Standard
Information for the Species* panel of the *Trees* pages, see [Standard
Information for the
Species](146_Standard%20Information%20for%20the%20Species.htm)). The
button is disabled if the standard initial trees information for the
species is not ready (incomplete or has invalid values).

**Tree Yield Formula: Growth Calibrations**

The [Tree Yield Formula](42_Growth%20Properties.htm) may have
alternative empirical calibrations available for a given tree species.
Options are listed here in the drop down menu. The Tree Yield Formula
parameters applied under these alternative options are listed under the
Trees-Growth tab.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
