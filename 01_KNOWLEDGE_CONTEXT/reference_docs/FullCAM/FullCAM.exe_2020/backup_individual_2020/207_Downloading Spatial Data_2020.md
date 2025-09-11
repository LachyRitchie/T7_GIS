---
title: Downloading Spatial Data
version: 2020
category: data
original_file: 207_Downloading Spatial Data_2020.md
---

This panel is for downloading data that is specific to a location, using
Data Builder.

**Inputs**

Specify the plot's location by entering its Latitude and
Longitude. The default latitude and
longitude is for Uluru.

The *Forest category* drop-down list provides a filter to help with
choosing trees species from DataBuilder. Selecting "All" will provide
all species, but choosing any other option from the list will narrow
down the options presented to those which would generally be available
for that type of land management.

The *Spatial data averaged over* list is where you choose the area over
which to average downloaded data. The purpose of this averaging is so
that the downloaded data represent the average conditions in a broader
area, which can be set from 1 hectare up to 2500 hectares. The area from
which the data is averaged for download, is centred on the plot
latitude/longitude, with the data to be averaged being climate, and
other inputs such as initial soil carbon.

The *Forest Percentage* is used to set
the initial masses in proportion between the forest and agricultural
systems, and it becomes the Initial Conditions For the Whole
Plot value. It
has no direct effect on any simulation of this plot. For modelling
systems transitioning from pasture to plantation, the initial forest
percentage for downloading should be set to 0.

When you download a species and set it as the initial species, the value
of the forest percentage for downloading is used to compute the initial
masses of the species. So if you later change the forest percentage for
downloading, you will have to reset the initial species.

**Download Spatial Data**

Press the *Download Spatial Data* button to download the location
specific data from the Departmental
Server. Text to the right of the window
will then become visible showing the state and SA2 region for that the
latitude and longitude resides within.

For Tree species, also displayed is the National
Plantation Inventory Region (NPI), which are plantation regions
published by ABARES, and the Growth Region, which are regions
determining the availability of species for environmental and mallee
plantings.

The Data Builder will download data for any point for which data is
available within the extent used. The FullCAM Server has spatial data
based on grids of varying resolutions from 25m to 1km.

**Downloading Crops and Trees**

This panel is for downloading crop and tree species.

**Basic Operation**

1.  After downloading spatial data, select a species from the lower
    *Available Crops / Available Trees* lists, and press the *Download
    Species* button. This will download the species data to the plot and
    update the upper *Crop Species / Tree Species* lists.
2.  Having the *Apply downloaded data* checkbox ticked will overwrite
    previously downloaded or manually entered species data within the
    plot.

**Details**

When downloading the first species to a plot, Data Builder will ask if
you wish to make the species the initial species. We recommend you
select "Yes". This will populate the initial conditions parameters. The
existence of and parameters for the initial species can be edited via
the Initial Conditions tab. This is the
preferred method of entering data into the initial conditions as all
data points will contain required default data.

Once at least one crop or tree species has been downloaded, regimes and
events are now ready to be added to the Event Queue.
