---
title: Decay Rate Window
version: 2020
category: Simulation
original_file: 86_Decay Rate Window_2020.md
---

This window is for entering a single number that describes the rate of
decay of a pool due to some process.

Enter the decay rate using any of the nine equivalent expressions (the
FullCAM interface only ever shows the half life).

**Definition**

The *decay rate* is the number that describes how fast material leaves a
pool. This window is for entering the decay rate for a decay process in
FullCAM.

**Example**. A decay rate of 10% per year means that:

- After the first year only 90% of the pool remains
- After two years only 90% * 90% = 81% of the original pool remains
- In the third year another 10% of the material present at the beginning
  of the third year is lost, so after three years only 90% * 90% * 90%
  = 72.9% of the original pool remains.

The simple model above occurs in many places in FullCAM, for example
when describing the turnover of plant components, the breakdown of
debris, or the decomposition of product pools.

Although the rate of outflow can be measured more easily if there is no
inflow into the pool, there can be inflows to the pool at the same time
as the decay process is causing material to leave the pool. The decay
rate simply measures the rate of the outflow due to the decay process.

The process by which material leaves the pool above is *exponential*,
because the rate at which material leaves is proportional to the amount
of material present. An exponential decay model is widely used in
FullCAM because it is a reasonably accurate representation of a wide
range of biological processes.

**Equivalent Expressions**

In the FullCAM interface the rate asked for is the half life. The half
life is the way that FullCAM stores a decay rate and the way it uses it
in the simulation calculations.

Some rates are not suitably expressed as the percentage lost per year.
For example, 99.999% lost per year is better expressed as 61.7% lost per
month, or 3.1% lost per day, or a half life of 22 days. There is no
single way for specifying the rates that is suitable over the wide range
that might be used in FullCAM.

There are nine equivalent expressions for the decay rate. Click on a
radio button to enter the rate in that form. Press the *Tab* key to
enter the number typed into FullCAM, and have the rate translated into
the other expressions.

**Graph**

The graph shows the amount left in the pool as a percentage of the
original amount in the pool (red), and the half life of the decay
process (orange).

**Decay Equation**

The equation for exponential decay, shown in the graph, is that after a
time *T*:

  ----------------------------------------- -- ------------------------------------------
  The fraction lost from the pool is           1 -- [(1 -- *f*) ^*T*]
  The fraction remaining in the pool is        (1 -- *f*) ^*T*
  The percentage lost from the pool is         100 * 1 -- [(1 -- 0.01 * *p*) ^*T*]
  The percentage remaining in the pool is      100 * (1 -- 0.01 * *p*) ^*T*
  ----------------------------------------- -- ------------------------------------------

where *f* is the fraction lost per year and *p* is the percentage lost
per year (*p* = 100 * *f*). Note that "^" means "to the power of", for
example 3^2 = 3 to the power of 2 = 3 squared = 9.

**Limits**

Because of limits in the numerical representation used in FullCAM some
equivalent expressions (conversion of percentage to half life, and vica
versa), will show values limited by the FullCAM display. For example,
entering a half life value of 800,000 years will show a percentage
remaining value of 0%, as the half life value has been converted to a
percentage value so high, it cannot be displayed accurately. However the
correct value is stored internally in FullCAM and is not a cause for
concern for calculations.

The decay rate entered in this window cannot be higher than 100% lost
(equivalent to a half life of 0.0 years) or lower than 0.0% lost per
year (equivalent to a half life of 800,000 years).

Values can be entered as either percentage remaining or half life. When
entering values as a percentage remaining, the display limitation will
be encountered much sooner than via half life. For most uses inputting
via the percentage remaining should be sufficient.
