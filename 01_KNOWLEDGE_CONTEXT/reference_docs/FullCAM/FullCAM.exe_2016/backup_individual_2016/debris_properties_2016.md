---
title: Debris Properties
version: 2016
category: Properties
original_file: 45_Debris Properties_2016.md
---

[Trees page or Crops page :
*Properties of the Species* panel : *Debris* button]

Specify the properties of the debris produced by the current species
(Select a Species). Debris from separate
species is treated entirely separately by FullCAM. See the discussion of
debris vs. mulch in Configure the Plot.

**Resistant Percentages**

The resistant percentage of a tree or crop pool is the percentage of the
mass of the pool that is resistant to decomposition. The interpretation
of "resistant" is left up to you; just be sure to interpret it
consistently as the material flows through the debris and soil.

More precisely, the resistant percentage of a tree or crop pool is the
percentage of material, by mass, that, should it get to the soil as
plant material, would go into the resistant plant material (RPM) pool
rather than the decomposable plant material (DPM) pool. The DPM and RPM
definitions are part of, and thus defined by, the RothC
model.

The tree or crop material that is not resistant is decomposable. When
material from the trees and crops enters the debris, it goes either into
either a decomposable or a resistant debris pool.

**More-Resistant Percentages**

The more-resistant percentage of a pool of resistant debris is the
percentage of the pool, by mass, that, upon entering the mulch, goes to
the *more-resistant plant mulch* pool (the rest of the material entering
the mulch goes to the *less-resistant plant mulch* pool). All the
resistant litter pools are assumed to have the same more-resistant
percentage, so FullCAM only requires a single more-resistant percentage.

**Breakdown Percentages**

The breakdown percentage of a debris pool is the percentage of the pool
that breaks down each year.

Breakdown is the process by which debris becomes: *Atmospheric breakdown
products* - Goes to the atmosphere. Consist mainly of CO~2~.

The breakdown percentage of a debris pool determines how long it takes
material to pass through the debris pool. Setting a breakdown percentage
to 0 means that none of the material in the debris pool ever leaves the
pool (so no plant material reaches the soil). Setting a breakdown
percentage to 100% means that in each simulation step all of the mass in
the debris pool at the beginning of the step moves either to the
atmosphere or to the soil or mulch (thus, no material builds up in the
debris pool).

The breakdown percentage of a debris pool is the percentage lost per
year due to breakdown (that is, 100% less the percentage of the original
material that is still there a year later, if breakdown is the only
process removing material from the pool). It assumes exponential decay
at constant decay rate. Click the exponential decay button for
alternative expressions, a graph, and a fuller explanation.

The chopped wood pools only have material in them due to a Chopper
Roller event, which can only occur in a forest
with no trees.

Typical values for a crop would be for complete breakdown of litter
annually. Table 13 of the report *Greenhouse Gas Emissions from Land Use
Change in Australia: An Integrated Application of the National Carbon
Accounting System* provides some typical rates for native forests:

**Atmospheric Percentages of Breakdown Products**

The atmospheric percentage of the breakdown product of a debris pool is
the percentage of the breakdown products of the debris pool that moves
to the atmosphere (the rest moves to the soil).

**Example.** Suppose that for the decomposable GBF litter pool,

> breakdown percentage = 80
> atmospheric percentage of breakdown product = 60

Then the pool would lose 80% of its mass due to breakdown over a whole
year, if there were no inputs to the pool, and of the broken down
material, 60% goes to the atmosphere and 40% goes to the soil. Thus, if
no inputs were added to the pool for a year, 80% * 60% = 48% of the
pool would go to the atmosphere over the year, 80% * 40% = 32% would go
to the soil, and 20% would still be in the pool at the end of the year.