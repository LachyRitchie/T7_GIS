---
title: "Soil for the Whole Plot"
version: 2020
category: Soil
original_file: 46_Soil for the Whole Plot_2020.md
---

\ page : *Whole Plot* panel\]

Enter properties of the soil shared by both the forest and agricultural
soil.

**Clay Percentage**

Percentage of the soil that is clay. *{target="_blank"}*
provides clay percentage values for major soil types.

Affects the parameters for decomposition of organic soil pools (the
 pools), and the parameters for the water content
of the soil (the topsoil moisture deficit or TSMD).

**Bulk Density**

Soil consists of:

- Particles --- either clay or quartz (in this context "quartz" just
  means "not-clay")
- Pore space --- the voids between the particles, usually filled with
  air or water.

The bulk density of the soil is the particle mass divided by its bulk
volume, where the bulk volume is the volume of the particles and pores
together in soil. Thus the bulk density is just the density of the soil
as it exists in the ground, treated as a bulk object (that is, a solid
object where we ignore the tiny holes / pores, so its boundary is as we
would normally see it from a couple of meters away). Units: tonnes per
cubic meter.

Used to compute the amount of water required to saturate the shallow
soil (namely the mm of water added from the point at which the TSMD is
zero until draining starts to occur), that is, the total porosity of the
soil expressed in mm of water.

By the way:

  ---------- --------------------------------------------------------------------------------
  Porosity   = pore space / bulk volume \.

------------------------------------------------------------------------