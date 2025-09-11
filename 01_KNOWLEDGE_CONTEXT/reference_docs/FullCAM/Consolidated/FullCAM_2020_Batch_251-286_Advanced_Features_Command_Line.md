---
version: 2020
batch_range: 251-286
batch_name: Advanced_Features_Command_Line
creation_date: 2025-08-28
total_files: 14
---

# FullCAM 2020 - Batch 251-286: Advanced Features Command Line

## Table of Contents

- [266. Server Settings 2020](#266-server-settings-2020)
- [267. Simulation Timing 2020](#267-simulation-timing-2020)
- [268. Whats New 2020](#268-whats-new-2020)
- [269. Generate Estate 2020](#269-generate-estate-2020)
- [274. New Regime 2020](#274-new-regime-2020)
- [276. Editing Regimes 2020](#276-editing-regimes-2020)
- [278. Regime Update 2020](#278-regime-update-2020)
- [280. Edit Regime 2020](#280-edit-regime-2020)
- [281. Plot Digest 2020](#281-plot-digest-2020)
- [282. Templates 2020](#282-templates-2020)
- [283. FullCAM Command Line Utility 2020](#283-fullcam-command-line-utility-2020)
- [284. Initial StandingDead 2020](#284-initial-standingdead-2020)
- [285. StandingDead 2020](#285-standingdead-2020)
- [286. XML Copy 2020](#286-xml-copy-2020)

---

## 266. Server Settings 2020

**Server Settings**

\[*Internet* menu : Server *Settings*\]

This window is for maintaining your FullCAM server settings.

**Use Alternate Server**

This option allows you to specify the address of an alternate server
that FullCAM uses for data. Otherwise the [Departmental
Server](219_Departmental%20Server.htm) will be used.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 267. Simulation Timing 2020

**Simulation Steps**

\[[Timing](199_Timing.htm) page : *Simulation Steps* panel\]

Set the amount of time in a simulation step (all simulation steps
simulate the same amount of time).

A (simulation) *step* is the unit of time considered by a FullCAM
simulation. In each step, there is exactly one material movement from
one pool to the next pool due to processes (see [Processes and
Events](58_Processes%20and%20Events.htm)). Each step always simulates
the same amount of time. Steps are like the heartbeats of the model:
material moves from pool to adjoining pool once per step (exception:
more than once if the step is interrupted by an event).

The minimum time length per step is an hour.

The shorter the steps, the longer a plot simulation takes.

### Choosing the Number of Simulation Steps Per Year

*Time Resolution of Input Data*

If you specify the rainfall to FullCAM as just the total rainfall each
year (that is, one number per year), then it is unrealistic to expect
FullCAM to accurately simulate monthly or weekly phenomena that are
influenced by rainfall. Monthly simulation steps might be appropriate,
but the results might have to be interpreted carefully.

*Computing Time and Memory*

In a very lengthy simulation or one with many outputs, there may not be
enough computer memory to do a simulation with short steps, or it might
take a long time to generate results.

*Graininess*

In FullCAM, each atom of material belongs to one pool (such as trees
leaves), and carbon moves between the various pools once per step (at
the end of the step). While the rate of circulation of material among
the pools is mainly governed by the various physiological and empirical
rate inputs, it is subtly influenced by the length of step and
occasionally this is significant.

Consider carbon that flows from pool A to pool B to pool C (for example,
tree leaves to leaf litter to soluble mulch). It takes one step for any
carbon from pool A to reach pool B, and a second step for any of it to
reach pool C. If the steps are yearly then it takes two years for ANY
carbon from pool A to reach pool C, while with daily steps some carbon
can get to pool C by the end of the second day.

In reality, the step length is vanishingly small: carbon moves between
pools continuously, rather than in discrete movements that occur once
every beat of our simulation clock. Now, we want to model the essential
nature of the system with as little computing effort as possible. If we
decrease the step length then we get a more realistic simulation, but we
do more computing. This dependence of the simulation results on the step
length is called *graininess*.

The precision of the quantities in FullCAM is relatively low so
round-off error is almost insignificant --- but there is little point in
using more steps than necessary in case the round off error begins to
affect your results. FullCAM\'s flexibility in its treatment of time
allows you to overcome the artificial barriers set by arbitrary and
fixed frequencies of simulations steps.

What is a sensible amount of time per step? As you decrease the step
length, you will find your simulated results will gradually approach
limiting values. The limiting values are simulation results that stay
the same, no matter how much you further decrease the step length. From
the perspective of graininess, an appropriate step length is the step
length that gets you close to the limiting values.

As a rough rule of thumb, for negligible graininess use a step length of
a month.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 268. Whats New 2020

## 

What\'s New?

### 

New in the 2020 pre-release

A number of changes have been included in the 2020 pre-release following
consultation on the 2019 pre-release. These changes include:

**Improvements to the FullCAM user interface**

**Including climate data for 2018**

**Correcting to the timing of events in a number of regimes, which
automate events common to some types of simulations**

**Reverting to the treatment of forest fires to the treatment in the
current FullCAM (prior to 2019), pending further data acquisition**\
*This has delayed the use of the standing dead pool for the incidence of
fire*

**Modifying the method for projecting the [Forest Productivity
Index](188_Forest%20Productivity%20Index.htm), to avoid the potential
for climate data for a single year to cause excessive variability in
biomass estimates over time**

### 

New in the 2019 pre-release

**Forest [Standing Dead](285_StandingDead.htm)**

**[Plot Digest](281_Plot%20Digest.htm)**

**[FullCAM Command Line
Utility](283_FullCAM%20Command%20Line%20Utility.htm)**

**[XML Copy](286_XML%20Copy.htm) tool**

**[Decay Rate](86_Decay%20Rate%20Window.htm) adjustments**

**[Tree Yield Formula](130_Tree%20Yield%20Formula.htm) growth
calibration. See also [Growth Properties](42_Growth%20Properties.htm)**

**User interface improvements**

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 269. Generate Estate 2020

**Generate Estate**

\[Utilities Menu: *Generate Estate* \]

**Use**

The Generate Estate function enables creation of a new estate file from
a set of pre-existing plots.

**Estate Template**

New estates are created from a template estate. The *template estate*
must already exist and contain all data that is not to be altered by
this process.

**Text Import File**

This text file contains all the data that is required for the new estate
to be generated. Data formatting rules are:

- Data is tab-delimited
- The file has 4 mandatory inputs, being:
  - Start Year for simulation of the plot.
  - Start Step for simulation of the plot. The start step number can be
    any number from one to the number of steps per year. If the
    simulation steps are yearly (one step per year) then the only valid
    step number is \"1\".
  - Area (ha) of the plot.
  - Name of the plot including extension (.plo).
- Named plots must already exist in the folder specified.

**Plot Folder**

Folder containing the plot files to be used in forming the estate

**Processing rules**

- If an input is invalid then the process will cease and error details
  will be reported in a log file in the directory specified for the
  template estate.
- If successful then this process will create a new estate from the
  template estate and inputs in the txt file. The new estate (.est) file
  can then be saved in a desired location.

### Examples

After creating a template estate and a directory containing your plots,
you can use the downloadable example text file (link below), to help you
get started.

**Example 1.** Template Input Text File

Create estate having 3 years data on planting area for two plots:

  Start Year   Start Step   Area (ha)   Plot File
  ------------ ------------ ----------- -------------
  2000         1            250         PlotOne.plo
  2001         1            350         PlotOne.plo
  2002         1            450         PlotOne.plo
  2000         1            100         PlotTwo.plo
  2001         1            200         PlotTwo.plo
  2002         1            300         PlotTwo.plo

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 274. New Regime 2020

**New Regime**

\[*Events* page : *New Regime* Panel\]

**Use**

The "New Regime" panel enables addition of new events to the "Events
List".

**Select Regime**

Of the species that have been downloaded, any of the default regimes
governing the typical planting, removing and management of the species
may be selected from the "Regime" selection drop-down list. The start
date, repeat period and end dates can be adjusted to suit the intended
modelling.

**Regime Name**

Regimes built from this tool can be given custom identifiers which will
appear in the regime column of the *Events* tab.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 276. Editing Regimes 2020

**Regime Editing**

\[*Events* page : *Regime Editing*\]

This section of the Events page shows the regimes that can occur during
a simulation.

Each Regime step is composed of multiple simulation steps composed of
continuous Events (such as planting or harvesting) - see [Processes and
Events](58_Processes%20and%20Events.htm).

**Populating the Regime List**

Regimes are loaded into the list by one of four methods:

1.  Using the [Data Builder](132_Data%20Builder.htm)
2.  Cloning an existing item
3.  Using the "New\..." button
4.  Select multiple Events and select "Create new Regime\..." from the
    right mouse click option menu

It is possible via the "Create new Regime\..." to move Events out of
existing Regimes and create a new Regime in their place by
multi-selecting (via Shift or Ctrl key selecting) the Events to be
included.

**Editing the Regime**

Click the Edit button to open the [Edit Regime](280_Edit%20Regime.htm)
window where the name and date of the regime can be altered.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 278. Regime Update 2020

**Regime Update**

\[*Events* page : *Clone Regimes* Panel\]

\[*Events* page : *Regime Edit* Dialogue\]

**Use**

Regime Timing can be updated for multiple regimes at once. This can be
either a positive or negative offset from the current timing, and is
irrespective of the type (Calendar date or Days since start of
simulation).

Regime Timing may be updated for multiple regimes by multi-selecting the
regimes on the Regime List, and then selecting Clone from the right
mouse options.

**Clone Regime**

Clones the selected regimes and applies an offset to the original events
of the years and days specified. This can be particularly useful if you
wish to clone [Regimes](235_Regimes.htm).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 280. Edit Regime 2020

**Edit Regime Window**

\[*Events* page : Regime *Edit* button\]

This window is for editing an individual Regime.

**Name**

Every Regime needs a (non-blank) name, and the name must be unique
within the regime list.

**Timing**

Specify the regime time, as either:

1.  . Calendar date\
    Examples: 1 Jan 2001, 31 Dec 2010.

    Enter the date in any unambiguous way, such as "4 Sep 2010", "s4",
    "au9 1999", "4s2000", "8/4/0" or "8.4.1999", except that you cannot
    use hyphens because they are interpreted as negative signs (for
    example 8 4 -35 is 8 Apr -35).

2.  Calendar years and days since the start of the simulation\
    Example: -10, 0, 2345.

A calendar year is from a date in one year to the same date in the next
year, and can contain either 365 or 366 days depending on leap years.
For exmplae, to set a two year calendar time period, set the calendar
years equal to two and the days to zero. For exactly 730 days then set
the calendar years to zero and the days to 730.

Changes in one date type are reflected in the other.

An event always occurs at midnight of the day on which it is specified
to occur, even if that time is in the middle of a simulation step.
FullCAM computes the continuous processes for the partial step up to the
event, executes it, then computes the continuous processes up to the
next event or the end of the step.

Each event occurs instantaneously - it begins and ends at midnight of
the same day.

**Add Days**

A offset may be applied to an event by entering a value in the *Days*
field and clicking *Add Days* button. This can be either positive or
negative and will move the event that number of days forward or back in
the event queue.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 281. Plot Digest 2020

**Plot Digest**

\[*Plot Digest* page of the plot digest (.pld) document\]

Within plot digest multiple scenarios can be created and edited.
Scenarios comprise a set of input values (i.e. the values editable
within FullCAM).

The plot digest function will simulate each scenario created using the
input values specified for each.

The Plot Digest window becomes visible when an open plot file is saved
as a plot digest (.pld) using the File\\Save As function.

**Scenario\\Input Editing**

1.  *New\...* will create allow creation of a new scenario.
2.  *Clone* will duplicate an existing scenario.
3.  *Delete* will permanantly remove a scenario.
4.  *Clone from Plots\...* will open a dialogue which prompts to select
    existing plot(\'s) which will be added as new scenarios.

**View By** Options to change the Digest view.

The plot digest tab can be viewed by scenario, scenario by category or
input.

1.  *Scenario* (default) - will show scenarios at the top of the tree.
    Inputs will be branches below the Scenario.
2.  *Scenario by category* - will show scenarios at the top of tree.
    Sub-branches will have Section names (these are the main tabs in a
    FullCAM plot window), then Inputs beneath.
3.  *Input* - will show Inputs at the top of the tree. Scenarios using
    those inputs will be branches below those Inputs. Some Digest
    functionality will be limited while in Input view.

**Simulation Options** Options for controlling the outputs from the
simulation and units reported.

1.  *Combine all Plots* will combine all the results into one set of
    values.
2.  *Per Scenario* will output separate results for each scenario.
    (Average results are not available).
3.  *Per Output* will ouput separate results for each FullCAM output.

The \'Average Combined plots (not sum)\' checkbox outputs an unweighted
average between scenarios when selected. When unselected, it will sum
the outputs of each scenario.

The \'Mass outputs converted to unit/ha\' checkbox divides the mass
output by hectares to give a unit per hectare figure.

The \'Update spatial data for each scenario\' updates the spatial data
for each scenario run.

**Scenario Inputs** The second column in the list is the values of the
input elements that will replace the current plot input values during
simulation. Plots will not actually be changed by these scenarios.

**Use**

On this page new digest elements can be added, edited, cloned, and
deleted.

A scenario must be selected on the Digest tab before some functionality
will become usable.

The input elements can be added to the current or all the digest
elements from right clicking and selecting the options from the Explorer
page which has all the inputs available.

Input elements can also be added from any tab within a FullCAM plot file
using the following keyboard shortcuts. The desired input should be
selected for editing when pressing the shortcut. A pop-up notification
will confirm when an output has been added.

1.  ctrl-alt-s - add field to selected scenario.
2.  ctrl-alt-d - add field to all scenarios.
3.  Explorer - use the right-click context menu on items to add to the
    selected (ctrl-alt-a) or all scenarios (ctrl-alt-d).

Once scenarios have been chosen, the digest can be run by running a
FullCAM plot digest simulation (F9) or clicking the FullCAM Running-Man.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 282. Templates 2020

**FullCAM Plot Templates**

\[File menu; *New From Template\...*\]

This panel is used for creating new [Plot](177_Plot%20Simulation.htm)
files based on pre-existing templates that have been provided on the
[Department Server](219_Departmental%20Server.htm).

**Use**

1.  Select a template from the list in the top panel. Notes for the
    template will be available in the second panel.
2.  Enter latitude and longtiude values for the location that the plot
    file will be generated at (optional).
3.  Enter the start and end dates for the location that the plot file
    will be generated at (optional).

Upon clicking \"OK\" to confirm creation, new plot files will be created
based on the template chosen and will have location and timing data
based on the optional inputs. Certain method-specific templates may also
download the applicable species data. More details are provided the
applicable method-specific FullCAM Guidelines.

**Select Digest Scenarios**

Digest scenarios may be applied to the templates.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 283. FullCAM Command Line Utility 2020

**FullCAM Command Line Utility**

The FullCAM command line utility is run via FullCAMCL.exe in a command
(MS-DOS) prompt.

Below is the syntax flags and some general aspects of simulating plots
in the FullCAM command line utility:

  Options               Description
  --------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  -help                 Launch online help page
  -sim                  Simulate plots (default)
  -update               Update plots to latest version and save
  -path folder          Name of folder to write output files
  -execl                Output windows to Excel
  -db                   Download latest spatial data
        type            \- combination of the letters below
            C           \- Climate (default)
            S           \- Species
        lat,long,area   Override location for DataBuilder download
                        Note: For Plot Digests (.pld), sets the \"Update Spatial Data for each Scenario\" flag. For more information see the [Plot Digest](281_Plot%20Digest.htm) help.
  -alt=url              Use alternate \"url\" for DataBuilder download
  \--mode               Set output mode
        PerDoc          Separate output file for each plot file (default)
        Combined        Sum all plot outputs into single output file
        PerOutput       Separate output file for each selected output
  -perhectare           Mass outputs in t/ha, Only when mode is Combined or PerOutput
  -average              Average across all plots (default Sum), Only when mode is Combined
  -patch                Apply \"patchfile.xml\" to plot files. More information is available on the [XML Copy](286_XML%20Copy.htm) page.
  -start                Override Simulation Start Date
  -end                  Override simulation End Date
  -silent               Hide progress messages
  -digest               Convert list of plots into Plot Digest, using Inputs for Scenarios
  -verify               Attempt to read a plot file and check if it is in a ready state.
        db              Verify if the plot would still be valid and in a ready state after a spatial data update.
        patch           Verify if the plot would still be valid and in a ready state after a patch application update.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 284. Initial StandingDead 2020

**Initial Standing Dead**

\[[Trees](201_Plants.htm) page: *Standard Information for the Species*
panel: *Initial Standing Dead* button\].

\[[Initial Conditions](205_Initial%20Conditions.htm) page : *Forest*
panel : *Standing Dead* button\]

Describe the standing dead biomass pool present in the plot at the start
of the simulation.

The standing dead biomass pools are used to represent slower
decomposition of woody biomass that is either standing dead woody
biomass (for example following fire or drought) or freshly cut
post-clearing or harvesting (for example piled in wind-rows). Such
biomass is expected to slowly senesce at breakdown rates that are slower
than breakdown rates for debris pools (based on litterbag studies) that
have better contact with the soil and organisms that decompose biomass.

Standing dead pools turnover into debris (with some loss as carbon
dioxide) rather than turnover into soil as per debris pools (see
[Standing Dead](285_StandingDead.htm)).

**Introduction**

All of the initial standing dead pool belongs to the initial tree
species, which is specified in the [Initial
Trees](185_Initial%20Trees.htm) window.

**Carbon Masses**

Enter the mass of carbon in the various standing dead pools, in tonnes
per hectare.

**Insert Standard Values**

\[Only present when the window is accessed via the [Initial
Conditions](205_Initial%20Conditions.htm) page.\] Press the Insert
Standard Values button to insert the standard initial standing dead
biomass values (set via the Initial Standing Dead button on the Standard
Information for the Species panel of the Trees or Crops pages, see
*Standard Information for the Species* of the initial species (specified
via the Trees or Crops buttons of the [Initial
Conditions](205_Initial%20Conditions.htm) page).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 285. StandingDead 2020

**Standing Dead**

\[[Trees](201_Plants.htm) page : *Properties of the Species* panel :
*Standing Dead* button\]

Specify the properties of the standing dead pools produced by the
current species (see [Select a Species](56_Select%20a%20Species.htm)).

**About standing dead pools in FullCAM**

The standing dead biomass pools are used to represent slower
decomposition of woody biomass that is either standing dead woody
biomass (for example following fire or drought) or freshly cut
post-clearing or harvesting (for example piled in wind-rows) Such
biomass is expected to slowly senesce at breakdown rates that are slower
than breakdown rates for debris pools (based on litterbag studies) that
have better contact with the soil and organisms that decompose biomass.

In FullCAM, standing dead pools are created through either an assumed
initial standing dead pool or through a disturbance event of fire or
thinning. When the standing dead pool is created, breakdown properties
for these pools must also be set accordingly. Typical values for
different events that create standing dead can be found in the most
recent annual [National Inventory Report, Volume
2](https://publications.industry.gov.au/publications/climate-change/climate-change/climate-science-data/greenhouse-gas-measurement/progress-inventory.html).

**Breakdown Percentages**

The breakdown percentage of the standing dead pool is the percentage of
the pool that breaks down each year due to the freshly cut or burnt
pools of standing dead material slowly senescing.

Breakdown is the process by which standing dead material senesces to
becomes a combination of:

- *Atmospheric breakdown products* - Goes to the atmosphere. Consist
  mainly of CO2.
- *Solid breakdown products* - Goes to the debris pool.

The breakdown percentage of a standing dead pool determines how long it
takes material to pass through the standing dead pool. Setting a
breakdown percentage to 0 means that none of the material in the
standing dead pool ever leaves the pool. Setting a high breakdown
percentage means that in each simulation step most of the standing dead
pool at the beginning of the step moves either to the atmosphere or
debris. It assumes exponential decay at a constant decay rate.

**Atmospheric Percentages of Breakdown Products**

The atmospheric percentage of the breakdown product of a standing dead
pool is the percentage of the breakdown products of the standing dead
pool that moves to the atmosphere (the rest moves to the corresponding
debris pool).

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 286. XML Copy 2020

**XML Copy**

\[*Edit* toolbar : *XML Copy* (toggle on\|off) menu item. \]\
\[FullCAMCL.exe -patch\]

Describes the use of *XML Copy* and FullCAM Command Line *Patching*.

**What is an XML Patch file**

A *XML Patch* is a file containing a selection of FullCAM inputs which
have been chosen via the *XML Copy* menu option and saved in a .xml
file.

The .xml patch file can then be applied against a plot file which is
simulated via the [FullCAM Command
Line](283_FullCAM%20Command%20Line%20Utility.htm).

These \"patches\" serve as a type of scenario (see the plot digest tab
help for an explanation of scenarios), being applied against a plot file
overwriting the inputs at the time of simulation, but without modifying
the .plo file.

**Creating a XML Patch file**

While having a plot file open that you wish to use to create patches, go
to the FullCAM *Edit* menu and turn on *XML Copy* (a tick will appear
next to it) .

With the toggle now turned on, navigate to the
[Explorer](234_Explorer.htm) tab, and in the left hand \"Documents\"
panel browse to the input you wish to patch, and right mouse click the
entry and select *Copy*.

Open notepad, or some other basic text editor (not Word or Excel), and
paste the values. Multiple inputs can be entered into a single patch
file, however only the first instance of \[\] and \[\], and final should
be kept, any further entries should have that row of text removed. Then
save this text file as your XML patch file (with extension .xml).

Example XML Patch file:



      
      
      

**Running the XML Patch file**

With the file now created, FullCAMCL can now be run using the -patch
command to apply the patch file aginst a plot file.

See [FullCAMCL help](283_FullCAM%20Command%20Line%20Utility.htm) or use
the -help flag within a command prompt.

**Example 1:** To run a plot utilising a patch file: \> FullCAMCL.exe
-sim -patch \"patchfile.xml\" ExamplePlot.plo

**Example 2:** To apply a patch to an existing plot file: \>
FullCAMCL.exe -update \"patchfile.xml\" ExamplePlot.plo

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
