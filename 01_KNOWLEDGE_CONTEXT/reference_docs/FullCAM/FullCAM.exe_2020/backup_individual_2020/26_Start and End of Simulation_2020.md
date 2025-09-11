---
title: Start and End of Simulation
version: 2020
category: timing
original_file: 26_Start and End of Simulation_2020.md
---

Set the time period over which the simulation runs.

**Daily Timing**

The simulation runs from the beginning of the start date to the end of
the end date.

Enter dates as, for example, "12 jan 1956" or "12 1 1956".

**Yearly Timing**

The starting time and ending times each consist of:

- A calendar year (such as 2005).
- A step number, which can be any number from one to the number of steps
  per year. If the simulation steps are yearly (one step per year) then
  the only valid step number is "1". The step number can never exceed
  8760, the maximum number of simulation steps per year and the number
  of hours in a year

A number with a red background is not ready:

- A year is not ready if the start year is greater than the end year.
- A step number is not ready if it greater than the number of simulation
  steps per year, or if the start and end years are the same and the
  start step number is greater than the end step number.
