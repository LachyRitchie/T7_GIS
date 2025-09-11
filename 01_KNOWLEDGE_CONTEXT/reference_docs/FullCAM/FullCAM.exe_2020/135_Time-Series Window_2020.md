+----------------------------------------------+-----------------------+-----------------------+
| [![coat of                                   |                       | [](index.htm)         |
| arms](imgs/DISER-inline_Mono.png){border="0" |                       |                       |
| width="320"}](http://www.industry.gov.au)    |                       | # FullCAM Help        |
+----------------------------------------------+-----------------------+-----------------------+
|                                              |                       |                       |
+----------------------------------------------+-----------------------+-----------------------+

**Time Series Window**

\[[Site : Water](12_Site_Water.htm) window : any *Time Series* button\]\
\[[Site : Temperature](13_Site_Temperature.htm) window : any *Time
Series* button\]\
\[[Site :
Light](http://www.fullcam.au/FullCAMServer2020/Help/35_Site_Light.htm)
window : any *Time Series* button\]\
\[[Site : Productivity](64_Site_Productivity.htm) window : any *Time
Series* button\]\
\[[Growth Properties](42_Growth%20Properties.htm) window : any *Time
Series* button\]\
\[[Plant Properties](43_Plant%20Properties.htm) window : any *Time
Series* button\]\
\[[Soil Inputs](193_Soil%20Inputs.htm) window : any *Time Series*
button\]\
\[[Crop Yields
Table](http://www.fullcam.au/FullCAMServer2020/Help/113_Crop%20Yields%20Table.htm)
window : any *Time Series* button\]

This window is for entering, editing, viewing, and exporting a time
series.

This topic is displayed when you click the *Window* help icon in any
time series window; when you press the *Data* help icon you open the
topic about that particular time series.

**Time Series Data**

In FullCAM, the data points in a year are assumed to be equally spaced
throughout the year. The exact way in which they are used depends on the
'Timing' and 'Amount of data' settings, as described below.

FullCAM will make the best possible use of the time series data you
enter, regardless of the amount of time series data and the number and
frequency of simulation steps. At the beginning of a simulation, FullCAM
interpolates and extrapolates the given time series into a full time
series, which consists of one data point per simulation step.

**Interpolation**

The interpolation is linear, between the nearest two given data points.

If there is any missing data in a time series FullCAM interpolates the
missing data values based on the average of the corresponding data
values from other years. For each column, the average for each data
column is calculated and used for all missing data values.

**Example 1.** Average value interpolation.

If there is annual rainfall data for 1994 - 1996 and July data is
missing for 1995, then the July 1995 value is calculated as the average
of the July 1994 and 1996 values.

  Year   Jan     Feb   Mar    Apr    May    Jun    Jul    Aug   Sep   Oct    Nov    Dec
  ------ ------- ----- ------ ------ ------ ------ ------ ----- ----- ------ ------ -----
  1994   105.9   2.7   5.9    36.3   14.8   10.9   23.1   6.6   2.5   0.8    19.7   9.5
  1995   1.6     6.1   25.4   6.0    2.6    5.7           1.9   9.2   8.2    0.8    7.6
  1996   0.4     1.0   0.3    28.9   0.3    0.6    0.1    0.3   6.7   10.9   9.2    2.2

The interpolated value for July 1995 is: (23.1 + 0.1) / 2 = 11.6

**Example 2.** Unable to interpolate data values.

If an entire column of values are missing then FullCAM is unable to
interpolate data values \-- the time series window will not be ready to
simulate, and the window button will be red.

*Timing: Start year, Years are*

The year that the time series is to start from. 'Start year' and 'Years
are' together determine the years that the data in the time series table
applies to.

**Example 1.** Calendar time

If 'Start year' is 2006 and 'Years are' is 'Calendar time', then the
time series data will be applied from 2006 onwards.

**Example 2.** Time since start of simulation

If 'Start year' is 2007 and 'Years are' is 'Time since start of
simulation', then the time series data will be applied from *2007 years
after the simulation start time*. It may be more appropriate to instead
set the 'Start Year' to 0.

**Example 3.** Years since plants sprouted

If 'Start year' is 2007 and 'Years are' is 'Years since plants
sprouted', then the time series data will be applied from *2007 years
after the plant event*. It may be more appropriate to instead set the
'Years are' to 0.

It should be noted that if this option is selected, the time series
headings are always entitled 'Data'. This is the case even if there are
12 Data points per year (in which case the column headings would be
months- Jan, Feb, Mar etc.). This is because the column values are
always relative from the plant event.

*Timing \-- Extrapolation*

You choose the extrapolation method (for generating data points outside
the range of given data): either use the data in the nearest year of
given data, or cycle the given data for all time. If you only enter one
year of data, it makes no difference which extrapolation method you use.

**Example 1.** Nearest year extrapolation method.

If you entered rainfall for the three years 1990 to 1992 and chose the
nearest year extrapolation for a simulation that went from 1980 to 2000,
then:

- In each year from 1980 to 1990 inclusive, FullCAM will use the 1990
  rainfall data.
- For 1991 FullCAM will use the 1991 data.
- For each year from 1992 to 2000 inclusive, FullCAM will use the 1992
  rainfall data.

**Example 2.** Nearest year extrapolation method.

If you enter rainfall data for just the one year 1990 and choose the
nearest year extrapolation, then in every year of the simulation FullCAM
will use the 1990 rainfall (even if the simulation is from 1950 to
1972).

**Example 3**. Cyclic extrapolation method.

If you entered rainfall for the three years 1990 to 1992 and choose the
cyclic extrapolation for a simulation that went from 1980 to 2000, then:

1980, 1983, 1986, 1989, 1992, 1995, and 1998 will use the 1992 rainfall
data.\
1981, 1984, 1987, 1990, 1993, 1996, and 1999 will use the 1990 rainfall
data.\
1982, 1985, 1988, 1991, 1994, 1997, and 2000 will use the 1991 rainfall
data.

**Example 4.** Cyclic extrapolation method.

If you enter rainfall data for just the one year 1990 and choose the
cyclic extrapolation, then in every year of the simulation FullCAM
(regardless of when the simulation starts or ends) will use the 1990
rainfall.

**Table**

Unless the time series is a spatial input (see below), the time series
data will be shown as a table of numbers.

Each row of the table has the data for one year. For example, if the
start year is 1962 and the years are calendar years, then the first row
in the table is for 1962, the next row for 1963, and so on.

You can cut, copy, and paste rectangular blocks of numbers from the
table. When pasting more than one number from the table at the same
time, you need only select the upper left cell of the rectangular block
you are pasting into to paste the entire selection.

**Amount of Data**

Change the size of the time series data by entering values in the *Years
of data* and the *Data points per year* boxes. A change will take effect
when the insertion point leaves a box or the *Update Data Siz*e button
is clicked.

If the *Years are* value is set to 'Calendar time' and *Data points per
year* (see below) is a multiple of 12, then data points will apply to
specific months. For example, if there are 12 data points for the year
then the first data point is for January, the next for February, and so
on. Similarly, if there are 24 data points for the year then the first
two data points are for the first and second halves of January, the next
two for February, and so on.

Change the size of the window, and thus the area available to the
visible part of the table, by dragging its lower right corner with the
mouse.

**Multiplier**

The *multiplier* simply multiplies every value in the table when FullCAM
uses the value in a simulation. For example, if the multiplier is 2.0,
then FullCAM will use 2.0 times the values in the table. The default
value of 1.0 (i.e. no multiplier imapct).

As the multiplier is species specific it cannot change over time.

------------------------------------------------------------------------

© 2025 [Department of Industry, Science, Energy and
Resources](http://www.industry.gov.au "Department of Industry, Science, Energy and Resources"),
All Rights Reserved. Do not copy without permission.
[Home](index.htm "help index")
