---
title: Yield and Net Primary Production
version: 2016
category: Concepts
original_file: 131_Yield and Net Primary Production_2016.md
---

Yield and net primary production are related concepts and you will need
to know how they are defined in order to understand plant growth in
FullCAM.

**Turnover**

A plant is normally "turning over" or shedding material, producing
"litterfall" aboveground and "root slough" belowground.

**Net Primary Production**

The net increase in plant mass due to the addition of new plant material
is called the *net primary production* (NPP), which includes the effects
of both photosynthesis and respiration. net primary production is
difficult to measure due to the confounding effect of *turnover* (in
which all plant components except tree stems lose portions via
turnover), and is of interest mainly to people tracking tree physiology.

net primary production is due to the combined effects of photosynthesis
and respiration. The mass added by photosynthesis is called *gross
primary production* (GPP). It is photosynthesis that removes carbon from
the atmosphere and adds it to the plant. However, much of the GPP is
promptly lost (and carbon returned to the atmosphere) due to
respiration. In trees, net primary production is typically about half of
GPP. In FullCAM, net primary production is measured in tonnes per
hectare.

Thus, in normal growth, a plant is simultaneously adding to its mass by
the process of production (which adds net primary production to the
plant) and losing mass by the process of turnover (which loses material
from the plant).

**Yield**

Due to the turnover of plant components, when we measure the change in
component mass over a period of time we actually measure the *yield*,
which is the net primary production less the turnover. Yield is
relatively easy to measure and is of interest to anyone who measures
plant masses.

The yield of a plant is the net primary production produced less the
material shed by turnover: in any given period,

*Yield = Net Primary Production -- Turnover*.

**Use Net Primary Production or Yield?**

Net primary production is due to production, material-turned-over is due
to turnover, and yield is due to the combined effects of production and
turnover.

There are two fundamentally different ways of specifying or measuring
plant growth:

1.  By yield changes --- changes in yield with time.
2.  By net primary production flows --- amounts of net primary
    production added to the plant component.

In practice, the material-turned-over is hard to measure precisely
(because material moving to debris via turnover is quickly dispersed
into the environment), while yields are relatively easy to measure
precisely (just measures the plant mass).

The yield is what you get if you simply measure the mass of the
specified plant component(s), and a "mass increment" (or "yield
increment") is the difference in measurements of mass over the period of
the increment.

For example, if you measure the leaves of the trees of a forest as 20
tdm/ha on June 1 then the yield of the tree leaves on June 1 is 20
tdm/ha. If you then measure the leaves of the trees as 26 tdm/ha on
August 1, the mass increment of the tree leaves is 6 tdm/ha over those
two months. If your increment time-series contained monthly leaf mass
increments, then it might have 3 tdm/ha in June and another 3 tdm/ha in
July.

A net primary production flow to a tree or crop component in a given
period is the mass of net primary production that is added to the
component in the period.

For example, continuing the previous example, suppose that the trees
shed 1 tdm/ha of leaves during June and a further 2 tdm/ha of leaves in
July. Then the net primary production flowing to the leaves in June must
have been 4 tdm/ha (the leaf mass increment was 3 tdm/ha in June, which
included shedding 1 tdm/ha of leaves) and in July must have been 5
tdm/ha (3 tdm/ha net gain, including a 2 tdm/ha loss). If your increment
time-series contained monthly leaf net primary production flows, then it
would have 4 tdm/ha in June and another 5 tdm/ha in July.