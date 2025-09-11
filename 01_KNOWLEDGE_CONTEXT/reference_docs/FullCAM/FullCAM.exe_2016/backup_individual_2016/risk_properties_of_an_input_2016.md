---
title: Risk Properties of an Input
version: 2016
category: Risk Analysis
original_file: 182_Risk Properties of an Input_2016.md
---

[Press F6 on any input in a plot document where either type of risk
analyses is turned on (see Configure Risk
Analysis)]

This window is where you create, edit, and delete a risk input. See
Risk Analysis.

**Making a Risk Input**

To make the input into a risk input, press the *Create Risk Properties*
button, enter the probability distribution, and edit any correlations
with other risk inputs.

Un-checking the *Risk properties are 'on'* checkbox turns the risk
properties off and effectively turns the input back into an ordinary
input, but retains the risk properties in case you want to turn them
back on.

The usual range for an input constrains the probability distribution of
the corresponding risk input. For example, the carbon percentage of bark
is a number from 0.0 to 100.0 (being a percentage), so the minimum and
maximum of the distribution cannot be outside 0.0 to 100.0.

You cannot choose the *OK* button unless the information in the window
is all valid. If a distribution parameter is invalid then it has a red
background --- so enter a new value for that parameter.

**Probability Distributions**

Only bounded distributions are allowed, to help ensure that the values
of the risk input always fall within their allowed range in FullCAM.

In all the distributions here, there is no possibility of a sampled
value less than the minimum or more than the maximum. When sampling the
distribution, the distribution is re-sampled as required until we get a
value that is in the min-max range.

The ranges of some inputs depend on other inputs. If those other inputs
are also risk inputs, then the situation can arise during a risk
analysis where the risk input is within its distribution range but is
out of the range allowed by FullCAM. If this happens, that simulation
within the risk analysis is discarded and another performed in its
place.

**Uniform Distribution**

Equal probability for every value from the minimum to the maximum.

**Triangular Distribution**

The probability density rises in a straight line from zero at the
minimum value to a peak at the most likely value, then declines in a
straight line to zero at the maximum value.

This is the simplest way to specify a distribution that is lumped around
the most likely value. Unless you know that the shape of that lumpiness
is definitely not triangular, this is generally the most suitable
distribution.

**Truncated Normal Distribution**

The normal (Gaussian) distribution has the classic, common, bell-shaped
probability distribution.

The mean must be between the minimum and the maximum.

Use this distribution where there are multiple independent sources of
error in factors that add to form the estimated value of the input.

**Truncated LogNormal Distribution**

The distribution of X when log(X) has a normal distribution (log =
logarithm, to any base).

The minimum must be greater than zero, and the mean must be between the
minimum and the maximum.

Use this distribution where there are multiple independent sources of
error in factors that are multiplied to form the estimated value of the
input.

**Correlations with Other Risk Inputs**

Risk inputs can be chosen to be correlated with one another --- choose
another risk input and edit its correlation (see Correlation Between
Two Risk Inputs).