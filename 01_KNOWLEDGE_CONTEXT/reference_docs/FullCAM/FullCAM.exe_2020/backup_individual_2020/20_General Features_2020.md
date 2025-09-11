---
title: General Features
version: 2020
category: general
original_file: 20_General Features_2020.md
---

Some general features that every user of FullCAM should know.

**Readiness**

A FullCAM document (plot, estate, spatial, database) has many inputs,
even in the simpler configurations. When all the inputs have been filled
with valid values, and some outputs specified, then the document is
ready to simulate. You cannot simulate a plot until it is ready.

Parts of the document that are not ready are coloured red.

The status bar at the bottom of the document window says whether a
document is ready. When the document is ready the 'Run Plot
Simulation' item in the 'Simulate' menu and its corresponding icon on
the toolbar of the Main Window become enabled.

The interface will only let you enter valid values. It will immediately
reject an invalid value. For some inputs, the valid range depends on
other inputs --- so if those other inputs change then the input can
become invalid, in which case it is shown with a red background.

**Fractions and Percentages**

In FullCAM:

A *fraction* is a number in the range 0.0 to 1.0.\
A *percentage* is a number in the range 0.0 to 100.0.

The fraction *f* corresponds to the percentage (100 * f). For
example, the fraction 0.25 corresponds to the percentage value of 25.

**Timing**

The timing of land use actions can impact carbon and nitrogen levels.
FullCAM has been designed to be flexible in relation to the timing of
these activities. Time is simulated as a series of equal-length steps.
There can be anywhere from 1 to 8760 steps per year, so FullCAM can run
a simulation on a yearly to an hourly basis. None of the other inputs
depends on this time scale, so you are free to run any model over any
time scale. Time scales can be changed by just re-entering the number of
steps per year --- so you could run a plot model with monthly time
steps, change the number of steps to 52 per year, and then run it on a
weekly time scale. You can instruct FullCAM to record the output data
after any number of steps (every step, every twelfth step, and so on),
so you can run the model with many steps per year and avoid being
overwhelmed with output data.

Input time series are always interpolated or extrapolated appropriately
to match the simulation steps. For example, if you enter annual rainfall
data but run the model daily, then the daily rainfall will simply be the
annual rainfall divided by 365 days. See the Time Series
Window for more information.

The primary unit of time in FullCAM is the year. A year in FullCAM
always has 365 days, there are no leap years.

**Units**

- The unit of mass is the metric tonne abbreviated "t", or kilogram
  abbreviated to "kg". Masses are often measured in tonnes of dry mass
  (tdm), tonnes of carbon (tC), or tonnes of nitrogen (tN).
- The unit of time is the year, abbreviated "yr".
- The unit of area is the hectare, abbreviated "ha".
- The unit of distance is the meter, abbreviated "m".
- The unit of water is the millimetre, abbreviated "mm".
- The unit of temperature is the degree Celsius, abbreviated "deg C".

**Inputs**

An *input* is a numerical input that you enter into a FullCAM document.
There are two types of inputs:

1.  *Single number* inputs - A single number, other than a data point of
    a time series.
2.  *Time series* inputs - A time series is a single value that varies
    with time.

The *regular value* of an input is what you type into the FullCAM
document, and is what is used in a plot simulation for a plot or spatial
document.

Double-click on any input (if a time series, on its multiplier) to get
information about it. Alternatively, press F2 while the input is
selected.

**Compatibility with Previous Versions of FullCAM**

FullCAM is under continual development; features are being added and,
occasionally, removed.

Each version of FullCAM generally has a unique file format. Newer
versions of FullCAM can open and read files that were created with the
older formats allowing them to be updated to the new current format.

**Windows**

Quit FullCAM by choosing *Exit* from the *Program* menu of the main
window (shortcut ctrl-Q), or by closing the main window by its close
box.

All FullCAM windows can be moved, and most can be resized. Move a window
by dragging it by its title bar; resize a window by dragging an edge or
a corner with the mouse. All FullCAM windows remember their sizes from
when you last resized them.

**Menus and Commands**

All the commands are either:

- In the menus (either the fixed menu in the Main
  Window, or the mouse right click context
  menu).
- On buttons in the toolbars of the various windows.

All of the keyboard shortcuts are noted in the menus or in the tool tips
of toolbar buttons, except for those noted in Special
Keys.

Most buttons have an shortcut key so you can activate it using the
keyboard instead of clicking it with the mouse. In the button's label,
its shortcut is underlined. You can always activate the key by holding
down the *Alt* key while pressing the underlined key. However if the
cursor is not currently in an object that accepts keyboard input (not in
a text box or drop-down list box), you can omit the *Alt* key and simply
press the underlined key.

