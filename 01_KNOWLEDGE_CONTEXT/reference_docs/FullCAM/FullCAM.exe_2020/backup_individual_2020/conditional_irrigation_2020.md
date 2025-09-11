---
title: Conditional Irrigation
version: 2020
category: Irrigation
original_file: 91_Conditional Irrigation_2020.md
---

This Time Series Window is where you
enter the percentage of the soil water capacity that is guaranteed by
conditional irrigation.

**Details**

In every simulation step, FullCAM applies just enough conditional
irrigation to bring the soil water level up to this specified percentage
of the maximum soil water level. All other water (namely rainfall and
definite irrigation) is applied first, and if the soil water level is
still below this guaranteed percentage then FullCAM applies the
conditional irrigation required to bring the water level up this
percentage. This window is a typical time series window provided that
irrigation was specified to occur as a time series in the 'Events or
Time Series' window of the 'Configuration' tab. If irrigation was
specified as events then irrigation events need to be added to the
'Events' tab.

This time series is only used when the *Irrigation* setting on the
Configure Event Or Time
Series window is set to
*Time series*.

See Site : Water.
