---
version: 2016
batch_range: 251-286
batch_name: Advanced_Features_Command_Line
creation_date: 2025-08-28
total_files: 12
---

# FullCAM 2016 - Batch 251-286: Advanced Features Command Line

## Table of Contents

- [253. Mineral Nitrogen Model 2016](#253-mineral-nitrogen-model-2016)
- [266. Server Settings 2016](#266-server-settings-2016)
- [267. Simulation Timing 2016](#267-simulation-timing-2016)
- [268. Whats New 2016](#268-whats-new-2016)
- [269. Generate Estate 2016](#269-generate-estate-2016)
- [270. Generate Plot Files from Directory 2016](#270-generate-plot-files-from-directory-2016)
- [271. At Risk 2016](#271-at-risk-2016)
- [274. New Regime 2016](#274-new-regime-2016)
- [274. Editing Event List Order 2016](#274-editing-event-list-order-2016)
- [276. Editing Regimes 2016](#276-editing-regimes-2016)
- [278. Regime Update 2016](#278-regime-update-2016)
- [280. Edit Regime 2016](#280-edit-regime-2016)

---

## 253. Mineral Nitrogen Model 2016

**No Help Available**

The Help Window shows this topic if there is no help in a context or
with certain sorts of errors.

Some windows (such as the [Main Window](217_Main%20Window.htm)) and some
pages have no help. When you are there, pressing "F1" leads you to here.

Otherwise, you may be here by error. If there was a help button (yellow
question mark on small green circle) on the window or page you had
selected, then you should have been lead to the help for that button ---
please [Contact Us](190_Contact%20Us.htm) so we know to fix the error.

Press the appropriate help button with the mouse if there are any
difficulties or ambiguity.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 266. Server Settings 2016

**Server Settings**

\[*Internet* menu : Server *Settings*\]

This window is for maintaining your FullCAM server settings.

**Use Alternate Server**

This option allows you to specify the address of an alternate server
that FullCAM uses for data. Otherwise the [Department of
Environment](http://www.environment.gov.au) server will be used.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 267. Simulation Timing 2016

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

The shorter the steps, the longer a plot simulation takes.

### Choosing the Length of Simulation Steps

*Time Resolution of Input Data*

If you specify the rainfall to FullCAM as just the total rainfall each
year (that is, one number per year), then it is unrealistic to expect
FullCAM to accurately simulate monthly or weekly phenomena that are
influenced by rainfall. Monthly simulation steps might be appropriate,
but the results might have to be interpreted carefully.

*Computing Time and Memory*

In a lengthy simulation or one with many outputs, there may not be
enough computer memory to do a simulation with very short steps, or it
might take longer to compute than is convenient. This problem will
probably only arise when simulating estates.

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
can get to pool C by the end of the second day!

In reality, the step length is vanishingly small: carbon moves between
pools continuously, rather than in discrete movements that occur once
every beat of our simulation clock. Now, we want to model the essential
nature of the system with as little computing effort as possible. If we
decrease the step length then we get a more realistic simulation, but we
do more computing. This dependence of the simulation results on the step
length is called *graininess*.

FullCAM performs its calculations efficiently. It runs near the maximum
possible speed on your computer --- and your computer is probably a
supercomputer by the standards of a decade ago. So speed of computation
is not much of a limiting factor. The precision of the quantities in
FullCAM is relatively low so round-off error is almost insignificant ---
but there is little point in using more steps than necessary in case the
round off error begins to affect your results. FullCAM's speed of
computation and flexibility in its treatment of time allows you to
overcome the artificial barriers set by arbitrary and fixed frequencies
of simulations steps that are present in many other models.

What is a sensible amount of time per step? As you decrease the step
length, you will find your simulated results will gradually approach
limiting values. The limiting values are simulation results that stay
the same, no matter how much you further decrease the step length. From
the perspective of graininess, an appropriate step length is the step
length that gets you close to the limiting values. For example, if
halving the step length does not change the results much then there is
no point in decreasing it further.

As a rough rule of thumb, for negligible graininess use a step length of
at most a month unless modelling for detailed results (such as in an
academic or scientific situation).

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 268. Whats New 2016

**What\'s New?**

What's new since the previous release?

**Baseline fraction maps of organic carbon in Australian soil**

Baseline spatial maps have been included for the RPM, HUM and Inert
pools of organic carbon in soil. Viscarra-Rossel et al. (2014) has
derived spatially explicit estimates, and their uncertainty, of the
distribution and stock of organic carbon in the soil of Australia. This
was achieved through the assembly and harmonisation of data from
Australia's National Soil Carbon Research Program (SCaRP), the National
Geochemical Survey of Australia (NGSA) and the Australian Soil Resource
Information System (ASRIS) to produce the most comprehensive set of data
on the current stock of organic carbon in soil of the continent.

Viscarra Rossel, R.A., Webster, R., Bui, E.N., and Baldock, J.A. (2014).
Baseline map of organic carbon in Australian soil to support national
carbon accounting and monitoring under climate change. Global Change
Biology. 20(9):2953-2970.

\

**[Regime Scheduler](136_Events.htm "Regime Scheduler")**

The Events tab has been redesigned to include an interface for managing
both the events and the regimes formed from those events. This
enhancement allows the regimes and events to be moved around, copied,
edited and managed as groups.

\

**User interface improvements**

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 269. Generate Estate 2016

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

[(Download example 1)](Generate%20Estate%20-%20Example%201.txt)

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 270. Generate Plot Files from Directory 2016

**Generate Plot Files from Directory**

\[Utilities Menu : *Generate Plot Files from Directory*\]

**Use**

The Generate Plot Files from Directory function enables the bulk
creation or update of plot files using a specially formatted text file
to specify new variable values for the derived plots.

Plots created by \"Generate plot files from Directory\" will be copies
of a base plot that already exists in the source directory.

Generate plot files will update existing plot files or create new ones
if they do not already exist.

**Base Plots**

Plots are created from one or more Base Plots contained in a directory
supplied as an input to this process. The base plots contain all data
that is not to be altered by this process. Generated plots will be
copies of the base plot, with changes as specified in the text import
file.

**Text Import File**

This file contains all the data that is required to be altered for the
new plots generated. Data formatting rules are:

- 1 plot per row.
- Data is tab delimited.
- Spaces in the file will be treated as ordinary characters that are
  part of the input (e.g. the space in \"Pinus radiata\"), not as a
  delimiter between fields.
- The first field must be the base plot name including file extension
  (.plo). The named base plot must already exist in the source directory
  specified.
- The second field must be the name of the new plot that is to be
  generated. The new plot name specified should not include file path or
  extension details as these will be added by the *Generate Plot Files
  from Directory* process.
- Inputs for a species must be preceded by the name of the species to
  which they apply.
- Note that any species used in the input text file must already exist
  in the named template plot. This function will not add new species, it
  will only modify ones that already exist in the template plot.
- Each input field is identified by its [programming
  name](141_Models%20and%20Inputs%20Window.htm#ProgrammingName) (e.g.
  Max forest aboveground biomass is maxAbgMF) and then the data item(s).

*time-Series Inputs*

Time series inputs must have the time series name (e.g. avgAirTemp-
Average Air Temperature) followed by 6 mandatory inputs, being:

- Start year
- Years are
- Extrapolation
- Years of data
- Data points per year
- Multiplier

The time-series inputs identifying the Years and Extrapolation are
stored in FullCAM internally as integers. Valid values for these inputs
are detailed below.

*Years are*\
0 Calendar time\
1 Time since start of simulation\
2 Years since plants sprouted

*Extrapolation*\
0 Use nearest year in table\
1 Cycle table data across all time\
2 Use average year of data

**Processing rules**

- If an input is invalid then the process will cease and error details
  reported. Plot files successfully created up until the error is
  encountered will be stored in the results directory specified.
- Inputs for multiple species may be imported, but these must be
  preceded by the species name input (nmSP). Multiple inputs per species
  are permissible as all inputs will be attributed to the last recorded
  species on the input row.
- If you attempt to update a species that does not exist in your named
  template plot, the output log will show \"Error - species \'Xxxx
  yyyyy\' not found\" and the plot will not be created / updated.
- Time-series inputs must include all information for the time series
  (e.g. Extrapolation method, Multiplier, etc.).
- Programming name inputs are case-sensitive.
- If a plot name already exists then this process will either update the
  existing plot, or create a new plot from the base plot and inputs in
  the txt file. This is determined by the prompt : \"If a generated plot
  exists already should it be updated with the new inputs from the input
  file?\" Yes- Existing plot files will be updated with the inputs from
  the file specified. No- Existing plot files will be over written,
  based on the base plot and the inputs from the file specified.

### Examples

After creating a directory containing your Base Plots, you can use the
downloadable example text files (links below), to help you get started.

**Example 1.** Create 3 plot files, adding a single tree species input
for each plot. Txt import file for tree species inputs (exclude
Description field):

  Template Plot   ID      Description                                                                         Type   Species               Variable        Value
  --------------- ------- ----------------------------------------------------------------------------------- ------ --------------------- --------------- -----------------------
  Plot_1.plo      Plot1   Turnover % of branches for tree species Eucalyptus globulus                         nmSP   Eucalyptus globulus   turnFracBranF   0.6
  Plot_2.plo      Plot2   Species note for tree species Eucalyptus globulus                                   nmSP   Eucalyptus globulus   notesSP         Imported species note
  Plot_3.plo      Plot3   *Tree age of max growth in tree yield formula (G)* for tree species Pinus radiata   nmSP   Pinus radiata         tyf_G           12.6

[(Download example
1)](Generate%20Plots%20from%20Directory%20-%20Example%201.txt)

**Example 2.** Create 3 plot files, adding a time-series for each plot.
Txt import file for time series inputs (exclude Description field):

  Template Plot   ID      Description                                        Type         Species/Yr            Variable       Data
  --------------- ------- -------------------------------------------------- ------------ --------------------- -------------- ---------------------------------------------------------------------
  Plot_1.plo      Plot1   5 years of annual *Stem volume increments* data    nmSP         Eucalyptus globulus   incrStemVoIf   0 2 1 5 1 1 41.1 98.8 128.9 175.1 219.5
  Plot_2.plo      Plot2   1 year of monthly *Average air temperature* data   avgAirTemp   1985                                 0 2 1 12 1 19.5 19.8 16.9 14.4 10.7 8.8 9.5 10.1 9.3 12.6 14.0 14.7
  Plot_3.plo      Plot3   1 year of monthly *Rainfall* data                  rainfall     1995                                 0 1 1 12 1 20 50 30 40 20 50 80 200 300 10 35 125

[(Download example
2)](Generate%20Plots%20from%20Directory%20-%20Example%202.txt)

**Example 3.** Create 3 plot files, adding multiple inputs (including
time-series) for each plot:

  ID      Description
  ------- -------------------------------------------------------------------------------------------------------------------------
  Plot1   *Turnover % of branches, Species note, Tree age of max growth in tree yield formula (G)* for tree species Pinus radiata
  Plot2   *Stem volume increments, Tree age of max growth in tree yield formula (G)* for tree species Eucalyptus globulus
  Plot3   *Tree age of max growth in tree yield formula (G)*

Txt import files for multiple inputs per plot:

  Template Plot   ID      Type   Species/Yr      Variable        Value   Variable   Value                   Variable   Value
  --------------- ------- ------ --------------- --------------- ------- ---------- ----------------------- ---------- -------
  Plot_1.plo      Plot1   nmSP   Pinus radiata   turnFracBranF   0.6     notesSP    Imported species note   tyf_G      12.6

  Template Plot   ID      Type   Species               Variable       Series                                    Variable   Value
  --------------- ------- ------ --------------------- -------------- ----------------------------------------- ---------- -------
  Plot_2.plo      Plot2   nmSP   Eucalyptus globulus   incrStemVoIf   0 2 1 5 1 1 41.1 98.8 128.9 175.1 219.5   tyf_G      10.5

  Template Plot   ID      Type   Species         Variable     Value   Variable     Value   Variable     Value   Variable     Value   Variable     Value   Variable     Value   Variable   Value
  --------------- ------- ------ --------------- ------------ ------- ------------ ------- ------------ ------- ------------ ------- ------------ ------- ------------ ------- ---------- -------
  Plot_3.plo      Plot3   nmSP   Pinus radiata   rFracStemF   1       rFracBranF   1       rFracBarkF   1       rFracLeafF   0.85    rFracCortF   1       rFracFirtF   0.65    maxAbgMF   160

[(Download example
3)](Generate%20Plots%20from%20Directory%20-%20Example%203.txt)

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 271. At Risk 2016

**\@Risk**

\@Risk (pronounced "at-risk") is third-party commercial off-the-shelf
software used by FullCAM for performing risk analyses. \@Risk is
available from the publisher, [Palisade
Corporation](http://www.palisade.com).

To perform an analysis, the \@Risk software must be installed and
licenced on your computer.

[Sensitivity analysis](218_Risk%20analysis.htm) uses \@Risk RDK
software. FullCAM and \@Risk work together to do the sensitivity
analysis. Use the FullCAM interface to organise and initiate the
sensitivity analysis, and when the analysis is completed FullCAM will
direct you to look at the results in the \@Risk window.

The \@Risk software is a product of Palisade Corporation. Department of
Environment recognises and acknowledges all trademarks and intellectual
property belonging to Pallisade Corporation.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 274. New Regime 2016

**New Regime**

\[*Events* page : *New Regime* Panel\]

**Use**

The "New Regime" panel enables addition of new events to the "Events
List".

**Select Species**

A species is selected from the "Species" drop-down list. As a visual
guide, species that have been used previously during the session are
displayed in bold.

**Select Regime**

Once a species has been selected, any of the regimes for that species
may be selected from the "Regime" selection drop-down list.

**Select Occurrences**

The "occurrences" edit box can be edited directly or can be set using
the up-down selector attached to it.

**OK Button**

Once the "OK" button has been pressed, the events of the selected regime
are added to the end of the event queue. The added regime is repeated at
the end of the event queue the number of times specified by the
"occurrences" setting.

**Regime Name**

Every Regime needs a (non-blank) name, and the name must be unique
within the regime list. A default name will be shown in the *Name*
field, but may be changed.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 274. Editing Event List Order 2016

**No Help Available**

The Help Window shows this topic if there is no help in a context or
with certain sorts of errors.

Some windows (such as the [Main Window](217_Main%20Window.htm)) and some
pages have no help. When you are there, pressing "F1" leads you to here.

Otherwise, you may be here by error. If there was a help button (yellow
question mark on small green circle) on the window or page you had
selected, then you should have been lead to the help for that button ---
please [Contact Us](190_Contact%20Us.htm) so we know to fix the error.

Press the appropriate help button with the mouse if there are any
difficulties or ambiguity.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 276. Editing Regimes 2016

**Regime Editing**

\[*Events* page : *Regime Editing*\]

This section of the Events page shows the regimes that can occur during
a simulation.

Each Regime step is composed of multiple simulation steps composed of
continuous Events (such as planting or harvesting) - see [Processes and
Events](58_Processes%20and%20Events.htm).

**Populating the Regime List**

Regimes are loaded into the list by one of four methods:

1.  Using the "[Data Builder](132_Data%20Builder.htm)"
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

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 278. Regime Update 2016

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

**Minimise Gaps**

The right mouse option includes the "minimise gaps" feature. This will
compress the regime queue by removing free time between regimes. It will
do this by changing the year value of later regimes if there is room for
them to occur earlier based on the date of the final event in the
earlier regime.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---

## 280. Edit Regime 2016

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

    A calendar year is from a date in one year to the same date in the
    next year, and can contain either 365 or 366 days depending on leap
    years. The number of days can also be huge. So if you mean the same
    date in two years time, set the calendar years equal to two and the
    days to zero, but if you mean exactly 730 days then set the calendar
    years to zero and the days to 730.

Go back and forth between the date types to see how they compare -
changes in one are reflected in the other, that is, they both show the
same date.

A regime always occurs at noon of the day on which it is specified to
occur, even if that time is in the middle of a simulation step. FullCAM
computes the continuous processes for the partial step up to the regime,
executes the regime, then computes the continuous processes up to the
next regime or the end of the step.

Each regime occurs instantaneously - it begins and ends at noon of the
same day.

**Add Days**

A offset may be applied to an event by entering a value in the *Days*
field and clicking *Add Days* button. This can be either positive or
negative and will move the event that number of days forward or back in
the event queue.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")


---
