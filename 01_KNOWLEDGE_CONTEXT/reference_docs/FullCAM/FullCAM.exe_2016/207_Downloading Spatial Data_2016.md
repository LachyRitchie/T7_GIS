+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Downloading Spatial Data**

\[[Data Builder](132_Data%20Builder.htm) page : *Spatial Data* panel\]

This panel is for downloading data that is specific to a location, using
Data Builder.

**Inputs**

Specify the plot's location by entering its [Latitude and
Longitude](180_Latitude%20and%20Longitude.htm). The default latitude and
longitude is for Uluru.

The *forest percentage for downloading* is the [Forest
Percentage](206_Forest%20Percentage.htm) used by the Data Builder to
determine what data to download. It is used to set the initial masses in
proportion between the forest and agricultural systems, and it becomes
the [Initial Conditions For the Whole
Plot](197_Initial%20Conditions%20For%20the%20Whole%20Plot.htm) value. It
has no direct effect on any simulation of this plot. For modelling
systems transitioning from pasture to plantation, the initial forest
percentage for downloading should be set to 0.

When you download a species and set it as the initial species, the value
of the forest percentage for downloading is used to compute the initial
masses of the species. So if you later change the forest percentage for
downloading, you will have to reset the initial species --- at which
point it is easiest to start a new plot and start over.

The start month simply reports the first month of the simulation, as per
the [Timing](199_Timing.htm) page. It is used to decide which initial
soil water level (topsoil moisture deficit, TSMD --- see [Initial
Soil](32_Initial%20Soil.htm)) to download.

**Download**

Press the *Download Spatial Data* button to download the location
specific data.

The Data Builder will download data for any point for which data is
available. The FullCAM Server has spatial data based on grids of varying
resolution --- from 250m to 1km. At these scales, many site specific
features which logically prevent tree and crop growth will be missed.
For example, the Data Builder will allow you to grow crops on major
roads, in minor rivers, and even on the top of Uluru. No tenure data is
known to the FullCAM Server.

You might receive an error message stating that the FullCAM Server was
unable to find some data. This usually occurs because the FullCAM Server
thinks that the plot is located in a large body of water, and the
missing data is typically for the soil. If the plot is within 100m of a
large water body such as the coast , the FullCAM Server is usually
unable to locate data. Try moving the plot away from the water body by
adjusting the [Latitude and
Longitude](180_Latitude%20and%20Longitude.htm) and try again.

**Soils**

The *regional soils* list contains the range of soil types known to
exist in the state and IBRA region. The soil type for which data has
been downloaded is displayed to the right of the *Download Spatial Data*
button.

Downloading another soil type (*Download Soil* button) discards the
previous soil data and replaces it with the new soil data. This will
also update the crop species list.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
