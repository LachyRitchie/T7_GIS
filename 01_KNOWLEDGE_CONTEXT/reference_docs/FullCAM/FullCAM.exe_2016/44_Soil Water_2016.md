+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Soil Water**

\[[Soil](203_Soil.htm) page : *Forest* or *Agricultural* panel : *Water*
button\]

Enter the water-related properties of the soil. It differs slightly
between agricultural and forest systems. See

[Site : Water](12_Site_Water.htm).

**Ratio of Evapotranspiration to Open-Pan Evaporation**

The *Ratio of evapotranspiration to open-pan evaporation* is the ratio
of water lost through evapotranspiration (in mm) to water lost by
open-pan evaporation (in mm).

The [RothC](114_RothC.htm) module uses rainfall and evapotranspiration
to calculate the topsoil moisture deficit (TSMD). The evapotranspiration
is calculated as the product of the open-pan evaporation and this ratio
(which is 0.75 for temperate soils).

Alternatively, obtain monthly evapotranspiration with adequate accuracy
from Muller\'s (1982) collection of meteorological data for sites around
the world, then enter the evapotranspiration data in the open-pan
evaporation time-series and set this ratio to one.

**Ratio of Bare-to-Covered Maximum TSMD**

The *ratio of maximum TSMD for bare soil to maximum TSMD for covered
soil* is the ratio of the maximum topsoil moisture deficit (TSMD) for
bare soil to the maximum TSMD for covered soil.

This input is generally taken to be 0.556 (= 5 / 9). It is used by
[RothC](114_RothC.htm).

**Water Info**

Opens a window of text information about the partition of the total
saturated water capability of the soil into:

- Inaccessible water.
- The maximum topsoil moisture deficit (TSMD) that is accessible by the
  plants.
- Water that drains off.

Water in excess of the amount to saturate the soil is excess, and runs
off.

Requires that nitrogen simulation be switched on in the
[Configuration](150_Configuration.htm) (which enables the bulk density
parameter on the [Soil for the Whole
Plot](46_Soil%20for%20the%20Whole%20Plot.htm) panel of the
[Soil](203_Soil.htm) page.)

**Parameters for the Top Soil Moisture Deficit (TSMD)**

Let

> c = the fraction of the soil that is clay, by weight (see [Soil for
> the Whole Plot](46_Soil%20for%20the%20Whole%20Plot.htm))\
> b = the bulk density of the soil, in t/m^3^ (see [Soil for the Whole
> Plot](46_Soil%20for%20the%20Whole%20Plot.htm))\
> d = depth of soil sampled, in cm (see [Soil
> Properties](3_Soil%20Properties.htm))\
> r = ratio of max TSMD for bare soil to max TSMD for covered soil (see
> above).

Then the maximum TSMD in mm is, by soil cover and RothC version,

(20 + 130 \* c - 100 \* c \* c) \* (d / 23), v26.3, Soil covered\
(20 + 130 \* c - 100 \* c \* c) \* (d / 23) \* r, v26.3, Soil bare

[]{.high
title="these do not appear to be equations, how are they related here and how should they be formatted?"}

(0.688405334 + 4.4746369 \* c - 3.44203 \* c \* c) \* d

\+ ln(9) \* (0.082530817 + 0.5364083 \* c - 0.41268 \* c \* c) \* d,
v26.5, Covered or bare

The depth of inaccessible water (water always in the soil, no matter how
long a dry spell continues, but it is inaccessible to plants) in mm is

> (0.0445 + 0.41 \* c) \* 10 \* d.

The total porosity (WFPS) (the water from totally dry to completely
saturated, after which any additional added water runs off) in mm is

> (1 - b / 2.65) \* 10 \* d.

The maximum drainage water is the total porosity less the maximum TSMD
less the inaccessible water:

total porosity = drainage (soil cannot hold this water, it drains)

> \+ available water (measured by TSMD, varying from 0 to maximum TSMD)\
> + inaccessible water (always present, no matter how dry the weather).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
