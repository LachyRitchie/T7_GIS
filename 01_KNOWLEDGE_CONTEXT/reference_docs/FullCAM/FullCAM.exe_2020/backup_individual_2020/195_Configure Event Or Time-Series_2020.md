---
title: Configure Event Or Time Series
version: 2020
category: configuration
original_file: 195_Configure Event Or Time-Series_2020.md
---

Specify certain inputs as either by time series or by events.

Press the 'Events' or 'Time Series' button to access the window where
you decide where various sorts of inputs are treated as event or as time
series data.

**Introduction**

FullCAM only allows events if a multilayer plot is modelled (see
Configure the Plot), so if modelling a
plot that is not multilayer then time series data will always be used.

You can change these settings at any time without losing any of the time
series or event data you may have entered.

If you do not want any of a particular input (for example, there is no
irrigation in your simulation), it is easiest to set its input type to
*Events*, but do not create any events of that type. This way you will
not be asked for the time series input.

Some inputs, such as irrigation, can be specified either as events or as
time series. This is where you configure how they are to be specified.

Unless a forest, agricultural or mixed system are modelled then FullCAM
does no allow events and thus time series data will always be used.

**Irrigation**

For a discussion of irrigation, see Site : Water.

Set the irrigation:

- As time series: The Definite
  Irrigation and Conditional
  Irrigation time series
- As events: Irrigation Change events.

**Manure-From-Offsite Added to the Soil**

Manure from offsite can be added to the soil whenever the soil is
modelled.

Set the manure additions:

- As time series: The Manure Inputs to Soil from
  Offsite time
  series
- As events: Manure-From-Offsite
  Change events.
