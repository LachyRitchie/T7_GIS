---
title: "Growth Properties"
version: 2020
category: Trees
original_file: 42_Growth Properties_2020.md
---

\ page or  page :
*Properties of the Species* panel : *Growth* button\]

These two windows, the tree growth and crop growth windows, are where
you specify how the current species grows ().

**Growth**

"Growth" on this window can mean either "production and turnover" or
"production only", depending on the second setting in the *Properties*
section. See .

**Properties of the Allocations, Increments and Other Species Time
Series**

- 
- 
- 
- 
-  ()
-  ( window)

Specify here whether the plant age used in any species time series is
the average or the maximum age of the plants. This input only applies to
species time series that are expressed in terms of times since the
plants were sprouted (although it is always a required input, regardless
of whether or not any species time series are in terms of times since
sprouting). The average and maximum plant age only differ if there have
been thinning or harvesting events that do not clear the plot, and thus
allow new plants to sprout alongside the older plants --- see the
 and  events.

**Tree Growth Method**

The tree growth method is set in the  panel. The methods
are:

1.  *Increments* - Use one of the increment time series on this window.
    Set whether the allocations and increments are in terms of NPP or
    yields.
2.  *Tree yield formula* - The increments are not used. The allocations,
    like the increments computed by the tree yield formula, are
    automatically in terms of yields.
3.  **
    ( only) - The
    increments are not used. The allocation time series, like the NPP
    computed by 3PG, are automatically in terms of NPP.

**Crop and Pasture Growth Methods**

Crop and pasture growth is always specified by increment time series,
and the allocation and increment time series are set in terms of NPP or
yields. There are two methods for modelling crop and pasture growth:

1.  *Sigmoidal* - Use for annual species. Grows using a sigmoidal curve
    to achieve the target yield amount.
2.  *Perennial* - Used for modelling perennial pastures. The growth
    curve is constructed from an initial value and steply (generally
    monthly) increments of growth and die-off.

A more detailed description on the different types of Crop and Pasture
growth is detailed on the .

**Allocations**

The allocation time series specify the growth of the plant components.
An allocation time series is required for each plant component.

The numbers in the allocation time series are the

*relative* allocations of yield or NPP to the various plant components
and they must be positive numbers. (See .)

**Increments**

An increment time series specifies the increase in one or a combination
of plant components. Only one increment time series is used by the
species --- select one by clicking on the radio button to the left of
the rectangular button displaying the name of the increment time series.

**Parameters in the Tree Yield Formula**

See the . Variation
in site, management, species and other factors greatly impact forest
growth and hence, vary growth curve characteristics.

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

When using  to download tree
species, the values of *G* and *r* or *y* that it downloads to your plot
are based on statistically calibrated models.

*Calculation of G and r for plantation tree species*

Default vaules for plantation tree species are based on statistically
calibrated models that are unique to combinations of regions and
management factors.

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

> *r* = exp(*ar* + *br* \* ln(*M*)) = exp(*ar*) \* (*M* \^ *br*)

where

*M* = As defined above.

*ar* = Constant, Depends on rotation length and region. *ar* is constant
for a given species, but varies between species.

*br* = Multiplier. Depends on the region. Constant for a given species,
but varies between species.

> *x* \^ *y* = *x* to the power of *y* (for example, 5 \^ 2 = 25).

This equation only applies within a range of allowable *r \* M* values
in which a species is expected to occur. If *r\*M* exceeds parameter
*r\*Mmax*, then *r* is set to *r\*Mmax/M* and *G* is assigned parameter
*Gmax*. Conversely, if *r\*M* is less than parameter *r\*Mmin*, then *r*
is set to *r\*Mmin/M* and *G* is assigned parameter *Gmin*. This
provides a growth curve that is consistent with the maximum (*Mmax*) and
minimum (*Mmin*) feasible values of *M* for the species.

------------------------------------------------------------------------