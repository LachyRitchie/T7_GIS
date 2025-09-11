+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Grazing Change**

\[[Event Window](137_Event%20Window.htm) : *Grazing Change* panel\]

Enter the grazing inputs that apply from this event until the next
grazing event. A plot simulation always starts with grazing switched
off. Grazing occurs to plants after production and turnover; it does not
affect either production or turnover.

**New Grazing Levels**

Specify the new level of grazing, to apply from this event until the
next grazing event.

In any aboveground plant or litter pool, if the amount of specified
grazing exceeds the amount of material in the pool then the grazing is
reduced such that all of that pool is eaten away (that is, the pool mass
is prevented from going negative).

Like all inputs in FullCAM, the grazing inputs apply to the crop or
litter as it is at the beginning of each processing time period (at the
later of the beginning of the last step or after the last event).

**New Root Slough**

Root sloughing keeps the root mass in proportion to the aboveground
plant mass.

Example: Suppose grazers remove 90% of the aboveground plant mass . If
root sloughing is on, the plant will turn over 90% of its roots to
debris --- except that if the maximum root slough percentage is less
than 90%, the percentage of roots sloughed off is the maximum root
slough percentage. But if root sloughing is off, then the plants will
keep all their roots regardless of how fiercely their aboveground mass
is grazed.

**New Fodder Destination Percentages**

*Fodder* is the plant material eaten by any grazing animals. The fodder
destination percentages specify where the carbon and nitrogen in the
fodder moves to after passing through the grazing animals.

Material gets to the DPM and RPM (see [RothC](114_RothC.htm)) via manure
(typically around 30%) and urine; it gets to the mineral pool via urine;
it gets to the atmosphere via urine, manure and enteric fermentation.

Typically all N from manure and urine goes into shallow ammonium.

The sum of the destination percentages for each of carbon and nitrogen
is always 100%; the last destination percentage in each column (animal
products) is calculated automatically for you.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
