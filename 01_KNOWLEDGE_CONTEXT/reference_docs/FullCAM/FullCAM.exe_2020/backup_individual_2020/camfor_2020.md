---
title: CAMFor
version: 2020
category: Simulation
original_file: 77_CAMFor_2020.md
---

The CAMFor model is one of the Constituent Models In
FullCAM.

**Description**

The name "CAMFor" comes from *C*arbon *A*ccounting *M*odel for
*FOR*ests.

CAMFor is a model of a forest ecosystem --- trees, debris, soil,
minerals, and products. It models all movements of carbon between a
forest system and the atmosphere.

CAMFor is a calculation tool, moving material around the forest system
with simple inputs such as ratios, rate constants, and growth tables. It
models processes such as growth, turnover, and decomposition that occur
continuously. It models events, such as planting, thinning, and fires.
It always tracks the carbon in each part of the system, and optionally
tracks the nitrogen as well. It can operate at any time scale from
yearly steps down to hourly steps.

CAMFor is a framework model. A tree growth model, a mulch model, and a
soil model can be plugged into it to provide more detailed modelling of
these layers. CAMFor does not model the soil itself; it requires a
specialist soil model to model the soil for it.

**Credits**

The CAMFor model within FullCAM finds its conceptual foundations in a
public domain FORTRAN program called *CO~2~Fix*, published in October
1990 by Frits Mohren, Kees Klein Goldewik, De Dorrchamp, Wageningen.

CAMFor should be cited as Richards, GP; Evans, DMW; (2000) Carbon
Accounting Model for Forests (CAMFor v3.35) User Manual, National Carbon
Accounting System Technical Report No.
26,
Australian Greenhouse Office.
