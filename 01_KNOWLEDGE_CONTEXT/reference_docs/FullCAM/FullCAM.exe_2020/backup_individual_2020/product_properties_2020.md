---
title: "Product Properties"
version: 2020
category: Configuration
original_file: 47_Product Properties_2020.md
---

\ page or  page :
*Properties of the Species* panel : *Products* button\]

Specify the properties of the products produced by the current species
().

*Products* are any plant material that is moved offsite from the plot.
Products from separate species is treated entirely separately by
FullCAM.

**Decomposition Percentages**

The decomposition percentage of a product pool (either "in use" or "in
landfill") is the average percentage of carbon mass lost to
decomposition (and thus as CO~2~ to the atmosphere) each year. The
higher the decomposition percentage, the faster the product returns its
carbon to the atmosphere.

A decomposition percentage of 0 means that none of the pool decomposes
(so no carbon returns to the atmosphere from the product). A
decomposition percentage of 100% means that in each simulation step all
of the pool decomposes, thereby returning all of its carbon to the
atmosphere.

The decomposition percentage of a debris pool is the percentage lost per
year due to decomposition (that is, 100% less the percentage of the
original material that is still there a year later, if decomposition is
the only process removing material from the pool). It assumes
exponential decay at constant decay rate. Click the exponential decay
button for alternative expressions, a graph, and a fuller explanation.

**Bio-energy, Move-to-Landfill**

Forest products may be burnt for bio-energy or moved to landfill after
being used.

Once in a landfill, material just decomposes --- thereby returning its
carbon to the atmosphere eventually. For a given species and product
type, the decomposition percentage for a product in use will generally
be higher than the decomposition percentage for the product in landfill.
Agricultural products may be burnt for bio-energy after being used, but
may not be moved to a landfill.

Material burnt for bio-energy is burnt immediately (it is NOT added to
the biofuel), thereby returning its carbon to the atmosphere. The
"biofuel" product category is there for a different purpose: the biofuel
product pool consists of biofuel stocks awaiting burning for bio-energy.
Setting the *Percentage Burnt for Bio-Energy Each Year* to 100% causes
all the biofuel in the pool at the beginning of a simulation step to be
burnt in that step. For completeness, you have the option of sending
forest biofuel to landfill instead of burning it for bio-energy.

**Product Categories**

The names of the wood products here do NOT define the products: the
behaviour of the various wood product categories are defined solely by
the product decomposition fractions. The only things of significance to
FullCAM are that a hectare of forest produces X tonnes of a wood product
that decomposes at a given rate, and so on.

Suppose a forest product is being used to produce fence palings for
suburban back yards. There is no category here called "fence palings".
The only thing relevant to carbon accounting is how fast those fence
palings decompose. Suppose you find that 1/20 of the carbon in the fence
palings returns to the atmosphere each year. Then the decomposition
percentage of the fence palings is 5%. Make sure that one of the wood
product decomposition fractions is about 5%, and add the fence palings
to that category. For instance, suppose you enter the decomposition rate
of packing wood as 5.2%. Add the fence palings to the category labelled
"packing wood".

The 0.2% difference in decomposition rate may be negligible but if not
allocate your decomposition rates as best as possible.

The wood product names used here are suggestive only (terms such as
"very long lived wood", "long lived wood", \..., "short lived wood" or
may be "wood life 7", \..., "wood life 1" could also have been used.

Crop product names can be taken more literally, but the same applies as
with the wood products --- the names do not matter per se, as only the
decomposition fractions define the behaviour of the plant products for
carbon accounting purposes.

The rationale behind the wood products life cycle pools used by the NCAS
can be found in the NCAS Technical Reports {target="_blank"}
and {target="_blank"}
().

------------------------------------------------------------------------