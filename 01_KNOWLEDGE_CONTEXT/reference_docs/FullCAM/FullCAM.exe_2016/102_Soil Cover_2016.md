+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Soil Cover**

\[[Soil](203_Soil.htm) page : *Agricultural* panel : *Soil Cover*
button\]

This [time-series Window](135_time-series%20window.htm) is where you
specify whether or not the agricultural soil is covered, in plot models
that only model the agricultural soil (see [Configure the
Plot](6_Configure%20the%20Plot.htm)).

**Agricultural Soil**

If you are modelling the soil but not the whole agricultural system,
then you have to tell FullCAM when the soil is covered or not. Soil
cover consists of debris and plants, and it affects the rate of moisture
loss from the soil and thus the agricultural soil water levels (more
precisely, the topsoil moisture deficit computed by the
[RothC](114_RothC.htm) model).

Enter the soil cover time-series to tell FullCAM when there is enough
soil cover to slow down the rate of water loss from the soil. If the
agricultural soil is covered by vegetation or debris (and thus less
prone to drying out) for the whole of the relevant period, then enter 1.
If it is bare for the whole period, enter 0. If it is partly covered for
all of the period, or covered for only part of the period, enter a
number between 0 and 1.

After interpolation and extrapolation to get a soil cover value in each
simulation step, a soil cover value of 0.5 or greater is treated as
covered and a soil over value of less than 0.5 is treated as bare.

When the soil cover is automatically calculated by FullCAM (that is,
when the soil is modelled as part of a multi-layer agricultural system),
the agricultural soil is considered to be always covered except during:

- The period between ploughing and the subsequent planting
- The period between an agricultural fire that immediately follows a
  herbicide, and the subsequent planting

The herbicides, ploughs and fires mentioned here are ignored if they
affect less than 50% of the plot.

**Forest Soil**

Forest soil is considered to be always covered.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
