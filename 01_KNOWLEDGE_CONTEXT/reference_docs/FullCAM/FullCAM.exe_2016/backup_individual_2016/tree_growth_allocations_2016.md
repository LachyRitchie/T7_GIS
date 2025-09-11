---
title: Tree Growth Allocations
version: 2016
category: Growth
original_file: 112_Tree Growth Allocations_2016.md
---

[Growth Properties window (for trees) :
Any of the *Allocations* buttons]

This time-series Window is one of the
tree allocation time-series windows, where you specify the relative
allocations of yield or NPP (see Yield and
NPP) to the six tree
components: stems, branches, bark, leaves, coarse roots, or fine roots.

**Introduction**

The allocations determine the growth of the component, relative to the
other tree components. A high allocation means more growth of the
component compared to the other components, a low allocation means the
component grows slower than the other components. The tree components
all grow in certain proportions to one another at various stages in the
tree's life; these allocations are the mechanism for determining those
proportions in FullCAM.

Enter an allocation for each period in the time-series. The allocations
are purely relative: it is not the size of the numbers by themselves
that matters, only the ratios between the allocations to the various
tree components.

**Examples**

In these examples we will assume yield allocations. Thus we are
concerned only with the mass increases of the tree components, relative
to one another.

Typically the stem (or bole) growth is your reference, and the mass
increases of the other components relative to the stems are noted. In
this case, set the relative stem growth to 1.0 and set the other
relative growths accordingly. For example, if leaf mass increment is a
half of the stem mass increment (in tdm/ha, over the relevant time
period) then set the stem allocation to 1.0 and the leaf allocation to
0.5.

**Example 1**. Suppose that, in a given year of tree growth, the mass of
the stems in a hectare of trees increases by 15 tonnes, while the mass
of bark on the same hectare increases by 5 tonnes. Then the ratio of
stem growth to bark growth is 15 / 5 = 3. Thus the relative growth
factors of stems and bark are respectively 3x and x, where x is any
non-negative number. You might choose any of the following as the
relative growths for that year:

- Stem allocation is 1.0 and bark allocation is 0.33 (the obvious
  choice).
- Stem allocation is 3.0 and bark allocation is 1.0
- Stem allocation is 6.0 and bark allocation is 2.0.

And so on.

**Example 2**. Suppose that in a given three month period of tree growth
that, in a hectare of trees, the mass increases in the components over
the period were as follows:

> 
>   Vegetation Component   Value in tdm/ha
>   ---------------------- -----------------
>   Stems                  0.25
>   Branches               0.50
>   Bark                   0.125
>   Leaves                 0.75
>   Coarse roots           0.25
>   Fine roots             0.125

The typical choice of yield allocations (namely, all relative to the
stems) for this period would be:

> 
>   Vegetation Component   Yield Allocation
>   ---------------------- ------------------
>   Stems                  1.0
>   Branches               2.0
>   Bark                   0.5
>   Leaves                 3.0
>   Coarse roots           1.0
>   Fine roots             0.0

Another choice (branches as reference) would be:

> 
>   Vegetation Component   Yield Allocation
>   ---------------------- ------------------
>   Stems                  0.5
>   Branches               1.0
>   Bark                   0.25
>   Leaves                 1.5
>   Coarse roots           0.5
>   Fine roots             0.25

And so on.

Data on allocations to various tree components can be found in the NCAS
Technical Reports
5a,
5b,
17,
25
and
44
(17
is the synthesis report).

General values for major vegetation types can be found in Table 3 of the
report *Greenhouse Gas Emissions from Land Use Change in Australia:
Results of the National Carbon Accounting System 1988--2001*. Additional
species specific allocations can be extracted from the FullCAM database.