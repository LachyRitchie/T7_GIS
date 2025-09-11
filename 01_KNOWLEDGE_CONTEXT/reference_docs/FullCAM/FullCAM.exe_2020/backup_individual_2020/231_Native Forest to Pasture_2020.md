---
title: Native Forest to Pasture
version: 2020
category: systems
original_file: 231_Native Forest to Pasture_2020.md
---

Details

Native forest to pasture management systems are created in FullCAM by
using a plot type of *Multilayer mixed system*.

Other systems that may be created by FullCAM are:

Pasture to Plantation
Forest\
Plantation Forest to Plantation
Forest\
Native Forest to Plantation
Forest\
Grazed Woodland\
Crop and Pasture Management

**Method**

*Configuration*

- Plot Type : Multilayer mixed system.

*Data Builder*

Set the *Forest percentage for downloading* to the initial tree crown
canopy cover.\
Select the required *Trees and Crops* (refer Downloading Spatial
Data).

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
