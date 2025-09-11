---
title: "Termite Change"
version: 2020
category: Events
original_file: 53_Termite Change_2020.md
---

\ : *Termite Change* panel\]

Contains the inputs specific to a termite change event.

**Details**

Enter the inputs that describe the level of termite activity from the
event date until a subsequent termite change event.

There is no termite activity at the beginning of a simulation. Termite
action begins with the first termite event. Turn off future termite
activity again by setting all the inputs of a termite event to zero.

In FullCAM, termites only eat deadwood and coarse dead roots in forests.
The eaten material goes immediately to the atmosphere.

A "percentage eaten by termites" is the percentage of the material in
the pool at the beginning of each simulation step that does not break
down during the step but that is eaten by termites. Material added to
the debris during a step cannot be eaten by termites --- so even with
100% termite percentages there may be a little coarse woody debris
present at the end of each step.

------------------------------------------------------------------------