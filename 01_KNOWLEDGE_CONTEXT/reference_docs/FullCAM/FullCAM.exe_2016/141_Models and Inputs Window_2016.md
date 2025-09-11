+---------------------------------------------------------------------+-----------------------+-----------------------+
| [![coat of                                                          |                       | [](index.htm)         |
| arms](imgs/coa_env.png){border="0"}](http://www.environment.gov.au) |                       |                       |
|                                                                     |                       | # FullCAM Help        |
+---------------------------------------------------------------------+-----------------------+-----------------------+
|                                                                     |                       |                       |
+---------------------------------------------------------------------+-----------------------+-----------------------+

**Models and Inputs Window**

\[[Configuration](150_Configuration.htm) page : *Models and Inputs*
button\]

This window shows information about the currently chosen configuration:

- The constituent models that will be used to simulate your
  configuration
- The data inputs required by your configuration.

You cannot change any aspect of the configuration or the document from
this window.

**Models**

See [Plots, Systems, Layers, and
Pools](57_Plots,%20Systems,%20Layers,%20and%20Pools.htm), [Yield and
NPP](131_Yield%20and%20Net%20Primary%20Production.htm), and [Constituent
Models In FullCAM](198_Constituent%20Models%20In%20FullCAM.htm).

*Plants (ex production)* is about modelling all the aspects of plants
other than production: partitioning of production to the various plant
components, turnover, thinning, harvesting, fire, and so on.

**Options Menu**

(The drop-down menu on the far left of the toolbar.)

**Show Values.** Show the current values in the document. If the value
belongs to a species, it shows the value in the species that is
currently chosen for editing (there may be multiple species). If the
value belongs to an event, the value shown comes from an arbitrarily
chosen event of that type. If there is no species or event or the value
is blank or the value is not a number or "On/Off", or if there is no
such value in that type of document, generally no value is shown.

**Show Programming Names.** The programming names are useful if you are
reading the FullCAM technical documentation or code. The configuration
is useful as a compact written reminder, especially if you copy the list
to put in another sort of document.

**Show Configuration.** Shows a record of the choices you made.

**Display.** Either:

1.  **All inputs** - Shows all inputs to FullCAM, ignoring the
    configuration and any other settings. Showing values is not
    generally possible because some inputs will not exist.
2.  **Inputs required by the current configuration** - Shows the inputs
    that could be required by the current configuration, but ignores the
    settings on other pages of the document. It is possible that some
    inputs will be shown that are not required because of other
    (non-configuration) settings --- for example, in a forest
    configuration the tree mortality inputs will be shown as required
    regardless of whether or not the *Tree mortality on* box is checked
    on the [Plant Properties](43_Plant%20Properties.htm) window for any
    species.
3.  **Inputs required by the current configuration and other
    settings** - Shows the inputs that could be required by the current
    configuration and the current settings on other pages of the
    document. Thus this option gives the smallest, most accurate picture
    of the data inputs required by FullCAM, but requires you to have
    entered all the input settings already (as would be the case if the
    document was ready to simulate).

These inputs are never shown:

- Names and note inputs
- Configuration settings (all the settings made on the
  [Configuration](150_Configuration.htm) page)
- Event type, timing, and name inputs.

**Copy**

There are two copy options on the toolbar. Either:

1.  **Copy** - Select all or part of the text in the usual manner and
    press control-C or use the mouse menu. This performs the usual copy,
    suitable for pasting into a word processor. Use an equi-spaced font,
    such as *Courier New*, in the word processor to preserve the exact
    layout of the list.
2.  **Spreadsheet Copy** - Press the *Copy All Text in Spreadsheet
    Format* button or use the mouse menu. This copies all of the text,
    using tabs to separate fields --- suitable for pasting into a
    spreadsheet.

------------------------------------------------------------------------

© 2025 [Department of
Environment](http://www.environment.gov.au "Department of Environment"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
