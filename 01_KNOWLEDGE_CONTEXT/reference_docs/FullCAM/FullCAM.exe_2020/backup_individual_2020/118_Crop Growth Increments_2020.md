---
title: Crop Growth Increments
version: 2020
category: crops
original_file: 118_Crop Growth Increments_2020.md
---

This Time Series Window is one of the following two crop and pasture time series windows, where you specify the:

**1. Growth** of the crop or pasture as either:

- Mass increments of the specified crop or pasture components [tdm/ha]
- NPP flows to various crop or pasture components [tdm/ha].

**2. Die off**, for perennial pastures only, as either:

- Mass decrements of leaf components [tdm/ha]
- NPP flows from leaf components [tdm/ha].

**Details**

Crops and pastures may be grown via three different methods:

*Sigmoidal* (for annual species) - growth will begin from the planting event and proceed to the harvest event, tracking along a sigmoidal curve. At the time of harvest, the plant will have reached optimal growth, which is the amount specified within the increment growth window. This value should normally be an annual value.

*Perennial growth* (for perennial/multi-year species) - growth will begin at time of planting from an initial standing dry matter amount, and proceed using monthly increments and decrements. Perennial growth can be used to accurately model seasonal variations and climatic impacts on pasture yields.

*Linear* - growth will begin from the planting event and proceed to the harvest event, tracking linearly from planting to harvest. At the time of harvest, the plant will have reached optimal growth, which is the amount specified within the increment growth window. This value should normally be an annual value. Linear growth is not recommended for modelling plant growth as it produces unrealistic amounts of biomass at any point along the growth time series.

Additional detail and reference material on sigmoidal and perennial growth methods can be found within Australia's National Inventory Report.

**Additional Comments**

Crop and pasture growth within FullCAM does not take into account climatic variability. It will simply model growth along a set curve to reach the optimal yield as entered. The yields that are entered into FullCAM should include climatic impacts into their modelling or measurement prior to insertion into FullCAM.
