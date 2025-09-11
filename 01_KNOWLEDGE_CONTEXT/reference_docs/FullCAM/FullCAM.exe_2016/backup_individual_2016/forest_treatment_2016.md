---
title: Forest Treatment
version: 2016
category: Forest Management
original_file: 51_Forest Treatment_2016.md
---

[Event Window : *Forest Treatment* panel]

Enter the inputs specific to a forest treatment event.

**Details**

A forest treatment can be applied to a forest whose growth is being
determined by the tree yield formula [Tree Yield
Formula]. The treatment alters the
growth characteristics of the trees onward from that point in time.

Each treatment has a Type 1 and a Type 2 effect as described in
*Snowden, P (2002) Modelling Type 1 and Type 2 Growth Responses in
Plantations after Application of Fertilizer or Other Silvicultural
Treatments. Forest Ecology and Management 163:229--244*.

Put simply, a Type 1 event occurs during the life of a rotation and has
an effect for a specified period (generally to advance the rate of
growth) in a way that would likely shorten overall rotation length. A
Type 2 event is an increase in site productivity (possibly due to
species change) over the entire rotation period.

**Type 1: Age Advance**

A type 1 treatment moves the forest back (or forth) along the growth-age
curve determined by the tree yield formula, by advancing (or retarding)
the adjusted age of the trees used in the formula. See Growth
Properties.

The tree age used in the tree yield formula is advanced by the *Age
advance due to treatment*, phased in steadily over the years in the
*Advancement period* (which begins starting with the event).

**Example**

Suppose that in May 2004 a pine plantation gets a nitrogen fertiliser
dose, whose effect is to speed up growth by moving the trees six years
along the growth-age curve over the next five years. Suppose that you
are modelling the plantation's growth using the tree yield formula. Then
you would create a forest treatment event in May 2004 whose "Age advance
due to treatment" is 1.00 (because the total extra advance due to the
treatment is +1.00 years --- six years growth in five real years is an
advance of one year) and whose "Advancement period" is 5 years (because
the advance is phased in over five real years).

The effects of multiple treatments ARE cumulative. For example, the
effect of an age advance of 1.0 years over five years starting 2004 and
another age advance of 1.5 years over 3 years starting 2005 would be an
age advance of 2.5 years from 2009 and onward (when both advances are
fully applied).

The effect of age advances persist for the life of the forest, but are
cancelled when the forest is cleared or a coppice created (that is, when
all the aboveground mass of the trees is removed).

The effect of the forest treatments is directly visible in the "Age of
trees used in tree yield formula" output (Element-independent : Timing).

A forest treatment with an age advance of zero should have no effect. In
practice, however, it may have a slight effect if the number of
simulation steps per year is low enough to cause significant graininess
(see Simulation Steps) --- because the
forest treatment event breaks a step into two parts.

**Type 2: Tree Yields**

When the tree yield formula is in use, the maximum aboveground biomass
is equal to the maximum aboveground biomass entered in the *Site* window
(*M* in the tree yield formula, see Tree Yield
Formula) multiplied by the current tree
yield multiplier (*y*).

Thus the "tree yield multiplier" multiplies the tree yield that would
otherwise be computed by the tree yield formula (because the tree yield
is proportional to the maximum aboveground biomass in the tree yield
formula), and likewise multiplies the maximum aboveground forest biomass
allowed on the site.

The tree yield multiplier always starts a simulation at 1.0, and only
changes due to forest treatments. Each type 2 forest treatment replaces
the previous treatment --- the effects of type 2 forest treatments are
NOT cumulative.