+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Site : Water**

\[[Site](200_Site.htm) page : *Water* button\]

This window is where you enter water and moisture information for the
plot, except that the soil-water information is entered in the [Soil
Water](44_Soil%20Water.htm) window.

**Introduction**

On occasion, constituent models ([RothC](114_RothC.htm) and
[CAMFor](77_CAMFor.htm)) will need to know the rainfall if the breakdown
of the debris of any tree species is sensitive to temperature and
rainfall, and for [CAMAg](78_CAMAg.htm) if the breakdown of the debris
of any crop species is sensitive to temperature and rainfall. Rainfall
can be supplemented by definite irrigation.

**Natural**

The soil model [RothC](114_RothC.htm) requires details of open-pan
evaporation, in order to work out the topsoil moisture deficit (TSMD).

**Irrigation**

The irrigation in the forest and agricultural systems of a plot are
entirely separate, and no water runs from one system to the other.

*Definite irrigation* is irrigation that definitely occurs, regardless
of conditions. If you have historical irrigation data, enter it as
definite irrigation and turn off conditional irrigation. See the
[Definite Irrigation](92_Definite%20Irrigation.htm) time-series.

*Conditional irrigation* is irrigation whose occurrence depends on the
conditions. Specify a minimum percentage of the maximum soil water
capacity in the conditional irrigation time-series, and FullCAM applies
just enough irrigation to guarantee that the soil water never drops
below this amount. Thus, conditional irrigation ensures a minimum level
of soil water - irrigation is used as conditions require. Use
conditional irrigation to simulate the effect of a management practice
that uses irrigation to ensure a minimum soil water level. Setting the
conditional irrigation percentage to 0% effectively turns off
conditional irrigation. See the [Conditional
Irrigation](91_Conditional%20Irrigation.htm) time-series.

The forest and agricultural water simulations are separate (FullCAM
assumes no lateral water movement on the plot), except that they share
the same rainfall, open-pan evaporation, and [Vapour Pressure
Deficit](97_Vapour%20Presser%20Deficit.htm). The forest and agricultural
irrigations are entirely separate.

Irrigation levels can be specified either with events or with
time-series (see [Configure Event Or
time-series](195_Configure%20Event%20Or%20time-series.htm)). If using
time-series, enter the time-series via the buttons on this window. If
using events, enter the events on the [Events](136_Events.htm) page. In
either case, enter all information about irrigation (namely whether
conditional irrigation is on, and which model it uses to operate in the
forest).

**Forest Irrigation**

RothC calculates soil water as a deficit, as the *topsoil moisture
deficit* (TSMD). The RothC soil water capacity (corresponds to a TSMD of
zero when the soil is at its wettest, but equal to the maximum TSMD when
the soil is at its driest) is calculated by RothC from the soil sample
depth, the ratio of bare-to-covered maximum TSMD, and the clay fraction
--- input these in the [Soil Water](44_Soil%20Water.htm) window and
[Soil for the Whole Plot](46_Soil%20for%20the%20Whole%20Plot.htm) panel,
respectively.

**Agricultural Irrigation**

Only the [RothC](114_RothC.htm) model runs an agricultural soil water
model. You can use conditional irrigation whenever the soil is included
in the plot. See the remarks on RothC in the forest irrigation section
above.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
