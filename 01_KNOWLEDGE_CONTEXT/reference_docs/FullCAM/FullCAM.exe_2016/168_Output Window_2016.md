+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Output Window**

\[[Output Windows](25_Output%20Windows.htm) : *Show Selected Output
Window* button\]

This window shows your selected outputs for the last simulation, either
in a graph or a table.

**Show Graph or Table, Choose Outputs**

To show the outputs as a graph, press the *View As Graph* button
(leftmost button in the toolbar in the Output window).

To show the outputs an a table of numbers, press the *View As Table*
button (second from the left in the toolbar in the Output window).

To change which outputs are showing in the graph and table, press the
*Choose Outputs* button (third from the left in the toolbar in the
Output window).

**Multiple Output Windows**

You may have more than one output window for a given document (plot or
estate). The outputs shown in each of the output windows can be
unrelated, which allows you to look at several different aspects of the
simulation simultaneously.

**Output Descriptions**

The *C mass* of X is the mass of carbon in X, that is, the mass of all
the carbon atoms in X.

*Whole* means the whole of the land under consideration. The "whole
land" consists of the forest land and the agricultural land (one of
which may be missing, depending on the configuration). The land under
consideration is a plot in a plot simulation and an estate in an estate
simulation.

The *complete* mass of some land (whole, forest, or agricultural) is the
mass on and due to that land. It includes the plants, debris and soil.

The *onsite* mass of some land (whole, forest, or agricultural) is the
mass on that land. It includes the plants, debris and soil.

*Yield rates* are the combined rates of production and turnover, and are
what is observed by simply measuring the plants periodically.

*Emit* and *sequester* refer to emissions to the atmosphere and removal
from the atmosphere. That is, emissions and sequestrations/removals are
always to and from the atmosphere respectively.

Any moves of material between pools comprise a net movement, that is, it
is the combined effect of movement one way and the other way. In most
cases a move is only possible in one direction, but moves involving the
minerals pools can often be bi-directional.

**Graph**

A few points to note when using the graphing feature:

- Double-clicking on a graph item opens the graph settings window at the
  appropriate place. Single-clicking an item selects it, whereupon you
  can drag it around the window, or resize it by dragging on a handle.
  Shift-select to select multiple items. For example, make the graph
  bigger by single-clicking on it, then dragging the lower-right handle
  of the graph.
- The content of the titles (graph, x-axis, and y-axis) can either be
  set automatically by FullCAM or entered manually. Double-click on the
  relevant title to open the graph settings window, and then choose
  either *Automatic* or *Manual*. If *Manual* is selected, type in the
  desired wording for the graph.
- The axis scales (that is, the starting number, ending number, and
  where the tick marks occur) can either be set automatically by FullCAM
  or chosen manually. Double-click on the axis numbers to open the graph
  settings window at the appropriate place. Choose either *Automatic* or
  *Manual*, and if *Manual* type in the desired parameters.
- The axis, line, and border widths are chosen in points. When they are
  shown on the screen they are rounded to the nearest whole number of
  pixels, but when printed they are shown as the correct number of
  points. Thus minor width changes will not show up on the screen, but
  will show up in a printed version.
- Change the order of the outputs in the legend by switching to the
  table and dragging the output columns to the desired order.

**Graphing Using an External Program**

The graph is very configurable and will satisfy most users. If you wish
to create a graph in a different program:

1.  Save the data to a file using the *Save to File* button
2.  Open the resulting `.csv` file in a graphing capable program.

Alternatively: go to the table view, select the data you want (see
selection shortcuts, below), copy it, then go to the other application
and paste it as needed.

**Table**

Each row shows the state of the simulation at the END of the simulation
step in the leftmost two columns. Thus, a table row shows the state of
the plot AFTER the simulation step labelled in the row. For example, if
there are 12 simulation steps per year then a row with *Step in Year*
equal to "Feb" shows the state of the simulation at the END of February.

The first row of results always shows the initial conditions of the
simulation. This row is coloured differently. Outputs that do not
describe the initial conditions in a non-trivial manner do not have an
entry in the initial conditions row.

Resize the columns by dragging the line separating the columns in the
header (the line between the names of adjoining columns). FullCAM
remembers your adjustments when it saves the plot.

Move a column by dragging its heading. FullCAM remembers the new
arrangement when it saves the plot. FullCAM uses the order of the
outputs in the table to make the graph legend (arrange the outputs in
the graph legend by moving the table columns around).

Change the mass units of a column (typically from t/ha to kg or Mt per
hectare) by selecting a cell in the column and using the mouse menu or
the *Increase/Decrease Mass Unit* buttons in the toolbar.

Change the size of the window, and thus the area available to the table,
by dragging a corner.

Select a column by double-clicking in the header or units rows of the
column (or, for the first two columns, in the units row only), and
select all the columns over to a second column by holding the shift key
down while double-clicking the second column.

Select a row (except the second) by double-clicking in the first two
columns of the row, and select all the rows down to a second row by
holding the shift key down while double-clicking the second row.

Select all the data by pressing the *Select All Data* button. Select
everything in the table by pressing the *Select All* button.

Make arbitrary selections of data and statistics by dragging the mouse.
Drags that start in the heading rows are ignored (because they change
the order of the columns instead), as are drags that start in the time
columns.

When you have a selection, you can copy it (look on the mouse menu that
pops up when you click on the secondary menu button --- the right
button, if you hold the mouse in your right hand). From there you can
paste it into other programs, such as Microsoft Excel.

**Notes on Specific Outputs**

"Production rates", "turnover rates" and "yield rates" are for the END
of the step. Consider using more simulation steps per year. For example:
if you have yearly steps, clear the forest in day 365 of a year (thus,
the clearing occurs at noon on day 365 of the year), and plant trees on
day 1 of the next year (the trees are planted at noon of day 1), then
the reported production rate for the year (step) with the clearing will
be zero because the rate is for the last part of the year --- from noon
until midnight on day 365, when there were no trees!

The conditional irrigation output is only accurate in simulation steps
with no events (it is calculated from the conditional irrigation in the
period from the latter of the beginning of the step or the last event in
the step to the end of the step).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
