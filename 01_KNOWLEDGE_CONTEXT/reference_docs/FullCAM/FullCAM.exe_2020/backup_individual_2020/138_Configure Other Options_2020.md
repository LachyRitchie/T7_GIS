---
title: Configure Other Options
version: 2020
category: configuration
original_file: 138_Configure Other Options_2020.md
---

Assorted configuration options.

**Economic Modelling**

Costs and incomes are added to various events, so that economic
calculations can be performed. All economic modelling is in constant
dollars.

If economic modelling is on then the site must have an area (see Site :
Area), so that the per-hectare costs can be added to
the fixed costs and be presented as a single cost.

If economic modelling is on then thins and harvests must be specified by
log and crop grades, because only log and crop grades include pricing
information on logs and crops. Note that, even using log grades, a thin
event can specify a 0% log grade and still specify which material moves
to debris - so forest management activities like pruning can still be
achieved with economic modelling on (same for crops).

**Events or Time Series**

See Configure Event Or Time
Series.

**RothC Version**

If the plot model includes the soil then the RothC
model is will be used to simulate the soil. If you are running the
Research Edition of FullCAM, then you can
then specify which version of RothC to use:

- RothC version **26.3**. Fully calibrated for Australian conditions
  with data available. This version is always used by the standard
  version of FullCAM.
- RothC version **26.5**. More sophisticated, but not calibrated. Only
  in the Research Edition of FullCAM.

If you model a mixed forest and agricultural system and model the soil,
then FullCAM will always use the same version of RothC for both the
forest soil and the agricultural soil.
