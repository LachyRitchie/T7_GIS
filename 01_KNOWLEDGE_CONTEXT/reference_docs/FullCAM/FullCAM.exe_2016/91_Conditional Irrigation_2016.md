+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Conditional Irrigation**

\[[Site : Water](12_Site_Water.htm) window : *Conditional Irrigation*
button (*Forest* or *Agricultural*)\]

This [time-series Window](135_time-series%20window.htm) is where you
enter the percentage of the soil water capacity that is guaranteed by
conditional irrigation.

**Details**

In every simulation step, FullCAM applies just enough conditional
irrigation to bring the soil water level up to this specified percentage
of the maximum soil water level. All other water (namely rainfall and
definite irrigation) is applied first, and if the soil water level is
still below this guaranteed percentage then FullCAM applies the
conditional irrigation required to bring the water level up this
percentage. This window is a typical time-series window provided that
irrigation was specified to occur as a time-series in the \'Events or
time-series\' window of the \'Configuration\' Tab. If irrigation was
specified as events then irrigation events need to be added to the
\'Events\' Tab.

This time-series is only used when the *Irrigation* setting on the
[Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm) window is set
to *time-series*.

See [Site : Water](12_Site_Water.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
