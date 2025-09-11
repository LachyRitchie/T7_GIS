+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

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
