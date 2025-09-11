+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Forest Percentage Change**

\[[Event Window](137_Event%20Window.htm) : *Forest Percentage Change*
panel\]

Enter the inputs specific to a forest-percentage change event.

**Details**

Enter the [Forest Percentage](206_Forest%20Percentage.htm) that will
apply to the plot, until the next forest percentage change event. See
[Initial Conditions For the Whole
Plot](197_Initial%20Conditions%20For%20the%20Whole%20Plot.htm).

Forest percentage change events with no valid choice are shown as a
simulating event in the event list (so you can change their type), but
are shown as not ready and have no effect on the simulation.

**Equal to a Constant**

Set the forest percentage manually here. It will not change until the
next forest change event. This is a reasonable approach to use for
activities such as the thinning of trees in a grazed woodland. Note that
the Forest Percentage Change does not automatically respond to a
[Thin](140_Thin.htm) event that removes a prescribed portion of trees.
If the thin event is being used to alter the tree canopy cover to
promote pasture growth, then the thin and forest percentage change
events should be manually aligned.

**Determined by the Tree Yield Formula**

Under this option the forest percentage rises from 0% at planting to
100% at the age of maximum growth. This relies on the evidence that the
age of maximum growth is at or near the age of canopy closure. The
growth determined by the tree yield formula is not affected by the
forest percentage, but the tree growth affects how much room is left for
pasture between the trees.

**Note**: Under this option, in simulation steps where the tree yield
formula is not in use, the forest percentage is equal to the constant
forest percentage entered in the initial conditions.

**Determined by the Tree Age**

This field may be used with or without the tree yield formula.

**Note**: Under this option, in simulation steps where the tree yield
formula happens to not be in use, the forest percentage is equal to the
constant forest percentage entered in the initial conditions. This is
similar to the linking of canopy closure and age of maximum growth in
the previous option but lets you set the age of canopy closure manually.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
