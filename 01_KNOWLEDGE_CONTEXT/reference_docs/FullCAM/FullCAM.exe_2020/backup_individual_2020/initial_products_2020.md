---
title: "Initial Products"
version: 2020
category: General
original_file: 33_Initial Products_2020.md
---

\ page or  page : *Initial
Products* button\]

\ page : *Forest* or
*Agricultural* panel : *Products* button\]

Describe the plot products existing at the start of the simulation.

**Introduction**

All of the initial forest products belong to the initial tree species,
which is specified in the 
window.

All of the initial agricultural products belong to the initial crop
species, which is specified in the  window.

If different species are planted later in the simulation, the products
of each species are treated separately because each species may have
different product decomposition rates (see ).

Forest products can start the simulation either in use as products or in
the landfill. Agricultural products can only start the simulation in use
as products (in FullCAM, agricultural products cannot go to landfill).

**Carbon Masses**

Enter the mass of carbon in the various product pools, in tonnes per
hectare as a time series.

The names of the products are only indicative: the various product
categories are effectively defined by their decomposition fractions
(entered as species inputs). All CAMFor cares about is that a hectare of
plot produces X tonnes of a product that decomposes at a given rate.

Suppose the plot is a forest that produces fence palings for suburban
back yards. There is no category here called "fence palings". The only
thing that matters to carbon accounting is how fast those fence palings
decompose. Suppose you find that 1/20 of the carbon in the fence palings
returns to the atmosphere each year. Then the decomposition fraction of
the fence palings is 0.05 / year. Make sure that one of the wood product
decomposition fractions is 0.05 / year, and add the fence palings to
that category.

**Insert Standard Values**

\ page.\]

Press the *Insert Standard Values* button to insert the standard initial
product values (set via the *Initial Product* button on the *Standard
Information for the Species* panel of the *Trees* or *Crops* pages, see
) of the
initial species (specified via the *Trees* or *Crops* buttons of the
*Initial Conditions* page). The button is disabled if the standard
initial product information for that species is not ready (incomplete or
has invalid values).

------------------------------------------------------------------------