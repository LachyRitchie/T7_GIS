+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

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

Plot information is stored in a *plot file*, whose extension ".plo".

A *plot* simulation tracks the carbon associated with a plot -- either
on the plot or in the products produced by the plot.

Typical use:

1.  Create a new plot:
    - Choose *New Plot* from the *File : New* menu. A blank plot
      document is created, and its input window appears with tabbed
      pages for [About](11_About.htm),
      [Configuration](150_Configuration.htm) and
      [Timing](199_Timing.htm). The titles on the *Configuration* and
      *Timing* pages are the colour red, indicating that you **must**
      complete these pages before you can simulate the plot.
    - As soon as you have entered the minimum required data for the
      *Configuration* and *Timing* pages, more tabbed pages appear on
      the plot input window. Exactly **which** pages appear depends on
      your particular configuration.
    - A list of inputs can be viewed using the 'Models and Inputs'
      function located in the 'About your Configuration' portion of the
      Configuration page. It is also possible to view flow diagrams of
      the configured model. This can be done using the 'Diagrams'
      function.
2.  When all the data is ready (with no red tabs visible) choose
    'Simulate' from the FullCAM main menu and 'Run Plot Simulation' from
    the drop--down menu or click on the 'Run Plot Simulation' button,
    located in the lower half of the FullCAM main menu bar.
3.  When you run your first simulation, a default output window will be
    displayed. Specify the outputs you want to look at, and create
    additional output windows if needed, then rerun the simulation.
4.  You can now alter any inputs and immediately rerun the simulation,
    as often as required.

Save your work at any time by choosing *Save* from the *File* menu, or
click the save button on the toolbar underneath the menu (the red dot
means the document has been changed). The resulting .plo file contains
the plot document, which includes the input window and all the
associated output windows.

Plot simulation is the basic unit of simulation in FullCAM -- simulating
estates just consists of simulating many plots.

**Estate Simulations**

A number of plots may be aggregated into an *estate* document (stored as
an ".est" file). An estate is a collection of plots, each of which has a
specified area and starting date for land use. As estate files are area
based, their masses are quoted in tonnes. Estate files may represent a
diverse area of forest with stands (trees) of different ages, types and
management systems, or similarly a diverse area of agricultural land.

When you create an estate document (choose *New Estate* from the *File :
New* menu), you create any number of plots with area, each of which has
its own:

1.  Plot file, which contains the document describing the plot, and
    which may be shared by multiple estate--plots.
2.  Area.
3.  Start date (when the estate--plot started being used as described in
    its plot file). You do **not** specify the actual geographic
    location of a plot.

Estate files are useful for simulating larger or heterogeneous areas of
land. You can also test varying timing and management options. See
[Estate Simulation](72_Estate%20Simulation.htm).

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

### Sensitivity Analysis

Monte Carlo analyses are a useful way to assess the relative effects of
model parameters. More specifically, they allow users to determine both
model sensitivity and the probability based distribution of potential
outputs, inherent uncertainties in each of the data inputs. FullCAM
links to the \@Risk RDK software by Palisade
([palisade.com](http://www.palisade.com){target="_blank"}) to provide
this capability. This capability is accessed by 'Sensitivity' check box
in the Risk Analysis section of the Configuration page. However,
completing a sensitivity analysis requires the presence of a licenced
version of the \@Risk RDK software on the computer used to run FullCAM.

### Material Flows

The main carbon flow is

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

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
