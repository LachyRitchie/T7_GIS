---
title: Forest Fire
version: 2016
category: Event
original_file: 144_Forest Fire_2016.md
---

[Event Window : *Forest Fire* panel]

Enter the inputs specific to a forest fire event.

**Affected Portion**

The affected portion is the fraction of the forest area being modelled
in which the fire takes place. It is typically the fraction of the plot
area that is burnt or partly burnt.

**Destination Percentages in the Affected Portion**

These destination percentages are applied to the portion of the forest
that is affected by the fire.

The tree material that is affected by the fire either goes to the
atmosphere, goes to the debris, or remains where it is. The debris and
mulch material either goes to the atmosphere, to the inert soil (as
charcoal), or remains where it is. The sum of the two destination
percentages for a single pool must, obviously, be less than or equal to
100%.

Material is moved from the trees to the debris after the amounts of
debris that move have been calculated (tree material cannot go
immediately to the inert soil as a result of a fire).

**Example**. The affected portion is 70%. The stem destination
percentages are 40 to the atmosphere and 10 to the debris --- for a
total stem destination percentage of 50. Then, of all the stem material
on the plot, in this fire 70% * 40% = 28% goes to the atmosphere, 70%
* 10% = 7% becomes deadwood, and the remaining (100% -- 70%) + 70% *
(100% -- 50%) = 65% does not move (stays onsite).

Typically very little if any of the deep minerals will be lost to the
atmosphere, and only a small portion or none of the shallow minerals.

**Clearing Fire**

For a fire to be clearing (that is, to clear the forest of trees), the
affected portion must be 100% and the destination percentages for each
pool (the sum of the destination percentages to the atmosphere and to
the debris) must sum to 100%.

**Leaf Regrowth Percentage**

The leaf regrowth percentage is the percentage of the leaves lost in the
fire that grow back over the next year --- in addition to any other
(that is, regular) growth.

At any stage a tree has some growth potential stored within it that has
not yet been expressed. If a fire burns all the leaves off a tree then
the tree will use this stored growth potential to regrow some leaves so
that regular growth (that is, capturing energy via photosynthesis in the
leaves) can resume.

The leaf regrowth percentage multiplied by the mass of leaves lost in
the fire is added back to the trees, at a uniform rate over the next
year, in addition to any other growth (and regardless of any changes in
the Forest Percentage). This ensures that
a forest that has lost all its leaves will continue to grow.