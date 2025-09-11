+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Forest Treatment**

\[[Event Window](137_Event%20Window.htm) : *Forest Treatment* panel\]

Enter the inputs specific to a forest treatment event.

**Details**

A forest treatment can be applied to a forest whose growth is being
determined by the tree yield formula [Tree Yield
Formula](130_Tree%20Yield%20Formula.htm). The treatment alters the
growth characteristics of the trees onward from that point in time.

Each treatment has a Type 1 and a Type 2 effect as described in Snowden
(2002). A Type 1 event occurs during the life of a rotation and has an
effect for a specified period (generally to advance the rate of growth)
in a way that would likely shorten overall rotation length. A Type 2
event is an increase in site productivity (possibly due to species
change) over the entire rotation period.

**Type 1: Age Advance**

A type 1 treatment moves the forest back or forth along the growth-age
curve determined by the tree yield formula, by advancing or retarding
the adjusted age of the trees used in the formula. See [Growth
Properties](42_Growth%20Properties.htm).

The tree age used in the tree yield formula is advanced by the *Age
advance due to treatment*, phased in steadily over the years in the
*Advancement period* (which begins starting with the event).

**Type 2: Tree Yields**

When the tree yield formula is in use, the maximum aboveground biomass
is equal to the maximum aboveground biomass entered in the *Site* window
(*M* in the [Tree Yield Formula](130_Tree%20Yield%20Formula.htm))
multiplied by the current tree yield multiplier (*y*).

Thus the "tree yield multiplier" multiplies the tree yield that would
otherwise be computed by the tree yield formula (because the tree yield
is proportional to the maximum aboveground biomass in the tree yield
formula), and likewise multiplies the maximum aboveground forest biomass
allowed on the site.

The tree yield multiplier always starts a simulation at 1.0, and only
changes due to forest treatments. Each type 2 forest treatment replaces
the previous treatment.

[Snowden, P. (2002). Modelling Type 1 and Type 2 Growth Responses in
Plantations after Application of Fertilizer or Other Silvicultural
Treatments. *Forest Ecology and Management* **163**:229--244.]{.small}

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
