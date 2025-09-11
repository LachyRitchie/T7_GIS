---
title: "Standing Dead"
version: 2020
category: General
original_file: 285_StandingDead_2020.md
---

\ page : *Properties of the Species* panel :
*Standing Dead* button\]

Specify the properties of the standing dead pools produced by the
current species (see ).

**About standing dead pools in FullCAM**

The standing dead biomass pools are used to represent slower
decomposition of woody biomass that is either standing dead woody
biomass (for example following fire or drought) or freshly cut
post-clearing or harvesting (for example piled in wind-rows) Such
biomass is expected to slowly senesce at breakdown rates that are slower
than breakdown rates for debris pools (based on litterbag studies) that
have better contact with the soil and organisms that decompose biomass.

In FullCAM, standing dead pools are created through either an assumed
initial standing dead pool or through a disturbance event of fire or
thinning. When the standing dead pool is created, breakdown properties
for these pools must also be set accordingly. Typical values for
different events that create standing dead can be found in the most
recent annual .

**Breakdown Percentages**

The breakdown percentage of the standing dead pool is the percentage of
the pool that breaks down each year due to the freshly cut or burnt
pools of standing dead material slowly senescing.

Breakdown is the process by which standing dead material senesces to
becomes a combination of:

- *Atmospheric breakdown products* - Goes to the atmosphere. Consist
  mainly of CO2.
- *Solid breakdown products* - Goes to the debris pool.

The breakdown percentage of a standing dead pool determines how long it
takes material to pass through the standing dead pool. Setting a
breakdown percentage to 0 means that none of the material in the
standing dead pool ever leaves the pool. Setting a high breakdown
percentage means that in each simulation step most of the standing dead
pool at the beginning of the step moves either to the atmosphere or
debris. It assumes exponential decay at a constant decay rate.

**Atmospheric Percentages of Breakdown Products**

The atmospheric percentage of the breakdown product of a standing dead
pool is the percentage of the breakdown products of the standing dead
pool that moves to the atmosphere (the rest moves to the corresponding
debris pool).

------------------------------------------------------------------------