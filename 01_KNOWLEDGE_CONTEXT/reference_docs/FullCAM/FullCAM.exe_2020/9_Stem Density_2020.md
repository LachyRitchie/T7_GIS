+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Stem Density**

\[[Plant Properties](43_Plant%20Properties.htm) window : *Stem Density*
button\]

This is a [Time Series Window](135_time-series%20window.htm) to
facilitate entering the stem density of a tree species.

**Details**

FullCAM uses masses for all its calculations, so stem density is only
used to convert between stem masses and stem volumes. Stem density is
required if:

- Modelling is of a multilayer forest and any of the following:
  - Tree growth is specified by stem volume increments;
  - The amount of stem material is specified by volume in the initial
    conditions; or
  - The amount of stem material in any tree planting is specified by
    volume.

See the *Properties of the Species Time Series* section of [Growth
Properties](42_Growth%20Properties.htm).

If only the trees are modelled, the plant age used in the stem density
time series is the maximum age of the plants (there are no events in
this configuration, so the maximum and average ages are the same).

Because the stem density is a time series, it may vary with the age of
the tree (set *Years are* to "Years since plants sprouted") or with the
year (set *Years are* to "Calendar years" or "Years since start of
simulation").

The stem density is of the whole stem at the time indicated, not of the
new stem growth in that year. The units are kilograms per cubic metre
(note: most other masses in FullCAM are in tonnes).

The density of stem wood is typically between 300--1,000 kgdm/m^3^. A
compendium of wood densities for Australian tree species can be found in
the NCAS Technical Report No. 18.

Typical values for native forest communities are described in Table 7 of
*Greenhouse Gas Emissions from Land Use Change in Australia: An
Integrated Application of the National Carbon Accounting System*.
Additional species specific values can be extracted from the FullCAM
database.

  Major Vegetation Group (MVG) Class            Wood Density (Basic, kg dry matter/m^3^)
  --------------------------------------------- ------------------------------------------
  Rainforest and Vine Thickets                  500
  Eucalyptus Tall Open Forests                  550
  Eucalyptus Open Forest                        625
  Eucalypt Low Open Forest                      550
  Eucalyptus Woodland                           890
  Acacia Forest and Woodland                    940
  Callitris Forest and Woodland                 650
  Casuarina Forest and Woodland                 860
  Melaleuca Forest and Woodland                 660
  Other Forests and Woodland                    800
  Tropical Eucalyptus Woodland/Grassland        830
  Eucalyptus Open Woodland                      890
  Acacia Open Woodland                          940
  Mallee Woodland and Shrubland                 1060
  Low Closed Forest and Closed Shrubland        1000
  Acacia Shrubland                              940
  Other Shrublands                              940
  Heath                                         900
  Chenopod Shrub, Samphire Shrub and Forbland   900
  Unclassified Native Vegetation                780

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
