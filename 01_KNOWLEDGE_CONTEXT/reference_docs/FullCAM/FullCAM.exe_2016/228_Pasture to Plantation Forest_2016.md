+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

Pasture to Plantation Forest

Details

Pasture to plantation forest management systems are created in FullCAM
by using a plot type of *Multi-layer mixed system*.

Other systems that may be created by FullCAM are:

[Plantation Forest to Plantation
Forest](229_Plantation%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Plantation
Forest](230_Native%20Forest%20to%20Plantation%20Forest.htm)\
[Native Forest to Pasture](231_Native%20Forest%20to%20Pasture.htm)\
[Grazed Woodland](232_Grazed%20Woodland.htm)\
[Crop and Pasture Management](233_Crop%20and%20Pasture%20Management.htm)

**Method**

*Configuration*

- Plot Type : Multi-layer mixed system.

*Timing*

- Set the timing. The *Start simulation at beginning of* year should be
  set to 20 years prior to plantation establishment.

It is always prudent to \'run the model in\' by setting the start year
earlier (up to 20 years) than the actual period of interest. This is
because the soil carbon data at initialisation represents a pristine
condition, a condition that does not reflect any prior management.

*Databuilder*

- Set the *Forest percentage for downloading* to 0.\
  Select the required *Trees and Events* (refer [Downloading Trees and
  Events](208_Downloading%20Trees%20and%20Events.htm)).
- Select an initial rotation *Tree-species/Regimes.* The initial list
  displayed will be ex-pasture plantation *Tree-species/Regimes* only.
- Select a subsequent rotation *Tree-species/Regimes.* Subsequent lists
  displayed will be subsequent rotation plantation
  *Tree-species/Regimes* only.

Subsequent rotation *Tree-species/Regimes* may be selected and
downloaded as often as required. Additional *Tree-species/Regimes* can
be added either within the same *Tree-species groups* or from other
groups to model transitions from one plantation species to another.

Select the required *Crops and Events* (refer [Downloading Crops and
Events](2_Downloading%20Crops%20and%20Events.htm)).

- Select *Download Tree and Crop Species Required By the Event Queue*.
  This will add crop species *Agriculture plantation weed species* and
  also relevant events.

The plot should now be ready to simulate. There is no need to
specifically download any crop information from *Crops and Events*.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
