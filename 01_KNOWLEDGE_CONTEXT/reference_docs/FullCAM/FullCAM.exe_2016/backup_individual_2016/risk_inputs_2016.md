---
title: Risk Inputs
version: 2016
category: Risk Analysis
original_file: 159_Risk Inputs_2016.md
---

[*Risk Inputs* page of the input window of a plot or spatial document]

Manage all the risk inputs for a plot document --- see Risk
Analysis. It is only accessible if the plot is
configured for sensitivity analysis --- Configure Risk
Analysis.

**Use**

The list shows all the current risk inputs, using colour to show their
status:

  Colour         Status
  -------------- -----------------------------------------------------------
  Solid yellow   required by document and on
  Pale yellow    required by document and off
  Orange         not required by document (not used in this configuration)
  Red            not ready (refers to a non-existent species or event )

Only the risk inputs that are required by the document and on are used
in an analysis involving risk inputs; the rest are treated as ordinary
inputs (that is, always have the same value).

The risk input for a time-series is a single number that is the
multiplier for the data in the time-series (see Time-series
Window).

This page is always ready, because the risk inputs do not affect whether
or not the document can simulate. However, if there are any risk inputs
that are not ready then the sensitivity analyses cannot be run.