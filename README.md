Scientific Programming for Earth and Ecological Discovery (SPEED)
=================================================================

This code was created specifically for the purposes of the SPEED class, run by [Alejandro Flores at Boise State University](https://earth.boisestate.edu/people/alejandro-n-flores/ "Lejo Flores").  As a result, the code is geared towards specific assignments and was written for the purpose of learning [in short, it was practice for me].  

It is likely there are better approaches to solving specific problems and even more likely that there are libraries already out there that solve the given problems in a superior manner.  That being said, the code can be useful to someone that is just learning to program to familiarize themselves with the way things function and hopefully offers a demonstration of quality code.

## Organization ##
The projects were divided up into Modules.  I tried to abstract away, from the Module requirements themselves, code that could be reused.  I put this code into their own modules.  The actual assignment code can be found in the modules titled Mod02-Mod14.

## Documentation ##
In an effort to practice using Python's Docstrings and a Javadoc-like program (in this case, [Epydocs](http://epydoc.sourceforge.net/ "Epydocs")), I have provided generated documentation of my various classes and methods.  It may lag behind the actual code sometimes, but I try to keep it relatively up-to-date.

## Code Style ##
While I value [coding standards](http://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting "Useful Guideline for Python Style") and [I try to hold to PEP8](https://www.python.org/dev/peps/pep-0008/ "Python PEP8 Standards") as much as possible, I do deviate from PEP8, particularly in the naming of classes and functions and arguments passed into them.  

I have my own naming style [more Java/C#-based] that I have developed over time and adhere to and it mostly involves CamelCase [I really think a bunch of underscores looks ugly].  I try to remain consistent and make things readable, regardless of what I choose to do. 

## Modules ##
I shall be adding to this document throughout the semester [end of 2015] to document the goals of each Module and what to look for if you download and run it.

----------

### Module 2 ###
**Requirements:**
>In this programming assignment you will create a "Hello, world!" Python program or script.  This script will print "Hello, world!" along with a brief introduction to your screen

>Use the editor pane to write your own "Hello, World!" script.  This script should print "Hello, World!" on one line and introduce you, including your name and one characteristic, on the second line.

>**Optional**:  Assign your name and the specific characteristic as variables in the script and print the variables instead of writing out your name in the print statement and/or explore some options for formatting the text printed to your screen.

**Solution:**
I created a small "Hello World!" script that meets the requirements as well as the optional requirements.  I chose to demonstrate the print function for Python 3.x as well as the way to suppress a newline.  I provided the code to do the same thing in Python 2.x in the comments below that. 

----------

### Module 3 ###
**Requirements:**
>In your first scientific programming exercise you will develop a  program to convert an input latent heat flux (i.e., evaporation of water in units of power per unit area of earth surface) to units of equivalent depth (i.e., volume of water evaporated per unit area of earth surface, per unit time). You will develop a code that takes as input evaporation as an energy flux in units of W/m2, and convert it to evaporation as a mass flux in units of mm/day.

**Solution:**
For this Module, I chose to make two conversion methods within an ET class (subclass of SpeedCalc), one for mass flux to amount of water evaporated and one for energy flux to amount of water evaporated.  These calculate the result from variables that are passed to them from the Mod03 module.

Tests were written for the methods within the ET class to ensure proper calculation, as will be the case for all future calculation methods.

----------

### Module 4 ###
**Requirements:**
>In the Programming Activity for this module, you will be computing the saturated vapor pressure for a wide range of air temperatures and printing the pairs of temperatures and saturation vapor pressures to the screen. The saturation vapor pressure is the partial pressure of water vapor in air when that air is at 100% relative humidity (i.e., saturated). It is used ubiquitously in ecology and hydrology when we need to calculate or model the rate of evaporation or transpiration. The equation for computing the saturation vapor pressure is the well known Clausius-Clapeyron equation and it is a function of temperature only. We will introduce the Clausius-Clapeyron equation in a subsequent activity. For now, it suffices to know that it is just one equation that is a function of temperature.

>Write a Python script to perform the calculation of saturation vapor pressure for values ranging from and air temperature of T = -15 °C to T = 35 °C in increments of 0.01 °C. For each value of temperature, the code should write out the temperature and value of saturation vapor pressure. The print statement should be something like "T = 20 deg. C, esat = 3.169 kPa."

**Solution:**
For this Module, I created a Pressure class (as a subclass of SpeedCalc) and created a vaporPressure_fromTemperature() method for it.  I used the Clausius-Clapeyron equation to design the method and made parameters not only for temperature, but for the water phase as well [liquid/ice; defaults to liquid] so that one could run the calculation for either phase.  The method defaults in Pascals, but can also currently be calculated in hPa and kPa if desired.

I also wanted to be able to see my results in more than a  console print out, so I incorporated matplotlib and created a plot of the values.

As a result of wanting more control over my result values and the number of decimals displayed, I included a constructor control for each subclass within SpeedCalc to determine the maximum number of (rounded) decimals that one wants to see their result values in.

----------

### Module 5 ###
**Requirements:**
>Write a Python code that has the following three functions defined in it:

>getSatVaporPressure → Inputs: temperature

>getVaporPressure → Inputs: temperature, relative humidity; should call getSatVaporPressure

>getVPD → Inputs: temperature, relative humidity; should call getVaporPressureAND getSatVaporPressure

>Compute values of VPD for a 24 hour period at a meteorological station in the Dry Creek Experimental Watershed by using a for loop and making the appropriate call to the getVPD function

**Solution:**
For this Module, I decided to build out some tools.  I divided the Module up into three parts:

1.  *Data Loading*: Since it is likely we will be processing more data from the Dry Creek Experimental Watershed, I wanted to develop a tool that would allow me to parse the data from (potentially) any csv file from the website [http://earth.boisestate.edu/drycreek/](http://earth.boisestate.edu/drycreek/ "Dry Creek Experimental Watershed Link").  It was assumed that they are standardized csv files with a standard header length; that appeared to remain true through the few files I downloaded.  
To this end, the speedloader.py module was created, which has the intent of using both GUI and/or command line tools to pull data into a module.

2. *Processing Data and Calculations*:  The next part involved extending features within the speedcalc module to support the calculations necessary for Vapor Pressure Deficit.  Additionally, there was a need to filter the processed data by a given date, so those features were added as well into the main() portion of Mod05.

3. *Data output and display*: For this module, I chose to delve into the GUI world a bit since I haven't done it in Python.  I chose to use the Tkinter Module.  It's not really all that flashy and not the easiest to use, but it gets the job done.  I intend to add command line tools as well since lately I prefer more scriptable options, but for now, it is just GUI-driven.  The final output is written to a textbox instead of the regular interpreter command line.

Similar to my time investment into the first Module to organize and build up tools, this took a lot of time.  I am hoping to be able to reuse the efforts put forth here in future modules.  

----------

### Module 6 ###
**Requirements:**
>**Step 01**: Modify the Python script you submitted in Module 05.05 so that: (1) the script takes as command line input the name of a text file, and (2) reads that text file and computes VPD, printing the output to the screen using the "print" function. Assume that the text file is formatted as a comma-separated variable (CSV) file. The first column is the air temperature (in °C) and the second column contains the relative humidity (in %). The rows of the CSV file represent successive hours of observation. The test CSV file to use is linked below.

>**Step 02**: Verify that your code works by posting a screen shot of the code being called with the text file as input and successfully executing and printing output to the screen as a reply to your initial post.

**Solution:**
Since I unwittingly did most of this Module already, I used this Module as an opportunity to flesh out some of the command line tools that I desired to finish in the previous Module.  

If the program is run without arguments, it will initiate the GUI.  Otherwise, it takes arguments in the following format:

-i <filename> -ipath <file path>(optional) -d <specific date in mm/dd/yyyy>(optional) -o <outputfile>(optional -- not yet implemented) -opath <output file path>(optional -- not yet implemented)  

A "Show All" option was added that allows one to view calculations for an entire file instead of just a single day.

To account for when there is a -6999 for no data, I added logic to print out "No Data" for the VPD when -6999 is encountered in the data and print out "No Data" for whichever element is missing.

Formatting was updated to be more uniform.  Formatting was created specifically for the CLI.

----------

### Module 7 ###
**Requirements:**
>In this activity we will continue to expand the Python code that you started in Programming Activity 05.05 and expanded in Programming Activity 06.05. In this Programming Activity you will save the functions that you created in Programming Activity 05.05 as a Python module, which you will then call from a script that reads as input the name of a comma-separated variable (CSV) formatted text file from the command line. The script will then call the functions from inside your module and compute the hourly vapor pressure deficit (VPD) based on the hourly values of air temperature (in °C) and relative humidity (in %) read from the text file. 

>**Step 01**: Take the Python functions you coded for Programming Activity 05.05 and move them into a file as a Python module.

>**Step 02**: Write another Python script that takes as input at the command line the name of a CSV file containing hourly values of air temperature and relative humidity. Assume that the first column of the file in the CSV file is air temperature data (in °C) and the second column contains relative humidity data (in %). The rows of the CSV file, again, represent successive hours of observation. Your script should read in the hourly observations of air temperature and relative humidity, and use the functions in your Python module to compute the corresponding hourly vapor pressure deficit and writing it to the screen using the "print" Python function. The CSV file is provided below.

>**Step 03**: Post a screen shot of the script being called and the code successfully executing (i.e., the printout of the hourly values of VPD). 

**Solution:**
As with Module 6, the requirements for this module were really achieved in what I did in Module 5.

----------

### Module 8 ###
banana banana banana

----------

### Module 9 ###
banana banana banana

----------

### Module 10 ###
banana banana banana

----------

### Module 11 ###
banana banana banana

----------

### Module 12 ###
banana banana banana

----------

### Module 13 ###
banana banana banana
