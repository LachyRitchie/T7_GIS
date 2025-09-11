---
title: Stem Loss and Stalk Loss
version: 2020
category: plants
original_file: 19_Stem Loss and Stalk Loss_2020.md
---

This Time Series Window is where you
enter the stem loss rate of a tree species or the stalk loss rate of a
crop species. See Mortality.

**Details**

| Vegetation Type | Definition of 'Plant Death' |
|-----------------|-------------------------------|
| Forest          | stem death                    |
| Agricultural    | stalk death                   |

This time series specifies plant mortality --- the percentage of stems
or stalks (and thus plants) that die per year. To make the mortality
rate a function of tree age, set the *Years are* in the *Timing* panel
to *Years since plants sprouted*.

The type of plant age to use in this time series, if it is expressed in
years since the plants sprouted, is chosen in the *Properties of the
Species Time Series* section in the Growth
Properties window.

The percentages in this time series are limited to less than 100% ---
use one of the Events to kill the whole forest or
crop.
