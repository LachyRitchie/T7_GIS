+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Initial Soil**

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest* or
*Agricultural* panel : *Soil* button\]

Describe the soil in the plot at the start of the simulation.

See the [RothC](114_RothC.htm) soil pool abbreviations.

**Carbon Masses**

Enter the mass of carbon in the various soil pools, in tonnes per
hectare as a time series.

**Water**

The topsoil moisture deficit (TSMD) is the amount of rainfall, in mm,
required to saturate the topsoil with water. It is a moisture *deficit*,
so the number you enter is zero or positive. The TSMD is used by RothC
to simulate soil decomposition.

The available soil water (ASW) is the amount of water available to the
trees, in mm, to rooting depth. It is used by
[3PG](http://www.fullcam.au/FullCAMServer2020/Help/115_3PG.htm) to
simulate tree growth and by 3PG-lite to compute the forest productivity
index (FPI).

FullCAM uses the two forest water balances, TSMD and ASW, separately and
simultaneously.

In an agricultural system FullCAM only uses the TSMD, but the
agricultural TSMD and the forest water balances (TSMD and ASW) are
completely unconnected.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
