---
title: RothC
version: 2016
category: Models
original_file: 114_RothC_2016.md
---

The RothC Soil model is one of the Constituent Models
In FullCAM.

**Description**

The Rothamsted Carbon
Model (RothC) model is a soil carbon model. RothC models the turnover of
organic carbon in non-waterlogged soils, taking into account clay
content, temperature, moisture content, plant and manure inputs, and
plant cover. RothC tracks the amount of microbes and several soil pools
containing active carbon.

The name "RothC" comes from
ROTHamsted-Institute
active soil Carbon model.

**Active Soil Pools**

RothC partitions the active soil into five components (soil pools):

  Component   Description
  -----------
  DPM         decomposable plant matter
  RPM         resistant plant matter
  BIO-F       fast decomposing biomass
  BIO-S       slow decomposing biomass
  HUM         humified organic matter.

The definitions of these soil pools can be found through the Rothamsted
website.

The DPM pool tends to small and transient, because material moves
quickly from DPM to BIO-F, BIO-S, and HUM (because it decomposes
easily).

The RPM pool is sometimes called "particulate organic matter" (POM)
elsewhere.

Typically the fraction of total soil carbon in the BIO-F and BIO-S pools
is very small --- these are small but very active pools of microbes. In
practice it is often difficult to impossible to measure BIO-F and BIO-S.

**RothC Version**

If the plot model includes the soil then the RothC
model will be used to simulate the soil (RothC version **26.3**; fully
calibrated for Australian conditions).

If you model a mixed forest and agricultural system and model the soil,
then FullCAM will always use the same version of RothC for both the
forest soil and the agricultural soil.

**Inert Soil**

The inert (or "inactive") soil is all in the inert pool in FullCAM (see
Soil). The inert material is sometimes called "charcoal
and charred plant material" (CHAR) elsewhere. In FullCAM the inert pool
is outside of RothC --- it is instead managed by CAMFor
or CAMAg --- even though the RothC model elsewhere has
an inert pool. The inert pool is simply a reservoir of soil material
that is very unlikely to move to any other pool in the foreseeable
future. It mainly consists of charcoal or material that is physically
encapsulated (perhaps by clay).

**Credits**

The RothC model within FullCAM implements the FORTRAN programs
"ROTHC-26.3" and "ROTHC-26.5_32" by K.W. Coleman, D.S Jenkinson, L.C.
Parry and J.H. Rayner. It draws on papers by Jenkinson and Coleman,
amongst others.

The model was enhanced by the CSIRO in Adelaide (Jan Skjemstad, +618
8303 8427) and the Australian Greenhouse Office. Enhancements include
the ability to use the historical weather time-series rather than
average weather (including the topsoil moisture deficit (TSMD)
computations). Equilibrium and radiocarbon dating computations were
omitted.