---
title: Initial Trees
version: 2016
category: Trees
original_file: 185_Initial Trees_2016.md
---

[Trees page : *Initial Trees* button]

[Initial Conditions page : *Forest*
panel : *Trees* button]

Describe the trees growing in the forest system at the start of the
simulation.

**Species**

[Only present when the window is accessed via the Initial
Conditions page.]

Even if there are no trees growing, there may be tree material in the
Initial Debris, so you **must** specify an
initial species.

Enter the initial tree species. Only one tree species can grow in the
forest at any one time (see the Select a
Species panel), so there can only be one
initial tree species. The species listed on the pull down on the menu
are those on the *Trees* page. The menu contains only a blank line if
there are no tree species, in which case you need to create a new
species on the *Trees* page.

The initial tree species is the (only) species of any trees growing in
the forest. Also, any debris in the forest, or any forest products in
use or in the landfill, are assumed to all belong to that species.

**Existence**

[Only present when the window is accessed via the Initial
Conditions page.]

Specify whether there are trees growing in the forest at the beginning
of the simulation. If there are not, then the forest is clear and the
other inputs need not be entered.

**Specify Tree Size By**

Choose the method by which you are going to specify the initial size of
the tree components.

Stems may be specified by either volume or mass; all the other
components must be specified by mass. (The Stem
Density needs to be specified as an input,
regardless of what you choose here.)

Alternatively, you can specify all the tree component sizes as
percentages of the maximum tree biomass (presumed to only occur in a
mature, undisturbed states). Thus, if the percentages of the components
add to 100%, the trees will be at their maximum biomass limit. The
maximum tree biomass *T* is computed from the maximum aboveground
biomass of the trees *A*, by:

**Masses**

The masses of the various tree components at the start of the
simulation, in tonnes of dry matter per hectare.

Note that these are true masses, not carbon masses as in some other
inputs. The "mass" of some material is the weight of all of the
material; the "carbon mass" of the material is the weight of the carbon
in the material. The carbon masses of most tree components are about
half of their masses.

Convert between the masses and carbon masses using the carbon
percentages (see Plant Properties).

If CAMFor is on, enter the six CAMFor tree components: stem, branches,
bark, leaves, coarse roots, fine roots.

**Volumes**

The stem volume is the total volume of stems in the forest, in cubic
meters per hectare. This volume will be converted to a mass in the
FullCAM simulation by multiplying it by the stem density. Please be sure
that the stem-density time-series for the initial tree species is
correct!

**Ages**

Tree ages are used to access the tree time-series.

The age of the oldest trees in the forest is the age of the forest ---
the number of years since the current forest was planted, plus the age
of the trees when they were planted.

The average age of the trees in the forest reflects the new trees that
are assumed to have grown after removal of tree stems in past thinnings.
The average tree age must be less than the age of the oldest trees. (The
average age is also used as initial value of the growth-age for the
yield formula, if the yield formula is used for the initial tree
species.)

The average age must not exceed the age of the oldest trees, or both
boxes are coloured red to indicate that the data is incomplete.

Unless there are thinning events that thin some but not all of the tree
stems, the age of the oldest trees will equal the average age of the
trees.

**Numbers of Trees**

Enter the number of stems per hectare, which is the stand stocking
level.

**Insert Standard Values**

[Only present when the window is accessed via the Initial
Conditions page.]

Press the *Insert Standard Values* button to insert the standard initial
tree values. The button is disabled if the standard initial trees
information for the species is not ready (incomplete or has invalid
values).