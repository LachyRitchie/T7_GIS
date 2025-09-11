---
title: Forest Fire
version: 2020
category: events
original_file: 144_Forest Fire_2020.md
---

Enter the inputs specific to a forest fire event.

**Affected Portion**

The affected portion is the fraction of the forest area that is burnt or
partly burnt.

**Age Adjustment**

The Age Adjustment allows for some additional growth of woody biomass
post-disturbance. This is achieved by effectively re-calculating the
stand age applied in the TYF such that it is less than the actual stand
age. The effective stand age applied in the TYF post Age Adjustment is
calculated from the biomass removed in the disturbance event. This
calculation is based on the TYF and its relationship between age and
above-ground biomass. The effective stand age is assumed to decline
backwards along the TYF such that the more biomass removed, the younger
the stand is assumed to be when growth resumes post-disturbance. Hence,
the impact of the Age Adjustment is dependent on both the amount of
biomass removed and also the stand age at the time of disturbance. For
relatively young stands, this will stimulate growth when the effective
stand age is moved back to be closer to the age of maximum biomass
increments (G years). However for mature stands, the Age Adjustment has
relatively little impact on growth.

It should be noted that the effective stand age used in the TYF may be
different to the actual stand age. Both of these stand ages are
available as outputs of the model.

**Destination Percentages in the Affected Portion**

These destination percentages are applied to the portion of the forest
that is affected by the fire.

The tree material that is affected by the fire can be transferred to the
atmosphere, to the standing dead pool, or to the debris pool. Standing
dead material created in an earlier event can be similarly transferred
to the atmosphere or to debris. Debris and mulch material can be
transferred to the atmosphere or to inert soil (as charcoal). Where the
sum of the destination percentages for a single pool does not sum to
100%, the remainder is taken to stay in its original pool.

Material transferred from one pool to another as a result of the fire
event will not be further affected by the fire event. For example, a
single forest fire event can move stems to debris, but not further to
inert soil.

**Years to Regrow Post-Fire**

If a forest fire event is applied to a forest layer where trees are
planted and growing (ie: not thinned), they will recover to their
previous level of growth within the time period specified. This behavior
should only be used to model fires that are not stand-replacing. If a
stand-replacing fire is being modelled, it should be accompanied by
other events for the thinning and re-planting of trees.

**Using Fire Events to Model Land Clearing**

Forest fire events can be applied following a thinning
(forest removal) event to remove the debris created during thinning,
consistent with the concept of a *conversion burn*. When creating a New
Regime for tree species, such fire events will be
created alongside thinning events.
