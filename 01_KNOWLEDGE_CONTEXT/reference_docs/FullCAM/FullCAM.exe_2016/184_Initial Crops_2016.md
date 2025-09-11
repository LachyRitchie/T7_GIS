+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Initial Crops**

\[[Crops](216_Crops.htm) page : *Initial Crops* button\]

\[[Initial Conditions](205_Initial%20Conditions.htm) page :
*Agricultural* panel : *Crops* button\]

Describe the crop growing in the agricultural system at the start of the
simulation.

**Species**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Even if there are no crops growing, there may be crop material in the
[Initial Debris](31_Initial%20Debris.htm), so you **must** specify an
initial species.

Enter the initial crop species. Only one crop species can grow in the
forest at once (see the [Select a Species](56_Select%20a%20Species.htm)
panel), so there can only be one initial crop species. The species on
the menu are those on the *Crops* page. The menu contains only a blank
line if there are no crop species, in which case you need to create a
new species on the *Crops* page.

The initial crop species is the (only) species of any crop plants
growing in the agricultural system. Also, any debris in the agricultural
system, or any agricultural products in use or in the landfill, are
assumed to belong to that species.

**Existence**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Specify whether there is a crop of plants growing in the agricultural
system at the beginning of the simulation. If there is not, then the
agricultural system is clear and the other inputs need not be entered.

**Ages**

Crop ages are used to access the crop time-series.

The age of the oldest plants in the crop is the age of the crop --- the
number of years since the current crop was planted, plus the age of the
plants when they were planted.

The average age of the plants in the crop reflects the new plants that
are assumed to have grown after removal of plants in any past partial
harvestings. The average plant age must be less than the age of the
oldest plants.

The average age must not exceed the age of the oldest plants, or both
boxes go red.

Unless there are harvesting events that remove some but not all of the
crop, the age of the oldest plants will equal the average age of the
plants.

**Masses**

The masses of the various crop components at the start of the
simulation, in tonnes per hectare.

Note that these are true masses, not carbon masses as in some other
inputs. The "mass" of some material is the weight of all of the
material; the "carbon mass" of the material is the weight of the carbon
in the material. The carbon masses of most crop components are about
half of their masses.

Convert between the masses and carbon masses using the carbon fractions
(see [Plant Properties](43_Plant%20Properties.htm)).

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\]

Press the *Insert Standard Values* button to insert the standard initial
crop values. The button is disabled if the standard initial crop
information for the species is not ready (incomplete or has invalid
values).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
