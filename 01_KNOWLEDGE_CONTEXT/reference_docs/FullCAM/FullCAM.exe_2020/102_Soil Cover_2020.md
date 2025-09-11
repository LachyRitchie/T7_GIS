+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Soil Cover**

\[[Soil](203_Soil.htm) page : *Agricultural* panel : *Soil Cover*
button\]

This [Time Series Window](135_time-series%20window.htm) is where you
specify whether or not the agricultural soil is covered, in plot models
that only model the agricultural soil (see [Configure the
Plot](6_Configure%20the%20Plot.htm)).

**Agricultural Soil**

The soil cover factor is a rate modifier applied against soil decay as
computed by the [RothC](114_RothC.htm) model. It is set as covered
(default value of 0.6) when a plant exists, slowing down decay. When a
plot is uncovered the value is set to 1, speeding up decay.

When the soil cover is automatically calculated by FullCAM as part of a
multilayer agricultural system, the agricultural soil is considered to
be always covered except after clearing events where crop and pasture is
fully removed.

If you are modelling the soil but not the whole agricultural system,
then you have to tell FullCAM when the soil is covered or not. Soil
cover consists of debris and plants, and it affects the rate of moisture
loss from the soil and thus the agricultural soil water levels.

Enter the soil cover time series to tell FullCAM when there is enough
soil cover to slow down the rate of water loss from the soil. If the
agricultural soil is covered by vegetation or debris (and thus less
prone to drying out) for the whole of the relevant period, then enter 1.
If it is bare for the whole period, enter 0. If it is partly covered for
all of the period, or covered for only part of the period, enter a
number between 0 and 1.

After interpolation and extrapolation to get a soil cover value in each
simulation step, a soil cover value of 0.5 or greater is treated as
covered and a soil over value of less than 0.5 is treated as bare.

**Forest Soil**

Forest soil is considered to be always covered.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
