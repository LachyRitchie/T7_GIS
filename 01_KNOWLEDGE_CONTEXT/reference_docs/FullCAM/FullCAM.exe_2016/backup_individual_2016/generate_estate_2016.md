---
title: Generate Estate
version: 2016
category: Utilities
original_file: 269_Generate Estate_2016.md
---

[Utilities Menu: *Generate Estate* ]

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
    step number is "1".
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
