+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Sensitivity of Debris Breakdown to Temperature and Water**

\[[Debris Properties](45_Debris%20Properties.htm) window : *Sensitivity*
section\]

Specify how the breakdown rates of the debris increase with increasing
temperature and water.

**Introduction**

You can choose either of both of two styles of sensitivity:

Mulch style.\
[Soil](203_Soil.htm) style (as in [RothC](114_RothC.htm)).

The mulch layer always has temperature and water sensitivity: the mulch
decomposition rates increase with increasing temperature and rainfall.
Turning on mulch-style sensitivity will cause the debris breakdown layer
to behave with mulch-like responses to conditions. Mulch-style
sensitivity can be used to provide a more mulch-like simulation, if
required.

The soil layer always has temperature and water sensitivity: the soil
decomposition rates increase with increasing temperature and decreasing
topsoil moisture deficit.

All debris pools are always affected in the same manner. The same
sensitivity factor applies to the breakdown rate of each debris pool.

**No Sensitivity To Temperature or Water**

If neither style of sensitivity is on, then the fraction of each debris
pool lost due to breakdown is equal to the breakdown percentage for the
pool (entered elsewhere on the window) adjusted to the relevant period
of time:

> *g* = *M \* L*,

where

*g* = mass of material lost from the pool due to breakdown in the time
period

*M* = mass of the pool at the beginning of the time period

*L* = fraction of mass in the pool at the beginning of the time period
that is lost due to breakdown

= 1 -- (1 -- *f*)\^*y*

*f* = breakdown fraction (fraction lost due to breakdown per year)

= breakdown percentage of pool / 100

*y* = number of years in time period.

Note that *g*, *M*, and *L* are independent of temperature and water. 0
\<= *f* \<= 1.

**Mulch-Style Sensitivity**

If mulch-style sensitivity is on and soil-style sensitivity is off, then
you must enter the sensitivity to temperature (*s*) and the sensitivity
to water (*v*), which determine how sensitive the breakdown rates are.

> *g* = *M \* L* \* \[ 1 -- exp(--*s \* T*) \] \* \[ 1 -- exp(--*v \*
> W*) \]

where

*s* = the sensitivity of breakdown to temperature (*s* \>= 0)

*T* = the average air temperature (in deg C, negative temperatures
treated as zero for this purpose) during the time period (*T* \>= 0),

*v* = the sensitivity of breakdown to water (*v* \>= 0)

*W* = the total rainfall and irrigation (in mm) during the time period
(*W* \>= 0). Notice that both the temperature factor

> 1 -- exp(--*s \* T*)
>
> and the water factor
>
> 1 -- exp(--*v \* W*)
>
> are:
>
> - Between 0 and 1
> - Nearer 0 (less breakdown) as *T* and *W* fall or as *s* and *v* fall
> - Nearer 1 (more breakdown) as *T* and W rise or as *s* and *v* rise.

The overall rate of breakdown is quite sensitive to *s* and *v*. If *s*
or *v* are too small then there is almost no breakdown; if *s* or *v*
are too large then sensitivity is lost. As a very rough guide:

- set *s* to about 1 / (average temperature in a simulation step)
- set *v* to about 1 / (average rainfall-plus-irrigation during a
  simulation step).

If mulch-style sensitivity is on, the rate of breakdown falls to zero
when the average air temperature is at or below freezing or there is no
rainfall or irrigation specified.

**Soil-Style Sensitivity**

This option is only possible when the soil is modelled, because it uses
the topsoil moisture deficit in the soil and various RothC soil inputs
to compute the rate of breakdown. If it is on then it will cause a
difference to aboveground results when the soil is and is not included
in the model --- because if the soil is included in the model then this
sensitivity is on but if the soil is not included then this sensitivity
is off.

If soil-style sensitivity is on and mulch-style sensitivity is off, then
you do not need to enter any inputs: FullCAM uses the sensitivity
defined in the soil model ([RothC](114_RothC.htm)), which does not have
any inputs exposed in the user-interface.

> *g* = *M* \* *L*,

where

*L* = fraction of mass in the pool at the beginning of the time period
that is lost due to breakdown

> = 1 -- (1 -- *f*)\^(*y* \* *a* \* *b*)
>
> *a* = rate modifier due to temperature
>
> = 47.91 / (1 + exp0(106.06 / (18.27 + *T*)) for *T* \> --5
>
> 0 for *T* \<= --5
>
> *b* = rate modifier due to water

= 0.2 + 0.8 \* (*e* -- TSMD) / (*h* \* \[(20 + 130 \* *c* -- 100 \* *c
\* c*) \* (*d* / 23)\])

if version 26.3 of RothC in use

1 / (1 + exp\[ (TSMD -- (0.688405334 + 4.4746369 \* *c* -- 3.44203 \* *c
\* c*) \* *d*)

/ ((0.082530817 + 0.5364083 \* *c* -- 0.41268 \* *c \* c*) \* *d*) \]

if version 26.5 of RothC in use

*c* = clay fraction of soil

*d* = sample depth of soil

*h* = Ratio of the maximum TSMD when soil is bare to the maximum TSMD
when soil is covered

TSMD = topsoil moisture deficit (as computed by RothC).

Increasing *a* or *b* increases the effective time of decomposition, or
effectively increases the rate of decomposition during a given time
period. Increasing *T* or *W* increases *a* and *b* respectively
(increasing *W* tends to increase the TSMD). 0 \<= *a* \<= 1 and 0 \<=
*b* \<= 1.

**Combined Mulch-Style and Soil-Style Sensitivity**

If soil-style sensitivity and mulch-style sensitivity are both on then
FullCAM combines both styles of sensitivity.

*g* = *M \* L* \* \[ 1 -- exp(--*s \* T*) \] \* \[ 1 -- exp(--*v \* W*)
\],

where

*L* = 1 -- (1 -- *f*)\^(*y* \* *a \* b*)

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
