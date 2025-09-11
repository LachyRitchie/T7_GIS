---
title: "Debris Properties"
version: 2020
category: Configuration
original_file: 45_Debris Properties_2020.md
---

\ page or  page :
*Properties of the Species* panel : *Debris* button\]

Specify the properties of the debris produced by the current species
(). Debris from separate
species is treated entirely separately by FullCAM. See the discussion of
debris vs. mulch in .

**Resistant Percentages**

The resistant percentage of a tree or crop pool is the percentage of the
mass of the pool that is resistant to decomposition.

The resistant percentage of a tree or crop pool is the percentage of
material that would go into the resistant plant material (RPM) pool
rather than the decomposable plant material (DPM) pool. The DPM and RPM
definitions are part of the  model.

The tree or crop material that is not resistant is decomposable. When
material from the trees and crops enters the debris, it goes either into
either a decomposable or a resistant debris pool.

**More-Resistant Percentages**

The more-resistant percentage of a pool of resistant debris is the
percentage of the pool that goes to the *more-resistant plant mulch*
pool (the rest of the material entering the mulch goes to the
*less-resistant plant mulch* pool). All the resistant litter pools are
assumed to have the same more-resistant percentage, so FullCAM only
requires a single more-resistant percentage.

**Breakdown Percentages**

The breakdown percentage of a debris pool is the percentage of the pool
that breaks down each year.

Breakdown is the process by which debris becomes a combination of:

1.  *Atmospheric breakdown products* - Goes to the atmosphere. Consist
    mainly of CO~2~.
2.  *Solid breakdown products* - Goes to the soil (if mulch is not
    modelled) or the mulch (if mulch is modelled).

The breakdown percentage of a debris pool determines how long it takes
material to pass through the debris pool. Setting a breakdown percentage
to 0 means that none of the material in the debris pool ever leaves the
pool. Setting a high breakdown percentage means that in each simulation
step most of the debris pool at the beginning of the step moves either
to the atmosphere, soil, or mulch. It assumes exponential decay at
constant decay rate.

The chopped wood pools only have material in them due to a  event, which can only occur in a forest
with no trees.

Typical values for a crop would be for complete breakdown of litter
annually. Table 13 of the report *Greenhouse Gas Emissions from Land Use
Change in Australia: An Integrated Application of the National Carbon
Accounting System* provides some typical rates for native forests:

\

Litter Decomposition Rates for Tree Components.

  Plant Component             Litter Decomposition Rate (1/yr)
  -------------------------- ----------------------------------
  Decomposable Leaf                         1.0
  Resistant Leaf                            1.0
  Decomposable Deadwood                     0.1
  Resistant Deadwood                        0.1
  Decomposable Bark                         0.5
  Resistant Bark                            0.5
  Decomposable Coarse Root                  0.4
  Resistant Coarse Root                     0.1
  Decomposable Fine Root                    0.3
  Resistant Fine Root                       0.4

**Atmospheric Percentages of Breakdown Products**

The atmospheric percentage of the breakdown product of a debris pool is
the percentage of the breakdown products of the debris pool that moves
to the atmosphere (the rest moves to the soil or the mulch).

------------------------------------------------------------------------