+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Site : Maximum Aboveground Biomass**

\[[Site](200_Site.htm) page : *Maximum Aboveground Biomass* panel\]

Enter information about the maximum aboveground biomass that can be
supported by the plot.

The *aboveground biomass* is the combined mass (in tdm/ha) of the
aboveground plant components:

- For trees: Stems, branches, bark, and leaves
- For crops: Grains, buds, fruit, stalks, and leaves.

It does not include the roots, or any debris or soil matter. It is a
mass, measured in tonnes per hectare of dry matter, not carbon mass.

The maximum aboveground biomass limits place absolute limits on the
amount of aboveground trees and crops can exist of the plot during a
simulation.

The growth of plants is calculated as specified elsewhere (see [Growth
Properties](42_Growth%20Properties.htm)), without regard to the maximum
aboveground biomass (except in the tree yield formula which uses the
maximum site biomass as the value toward which growth will approach).
After growth and turnover has been calculated for the plant components,
if the aboveground biomass of the plants exceeds the maximum aboveground
biomass for the site, then the masses of all of the plant components are
reduced, in proportion to their pre-reduction masses.

The mass removed from the plant components becomes turnover and is
treated as turnover, except that aboveground-biomass-limit-reduction
mass is added to turnover after yield-versus-production has been
determined (yield measurements do include the effects of regular
turnover, but do not include the effects of mortality or site biomass
limits).

There are separate aboveground biomass limits for trees and for crops
--- that is, the site may support different aboveground biomasses of
trees or crops.

In a mixed plot, limits apply to trees and crops separately and
proportionally. For example, if the maximum aboveground biomass for
trees is entered here as 80 tdm/ha (if the whole plot is covered in
forest then it can support 80 tdm/ha of aboveground biomass) but
currently only 20% of the plot is forested, then the maximum aboveground
biomass of trees is 20% \* 80 tdm/ha = 16 tdm/ha (the plot can support a
maximum aboveground tree biomass of 16 tdm/ha while 20% of it is
forested).

If the aboveground biomass of the plants never exceeds the maximum
aboveground biomass, then the maximum aboveground biomass has no effect
on the simulation --- except if the tree yield formula is used, in which
case the maximum forest aboveground biomass affects the tree growth rate
at all times (see [Growth Properties](42_Growth%20Properties.htm)).

If you do not wish there to be any upper limit on growth, simply set the
maximum aboveground biomass to a number high enough so as not to act as
a limiting effect (such as 999) --- effectively rendering it
inoperative.

The maximum aboveground biomass limit is intended to simulate
self-thinning and depends on the site, but not on the species.

**Trees**

The maximum aboveground tree biomass is also used to calculate tree
growth, if the option to use the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) is used (see [Configure Tree
Production](108_Configure%20Tree%20Production.htm)). Basically, the
aboveground tree mass asymptotically approaches the maximum aboveground
biomass.

If any tree species uses the tree yield formula then the maximum
aboveground biomass of the trees cannot exceed 764 tdm/ha (which
corresponds to the maximum possible aboveground biomass under the tree
yield formula). If you choose to use the tree yield formula when the
maximum aboveground biomass of the trees exceeds this amount, the input
here is coloured red to indicate it needs changing.

Information on aboveground biomass estimates can be found in [NCAS
Technical Report
No.44](reps/TR44%20Spatial%20Estimates%20of%20Biomass%20in%20'Mature'%20Native%20Vegetation.pdf){target="reps44"}.
Values for *Maximum Aboveground Biomass* can be downloaded from the
FullCAM server using [Data Builder](132_Data%20Builder.htm).

**Crops**

There is no crop-growth-by-formula option; the maximum crop biomass is
only used to limit crop mass.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
