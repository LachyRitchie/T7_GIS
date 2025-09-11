+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Soil for the Whole Plot**

\[[Soil](203_Soil.htm) page : *Whole Plot* panel\]

Enter properties of the soil shared by both the forest and agricultural
soil.

**Clay Percentage**

Percentage of the soil that is clay. *[NCAS Technical Report No
12](reps/TR12%20Pre-Clearing%20Soil%20Carbon%20Levels%20in%20Australia.pdf){target="reps12"}*
provides clay percentage values for major soil types.

Affects the parameters for decomposition of organic soil pools (the
[RothC](114_RothC.htm) pools), and the parameters for the water content
of the soil (namely the topsoil moisture deficit or TSMD).

**Bulk Density**

Soil consists of:

- Particles --- either clay or quartz (in this context \"quartz\" just
  means \"not-clay\")
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

Clarifications:

  ---------- --------------------------------------------------------------------------------
  Porosity   = pore space / bulk volume \[a fraction\]
             = (bulk volume - particle volume) / bulk volume
             = 1 - \[ particle volume \* particle mass) / (bulk volume \* particle mass) \]
             = 1 - (bulk density) / (particle mass / particle volume)
             = 1 - (bulk density) / (particle density)
  WFPS       = water filled pore space fraction
             = water-filled-pore-space / total-pore-space \[a fraction\]
  ---------- --------------------------------------------------------------------------------

Water is always measured in mm of clear water, a 1-D measurement that
suffices for volumes in soils.

See [Soil Water](44_Soil%20Water.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
