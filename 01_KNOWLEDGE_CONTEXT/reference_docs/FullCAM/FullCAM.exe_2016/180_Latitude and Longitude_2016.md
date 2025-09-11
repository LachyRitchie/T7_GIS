+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Latitude and Longitude**

The use of latitude and longitude in FullCAM.

**Decimal Degrees**

Always enter latitude and longitude in FullCAM in decimal degrees. All
spatial measurements in FullCAM are defined and exact in terms of
degrees, although we commonly speak of length approximations in
kilometres or meters.

Latitude measures degrees from the equator; positive latitudes are in
the northern hemisphere, negative latitudes are in the southern
hemisphere (Australia is at about --30 degrees latitude). Goes from --90
deg N to +90 deg N ("N" is for = "north").

Longitude measures degrees east of Greenwich, London. Goes from --180
deg E to +180 deg E ("E" is for "east").

**Conversion from Minutes and Seconds**

To convert between decimal degrees and minutes and seconds:

> 1 minute = 1/60 degree\
> 1 second = 1/ 60 minute = 1/3600 degree.

**Example.** 12 degrees, 15 minutes and 1 second (12 deg 15\' 1\") is
equal to

> 12 degrees + 15 / 60 degrees + 1/3600 degrees\
> = 12 + 0.25 + 0.000277777778 degrees\
> = 12.25028 degrees (to about 1m precision)

**Length Approximations**

One degree of latitude is roughly 100 km (closer to 110 km). Except near
the poles, a degree of latitude is roughly equal in length to a degree
of longitude. Thus:

- One hundredth of a degree (0.01 degrees) is about 1 km
- Five decimal places gives about 1m precision (0.00001 degrees is about
  a meter).

**Example.** To move about 1 km west from 131.08123 deg E, move to
131.07123 deg E.

The size of a degree of longitude varies with latitude. For Australia, a
degree of longitude at the tip of Cape York corresponds to approximately
109km, while at southern Tasmania it is approximately 80km.

We use these length approximations often when talking about spatial
grids and cells, but the size of the cells and grids is defined in terms
of degrees. For example, when we talk about a woodiness cell of "25
meters" or "25 m resolution" what we mean is the cell of the woodiness
grid is 0.00025 degrees square --- as drawn on the ground, such a the
cell has slightly curved edges, the northern and southern edges have
slightly different lengths, and the northern and eastern edges may have
quite different lengths.

**Curvature of the Earth**

Grids and their cells are specified as rectangles and squares
respectively, as measured in degrees of latitude and longitude. Due to
the curvature of the earth, the outline of the area of earth covered by
a grid is not quite rectangular. Likewise, the cells are not quite
square: the north-south side of each cell is not quite the same as the
length of the east-west sides, and the east-west side nearer the equator
is longer than the east-west side nearer the nearest pole.

FullCAM corrects for these effects when reporting areas, that is,
FullCAM always reports true areas (areas as you would measure on the
earth's surface).

**Australia**

Latitude and longitude coordinates must be from the Geographic Datum of
Australia (GDA) system, not from the Australian Map Grid (AMG) system.

Mainland Australia and Tasmania extend approximately from latitude
--10.6 deg N (Cape York, Queensland) to --43.6 deg N (South-east Cape,
Tasmania), and longitude 113.2 deg E (Steep Point, Western Australia) to
153.6 deg E (Cape Byron, NSW).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
