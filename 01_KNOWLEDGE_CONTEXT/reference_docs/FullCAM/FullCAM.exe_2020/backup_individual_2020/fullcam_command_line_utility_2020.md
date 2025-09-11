---
title: "FullCAM Command Line Utility"
version: 2020
category: Configuration
original_file: 283_FullCAM Command Line Utility_2020.md
---

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
                        Note: For Plot Digests (.pld), sets the \"Update Spatial Data for each Scenario\" flag. For more information see the  help.
  -alt=url              Use alternate \"url\" for DataBuilder download
  \--mode               Set output mode
        PerDoc          Separate output file for each plot file (default)
        Combined        Sum all plot outputs into single output file
        PerOutput       Separate output file for each selected output
  -perhectare           Mass outputs in t/ha, Only when mode is Combined or PerOutput
  -average              Average across all plots (default Sum), Only when mode is Combined
  -patch                Apply \"patchfile.xml\" to plot files. More information is available on the  page.
  -start                Override Simulation Start Date
  -end                  Override simulation End Date
  -silent               Hide progress messages
  -digest               Convert list of plots into Plot Digest, using Inputs for Scenarios
  -verify               Attempt to read a plot file and check if it is in a ready state.
        db              Verify if the plot would still be valid and in a ready state after a spatial data update.
        patch           Verify if the plot would still be valid and in a ready state after a patch application update.

------------------------------------------------------------------------