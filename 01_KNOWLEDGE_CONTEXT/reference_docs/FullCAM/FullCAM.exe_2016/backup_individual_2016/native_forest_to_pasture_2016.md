---
title: Native Forest to Pasture
version: 2016
category: Land Use Change
original_file: 231_Native Forest to Pasture_2016.md
---

Details

Native forest to pasture management systems are created in FullCAM by
using a plot type of *Multi-layer mixed system*.

Other systems that may be created by FullCAM are:

Pasture to Plantation
Forest
Plantation Forest to Plantation
Forest
Native Forest to Plantation
Forest
Grazed Woodland
Crop and Pasture Management

**Method**

*Configuration*

- Plot Type : Multi-layer mixed system.

*Databuilder*

- Set the *Forest percentage for downloading* to the initial tree crown
  canopy cover.\
  Select the required *Trees and Events* (refer Downloading Trees and
  Events).
- Select Tree species group *Native Forest Groups*.\
  Select the required *Crops and Events* (refer Downloading Crops and
  Events).
- Select a pasture species that will replace the native forest.
- Select an appropriate pasture regime. This regime will cycle through
  time.

*Events*

To clear the forest, Thin and Forest Percentage
Change events must be created.

A Thin event is created to clear the trees.

- Select *New...*
- Set the *Type* drop down list value to *Thin*.
- Enter the *Timing* details of the clearing.
- Select *Insert Standard Values*.
- Select a standard event. This will populate all values for the *Thin*
  event.
- Enter an event name, or alternatively select the *Autoname* button.
- Select *OK*. The event will now be stored on the
  Events page*.*

A Forest Percentage Change event
is created by repeating the previous procedure with the following
exceptions:

- Set the *Type* to *Forest Percentage Change*.
- Set the *Timing* details to 1 day after the clearing *Thin* event.

If you wish to burn the debris, repeat the previous procedure and set
the *Type* to Forest Fire.
