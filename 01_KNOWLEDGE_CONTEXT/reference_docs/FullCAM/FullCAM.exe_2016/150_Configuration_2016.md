+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Configuration**

\[*Configuration* page of the input window of a plot\]

This page is where you specify the configuration of your plot, that is,
choose which parts of the plot should be modelled. This topic describes
configuration issues in general terms; for more specifics see:

[Configure the Plot](6_Configure%20the%20Plot.htm)\
[Configure Tree Production](108_Configure%20Tree%20Production.htm)\
[Configure Risk Analysis](8_configure%20risk%20analysis.htm)\
[Configure Other Options](138_Configure%20Other%20Options.htm)

**About**

This window allows users to view a list of all inputs (click on the
\'Models and Inputs\'\... button) or a diagram showing all pools and
fluxes of C and N (click on the \'Diagrams\...\' button) for the model
configuration selected. Note that there is no capacity to model nitrogen
in this edition of FullCAM but the diagrams show the full theoretical
form of the model including nitrogen.

**Models and Inputs**

Clicking the \'Models and Inputs\' button brings up a new window which
lists a variety of information for the model configuration selected. The
level of detail of information presented in this window can be specified
using the \'Options\' button located at the far left of the menu bar for
this window. Additional menu bar buttons allow the user to copy and
select various components of the window, turn on word wrap if required,
export the information in the window to a text file, find text and view
help file.

Clicking the Options button and scrolling down to the \'Display\' menu
option allows the user to specify the inputs that will be displayed in
the window. Options include:

- All inputs: lists all inputs whether required or not for the current
  configuration settings.
- Inputs required by the current configuration: only displays inputs
  required by the current configuration.
- Inputs required by the current configuration and other settings:
  displays inputs required by the current configuration plus additional
  information pertaining to other events such as fire, plough,
  herbicide, grazing, irrigation, manure application, etc.

The other three menu items on the Options button allow the user to
specify the nature of the information presented:

*Show values*: presents the values entered into the various tabs and
windows to the right of the descriptor of each input (e.g. Carbon % of
fine roots = 38.4 %). If the value belongs to a species, it shows the
value of the species that is currently selected for editing in the
appropriate tab. If the value belongs to an event, the value shown comes
from the chosen event of that type. No value is shown if there is no
species or event or the value of the input is blank.

*Show programming names*: presents the name assigned by FullCAM
programming code for the variables in square brackets \[\] (e.g. Carbon
% of fine roots \[CFracFirtA\] = 38.4%). Programming names are useful if
you are reading and referring to the FullCAM Function Specification.

*Show configuration*: presents the user specified configuration for the
plot as the first item in the information displayed. If any
discrepancies exist between this list and the regular interface, the
regular interface is correct.

You can get help related to a specific input by placing the cursor in
the line in which the input is presented and clicking the \'Help for
Input on Selected Line\' button in the menu bar (Ctrl + i). General help
pertaining to this window can be obtained by clicking on the \'Help\'
button in the menu bar (F1)

**Configuration Determines Inputs**

The configuration you choose will affect which inputs are required. For
example, if you model a forest system only, then none of the
agricultural inputs will be required.

You might want to experiment with different configurations in order to
determine the most configuration that most suits your needs, given the
available inputs and your required outputs. To help in this process, for
each configuration you can see model diagrams ([Diagrams
Window](50_Diagrams%20Window.htm)) and a list of required inputs
([Models and Inputs Window](141_Models%20and%20Inputs%20Window.htm)).

**FullCAM Integrates Its Constituent Models**

The [Constituent Models In
FullCAM](198_Constituent%20Models%20In%20FullCAM.htm) models may be used
either independently or in combination. [CAMFor](77_CAMFor.htm) and
[CAMAg](78_CAMAg.htm) are multi-layer framework models, while
[RothC](114_RothC.htm) is a single-layer specialist model. FullCAM
allows you to run combinations of these models to simulate single or
multi-layer models (see [Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm)), as forest,
agricultural or mixed.

**Readiness**

When the *Configuration* page is unready (that is, incomplete --- as
when you create a new document):

- The writing on the tab of the page is red.
- Only the [About](11_About.htm), Configuration, and
  [Timing](199_Timing.htm) tabbed pages appear in the input window of
  the document.

When the *Configuration* page is ready (that is, complete):

- The writing on the tab of the page is black.
- If the *Timing* page is also ready then more than three tabbed pages
  appear in the input window. Exactly which pages appear depends on the
  configuration --- for example, the [Mulch](202_Mulch.htm) page only
  appears if mulch is modelled.

While all the input pages use the red or black tab to indicate
unreadiness (see [General Features](20_General%20Features.htm)), only
the *Configuration* page also controls which other tabbed pages appear
in the document input window.

**Simpler Is Usually Better**

The more layers and the more sophisticated features you choose in your
model, the more difficult it will be to find all the required input
data. We recommend:

- Only modelling those layers and simulating those elements that you
  need;
- Restrict model configurations to those for which data is available and
  for which the outputs are understandable.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
