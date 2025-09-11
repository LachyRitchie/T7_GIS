---
title: General Features
version: 2016
category: General
original_file: 20_General Features_2016.md
---

Some general features that every user of FullCAM should know.

**Readiness**

A FullCAM document (plot or estate) has many inputs, even in the simpler
configurations. When all the inputs have been filled with valid values,
and some outputs specified, then the document is *ready* to simulate. In
particular, you cannot simulate a plot until it is ready.

Parts of the document that are not ready are coloured red. Red writing
and colouring guide you to the parts that are not ready --- the bits you
need to complete before the plot can be simulated.

The status bar at the bottom of the document window says whether a
document is ready. When the document is ready the 'Run Plot
Simulation' item in the 'Simulate' menu and its corresponding icon on
the toolbar of the Main Window become enabled.

The interface will only let you enter valid values. It will immediately
reject an invalid value, such as a percentage that is greater than 100,
less than 0.0, or non-numeric. For a few inputs, the valid range depends
on other inputs --- so if those other inputs change then the input can
become invalid, in which case it is shown with a red background.

When a simulation is ready all tabs will not be in red, and the 'Run
Simulation' icon on the toolbar of the Main
Window will be highlighted.

**Fractions and Percentages**

In FullCAM:

A *fraction* is a number from 0.0 to 1.0, inclusive.\
A *percentage* is a number from 0.0 to 100.0, inclusive.

The fraction *f* corresponds to the percentage (100 * f). For
example, the fraction 0.25 = 25% (recall that "%" just means "/100")
corresponds to the percentage 25.

We use fractions in FullCAM for computations, because it is easier to
calculate with fractions. But we use percentages in the user interface,
because it is quicker to type percentages than it is to type decimal
points or "%" symbols.

This also affects the terminology. For example, the "carbon percentage"
of leaves is the percentage of dry leaves by weight that is carbon, and
is approximately 50 (which we might write as 50%, if we regard the "%"
symbol in this instance like a unit), while the "carbon fraction" of
leaves is about 0.5, which is 50%.

**Timing**

The timing of land use actions can impact carbon levels. FullCAM has
been designed to be very flexible in relation to the timing of these
activities. Time is simulated as a series of equal-length steps. FullCAM
Standard Edition can run a simulation on anywhere from a yearly to a
daily basis. None of the other inputs depends on this time scale, so you
are free to run any model over any timescale. Timescales can be changed
by re-selecting the step length --- so you could run a plot model with
monthly time-steps, then change to weekly timescale.

Input time-series are always interpolated or extrapolated appropriately
to match the simulation steps. For example, if you enter annual rainfall
data but run the model daily, then the daily rainfall will simply be the
annual rainfall divided by 365 days.

The primary unit of time in FullCAM is the year. A year in FullCAM
always has 365 days (leap years are irrelevant to modelling with this
precision, but would just add significant complexity).

**Units**

- The unit of mass is the metric tonne, abbreviated "t", or kilogram,
  abbreviated to "kg". Masses are often measured in tonnes of dry mass
  (tdm) or tonnes of carbon (tC).
- The unit of time is the year, abbreviated "yr".
- The unit of area is the hectare, abbreviated "ha".
- The unit of distance is the meter, abbreviated "m", except when
  measuring water it is millimetres, "mm".
- The unit of temperature is the degree Celsius, abbreviated "deg C".

The expression "a/b/c" means "(a / b) / c" or equivalently "a / (b *
c)", because order of operations is implicitly left to right. For
example, "t/ha/yr" means "(tonnes per hectare) per year".

**Inputs**

An *input* is a numerical input that you enter into a FullCAM document.
There are two types of inputs:

1.  *Single number* inputs - A single number, other than a data point of
    a time-series.\
    Example: the initial mass of leaves in the forest.
2.  *time-series* inputs - A time-series is a single value that varies
    with time.\
    Example: the rainfall falling on a plot.

The *regular value* of an input is a value specified by the user and
used in a normal plot simulation. You can perform a risk analysis by
attaching a probability distribution to an input (which then becomes a
*risk input*). Double-click on any input (if a time-series, on its
multiplier) to get information about it, or to edit its associated risk
properties (if a risk analysis is turned on). Alternatively, press F2
while the input is selected.

