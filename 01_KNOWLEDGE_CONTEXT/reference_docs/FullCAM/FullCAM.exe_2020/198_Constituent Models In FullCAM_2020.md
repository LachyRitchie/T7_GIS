+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Constituent Models In FullCAM**

This topic is about the constituent models ("submodels") within FullCAM.

**Introduction**

FullCAM was initially formed by integrating these models into a single
cohesive model. FullCAM has since been expanded with capabilities that
go well beyond just the constituent models.

**FullCAM Consists of Constituent Models**

FullCAM is a flexible and highly integrated system of the following
models, each of which deals with particular aspects of the carbon
cycling and greenhouse emissions accounting. The models can be used in
various configurations, depending on your requirements.

1.  [CAMFor](77_CAMFor.htm) --- **C**arbon **A**ccounting **M**odel for
    **For**ests models carbon cycling in a forest, including the trees,
    debris, soil, minerals, and wood products. Forest growth can be
    included as yield curves, empirical growth formula, or process
    modelling.
2.  [CAMAg](78_CAMAg.htm) --- **C**arbon **A**ccounting **M**odel for
    **Ag**riculture models carbon cycling in an agricultural system,
    including the crops, debris, soil, minerals, and agricultural
    products. Includes both cropping and grazing.
3.  [RothC](114_RothC.htm) --- **Roth**amsted Institute active soil
    **C**arbon Model models carbon cycling in the active soil.

**Seamless Integration Into a Single Model**

FullCAM always uses the constituent models appropriately, combining them
as required into what appears as a single model of your specified plot.

CAMFor and CAMAg are framework models --- they model multiple layers of
a forest or an agricultural system respectively, and provide frameworks
into which the other models can be embedded. GENDEC, RothC and 3PG are
specialist models --- they only simulate a single layer of a forest or
agricultural system, but do so in more detail than CAMFor or CAMAg.

When you configure FullCAM, the constituent models are switched on and
off as required by the configuration. The FullCAM
[Configuration](150_Configuration.htm) page only allows you to enter
configurations that makes physical sense.

For each of the constituent models, there is a configuration that allows
the model to be run on its own --- which is useful for verifying that
FullCAM properly incorporates that model.

**Types of Plot That Can Be Modelled**

FullCAM allows you to run all sensible combinations of these models, to
model any of the following:

1.  A forest
2.  An agricultural system
3.  A mixed forest and agricultural system
4.  Trees only

FullCAM can model one forest and one agricultural system simultaneously.
Forests and agricultural systems both have debris and both have soil, so
both GENDEC and RothC have both forest and agricultural versions.
Forests have trees but agricultural systems do not. There are the
following model-instances:

1.  CAMFor
2.  CAMAg
3.  Forest RothC
4.  Agricultural RothC

Forest RothC and agricultural RothC are identical except that the soil
is always covered in forest RothC but may be either bare or covered in
agricultural RothC.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
