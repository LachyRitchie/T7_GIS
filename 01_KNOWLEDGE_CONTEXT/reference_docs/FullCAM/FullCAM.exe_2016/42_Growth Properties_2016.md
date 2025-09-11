+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Growth Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Growth* button\]

These two windows, the tree growth and crop growth windows, are where
you specify how the current species grows ([Select a
Species](56_Select%20a%20Species.htm)). The two windows are very
similar, so are discussed together.

**Growth**

"Growth" on this window can mean either "production and turnover" or
"production only", depending on the second setting in the *Properties*
section. See [Yield and
NPP](131_Yield%20and%20Net%20Primary%20Production.htm).

**Tree Growth Method**

The tree growth method is set in the [Configure Tree
Production](108_Configure%20Tree%20Production.htm) panel. The methods
are:

1.  *Increments* - Use one of the increment time-series on this window.
    Set whether the allocations and increments are in terms of NPP or
    yields.
2.  *Tree yield formula* - The increments are not used. The allocations,
    like the increments computed by the tree yield formula, are
    automatically in terms of yields.

**Crop Growth Method**

Crop growth is always specified by increment time-series, and you always
set whether the allocation and increment time-series are in terms of NPP
or yields.

**Properties of the Species time-series**

The *species time-series* are:

- [Tree Growth Allocations](112_Tree%20Growth%20Allocations.htm) (this
  window)
- [Crop Growth Allocations](124_Crop%20Growth%20Allocations.htm) (this
  window)
- [Tree Growth Increments](110_Tree%20Growth%20Increments.htm) (this
  window)
- [Crop Growth Increments](118_Crop%20Growth%20Increments.htm) (this
  window)
- [Mortality](121_Mortality.htm) ([Plant
  Properties](43_Plant%20Properties.htm) window)
- [Stem Density](9_Stem%20Density.htm) ([Plant
  Properties](43_Plant%20Properties.htm) window)

Specify here whether the plant age used in any species time-series is
the average or the maximum age of the plants. This input only applies to
species time-series that are expressed in terms of times since the
plants were sprouted (although it is always a required input, regardless
of whether or not any species time-series are in terms of times since
sprouting). The average and maximum plant age only differ if there have
been thinning or harvesting events that do not clear the plot, and thus
allow new plants to sprout alongside the older plants --- see the
[Thin](140_Thin.htm) and [Harvest](153_Harvest.htm) events. Note that
the term "sprouting" is used to specify the time of germination. The
time of planting is when the plant is moved in site to the plot. The age
of planting will be the same or less than the age of sprouting (such as
to account for nursery time).

Specify whether the allocations and increases are for yields (measured
mass increments) or NPP flows. Most people will choose yields; the NPP
option is mainly for academic researchers. If the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) is being used, this choice has
been made for you (yields).

**Allocations**

The allocation time-series specify the growth of the plant components
relative to each other. We need one allocation time-series for each
plant component.

The numbers in the allocation time-series are the

*relative* allocations of yield or NPP to the various plant components.
Use any non-negative numbers; they are only meaningful in relation to
one another (for example, 1.0 for leaves and 0.2 for coarse roots is the
same as 1000 for leaves and 200 for coarse roots).

**Increments**

An increment time-series specifies the increase in one or a combination
of plant components. Only one increment time-series is used by the
species --- select one by clicking on the radio button to the left of
the rectangular button displaying the name of the increment time-series.

**Parameters in the Tree Yield Formula**

See the [Tree Yield Formula](130_Tree%20Yield%20Formula.htm). Variation
in site, management, species and other factors greatly impact forest
growth and hence, vary growth curve characteristics

Enter the tree age in years at which the tree's growth (measured in
tonnes per year) is highest. This is *G* in the description of the yield
formula.

The roles of the non-endemic species multiplier *r* of the maximum
aboveground biomass *M* (entered in the *Site : Maximum Aboveground
Biomass* panel) are:

- To change the effective maximum biomass in the tree yield formula from
  *M* to *r \* M*.
- To change the maximum tree biomass limit for the plot from *M* to *r
  \* M*.

Because *r* is species-dependent, the site's growth rate and maximum
biomass can vary by species for the same site. Normally r will be close
to 1 (assuming that *M*, entered in the *Site : Maximum Aboveground
Biomass* panel, is a realistic value).

*Calculation of G and r on the Departmental Server*

When you use [Data Builder](132_Data%20Builder.htm) to download tree
species, the [Departmental Server](219_Departmental%20Server.htm)
calculates the values of *G* and *r* that it downloads to your plot as
follows. These calculations are based on statistically calibrated models
involving site and management factors.

The age of maximum biomass increment *G* varies with productivity and
management regime. It is calculated using a linear model:

> *G = ag + bg \* M*

where

*M* = Maximum aboveground biomass of trees, in tdm/ha (*Site* page).
This is the unadjusted value, prior to multiplication by *r* and prior
to any type 2 forest treatments.

*ag* = Maximum age at which the trees reach maximum aboveground biomass
increment at the lowest *M* values (that is, on the lowest quality site
on which the plantation species is used). *ag* is constant for a given
species, but varies between species.

*bg* = Multiplier. Constant for a given species, but varies between
species.

Thus, for a given species, the downloaded *G* only varies with *M*.

The non-endemic species multiplier *r* varies with region and management
regime. It is calculated by:

> *r* = exp(*ar* + *br* \* ln(*Pavg*)) = exp(*ar*) \* (*Pavg* \^ *br*)

where

*Pavg* = Average annual site FPI (forest productivity index). *Pavg* is
calculated solely from *M*, as described in the [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm) topic.

*ar* = Constant, Depends on rotation length and region. *ar* is constant
for a given species, but varies between species.

*br* = Multiplier. Depends on the region. Constant for a given species,
but varies between species.

> *x* \^ *y* = *x* to the power of *y* (for example, 5 \^ 2 = 25).

This equation only applies within a range of *Pavg* values in which a
species is expected to occur; outside of this range *r* is set to 1.
Thus, for a given species and in the range of *Pavg* in which the
species is expected to occur, the downloaded *r* only varies with *M*.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