**Compatibility with Previous Versions of FullCAM**

FullCAM is under continual development; features are being added, and
occasionally removed.

Often a new version of FullCAM will have a unique file format. However,
newer versions of FullCAM can read many files that were created with
older formats. Generally, it is a good idea to use files in the latest
format. To do so, download the latest version of FullCAM and when you
open a file, if the file format can be updated, FullCAM will ask if you
wish to overwrite the file with the latest format. If you do not wish to
overwrite the file, you can also use the File menu to save a version of
the plot or estate with the latest format using an alternate name.

**Windows**

The main window is the thin window across the top of your screen with a
menu and toolbar, entitled "FullCAM X.X", where X.X is the version
number of the FullCAM program.

The main window is open whenever FullCAM is open. Individual FullCAM
documents or windows do not appear separately on the Windows taskbar. If
you close the main window (by clicking its close box) then you exit
FullCAM. You cannot resize the main window, but you can move it.

All FullCAM windows can be moved, and most can be resized. Move a window
by dragging it by its title bar; resize a window by dragging an edge or
a corner with the mouse. All FullCAM windows remember their positions
and sizes from when you last moved or resized them.

Quit FullCAM by choosing *Exit* from the *Program* menu of the main
window, or by closing the main window.

**Special Keys**

The following keys have special meanings that are not necessarily
apparent from looking through the menus. You do not need to know any of
these meanings to use FullCAM with a mouse and the usual keys, but these
meanings can speed you up.

- *Enter ---* If you are in a number entry box, FullCAM immediately
  process the number.

- *Tab* --- Jumps to the next data entry control (box, menu, button, and
  so on).

- *Shift-Tab* --- Jumps to the previous data entry control (box, menu,
  button, and so on).

- *Space* --- If a button is selected, pressing the *Space* bar presses
  the button.

- *Home, End, Page Up, Page Down* --- Move between pages in tabbed
  windows (such as the document input windows), move between help topics
  in the *Help* window, and move between records in the table windows.

- *Delete* --- Deletes selected items from lists.

- *F1* --- Opens the *Help* window at the help topic for the current
  window. If there are several help buttons on the window, pressing F1
  opens the Help at the topic for the first of the buttons --- you can
  then move to other topics using control-N (next) and control-B (back).
  However, in general we recommend you press the help button with the
  mouse to move straight to the topic you want.

- *F2* --- Opens the *Input Properties* window for the current input
  control (box, menu, and so on). If *Risk Analysis* is on, it instead
  opens the *Risk Properties* window for the input.

- *F9* --- Simulates a plot or estate document (refer Introduction to
  Using FullCAM for further
  details).

- *F12* --- Closes the window, automatically pressing any *OK* or *Done*
  button on the window.

- *Escape* --- Closes the window, automatically pressing any *Cancel*
  button on the window. Same as if the close-window box was clicked.

- *Alt* --- Shifts focus to the Main Window,
  ready for a letter to choose a menu. A second *Alt* key press returns
  you to the previous window.

**Underlines on buttons** --- If there is a button in the current window
with an underlined letter, pressing that "Alt-" and that letter on the
keyboard presses that button (if there is no ambiguity due to currently
being in a text box and so on, just pressing the letter on the keyboard
has the same effect).

Most keyboard shortcuts are noted in the menus or in the tool tips of
toolbar buttons.

Most buttons have an *accelerator* key so you can activate it using the
keyboard instead of clicking it with the mouse. In the button's label,
its accelerator key is underlined. You can always activate the
accelerator key by holding down the *Alt* key while pressing the
underlined key. However if the cursor is not currently in an object that
accepts keyboard input (not in a text box or drop-down list box), you
can omit the *Alt* key and simply press the underlined key.

**Example.** A button labelled "Delete", where the "D" is underlined,
can be activated by pressing either "d" or "D" on the keyboard, or if
you are currently entering text or in a drop-down list box, press
"Alt-d" or "Alt-D".

**Entering Numbers**

FullCAM often requests information in the form of numbers. You enter
most numbers into text boxes, which are white against the grey
background of the window.

If you enter a number that is outside the allowed range of numbers, or
enter text that is not a number, FullCAM will ask you to re-enter the
number immediately you either try to leave the text box (move the focus
elsewhere) or you press the *Enter* key.
