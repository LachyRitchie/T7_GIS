+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Configure Other Options**

\[[Configuration](150_Configuration.htm) page: *Other Options* panel\]

Assorted configuration options.

**Economic Modelling**

Costs and incomes are added to various events, so that economic
calculations can be performed. All economic modelling is in constant
dollars.

If economic modelling is on then the site must have an area (see [Site :
Area](157_Site_Area.htm)), so that the per-hectare costs can be added to
the fixed costs and be presented as a single cost.

If economic modelling is on then thins and harvests must be specified by
log and crop grades, because only log and crop grades include pricing
information on logs and crops. Note that, even using log grades, a thin
event can specify a 0% log grade and still specify which material moves
to debris - so forest management activities like pruning can still be
achieved with economic modelling on (same for crops).

**Events or Time Series**

See [Configure Event Or Time
Series](195_Configure%20event%20or%20time-series.htm).

**RothC Version**

If the plot model includes the soil then the [RothC](114_RothC.htm)
model is will be used to simulate the soil. If you are running the
[Research Edition](48_Research%20Edition.htm) of FullCAM, then you can
then specify which version of RothC to use:

- RothC version **26.3**. Fully calibrated for Australian conditions
  with data available. This version is always used by the standard
  version of FullCAM.
- RothC version **26.5**. More sophisticated, but not calibrated. Only
  in the [Research Edition](48_Research%20Edition.htm) of FullCAM.

If you model a mixed forest and agricultural system and model the soil,
then FullCAM will always use the same version of RothC for both the
forest soil and the agricultural soil.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
