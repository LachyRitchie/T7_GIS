+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Plant Properties**

\[[Trees](215_Trees.htm) page or [Crops](216_Crops.htm) page :
*Properties of the Species* panel : *Plants* button\]

Specify the non-growth properties of the species, for the current
species ([Select a Species](56_Select%20a%20Species.htm)).

**Carbon Percentages**

The carbon percentage of a tree or crop component is the mass of carbon
in the component.

The carbon percentages for a range of tree components can be found in
the NCAS Technical Reports No.s
[7](reps/TR7%20Carbon%20Content%20of%20Woody%20Roots%20Revised%20Analysis%20and%20a%20Comparison%20with%20Woody%20Shoot%20Components%20(Revision%201).pdf){target="_blank"}
and
[22](reps/TR22%20Carbon%20Contents%20of%20Above-Ground%20Tissues%20of%20Forest%20and%20Woodland%20Trees.pdf){target="_blank"}.

**Typical carbon contents for tree species (taken from Table 9 of the
*Land Use Change Methods* Report):**

  Tree component      Carbon Content
  ------------------ ----------------
  Stems                    50.0
  Branches                 47.0
  Bark                     49.0
  Leaves and twigs         52.0
  Coarse Roots             50.0
  Fine Roots               48.0

**Typical carbon contents for some plant species:**

Crop Type

GBF

Stalks

Leaves

Coarse Roots

Fine Roots

Cereal

43.43

43.75

44.1

Improved Pasture

37.46

37.46

Unimproved/Native Pasture

40.9

40.9

Irrigated Cotton

43.43

45.0

43.25

45.0

43.25

Sugarcane

39.0

43.75

44.1

**Turnover Percentages**

Turnover represents the part of a plant component being shed by the
plant. Turnover material is dead, and moves to the debris. All of the
parts of a plant except tree stems are subject to turnover.

The turnover percentage of a plant pool determines how much material is
turned over. Setting a turnover percentage to 0 means that there is no
turnover. A turnover percentage of 100% means that in each simulation
step all of the pool dies and moves to debris, so the only material in
the pool at the end of the step is new material that was produced during
the step.

In FullCAM, turnover rates are assumed to be constant throughout the
year using the same turnover fraction in every simulation step. This
would be an unrealistic assumption for the turnover of leaves for
deciduous trees and perennial grasses.

The turnover percentage of a plant pool is the percentage lost per year
due to turnover. It assumes exponential decay at a constant decay rate.

Typical turnover rates for trees are described in Table 10 of the report
*Land Use Change in Australia: In Integrated Application of the National
Carbon Accounting System*. Turnover rates for additional species can be
extracted from the FullCAM database.

\

Typical turnover rates for tree species, (taken from Table 10 of the
*Land Use Change Methods* Report) :

  Tree component    Turnover Rate
  ---------------- ---------------
  Leaf                  4.70
  Branch                0.56
  Bark                  0.83
  Coarse Root           5.60
  Fine Root             10.42

\

Typical turnover rates for crop species

  Crop component    Turnover Rate
  ---------------- ---------------
  GBF                    0.0
  Leaf                  86.0
  Stalk                 10.0
  Coarse Root           10.0
  Fine Root             150.0

**Stem Density**

For trees only. See the [Stem Density](9_Stem%20Density.htm) time
series.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
