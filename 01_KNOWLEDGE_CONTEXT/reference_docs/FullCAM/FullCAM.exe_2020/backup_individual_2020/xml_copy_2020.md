---
title: "XML Copy"
version: 2020
category: General
original_file: 286_XML Copy_2020.md
---

\.

These \"patches\" serve as a type of scenario (see the plot digest tab
help for an explanation of scenarios), being applied against a plot file
overwriting the inputs at the time of simulation, but without modifying
the .plo file.

**Creating a XML Patch file**

While having a plot file open that you wish to use to create patches, go
to the FullCAM *Edit* menu and turn on *XML Copy* (a tick will appear
next to it) .

With the toggle now turned on, navigate to the
 tab, and in the left hand \"Documents\"
panel browse to the input you wish to patch, and right mouse click the
entry and select *Copy*.

Open notepad, or some other basic text editor (not Word or Excel), and
paste the values. Multiple inputs can be entered into a single patch
file, however only the first instance of \ or use
the -help flag within a command prompt.

**Example 1:** To run a plot utilising a patch file: \> FullCAMCL.exe
-sim -patch \"patchfile.xml\" ExamplePlot.plo

**Example 2:** To apply a patch to an existing plot file: \>
FullCAMCL.exe -update \"patchfile.xml\" ExamplePlot.plo

------------------------------------------------------------------------