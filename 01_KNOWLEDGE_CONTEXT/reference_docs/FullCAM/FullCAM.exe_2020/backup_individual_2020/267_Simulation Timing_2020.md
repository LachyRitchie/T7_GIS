---
title: Simulation Steps
version: 2020
category: timing
original_file: 267_Simulation Timing_2020.md
---

Set the amount of time in a simulation step (all simulation steps
simulate the same amount of time).

A (simulation) *step* is the unit of time considered by a FullCAM
simulation. In each step, there is exactly one material movement from
one pool to the next pool due to processes (see Processes and
Events). Each step always simulates
the same amount of time. Steps are like the heartbeats of the model:
material moves from pool to adjoining pool once per step (exception:
more than once if the step is interrupted by an event).

The minimum time length per step is an hour.

The shorter the steps, the longer a plot simulation takes.

### Choosing the Number of Simulation Steps Per Year

*Time Resolution of Input Data*

If you specify the rainfall to FullCAM as just the total rainfall each
year (that is, one number per year), then it is unrealistic to expect
FullCAM to accurately simulate monthly or weekly phenomena that are
influenced by rainfall. Monthly simulation steps might be appropriate,
but the results might have to be interpreted carefully.

*Computing Time and Memory*

In a very lengthy simulation or one with many outputs, there may not be
enough computer memory to do a simulation with short steps, or it might
take a long time to generate results.

*Graininess*

In FullCAM, each atom of material belongs to one pool (such as trees
leaves), and carbon moves between the various pools once per step (at
the end of the step). While the rate of circulation of material among
the pools is mainly governed by the various physiological and empirical
rate inputs, it is subtly influenced by the length of step and
occasionally this is significant.

Consider carbon that flows from pool A to pool B to pool C (for example,
tree leaves to leaf litter to soluble mulch). It takes one step for any
carbon from pool A to reach pool B, and a second step for any of it to
reach pool C. If the steps are yearly then it takes two years for ANY
carbon from pool A to reach pool C, while with daily steps some carbon
can get to pool C by the end of the second day.

In reality, the step length is vanishingly small: carbon moves between
pools continuously, rather than in discrete movements that occur once
every beat of our simulation clock. Now, we want to model the essential
nature of the system with as little computing effort as possible. If we
decrease the step length then we get a more realistic simulation, but we
do more computing. This dependence of the simulation results on the step
length is called *graininess*.

The precision of the quantities in FullCAM is relatively low so
round-off error is almost insignificant --- but there is little point in
using more steps than necessary in case the round off error begins to
affect your results. FullCAM's flexibility in its treatment of time
allows you to overcome the artificial barriers set by arbitrary and
fixed frequencies of simulations steps.

What is a sensible amount of time per step? As you decrease the step
length, you will find your simulated results will gradually approach
limiting values. The limiting values are simulation results that stay
the same, no matter how much you further decrease the step length. From
the perspective of graininess, an appropriate step length is the step
length that gets you close to the limiting values.

As a rough rule of thumb, for negligible graininess use a step length of
a month.
