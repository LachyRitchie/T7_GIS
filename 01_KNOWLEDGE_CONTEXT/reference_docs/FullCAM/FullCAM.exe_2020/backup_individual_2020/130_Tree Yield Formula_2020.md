---
title: Tree Yield Formula
version: 2020
category: trees
original_file: 130_Tree Yield Formula_2020.md
---

The tree yield formula is one of the tree production methods in a
multilayer forest (see Configure Tree Production). It is an equation
for calculating tree growth, whose main inputs are maximum aboveground
biomass, tree age, and productivity.

**The Tree Yield Formula**

The tree yield formula for tree growth is

> *T(A) = r * M * y \** exp(*--k / d*)

where

*T* = Aboveground mass of the trees, in tdm/ha, if there was constant
(and thus average) productivity

*A* = Age of the tree (either the age of the oldest trees, or the
average age of the trees --- see the Growth
Properties window), in years

*M* = Maximum aboveground biomass of trees, in tdm/ha
(Site page)

*r* = Maximum aboveground biomass multiplier (Growth
Properties window), a species-dependent
modifier of *M* (thus the maximum aboveground biomass used is *r * M*)

*y* = Tree yield multiplier. Initially equal to one in any plot
simulation, then changed to the type 2 growth multiplier of the latest
forest treatment event

*k* = *2 * G* -- 1.25.

> *G* = Tree age of maximum growth, in years (Growth
> Properties window, expressed as a
> multiplier of the maximum aboveground biomass plus a constant). This
> is also usually the age at which the canopy closes.

*d* = Adjusted age of the trees, in years

> = *A* + sum over each treatment of
> 
>   --------------------- -- --------------------------------
>   0                        if *A <= W*
>   *v * (A -- W) / U*      if *A >= W* and *A <= W + U*
>   *v*                      if *A > W + U*
>   --------------------- -- --------------------------------
> 
> where, for each treatment undergone by the forest, specified by the
> type 1 parameters in the forest treatment events,
> 
> *v* = the age advance due to the treatment, either positive or
> negative, in years\
> *U* = the advancement period, in years\
> *W* = the age (of same type as *A*) at which the treatment was
> applied, in years.

**Notes**

*T* asymptotically approaches *r * M * y* from below as *d* increases.
Note that exp(0) = 1, exp(negative) < 1, and exp(any) > 0. The maximum
aboveground biomass for trees when the tree yield formula is in use is
*r * M * y*. The forest treatment events move the forest back and
forth along the growth-age curve described by the tree yield formula,
where each age advance is phased in linearly over the advancement
period. When the tree yield formula is in use (that is, the current tree
species uses the tree yield formula to determine its growth), all
age-based properties of the trees use the adjusted age of the trees
(*d*), including the Tree Growth
Allocations,
Mortality, and Stem Density
time series.

**Non-Constant Productivity**

The tree yield formula above gives the generic biomass yield curve under
average climatic conditions. To account for year-to-year variations in
climatic data, the tree yield formula-predicted increment in aboveground
biomass is moderated up or down at annual time steps based on the ratio
of the forest productivity index to the average forest productivity
index. See Forest Productivity
Index.

**Data Inputs to the Formula**

Thus the data inputs to the tree yield formula are:

1.  *M*, the maximum aboveground biomass
2.  *r*, the species-multiplier of the maximum aboveground biomass
3.  *G*, the tree age of maximum growth
4.  *FPI*, the time series of the forest productivity index
5.  *y*, the tree yield multiplier (which can be changed by type 2
    forest treatment events)
6.  The age advances specified by the type 1 forest treatment events.

On the Departmental Server, *r* and *G*
are calculated from other inputs. See Growth
Properties.
