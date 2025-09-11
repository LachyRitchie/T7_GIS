---
title: Decay Rate Window
version: 2016
category: Interface
original_file: 86_Decay Rate Window_2016.md
---

[Plant Properties window : any *Decay
Rate* button]
[Debris Properties window : any *Decay
Rate* button]

This window is for entering a single number that describes the rate of
decay of a pool due to some process.

Enter the decay rate using any of the nine equivalent expressions (the
FullCAM interface only ever shows rate as the percentage lost after a
year).

**Definition**

Consider a pool of material where:

1.  Material leaves the pool at a rate that is proportional to the
    amount of material in the pool
2.  No material enters the pool.

The *decay rate* is the number that describes how fast the material in
the pool leaves the pool. This window is for entering the decay rate for
a decay process in FullCAM.

**Example**. A decay rate of 10% per year means that:

- After the first year only 90% of the pool remains
- After two years only 90% * 90% = 81% of the original pool remains
- In the third year another 10% of the material present at the beginning
  of the third year is lost, so after three years only 90% * 90% * 90%
  = 72.9% of the original pool remains,

and so on.

The simple model above occurs in many places in FullCAM, for example
when describing the turnover of plant components, the breakdown of
debris, or the decomposition of product pools.

Although the rate of outflow can be measured more easily if there is no
inflow into the pool, there can be inflows to the pool at the same time
as the decay process is causing material to leave the pool. The decay
rate simply measures the rate of the outflow due to the decay process.

(The process by which material leaves the pool above is *exponential*,
because the rate at which material leaves is proportional to the amount
of material present. An exponential decay model is widely used in
FullCAM because it is a reasonably accurate representation of a wide
range of biological processes, while being mathematically simple).

(The process by which material leaves the pool above is *exponential*,
because the rate at which material leaves is proportional to the amount
of material present. An exponential decay model is widely used in
FullCAM because it is a reasonably accurate representation of a wide
range of biological processes, while being mathematically simple).

**Equivalent Expressions**

In the FullCAM interface, the rate asked for is the percentage lost per
year (for example the percentage of coarse roots turnover per year, or
the percentage of product decomposed each year). The "percentage lost
per year" is the way that FullCAM stores a decay rate and the way it
uses it in the simulation calculations.

However, some rates are not suitably expressed as the percentage lost
per year. For example, 99.999% lost per year is better expressed as
61.7% lost per month, or 3.1% lost per day, or a half life of 22 days.
There is no single way for specifying the rates that is suitable over
the wide range that might be used in FullCAM. Hence this window.

By clicking on the button next to the rate box in the FullCAM interface,
you opened this window, the decay rate window. The only purpose of this
window is to enter a single number, the decay rate. The use of this
window is optional --- the single number in the regular FullCAM
interface (which is always the percentage lost after a year) is usually
enough.

There are nine equivalent expressions for the decay rate. Click on a
radio button to enter the rate in that form. Press the *Insert* key to
enter the number you type into FullCAM (as in the FullCAM interface),
and have the rate translated into the other eight expressions.

**Graph**

The graph shows the amount left in the pool as a percentage of the
original amount in the pool (red), and the half life of the decay
process (orange).

**Decay Equation**

The equation for exponential decay, shown in the graph, is that after a
time *T*:

  ----------------------------------------- -- ------------------------------------------
  The fraction lost from the pool is           1 -- [(1 -- *f*) *T*]
  The fraction remaining in the pool is        (1 -- *f*) *T*
  The percentage lost from the pool is         100 * 1 -- [(1 -- 0.01 * *p*) *T*]
  The percentage remaining in the pool is      100 * (1 -- 0.01 * *p*) *T*
  ----------------------------------------- -- ------------------------------------------

where *f* is the fraction lost per year and *p* is the percentage lost
per year (*p* = 100 * *f*). Note that "^" means "to the power of", for
example 3^2 = 3 to the power of 2 = 3 squared = 9.

**Limits**

The decay rate shown in this window cannot be:

- Higher than 99.999 999 998% lost per year (equivalent to 6.5% lost per
  day and to a half life of 0.028 years)
- Lower than 0.0001% lost per year (equivalent to 0.000000274% lost per
  day and to a half life of 693,146 years)

Above and below these limits not all the nine equivalent expressions can
be shown, because of limits in the numerical representation used in
FullCAM (64-bit floating point numbers). Near these limits, some of the
equivalent expressions may be slightly different to what you type in.
This phenomenon is intrinsic to the equivalent expressions, and of no
concern. The expression stored by FullCAM is the percentage lost after a
year. A number typed into another expression is converted to this form
in FullCAM, and then displayed by converting back to the appropriate
equivalent expression. So, when you type in a number in one of the
equivalent expressions, the number is converted to a percentage lost
after a year and then converted back before being displayed. These
conversions are slightly inaccurate at extreme values, due to numerical
roundoff. Any conversion errors are insignificant compared to
experimental error, so, while slightly annoying, are of no concern.

If this decay rate window is used to edit a decay rate outside the
limits, the decay rate is first changed to fit just within the limits.

If you want to enter a decay rate of zero, you have to do so in the
FullCAM interface rather than in this decay rate window.

**Window Navigation**

Although it is possible to navigate the screen with tabs and up-down
arrow keys, we recommend selecting the type of description (the radio
buttons) with the mouse. Because you have to use the mouse in this
window anyway, you can only use the mouse to click the buttons that open
the decay rate window (rather than being able to tab to those buttons).