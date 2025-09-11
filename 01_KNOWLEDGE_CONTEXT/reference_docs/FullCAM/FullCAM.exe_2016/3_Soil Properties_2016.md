+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Soil Properties**

\[[Soil](203_Soil.htm) page : *Forest* or *Agricultural* panel :
*Properties* button\]

Enter the general properties of the soil. See the [RothC](114_RothC.htm)
soil pool abbreviations.

**Soil Properties**

The *HUM encapsulation percentage* is the percentage of the HUM carbon
mass that is encapsulated by clay, and thus becomes inert, each year.
Encapsulation transfers carbon to the inert pool, which is very
sensitive to build-up over time, so the encapsulation percentage is
typically pretty low. In sandy soils the HUM encapsulation percentage is
typically zero, and the inert pool only builds up due to fires.

The *Depth of soil sampled* is the maximum depth soil, in centimetres,
that is being modelled. Typically equal to 30 cm. Soil above the sample
depth is considered shallow and topsoil. Soil below the sample depth is
ignored, except that if nitrogen simulation is switched on in the
[Configuration](150_Configuration.htm) then there is a deep ammonium
pool and a deep nitrate pool --- see [Mineral Nitrogen
Model](253_Mineral%20Nitrogen%20Model.htm)).

The *pH of sampled soil* is the pH of the shallow soil, which is used to
compute nitrification rates if nitrogen simulation is switched on. A
soil that is neither acidic not alkaline (or basic) has a pH of 7.0,
less if it is acidic (minimum 0), more if it is alkaline (maximum 14).

**Decomposition Rate Multipliers**

The quantity of carbon in each [RothC](114_RothC.htm) soil pool (DPM,
RPM, BIO-F, BIO-S, HUM) decays exponentially with time if there is no
new carbon flowing into the pool: After a time *t* (in years), the
fraction of the original carbon still in the pool is

> [y]{style="font-size:large;"} = [x]{style="font-size:large"}
> ^(--*abct*)^
>
> where
>
> *a* = rate modifier for temperature\
> *b* = rate modifier for topsoil moisture\
> *c* = rate modifier for soil cover\
> *k* = decomposition rate multiplier \[1/y\].

*a*, *b* and *c* are the same for all pools, but *k* can be different
for different pools.

In a step of *T* years (*T* \<= 1), the fraction of the carbon that is
in the pool at the beginning of the step and that leaves the pool during
the step (the "decomposition fraction" of the pool for that step) is
thus

> [y]{style="font-size:large;"} = [x]{style="font-size:large"}
> ^(--*abckT*)^
>
> Typically, the decomposition rate multipliers are approximately:
>
> *k*
>
>   ------- -----------------------------------------------
>   10.00   DPM
>   0.30    RPM
>   0.66    BIO-F (only entered in version 26.3 of RothC)
>   0.66    BIO-S (only entered in version 26.3 of RothC)
>   0.02    HUM
>   ------- -----------------------------------------------

In version 26.5 of RothC: The BIO-F and BIO-S decomposition rate
multipliers when the soil is bare are computed by RothC. When the soil
is covered, both of these multipliers are further multiplied by the
*BIO-F and BIO-S modifier*, which is typically about 3.25. Note that the
forest soil is always covered, but covering of the agricultural soil
depends on a time-series that is entered.

**Plant Material, Biomass, and Humus Destination Percentages**

Any material in the active soil pools that undergoes decomposition
moves. In each step of the simulation, material moves to the various
active soil carbon pools and to the atmosphere. The fraction of moving
material that leaves the soil for the atmosphere as gas is computed by a
RothC formula from the clay content of the soil (a higher clay content
means that a lower fraction leaves as gas). The remainder of the moving
material, called the "solids", moves to another or the same active soil
pool.

Moving material that is not given off as gas moves to the BIO-F, BIO-S
and HUM pools. The percentages moving to these pools are the same for
each of the plant material (DPM and RPM) and biomass (BIO-F and BIO-S)
pools. In version 26.3 of RothC, no material moves from the plant
material or biomass pools to the BIO-S pool, or from the HUM pool to the
BIO-F pool. The destination percentages add to 100%; the HUM percentage
is automatically calculated.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
