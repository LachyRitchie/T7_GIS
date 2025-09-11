---
title: Forest Percentage Change
version: 2020
category: events
original_file: 116_Forest Percentage Change_2020.md
---

Enter the inputs specific to a forest-percentage change event.

**Details**

Enter the Forest Percentage that will apply to the plot, until the next forest percentage change event. See Initial Conditions For the Whole Plot.

Forest percentage change events with no valid choice are shown as a simulating event in the event list (so you can change their type), but are shown as not ready and have no effect on the simulation.

**Equal to a Constant**

This is the recommended way to adjust the forest percentage when using the default parameters available from downloaded data. The forest percentage will be changed to the specified value and will not change until a subsequent forest change event occurs.

Note that the Forest Percentage Change does not automatically respond to events that plant or remove trees. A forest percentage change event should always be created alongside another event that purports to change land management practices and/or influence the presence of a forest, consistent with the events created from new regimes.

**Determined by the Tree Yield Formula**

Under this option the forest percentage rises from 0% at planting to 100% at the age of maximum growth. This relies on the evidence that the age of maximum growth is at or near the age of canopy closure. The growth determined by the tree yield formula is not affected by the forest percentage, but the tree growth affects how much room is left for pasture between the trees.

**Note**: Under this option, in simulation steps where the tree yield formula is not in use, the forest percentage is equal to the constant forest percentage entered in the initial conditions.

**Determined by the Tree Age**

It may be used with or without the tree yield formula.

**Note**: Under this option, in simulation steps where the tree yield formula happens to not be in use, the forest percentage is equal to the constant forest percentage entered in the initial conditions. This is similar to the linking of canopy closure and age of maximum growth in the previous option but lets the user set the age of canopy closure manually.
