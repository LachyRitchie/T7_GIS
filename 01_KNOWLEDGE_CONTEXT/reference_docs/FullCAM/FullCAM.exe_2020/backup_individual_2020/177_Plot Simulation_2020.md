---
title: Plot Simulation
version: 2020
category: simulation
original_file: 177_Plot Simulation_2020.md
---

Some general aspects of simulating a plot in FullCAM.

**Timing: Steps and Time Periods**

The simulated time is partitioned into equal-length *steps*. Each step
may be punctuated by one or more events, because an event may occur at
any time.

A *time period* is the period of time from an event or step boundary to
the next event or step boundary (whichever occurs first). During a time
period, the only things that happen are processes (because, by
definition, there are no events). Within each time period, all the
processes are simulated as a single calculation that computes the effect
of the processes for the whole time period.

**System Separation**

The forest and agricultural systems are completely separate in a FullCAM
simulation, except for interaction through the Forest
Percentage. The forest and agricultural
systems have no effect on each other, except that the forest percentage
partitions the production in the two systems.

**Species Dependency**

An input is *species-dependent* if it depends on the species of plant by
describing a characteristic of material unique to that particular
species. Species dependency extends down to and includes the debris
layer, and and across to the product layer, but extends no further:

- Most of the inputs for the plant, debris and product layers are
  species dependent.
- None of the inputs for the mulch, soil, mineral or atmosphere layers
  are species dependent. Once in the mulch or soil, it is sufficient
  just to classify the plant material as either *resistant* or
  *decomposable* (and if mulch is being simulated, the resistant
  material as either *less resistant* or *more resistant*).

**Rationing of Scarce Resources**

If a resource is scarce (such as available nitrogen from the mineral
pool), the processes that use that resource compete for it. During each
time period:

1.  At the beginning of the time period, we compute all the *non-limited
    moves* of material from pool to pool due to each process (the moves
    that would occur if there were no scarcity of resources).
2.  The resources are rationed to each process on either a pro-rata or
    sequential basis (the choice is a plot input).
    - Pro-rata: Each actual move (exchange of material) is equal to the
      corresponding non-limited move multiplied by the *rationing
      fraction r*, where *r* is equal to the actual resource available
      divided by the sum of the amounts of the resource required by the
      non-limited moves.
    - Sequential: An order of processes that affect the resource that
      was specified in the plot input. For each process in turn, the
      moves (and exchanges of scarce resources) due to the process are
      recomputed --- and the remaining amount of scarce resource is
      updated after each process. Generally, early processes are
      allocated as much as they need and later processes (events)
      receive nothing.
3.  All the moves are applied.

The justification for pro-rata rationing is that each process is assumed
to use the scarce resource it requires at a constant rate over the time
period. Therefore, if there is not enough of the resource, then all of
the processes will be limited at the same time, having each received the
same fraction of its desired amount. Unless you are aware of the process
order for sequential rationing, it is recommended that resources be
rationed on a pro-rata basis.

Thus, for each time period, the processes are simulated as being
continuous and simultaneous.

The only scarce (potentially limiting) resource included in FullCAM at
this stage is available nitrogen.

**Example**. Suppose that in a given period of time:

- Process A requires 10 tN/ha of nitrogen (N) from the mineral pool.
- Process B requires 5 tN/ha.
- Process C requires 1 tN/ha.

Thus a total of 16 tN/ha of N is needed from the mineral pool. Suppose
there is only 7 tN/ha of N in the mineral pool. Then, under pro-rata
rationing, each process receives only 7/16 (the rationing fraction) of
what it requires:

- Process A gets (7/16) * 10 tN/ha of N from the mineral pool
- Process B gets (7/16) * 5 tN/ha
- Process C gets (7/16) * 1 tN/ha.
