+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Simulation Steps**

\[[Timing](199_Timing.htm) page : *Simulation Steps* panel\]

Set the amount of time in a simulation step (all simulation steps
simulate the same amount of time).

A (simulation) *step* is the unit of time considered by a FullCAM
simulation. In each step, there is exactly one material movement from
one pool to the next pool due to processes (see [Processes and
Events](58_Processes%20and%20Events.htm)). Each step always simulates
the same amount of time. Steps are like the heartbeats of the model:
material moves from pool to adjoining pool once per step (exception:
more than once if the step is interrupted by an event).

The minimum time length per step is an hour.

The shorter the steps, the longer a plot simulation takes.

If you are simulating carbon only, monthly time steps are usually
sufficient. If simulating nitrogen, we recommend daily time steps
because nitrogen often gets used and replenished in a few days.

### Choosing the Number of Simulation Steps Per Year

*Time Resolution of Input Data*

If you specify the rainfall to FullCAM as just the total rainfall each
year (that is, one number per year), then it is unrealistic to expect
FullCAM to accurately simulate monthly or weekly phenomena that are
influenced by rainfall. Monthly simulation steps might be appropriate,
but the results might have to be interpreted carefully.

*Computing Time and Memory*

In a lengthy simulation or one with many outputs, there may not be
enough computer memory to do a simulation with very short steps, or it
might take longer to compute than is convenient.

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
reach pool C. If the steps are yearly then it takes two years for any
carbon from pool A to reach pool C, while with daily steps some carbon
can get to pool C by the end of the second day!

In reality, the step length is vanishingly small: carbon moves between
pools continuously, rather than in discrete movements that occur once
every beat of our simulation clock. This dependence of the simulation
results on the step length is called *graininess*.

As you decrease the step length, you will find your simulated results
will gradually approach limiting values. The limiting values are
simulation results that stay the same, no matter how much you further
decrease the step length. From the perspective of graininess, an
appropriate step length is the step length that gets you close to the
limiting values. For example, if halving the step length does not change
the results much then there is no point in decreasing it further.

For negligible graininess use a step length of at most:

- A month if just modelling carbon.
- A day if modelling mulch or nitrogen.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
