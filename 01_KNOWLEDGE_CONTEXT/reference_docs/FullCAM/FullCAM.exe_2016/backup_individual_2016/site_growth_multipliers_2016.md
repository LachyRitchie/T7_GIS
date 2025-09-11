---
title: Site Growth Multipliers
version: 2016
category: Site
original_file: 39_Site_Growth Multipliers_2016.md
---

[Site page : *Growth Multipliers* button]

Enter information about growth variations on the plot compared to the
standard site for which the plant growth information is intended.

**Use**

The growth multipliers multiply the growth rates of the trees and crops,
to reflect site variation from a standard site.

Each input multiplies the growth of its component in every step of the
simulation. A setting of 1.0 is neutral (no adjustment); a setting of
1.10 will cause the plant component to grow 10% faster than the amount
otherwise calculated; a setting of 0.0 cuts off growth altogether.
"Growth" here means NPP if the growth is calculated using NPPs, or yield
if the growth is calculated using yields. These multipliers are applied
after all other growth computations (such as allocations).

These inputs should generally remain neutral (that is, 1.0) when
developing a model, but may be used to model the effect of different
environmental conditions --- such as less allocation to roots with
better moisture and nutrient availability. These growth multipliers can
be used as a shortcut to altering the relative growth tables. They are
useful as risk inputs in a risk analysis.