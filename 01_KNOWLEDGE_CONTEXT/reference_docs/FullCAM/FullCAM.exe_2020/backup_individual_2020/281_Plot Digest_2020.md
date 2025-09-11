---
title: Plot Digest
version: 2020
category: simulation
original_file: 281_Plot Digest_2020.md
---

Within plot digest multiple scenarios can be created and edited.
Scenarios comprise a set of input values (i.e. the values editable
within FullCAM).

The plot digest function will simulate each scenario created using the
input values specified for each.

The Plot Digest window becomes visible when an open plot file is saved
as a plot digest (.pld) using the File\Save As function.

**Scenario\Input Editing**

1.  *New...* will create allow creation of a new scenario.
2.  *Clone* will duplicate an existing scenario.
3.  *Delete* will permanantly remove a scenario.
4.  *Clone from Plots...* will open a dialogue which prompts to select
    existing plot('s) which will be added as new scenarios.

**View By** Options to change the Digest view.

The plot digest tab can be viewed by scenario, scenario by category or
input.

1.  *Scenario* (default) - will show scenarios at the top of the tree.
    Inputs will be branches below the Scenario.
2.  *Scenario by category* - will show scenarios at the top of tree.
    Sub-branches will have Section names (these are the main tabs in a
    FullCAM plot window), then Inputs beneath.
3.  *Input* - will show Inputs at the top of the tree. Scenarios using
    those inputs will be branches below those Inputs. Some Digest
    functionality will be limited while in Input view.

**Simulation Options** Options for controlling the outputs from the
simulation and units reported.

1.  *Combine all Plots* will combine all the results into one set of
    values.
2.  *Per Scenario* will output separate results for each scenario.
    (Average results are not available).
3.  *Per Output* will ouput separate results for each FullCAM output.

The 'Average Combined plots (not sum)' checkbox outputs an unweighted
average between scenarios when selected. When unselected, it will sum
the outputs of each scenario.

The 'Mass outputs converted to unit/ha' checkbox divides the mass
output by hectares to give a unit per hectare figure.

The 'Update spatial data for each scenario' updates the spatial data
for each scenario run.

**Scenario Inputs** The second column in the list is the values of the
input elements that will replace the current plot input values during
simulation. Plots will not actually be changed by these scenarios.

**Use**

On this page new digest elements can be added, edited, cloned, and
deleted.

A scenario must be selected on the Digest tab before some functionality
will become usable.

The input elements can be added to the current or all the digest
elements from right clicking and selecting the options from the Explorer
page which has all the inputs available.

Input elements can also be added from any tab within a FullCAM plot file
using the following keyboard shortcuts. The desired input should be
selected for editing when pressing the shortcut. A pop-up notification
will confirm when an output has been added.

1.  ctrl-alt-s - add field to selected scenario.
2.  ctrl-alt-d - add field to all scenarios.
3.  Explorer - use the right-click context menu on items to add to the
    selected (ctrl-alt-a) or all scenarios (ctrl-alt-d).

Once scenarios have been chosen, the digest can be run by running a
FullCAM plot digest simulation (F9) or clicking the FullCAM Running-Man.
