---
title: Output Windows
version: 2020
category: output
original_file: 25_Output Windows_2020.md
---

Control the output windows of the document.

Note that the **contents** of an Output
Window, such as which simulation outputs to
display, are controlled from the output window itself.

**List**

This page lists the output windows. A check beside the name means that
the output window will open after you run a simulation. At least one
output window must exist - you cannot delete the last output window, but
you can uncheck it.

**Estate Outputs**

You may obtain any non-timing FullCAM outputs in the output windows of
an estate, because an estate consists of plot files with configurations
that may vary, and these configurations are not necessarily known when
you specify the estate outputs.

If an output is not possible for a plot that is simulated during an
estate simulation due to the configuration settings, then the plot will
not contribute, or will contribute zeroes, to that estate output. For
example, if you choose to report forest products but these are not
included in the plot files they will contribute zero to the estate
outputs.

**Subrule**

Create Subrule
Report
output windows and enable subrule calculations.
