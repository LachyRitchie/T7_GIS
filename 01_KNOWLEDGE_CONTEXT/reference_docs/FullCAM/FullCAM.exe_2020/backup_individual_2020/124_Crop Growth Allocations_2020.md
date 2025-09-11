---
title: Crop Growth Allocations
version: 2020
category: crops
original_file: 124_Crop Growth Allocations_2020.md
---

This Time Series Window is one of the crop allocation time series windows, where you specify the relative allocations of yield or NPP (see Yield and Net Primary Production) to the five crop components: GBF (grains, buds, and fruit), stalks, leaves, coarse roots, or fine roots.

**Introduction**

The allocations determine the growth of the component, relative to the other crop components. A high allocation means more growth of the component compared to the other components, a low allocation means the component grows slower than the other components. The crop components all grow in certain proportions to one another at various stages in the plant's life; these allocations are the mechanism for determining those proportions in FullCAM.

Enter an allocation for each period in the time series. The allocations are purely relative: it is not the size of the numbers by themselves that matters, only the ratios between the allocations to the various crop components.

**Examples**

In these examples we will assume yield allocations. Thus we are concerned only with the mass increases of the crop components, relative to one another.

**Example 1**. Suppose in a given period of crop growth that the mass of the stalks in a hectare of crop increases by 2 tonnes, while the mass of leaves on the same hectare increases by 3.5 tonnes. Then the ratio of stalk growth to leaf growth is 3.5 / 2 or 1.75. Thus the relative yield allocations factors of stalks and leaves are respectively x and 1.75*x*,
where *x* is any non-negative number. You might choose any of the following as the relative yield allocations for that year:

- Stalk allocation is 1.0 and leaf allocation is 1.75 (stalks are the reference component).
- Stalk allocation is 0.5714 and leaf allocation is 1.0 (leaves are the reference component)
- Stalk allocation is 100 and leaf allocation is 175.

**Example 2**. Suppose that in a given one month period of crop growth that, in a hectare of crop, the mass increases in the components over the period were as follows:

> 
>   Vegetation Component    tdm/ha value
>   ---------------------- --------------
>   GBF                         2.0
>   Stalks                      5.0
>   Leaves                      20.0
>   Coarse roots                10.0
>   Fine roots                  1.0

One choice of relative yield allocations (all relative to the GBF allocation) for this period would be:

> 
>   Vegetation Component    Relative Yield
>   ---------------------- ----------------
>   GBF                          1.0
>   Stalks                       2.5
>   Leaves                       10.0
>   Coarse roots                 5.0
>   Fine roots                   0.5

Another choice (stalk growth as reference) would be:

> 
>   Vegetation Component    Relative Yield
>   ---------------------- ----------------
>   GBF                          0.4
>   Stalks                       1.0
>   Leaves                       4.0
>   Coarse roots                 2.0
>   Fine roots                   0.2
