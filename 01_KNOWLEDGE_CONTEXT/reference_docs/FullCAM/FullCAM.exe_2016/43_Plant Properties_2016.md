+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Plant Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Plants* button\]

Specify the non-growth properties of the species, for the current
species ([Select a Species](56_Select%20a%20Species.htm)).

**Carbon Percentages**

The carbon percentage is the fraction of the dry mass that is carbon.

**Turnover Percentages**

Turnover represents the part of a plant component being shed by the
plant. Turnover material is dead and moves to the debris pool. All of
the parts of a plant except tree stems are subject to turnover,
including roots.

The turnover percentage of a plant pool determines how fast material is
turned over (how frequently it falls from the plant). Setting a turnover
percentage to 0 means that there is no turnover. A turnover percentage
of 100% means that in each simulation step all of the pool dies and
moves to debris (so the only material in the pool at the end of the step
is new material --- plant components --- that was produced during the
step).

In FullCAM, turnover rates are assumed to be constant throughout the
year --- that is, the same turnover fraction is used in every simulation
step.

The turnover percentage of a plant pool is the percentage lost per year
due to turnover (that is, 100% less the percentage of the original
material that is still there a year later, if turnover is the only
process removing material from the plant pool). It assumes exponential
decay at a constant decay rate. Click the exponential decay button for
alternative expressions, a graph, and a fuller explanation.

Typical turnover rates for trees are described in Table 10 of the report
*Land Use Change in Australia: In Integrated Application of the National
Carbon Accounting System*. Turnover rates for additional species can be
extracted from the FullCAM database.

TABLE -- Typical turnover rates for tree species, (taken from Table 10
of the *Land Use Change Methods* Report) :

  Tree component   Turnover Rate (Fraction)
  ---------------- --------------------------
  Leaf             0.0470
  Branch           0.0056
  Bark             0.0083
  Coarse Root      0.0560
  Fine Root        0.1042

Turnover rates for annual crops are typically set at 0.81/yr.

**Stem Density**

For trees only. See the [Stem Density](9_Stem%20Density.htm)
time-series.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
