---
title: Output Steps
version: 2016
category: Output
original_file: 27_Output Steps_2016.md
---

[Timing page : *Output Steps* panel]

Choose which simulation steps produce outputs, that you can view on the
Output Windows.

**Output Steps**

An *output step* is a simulation step in which the state of the
simulation is recorded in the outputs, for viewing in the output windows
(which show graphs and tables of results), for risk analysis, and so on.

The simulation state is recorded at the END of the output step, that is,
after the movements of material for that step have occurred.

FullCAM always records the simulation step at the beginning and the end
of the simulation, that is, the "step immediately before the simulation
starts" (as it were) is always an output step, and the last step of the
simulation is always an output step.

In a plot simulation, FullCAM typically spends more time displaying the
simulation results in a table or graph than it spends calculating the
results. Have as few output steps as possible, consistent with getting
enough output for your purposes. If you want to increase the underlying
resolution in the simulation, decrease the simulation step length
instead (Simulation Steps).
