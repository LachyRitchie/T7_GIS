---
title: Estate Simulation
version: 2016
category: Simulation
original_file: 72_Estate Simulation_2016.md
---

Some general aspects of simulating an estate in FullCAM.

**Estates**

An estate is an arbitrary collection of plots, where each plot is
assigned an area.

A FullCAM plot is a model of what is happening at a particular point (a
position with no area), and is limited to one tree species and one crop
species and the interplay between them. An estate provides the mechanism
for combining FullCAM plots into an area.

For example, to model a few hectares of plantation containing five
species of trees, you would create:

1.  Five FullCAM plots, one for each of the tree species.
2.  One FullCAM estate that defines the appropriate area for each plot,
    multiples plot results by plot areas and adds the resultant values
    together to give a single estate value for each output variable
    selected.

**Estate Documents**

An estate document specifies a list of plots, where each plot also has:

1.  An area (in hectares);
2.  A starting date for simulation of the plot.

The estate represents the sum of the individual areas assigned to each
plot. Each plot and its associated area is entered into the estate
simulation on the basis of the starting time specified. See Plots in
the Estate.

**What Happens in an Estate Simulation**

An estate simulation performs a plot simulation for each plot in the
estate. The results (typically in t/ha) are multiplied by the plot area
(so the results are, typically, in tonnes). The results for all plots
are added together, to give the results for the entire estate.

1.  FullCAM creates a plot document in memory, called the *working
    plot*. The working plot is blank, but copies the timing and output
    information from the estate document.
2.  FullCAM zeroes the outputs in the estate document.
3.  For each plot in the estate FullCAM:
    - Reads the plot file into the working plot, except for the timing
      and output information.
    - Performs a plot simulation on the working plot.
    - Multiplies the working plot outputs by the area of the plot (for
      appropriate outputs) and add them to the outputs in the estate
      document.
4.  Scales the outputs in the estate document to allow for additive
    (such as carbon mass) or average (such as rainfall) outputs.
5.  Destroys the working plot.