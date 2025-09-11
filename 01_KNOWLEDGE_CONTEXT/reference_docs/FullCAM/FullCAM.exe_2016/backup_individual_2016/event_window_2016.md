---
title: Event Window
version: 2016
category: Event
original_file: 137_Event Window_2016.md
---

[Events page : *New* or *Edit* button]
[Standard Events of a
Species window : *New* or
*Edit* button]

This window is for viewing and editing an individual event. See

Event Timing
Autoqueue

For help on the event-specific panel at the bottom of the window, see:

Plant Trees
Plant Crop
Thin
Harvest
Forest Fire
Agricultural Fire
Plough
Herbicide
Grazing Change
Forest Treatment
Chopper Roller
Termite Change
Irrigation Change
Manure-From-Offsite Change
Forest Percentage Change

**Name**

Every event needs a (non-blank) name, and the name must be unique within
the event list (either the events for the plot, or the events for a
species). Press the *Auto Name* button and FullCAM will insert a unique
name based on the properties of the event.

**Type**

Select the type of event:

- If you are modelling a forest, the forest events are available
  (written in green).
- If you are modelling an agricultural system, the agricultural events
  are available (yellow).
- If you are modelling a mixed plot, both forest and agricultural events
  are available (brown).

Only events that are possible with the current configuration and current
species inputs can be created or edited (if they are not possible then
they are also not shown in the *Events* page in the input window). Note
that:

- Forest treatments are possible if and only if CAMFor
  is on and one or more tree species are using the tree yield formula.
- Forest irrigation change events are only possible if forest
  RothC is on, or CAMFor is on and one of more tree
  species has debris whose breakdown is sensitive to temperature and
  rainfall.
- Agricultural irrigation change events are only possible if
  agricultural RothC is on, or CAMAg is on and one of more crop species
  has debris whose breakdown is sensitive to temperature and rainfall.
- The following events are only possible if they are used in preference
  to their corresponding time-series (see Configure Event Or
  time-series) :
  - Forest/Agricultural irrigation change
  - Forest/Agricultural manure-from-offsite change.

**Notes**

Enter anything you like in this field. It will have no effect on
simulation but it may be useful for sorting events in the Standard
Events of a Species
window.

**Add Days**

A offset may be applied to an event by entering a value in the *Days*
field and clicking *Add Days* button. This can be either positive or
negative and will move the event that number of days forward or back in
the event queue.