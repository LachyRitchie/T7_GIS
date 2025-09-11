---
title: Downloading Trees and Events
version: 2016
category: Data Management
original_file: 208_Downloading Trees and Events_2016.md
---

[Data Builder page : *Trees and Events*
panel]

This panel is for downloading tree species and forest event data, using
Data Builder.

**Basic Operation**

1.  Select a tree-species group from the upper list, and press the
    *Download List of Tree-Species/Regimes for This Species-Group*
    button. This just updates the lower list.
2.  Select a species/regime from the lower list and press the *Download
    Events for This Regime* button. This puts the events for the
    selected species/regime onto the events list on the
    Events page.
3.  While still with the same species/regime selection on the lower
    list, press the *Download This Species* button. This will download
    the species information for the selected species/regime to the list
    of tree species on the Trees page.

As an alternative to step 3, just be sure to press the *Download Tree
and Crop Species Required by the Event Queue* button (at the bottom of
the Data Builder page) before trying to run a simulation. See Data
Builder for details.

**Details**

A tree regime and the tree species planted in that regime have the same
name. The regime names reflect the type of management applied to the
species.

When downloading a species, the Data Builder will ask if you wish make
the species the initial species. We recommend you select "Yes", unless
you wish to apply a different species as the initial species. Selecting
"Yes" does not necessarily mean that the species exists at the start of
the simulation, only that the initial conditions for the forest (mainly
the debris) will be set using that species.

The forest portion of the plot should now be ready to simulate (so the
*Trees* tab should not be red, and the buttons in the *Forest* panel of
the *Initial Conditions* page will not be red).

You can download subsequent Regimes after the first
forest regime. After downloading the first forest regime, the list of
tree-species/regimes available for download is updated to include only
those that are applicable for second and subsequent rotations. Forest
regimes which start from pasture or native forest will not be available
after the first regime is downloaded, because it is expected that you
will be moving from a plantation to another plantation. You can select
different species groups (for example, move from Pinus radiata to
Eucalyptus globulus) and apply different establishment techniques within
each species.

If you make a mistake in building the forest event queues, click the
*Clear Forest Events* button to clear all the events downloaded as part
of the Regimes.