+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

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

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
