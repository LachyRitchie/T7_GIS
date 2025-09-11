+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

Native Forest to Pasture

Details

Native forest to pasture management systems are created in FullCAM by
using a plot type of *Multi-layer mixed system*.

Other systems that may be created by FullCAM are:

[Pasture to Plantation
Forest](228_Pasture%20to%20Plantation%20Forest.htm)\
[Plantation Forest to Plantation
Forest](229_Plantation%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Plantation
Forest](230_Native%20Forest%20to%20Plantation%20Forest.htm)\
[Grazed Woodland](232_Grazed%20Woodland.htm)\
[Crop and Pasture Management](233_Crop%20and%20Pasture%20Management.htm)

**Method**

*Configuration*

- Plot Type : Multi-layer mixed system.

*Databuilder*

- Set the *Forest percentage for downloading* to the initial tree crown
  canopy cover.\
  Select the required *Trees and Events* (refer [Downloading Trees and
  Events](208_Downloading%20Trees%20and%20Events.htm)).
- Select Tree species group *Native Forest Groups*.\
  Select the required *Crops and Events* (refer [Downloading Crops and
  Events](2_Downloading%20Crops%20and%20Events.htm)).
- Select a pasture species that will replace the native forest.
- Select an appropriate pasture regime. This regime will cycle through
  time.

*Events*

To clear the forest, [Thin](140_Thin.htm) and [Forest Percentage
Change](116_Forest%20Percentage%20Change.htm) events must be created.

A [Thin](140_Thin.htm) event is created to clear the trees.

- Select *New\...*
- Set the *Type* drop down list value to *Thin*.
- Enter the *Timing* details of the clearing.
- Select *Insert Standard Values*.
- Select a standard event. This will populate all values for the *Thin*
  event.
- Enter an event name, or alternatively select the *Autoname* button.
- Select *OK*. The event will now be stored on the
  [Events](136_Events.htm) page*.*

A [Forest Percentage Change](116_Forest%20Percentage%20Change.htm) event
is created by repeating the previous procedure with the following
exceptions:

- Set the *Type* to *Forest Percentage Change*.
- Set the *Timing* details to 1 day after the clearing *Thin* event.

If you wish to burn the debris, repeat the previous procedure and set
the *Type* to [Forest Fire](144_Forest%20Fire.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
