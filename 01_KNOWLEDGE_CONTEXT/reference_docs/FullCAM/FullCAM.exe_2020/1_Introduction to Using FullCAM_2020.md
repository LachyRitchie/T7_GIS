+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

### Introduction to Using FullCAM

An introduction to the sorts of things you might do with FullCAM.

### Simulations

**Plot Simulations**

A *plot* is a piece of land with uniform characteristics, such as a
forest stand or a paddock. A plot can have either:

1.  No area -- the plot is a *point* model, and its output masses are in
    tonnes per hectare.
2.  A specified area -- the plot has an area, so its output masses are
    in tonnes.

Plot information is stored in a *plot file*, with extension ".plo".

A *plot* simulation tracks all the carbon (and optionally, nitrogen)
associated with a plot -- either on the plot or in the products produced
by the plot.

Typical use:

1.  Create a new plot:
    1.  Choose *New Plot* from the *Document* menu. A blank plot
        document is created, and its input window appears with tabbed
        pages for [About](11_About.htm),
        [Configuration](150_Configuration.htm) and
        [Timing](199_Timing.htm). The titles on the *Configuration* and
        *Timing* pages are coloured red, indicating that these tabs are
        incomplete and must be completed before the plot can be
        simulated.
    2.  As soon as you have entered the minimum required data for the
        *Configuration* and *Timing* pages, more tabbed pages appear on
        the plot input window. Exactly **which** pages appear depends on
        your particular configuration.
    3.  If your configuration includes any of the multi--layer options
        then the *Data Builder* page appears. You can use this to
        download data needed to run a simulation.
    4.  A list of inputs can be viewed using the 'Models and Inputs'
        function located in the 'About your Configuration' portion of
        the Configuration page. It is also possible to view flow
        diagrams of the configured model. This can be done using the
        'Diagrams' function.
2.  When all the data is ready (with no red tabs visible) choose
    'Simulate' from the FullCAM main menu and 'Run Plot Simulation' from
    the drop down menu or click on the 'Run Plot Simulation' button,
    located in the lower half of the FullCAM main menu bar.
3.  When you run your first simulation, a default output window will be
    displayed. Specify the outputs you want to look at, and create
    additional output windows if needed, then rerun the simulation.
4.  You can now alter any inputs and immediately rerun the simulation.

Save your work at any time by choosing *Save* from the *File* menu, or
click the floppy disk button on the toolbar underneath the menu (the red
dot means the document has been changed). The resulting `.plo` file
contains the plot document, which includes the input window and all the
associated output windows.

Plot simulation is the basic unit of simulation in FullCAM -- simulating
estates consists of simulating many plots.

**Estate Simulations**

A number of plots may be aggregated into an *estate* document (stored as
an ".est" file). An estate is a collection of plots, each of which has a
specified area and starting date for land use. As estate files are area
based, their masses are quoted in tonnes. Estate files may represent a
diverse area of forest with stands (trees) of different ages, types and
management systems, or similarly a diverse area of agricultural land.

When you create an estate document (choose *New Estate* from the
*Document* menu), you create any number of plots with area, each of
which has its own:

1.  Plot file, which contains the document describing the plot, and
    which may be shared by multiple estate--plots.
2.  Area.
3.  Start date (when the estate-plot started being used as described in
    its plot file). You do **not** specify the actual geographic
    location of a plot.

Estate files are useful for simulating larger or heterogeneous areas of
land. You can also test varying timing and management options. See
[Estate Simulation](72_Estate%20Simulation.htm).

### Databases

FullCAM stores tabular data in database documents. This data can be
downloaded into plot documents by [Data
Builder](132_Data%20Builder.htm).

### List of Inputs

In configuring data for analysis by any model within FullCAM, users are
presented with a specific list of input data needed to support each
configuration. The list of required input data can be viewed using the
'Models and Inputs' button in the 'About your Configuration' section of
the Configuration page (tab). Various options can be selected to display
the model configuration, the variable names used by FullCAM and the
values assigned to the variables. This information can also be saved in
a spreadsheet or text format. This capacity allows users to find a
balance between the data they have available, the sophistication of the
model configuration and the type and accuracy (certainty) of the outputs
required.

### Material Flows

The main carbon flow is:

Atmosphere → plants → debris → mulch → soil.

At this level the flow is unidirectional. There are only two carbon
feedback loops:

1.  Within the mulch, due to microbes eating and dying.
2.  Within the soil, due to microbes eating and dying.

Each of these loops is strictly confined to its layer (mulch and soil
respectively).

The other large carbon flows are:

- Carbon moves from the debris, mulch, soil, and products to the
  atmosphere due to decomposition.
- Carbon moves directly from the root debris to the soil, bypassing the
  mulch.
- In a thinning or harvest event, carbon moves from the plants and
  debris to the products.
- In a fire, carbon moves from the plants, debris and mulch to the
  atmosphere and soil.

To get your simulation working realistically, you may need to alter the
FullCAM inputs that determine the flows. Work back from where the
simulation appears to be giving unrealistic results to where the carbon
is coming from, and so on back until realism is achieved.

Nitrogen is more complex, due to its mobility. Simulating nitrogen
introduces the mineral nitrogen pool, which is assumed to be in contact
with all the other pools. Nitrogen flows through the same pools as
carbon, however several additional processes exist to consume or
generate nitrogen. The required or excess nitrogen associated with any
of the organic pools flow into, or out of the mineral pool. If there is
insufficient nitrogen in the mineral pool for all the processes to
consume the amount they wish, then *nitrogen rationing* occurs -- which
means that less of the processes occur (for example, slowing plant
growth).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
