+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Soil Inputs**

\[[Soil](203_Soil.htm) page : *Forest* or *Agricultural* panel :
*Inputs* button\]

Specify the material that enters the soil. See the
[RothC](114_RothC.htm) soil pool abbreviations.

**Soil Input Percentages of Humified Mulch**

Specify where the humified mulch goes to within the active soil. FullCAM
only includes mulch if you have configured
[GENDEC](http://www.fullcam.au/FullCAMServer2020/Help/109_GENDEC.htm) to
model the mulch, and this section is only on if RothC models the active
soil.

With such a configuration, each pool in the mulch undergoes
humification, the process whereby material is transported from the mulch
down to the soil. This material, the humified mulch, can enter the DPM,
RPM or HUM pools within the soil. Specify, for each mulch pool, which of
these soil pools the humified mulch enters.

Humified mulch from the soluble mulch pools, being decomposable, can
only go to the DPM or HUM pools. Humified mulch from the more-resistant
and less-resistant mulch pools, being resistant , can only go to the RPM
or HUM pools. Humified mulch from the live microbes pools contains both
decomposable and resistant material, so specify the percentage that goes
to DPM and RPM versus HUM.

Naturally, the sum of each pair of percentages is 100%. Therefore the
HUM percentage is calculated automatically from the DPM/RPM value.

**Typical values used are:**

  Variable                    To DPM or RPM   To HUM
  -------------------------- --------------- --------
  Plant Soluble litter             100          0
  Plant Less Resistant             80           20
  Plant More Resistant             50           50
  Microbial Soluble Litter         100          0
  Microbial Less Resistant         60           40
  Microbial More Resistant         40           60
  Live Microbes                    75           25

**Soil Input Percentages of Broken-Down Litter**

Specify where the broken-down litter goes to within the active soil.

The material in each litter pool breaks down, thereby transporting
material from the litter to the soil. This material, the broken-down
litter, can enter the DPM, RPM or HUM pools within the soil. Here, you
specify, for each type of broken down litter, which of these soil pools
the broken-down litter enters.

The decomposable and resistant broken-down litter always goes to either
the DPM, RPM or HUM.

Naturally, the sum of each pair of percentages is 100%. Therefore the
HUM percentage is calculated automatically from the DPM/RPM value.

**Typical values used are:**

  Variable               To DPM or RPM   To HUM
  --------------------- --------------- --------
  Decomposable Litter         90           10
  Resistant Litter            90           10

**Manure from Offsite**

Manure from offsite (from outside the plot) may be added to the forest
or agricultural soil. Offsite manure inputs are only available if RothC
is used to model the soil.

Enter the time series of manure carbon additions or add manure
application events to the 'Events' tab depending on how manure additions
were configured in the 'Events' or time series window of the
'Configuration tab'

Manure from offsite may be added to the forest or agricultural soil.
Enter the carbon mass in the manure, in tonnes per hectare, over time.

'Offsite' means 'from outside the plot'. Offsite manure inputs are only
available if Roth-C is used to model the soil.

In an agricultural system, manure from animals on the plot is dealt with
by grazing events (plant material eaten by grazing animals becomes
fodder, which may move to destinations including the DPM an RPM pools of
the soil). The offsite manure is the only explicit treatment of manure
by FullCAM.

Specify the percentages of the carbon in any offsite manure added to the
soil that move to the various organic soil components. The percentages
add to 100%; the HUM percentage is automatically calculated from the
others.

Note that manure from offsite and grazing are entirely separate. The
manure inputs entered here have no effect on any grazing manure, and
vice versa.

**Typical values used are:**

Variable

Percentage of Manure

DPM

49

RPM

49

BIO-F

0

BIO-S

0

**Plant Residues**

Plant residue inputs are plant material from the debris or mulch that
enters the soil. The material enters the DPM soil pool if it is
decomposable, or the RPM soil pool if it is resistant. Specify the total
amount of plant material entering the soil over time.

Plant residues can only be specified here if you are simulating the
[Soil](203_Soil.htm) by itself. If you are simulating a multilayer
system, then the plant residues from the debris or mulch are
automatically calculated, so an explicit input for plant residues is
neither required nor desired.

The ratio of DPM to RPM is the mass of DPM divided by the mass of RPM in
the plant matter added to the soil, and is also known as the "quality
factor for incoming plant debris". Typical values for the ratio of DPM
to RPM are:

1.44 - Most agricultural crops and improved grassland\
0.67 - Unimproved grassland and scrub (including savanna)\
0.25 - Deciduous and tropical woodland.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
