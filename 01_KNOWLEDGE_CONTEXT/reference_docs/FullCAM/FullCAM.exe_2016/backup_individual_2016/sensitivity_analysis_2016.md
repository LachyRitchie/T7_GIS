---
title: Sensitivity Analysis
version: 2016
category: Risk Analysis
original_file: 160_Sensitivity Analysis_2016.md
---

[*Sensitivity Analysis* page of the input window of a plot document]

This page is for performing a sensitivity analysis on the plot. It is
only accessible if the plot is configured for sensitivity analysis ---
Configure Risk Analysis.

The @Risk software that is used to perform the risk analysis (see
below) currently has some practical issues which are described at the
bottom of this page.

**Overview**

Choose the analysis outputs and the analysis properties, then press the
*Run Sensitivity Analysis* button to do the analysis. FullCAM and @Risk
then jointly perform the risk analysis, after which you can view the
results in @Risk (as prompted by FullCAM).

To complete the sensitivity analysis requires the RDK version of the
@Risk software from Palisade to be purchased and installed on the
computer being used to run FullCAM.

During a sensitivity analysis, the risk inputs replace their
corresponding (ordinary) inputs. In each simulation during the
sensitivity analysis, for each risk input FullCAM randomly generates one
number from the probability distribution of the risk input, and that
value is used as the input for that simulation.

**Analysis Inputs**

Analysis inputs are the risk inputs (showing on the Risk
Inputs page) that are both available (relevant
to this plot configuration) and on (not switched off in their Risk
Properties of an Input
window).

**Analysis Outputs**

The analysis outputs are the FullCAM outputs that you choose in the
Select Outputs window you get to by pressing
the *FullCAM Outputs* button.

Also choose whether the sensitivity analysis outputs should be:

1.  The values of the chosen outputs for all the simulation steps
2.  Just the values of the chosen outputs for the last step in the
    simulation.

If you choose the outputs for all the simulation steps, the sensitivity
analysis can take a long while to compute, your computer may run low of
memory and thus run very slowly, and you may be overwhelmed by the
number of outputs in the analysis results. Choosing just the
end-of-simulation values of the FullCAM outputs is often sufficient, and
will mean that the analysis runs much faster.

**Analysis Properties**

The sampling types are:

- Traditional Monte Carlo. Each risk input is sampled independently of
  the others.
- Latin hypercube. The risk inputs samples are all chosen together, in a
  manner designed to explore the space of possibilities faster. Latin
  hypercube tends to get better results for a given number of plot
  simulations (iterations).
- Distribution means. Each risk input sample is always equal to the mean
  of its probability distribution. Only use this for checking.

Typically we use Latin hypercube.

The maximum number of iterations is the maximum number of iterations
(plot simulations) that will be performed in a sensitivity analysis,
regardless of whether or not convergence-stopping is on. If
convergence-stopping is off, the analysis will perform the maximum
number of iterations. A typical value is 1,000.

Often a sensitivity analysis will converge before the maximum number of
iterations. Convergence is where doing more iterations (plot
simulations) does not significantly change the results. Typically you
should check for convergence to save unnecessary computation; typically
define convergence as less than 1.5% changes, and check every 100
iterations.

**Running the Sensitivity Analysis**

Select the 'Sensitivity Analysis' tab and perform the following steps:

1.  Select the desired output variables using the 'FullCAM Outputs'
    button in the Analysis Outputs window. The outputs are selected in
    the same manner as described previously for the normal Output window
    (item 22, section B). Define whether results are required for every
    simulation step or just for the last step only.
2.  In the 'Analysis Properties' window select the sampling type,
    define the maximum number of iterations to be used in the
    simulations and define the convergence conditions.
3.  Once all parameters for the simulation have been defined click on
    the 'Run Sensitivity Analysis' button. This button will be
    disabled if the plot file is not ready. You will then be prompted on
    how to view the results in @Risk.

Each iteration is a complete plot simulation, and a sensitivity analysis
will perform hundreds or thousands of them. Thus, the analysis can take
a while. If you have a lot of analysis outputs, or the analysis outputs
are every FullCAM output step, the analysis will take longer than
otherwise.

For a plot with a thousand steps (for example, 80 years of monthly
steps) and just a couple of outputs, a thousand iterations will
generally finish in less than a minute on most computers.

After the sensitivity analysis is finished according to the progress
window, @Risk can take a while to open the @Risk *Results* window. For
complex sensitivity analyses, the delay here can be minutes!

We recommend you start with a simple plot and a simple sensitivity
analysis to get a feel for the computation times on your computer.

Ignore the "simulations" in the @Risk window that tells you the
progress of the sensitivity analysis --- @Risk uses the word
"simulation" to mean something other than a plot simulation. Both
FullCAM and @Risk mean an "iteration" to be a FullCAM plot simulation.

**Practical Issues**

Observing a few simple rules should help you avoid some pitfalls that
have been identified in the way FullCAM and @Risk interact.

@Risk output is displayed in a separate process with its own window
that is labelled "@Risk - Results" on the Windows Task Bar. It will be
referred to here simply as the "@Risk" window. If no @Risk windows are
present then FullCAM automatically creates one when the first @Risk
function (such as a sensitivity analysis) is run.

When FullCAM is running, do not close all @Risk windows. If you do then
either restart FullCAM, or manually create an @Risk window by choosing
the appropriate command from the Palisade group in the Windows Start
menu.