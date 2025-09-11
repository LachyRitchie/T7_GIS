+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Tree Yield Formula**

The tree yield formula is one of the tree production methods in a
multi-layer forest (see [Configure Tree
Production](108_Configure%20Tree%20Production.htm)). It is an equation
for calculating tree growth, whose main inputs are maximum aboveground
biomass, tree age, and productivity.

**The Tree Yield Formula**

The tree yield formula for tree growth is

> *T(A) = r \* M \* y \** exp(*--k / d*)

where

*T* = Aboveground mass of the trees, in tdm/ha, if there was constant
(and thus average) productivity

*A* = Age of the tree (either the age of the oldest trees, or the
average age of the trees --- see the [Growth
Properties](42_Growth%20Properties.htm) window), in years

*M* = Maximum aboveground biomass of trees, in tdm/ha
([Site](200_Site.htm) page)

*r* = Maximum aboveground biomass multiplier ([Growth
Properties](42_Growth%20Properties.htm) window), a species-dependent
modifier of *M* (thus the maximum aboveground biomass used is *r \* M*)

*y* = Tree yield multiplier. Initially equal to one in any plot
simulation, then changed to the type 2 growth multiplier of the latest
forest treatment event

*k* = *2 \* G* -- 1.25.

> *G* = Tree age of maximum growth, in years ([Growth
> Properties](42_Growth%20Properties.htm) window, expressed as a
> multiplier of the maximum aboveground biomass plus a constant). This
> is also usually the age at which the canopy closes.

*d* = Adjusted age of the trees, in years

= *A* + sum over each treatment of

  --------------------- -- --------------------------------
  0                        if *A \<= W*
  *v \* (A -- W) / U*      if *A \>= W* and *A \<= W + U*
  *v*                      if *A \> W + U*
  --------------------- -- --------------------------------

where, for each treatment undergone by the forest, specified by the type
1 parameters in the forest treatment events,

*v* = the age advance due to the treatment, either positive or negative,
in years\
*U* = the advancement period, in years\
*W* = the age (of same type as *A*) at which the treatment was applied,
in years.

**Notes**

Thus *T* asymptotically approaches *r \* M \* y* from below as *d*
increases. Note that exp(0) = 1, exp(negative) *\<* 1, and exp(any) *\>*
0. The maximum aboveground biomass for trees when the tree yield formula
is in use is *r \* M \* y*. The forest treatment events move the forest
back and forth along the growth-age curve described by the tree yield
formula, where each age advance is phased in linearly over the
advancement period. When the tree yield formula is in use (that is, the
current tree species uses the tree yield formula to determine its
growth), all age-based properties of the trees use the adjusted age of
the trees (*d*), including the [Tree Growth
Allocations](112_Tree%20Growth%20Allocations.htm),
[Mortality](121_Mortality.htm), and [Stem Density](9_Stem%20Density.htm)
time-series.

**Non-Constant Productivity**

The tree yield formula above gives the growth-age curve of the tree if
the productivity of the site remains constant. Site productivity is
specified by the [Forest Productivity Index
(FPI)](188_Forest%20Productivity%20Index.htm) time-series. In practice
the FPI can vary substantially over time in some environments, which can
have a very marked effect on tree growth.

The relationship between *M* and the average annual FPI *Pavg* over the
life of the tree is taken to be (from observations in experiments)

> *M =* \[ 6.0109 \* sqrt(*Pavg*) *--* 5.2912 \] *\^* 2.
>
> Notation: *x \^* 2 = *x \* x*, and *x* = sqrt(*x \* x*).

Thus, we calculate *Pavg* from *M*. We assume a linear relationship
between FPI and aboveground tree mass in the short term, so the
aboveground mass increment from adjusted age *a1* to *a2* is

> *r \* M \** \[ *y2 \** exp(*--k / a2*) *- y1 \** exp(*--k / a1*) \] \*
> (*P / Pavg*)

where

*P* = the actual FPI over the period *a1* to *a2* (so if using monthly
time steps, *P* will be about *Pavg*/12 on average) (*Site :
Productivity* window),

*y1* = the value of *y* at age *a1*,

*y2* = the value of *y* at age *a2*.

If the maximum annual FPI of 30 was present during the whole life of the
trees, the average annual FPI *Pavg* would be 30 and thus the maximum
aboveground biomass *M* would be 764 tdm/ha (which is the maximum *M*
value you can enter for trees on the *Site* page) (note that (6.0109 \*
sqrt(30) -- 5.2912)\^2 = 764).

**Data Inputs to the Formula**

Thus the data inputs to the tree yield formula are:

1.  *M*, the maximum aboveground biomass
2.  *r*, the species-multiplier of the maximum aboveground biomass
3.  *G*, the tree age of maximum growth
4.  *P*, the time-series of the forest productivity index
5.  *y*, the tree yield multiplier (which can be changed by type 2
    forest treatment events)
6.  The age advances specified by the type 1 forest treatment events.

On the [Departmental Server](219_Departmental%20Server.htm), *r* and *G*
are calculated from other inputs. See [Growth
Properties](42_Growth%20Properties.htm).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
