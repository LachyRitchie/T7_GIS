---
title: CAMAg
version: 2020
category: Simulation
original_file: 78_CAMAg_2020.md
---

The CAMAg model is one of the Constituent Models In
FullCAM.

**Description**

CAMAg is a model for agricultural ecosystems --- crop, debris, soil,
minerals, and products. It models all movements of carbon between an
agricultural system and the atmosphere.

CAMAg is a calculation tool, moving material around the agricultural
system. It models processes such as growth, turnover, and decomposition
that occur continuously. It models events, such as planting, harvest,
and fires. It tracks the carbon in each part of the system, and
optionally tracks the nitrogen as well. It can operate at any time scale
from yearly steps down to hourly steps. It tracks animal fodder as a
product, thus modelling emissions due to grazing.

CAMAg is a framework model. A mulch model and a soil model can be
plugged into it to provide more detailed modelling of these layers.
CAMAg does not model the soil itself; it requires a specialist soil
model to model the soil for it.
