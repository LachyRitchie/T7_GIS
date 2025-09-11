+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Post-Thin Period**

\[[Event Window](137_Event%20Window.htm) : [Thin](140_Thin.htm) panel :
*Post-Thin Period* section\]

Specify the relative allocations of new growth to the tree components in
the period immediately after a thin.

**Details**

Tree growth is often different for a period after a thin, due to the
response of the trees to the thin. Leaves and branches especially tend
to grow with extra vigour after a thin.

FullCAM models the post-growth differences using relative allocation
multipliers. Each multiplier multiplies the relative allocation that
would otherwise occur, for the whole length of the post thin period
(except that the boost period ends immediately if there is another
thin). That is, the relative multiplication multipliers here allow you
to modify the relative allocations for the period after a thin. No extra
growth occurs, just the allocation of any growth to the various
components can be changed.

For example, a leaf multiplier of 1.2 (while the multipliers for all the
other components are 1.0), and a post thin period of 0.5 years, would
mean that the relative allocation of growth to leaves would be 20% more
than otherwise for whole of the half year following the thin (assuming
there is no other thin in those six months).

Note that relative allocations are relative to each other, so
multiplying all the relative allocations by the same amount has no
effect.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
