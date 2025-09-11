---
title: Output Windows
version: 2016
category: Output
original_file: 25_Output Windows_2016.md
---

*Output Windows* page of the input window of a plot or estate
document

Control the output windows of the document.

Note that the **contents** of an Output
Window, such as which simulation outputs to
display, are controlled from the output window itself.

**List**

This page lists the output windows, by name. A check beside the name
means that the output window will open after you run a simulation. You
cannot delete the last output window, but you can uncheck it.

An output window is listed in red if it is not ready and black if its
data is complete and ready to simulate. An output window is ready if it
has one or more available outputs selected. Make an unready output
window ready by showing the output window then selecting one or more
outputs to show in the window.

**Estate Outputs**

You may obtain any non-timing FullCAM outputs in the output windows of
an estate, because an estate consists of plot files with configurations
that may vary, and these configurations are not necessarily known when
you specify the estate outputs.

If an output is not possible for a plot (due to the configuration of the
plot file) that is simulated during an estate simulation, then the plot
will not contribute (or will contribute zeroes) to that estate output.