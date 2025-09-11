---
title: "Site : Maximum Aboveground Biomass"
version: 2020
category: Site
original_file: 36_Site_Maximum Aboveground Biomass_2020.md
---

\ page : *Maximum Aboveground Biomass* panel\]

Enter information about the maximum aboveground biomass that can be
supported by the plot.

The *aboveground biomass* is the combined mass of the aboveground plant
components:

- For tree systems: Stems, branches, bark, and leaves
- For agricultural systems: Grains, buds, fruit, stalks, and leaves.

It does not include the roots, debris, standing dead material, mulch, or
soil matter. It is measured in tonnes per hectare of dry matter
(tDM/ha).

The maximum aboveground biomass provides an upper limit on the amount of
aboveground biomass of trees and crops that can exist on the plot during
a simulation.

The growth of plants is calculated as specified under . After growth and turnover has
been calculated for the plant components, if the aboveground biomass of
the plants exceeds the maximum aboveground biomass for the site, then
the masses of all of the plant components are reduced, in proportion to
their pre-reduction masses.

If the aboveground biomass of the plants never exceeds the maximum
aboveground biomass, then the maximum aboveground biomass has no effect
on the simulation --- except if the Tree Yield Formula is used, in which
case the maximum forest aboveground biomass affects the tree growth rate
at all times (see ).

If you do not wish there to be any upper limit on growth in cases where
the Tree Yield Formula is not being applied, simply set the maximum
aboveground biomass to a number high enough so as not to act as a
limiting effect (such as 9,999) --- effectively rendering it
inoperative.

**Relationship to the Tree Yield Formula**

For tree systems and mixed systems, if the option to use the  is used (see ), the aboveground
biomass of the trees will asymptotically approach the specified maximum
aboveground biomass.

Information on aboveground biomass estimates can be found in NCAS
Technical Report No.44 and Roxburgh *et al.* 2019. Values for *Maximum
Aboveground Biomass* can be downloaded from the FullCAM server using
 for specified spatial
coordinates.

,
*Spatial Estimates of Biomass in \'Mature\' Native Vegetation* (2003).

Roxburgh, S., Karunaratne, S., Paul, K., Lucas, R., Armston, J., Sun,
J., 2019. *A revised above-ground maximum biomass layer for the
Australian continent*. Forest Ecology and Management **432**: 264--275.

**Plantation Species simulations**

When simulating a plantation tree species, changing this maximum
aboveground biomass (M) value will make the  default parameters (G and *r*)
invalid. Therefore you will need to recalibrate these tree yield formula
parameters.

------------------------------------------------------------------------