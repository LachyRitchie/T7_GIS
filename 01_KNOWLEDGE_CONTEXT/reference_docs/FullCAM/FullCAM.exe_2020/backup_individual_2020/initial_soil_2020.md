---
title: "Initial Soil"
version: 2020
category: Soil
original_file: 32_Initial Soil_2020.md
---

\ page : *Forest* or
*Agricultural* panel : *Soil* button\]

Describe the soil in the plot at the start of the simulation.

See the  soil pool abbreviations.

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
 to
simulate tree growth and by 3PG-lite to compute the forest productivity
index (FPI).

FullCAM uses the two forest water balances, TSMD and ASW, separately and
simultaneously.

In an agricultural system FullCAM only uses the TSMD, but the
agricultural TSMD and the forest water balances (TSMD and ASW) are
completely unconnected.

------------------------------------------------------------------------