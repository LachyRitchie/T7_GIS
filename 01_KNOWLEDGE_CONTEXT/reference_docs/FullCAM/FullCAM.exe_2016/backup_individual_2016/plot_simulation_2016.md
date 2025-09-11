---
title: Plot Simulation
version: 2016
category: Simulation
original_file: 177_Plot Simulation_2016.md
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

An input is *species-dependent* if it depends on the species of plant
(that is, it describes a characteristic of material unique to that
particular species). Species dependency extends down to and includes the
debris layer, and across to the product layer, but extends no further:

- Most of the inputs for the plant, debris and product layers are
  species dependent.
- None of the inputs for the mulch, soil, mineral or atmosphere layers
  are species dependent. Once in the mulch or soil, it is sufficient
  just to classify the plant material as either *resistant* or
  *decomposable* (and if mulch is being simulated, the resistant
  material as either *less resistant* or *more resistant*).

**Rationing of Scarce Resources**

If a resource is scarce, the processes that use that resource compete
for it. During each time period:

1.  At the beginning of the time period, we compute all the *non-limited
    moves* of material from pool to pool due to each process (the moves
    that would occur if there were no scarcity of resources).
2.  The resources are rationed to each process on either a pro-rata or
    sequential basis (the choice is a plot input).
    - Pro rata: Each actual move (exchange of material) is equal to the
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