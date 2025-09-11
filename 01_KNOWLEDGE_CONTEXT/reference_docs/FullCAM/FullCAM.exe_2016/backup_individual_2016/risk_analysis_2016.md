---
title: Risk Analysis
version: 2016
category: Risk Analysis
original_file: 218_Risk analysis_2016.md
---

This topic explains some general aspects of risk analysis in FullCAM.

Performing risk analysis in FullCAM requires use of the \@Risk software
product (refer to the \@Risk help page for further
information).

**Introduction**

*Risk analysis* is where you replace the single value of an input by a
probability distribution. That is, in risk analysis we consider the
value of some inputs to be probability distributions instead of single
numbers. See risk input, below.

Risk analysis is useful for exploring the effects of uncertainty in our
inputs. For example, in a regular plot simulation the value of the clay
fraction of the soil might be 13%. But what effect does it have on the
simulation if all we know about the clay fraction is that it is between
10% and 20% and most likely around 13%?

The type of risk analysis performed in FullCAM is 'sensitivity analysis'
and is performed only on plot documents.

Sensitivity Analysis estimates how
sensitive an output is to each input. Used to explore the range of
probable outputs, given uncertainty in the inputs.

Risk analysis needs to be turned on in the configuration --- see
Configure Risk Analysis. All the
risk inputs can be viewed at once on the Risk
Inputs page.

**Risk Inputs**

A *risk input* is a FullCAM input with risk properties attached to it.
Those properties are:

- A probability distribution
- Correlations with other risk inputs
- An on/off switch.

See the Risk Properties of an
Input window.

Almost any FullCAM input that is a single number can be a risk input
(others, such as the start time for the simulation, are too intrinsic to
the simulation to be allowed to vary during a risk analysis). Each
time-series has a multiplier that can be a risk input. Typically you
will want to focus on only a small number of risk inputs at once,
because the risk analysis slows down with each risk input added.

To create a risk input for a given plot input:

1.  Ensure that the plot is configured for risk analysis --- Configure
    Risk Analysis.
2.  Select the field where you would normally enter the input (so that
    if you pressed a key it would write into the field).
3.  Press the F6 key which will cause the Risk Properties of an
    Input window to open.
4.  Fill out the properties and close the window.

The input now appears in the plot window as per normal, but with a
yellow background to signal that it is also a risk input (the yellow is
faded when it has been switched off; the yellow is overridden by red if
the regular value of the input is invalid). The input continues to use
its normal single value in plot simulations, regardless of its risk
properties.

The current risk inputs in a document are listed in the Risk
Inputs page.