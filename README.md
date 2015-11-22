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
> **Step 01**: Write a Python script that takes as input (at the command line) the name of a comma-separated variable (CSV) file containing 2 columns and an arbitrary number of rows. The file in question is linked above. The first column is the predictor variable, and the second column is the response variable. The Python script should read that file and store each column in a separate python array. 

> Hint: see the I/O (input / output) section of the online numpy documentation

> **Step 02**: Use the numpy polyfit function to determine the coefficients of a first, second, and third order polynomial function to the data

> **Step 03**: Create a plot that shows the fit polynomial functions (first, second, and third order) as lines and the original X and y data as points on the same plot

> **Step 04**: Post the produced plot as a reply to your initial discussion board post.

**Solution:**
For this Module, I reused the speedcli for the command-line arguments.  I added a small function to create directories for the default locations if they did not exist.

The Module08 program expects an input from the command-line interface, for example:

```
python Module08_FittingDataToPolynomials.py -i <inputFileName> -o <outputFileName>(optional) -ipath <pathToInputFile>(optional) -opath <pathForOutputFile>(optional)
```

The default output is in .jpg format with the name "RDD_Module08.jpg" and defaults into the output directory (will be created if it is not found).  One can change the output name with the -o argument.  The output path can also be changed with the -opath argument.

----------

### Module 9 ###
> **Step 01**: Create a Python class with the following attributes:

> The constructor takes as input an array x and an array y that contain, respectively, the x- and y-coordinate pairs of each of the vertices. Note that it's a good idea to error trap whether or not x and y are the same length  (they should be, otherwise noting else will work)
Parameters that include the number of vertices, the x- and y-coordinates of the polygon arrays, area, centroid x and y coordinates, and perimeter

> - A SetPolyArea function that takes as input the x and y coordinate arrays and computes the polygon area
- A SetPolyCentroid function that takes as input the x and y coordinate arrays and computes the polygon centroid x and y coordinates
- A SetPolyPerimeter function that takes as input the x and y coordinate arrays and computes the polygon perimeter
- A GetPolyArea function that returns the polygon area
- A GetPolyCentroid function that returns the x- and y- coordinates of the polygon centroid
- A GetPolyPerimeter function that returns the perimeter of the polygon

> **Step 02**: Write another Python script that defines the x and y arrays as defined below and then creates a new MyPolygon class instance called TodaysPoly. The script should then call the GetPolyArea, GetPolyCentroid, and GetPolyPerimeter functions. It should print the labeled area, centroid coordinates, and perimeter values to the screen.

> **Step 03**: Post a screen shot of the script you created successfully running with the values of the area, centroid coordinates, and perimeter written to the screen as a response to your initial discussion forum post.

> ![](http://i.imgur.com/Gg4FhPb.jpg)

**Solution:**
To keep things together from the rest of the semester, instead of making a Polygon class named "MyPolygon", I created a "Polygon" subclass that is under the class SpeedCalc within the speedcalc module.

I added the test vertices to the project as a .csv file within the data folder.  The project is designed to be able to load a csv with the vertices of a polygon from the command line, using the format:

```
python Module09_PolygonClass.py -i <inputFileName> -ipath <pathToInputFile>(optional)
```
Note that the vertices should be in order (clockwise or counterclockwise).  Absolute values have been added to the area and the centroid calculations so that there will not be negative values (intended for first quadrant (positive) vertices).

Tests were made for the calculations of the polygon area, centroid and perimeter.

All polygon validations and calculations are done upon instantiation of the Polygon class object and the information is returned by using the get functions.

----------

### Module 10 ###
> **Step 01**: Write the Python script to create an ensemble of random walkers with the following characteristics:

> Number of random walkers = 100
Number of steps = 500
Beginning position, x0 = 0
Average step size = 1
Standard deviation in step size = 2.5
Hint: Use numpy arrays to store the position of the jth random walker at the ith step at the ith row and jth column of a 2-dimensional array.
 
> **Step 02**: Create a plot of the trajectory of every random walker during every step of the random walk process. Post that plot as a response to your initial discussion board post for this module. Note: Extra credit will be given to those who figure out how to compute and plot the average location of all random walkers at every step in the random walk process (hint: look at the [numpy mean function](http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)).

**Solution:**
For the implementation of this module, I chose to create a new RandomWalker subclass to go into the speedcalc module.  Since it was unclear at the outset whether this was supposed to be a 1-dimensional implementation or 2-dimensional implementation, I chose to make it possible to do either based on the given parameters [Update: it was made clear that it is supposed to be a 1D implementation, but I utilized the 2D implementation from the book to get a better sense of what I am doing for the 1D].

For the parameters, a simple argument list implementation was used instead of argparsing, so order matters.  The format of arguments required is (listed on multiple lines for readability, but should be entered sequentially):

```
Module10_RandomWalk.py <number of random walkers> 
	<number of steps> 
	<average step size>(optional; defaults at 1) 
	<standard deviation in step size>(optional; defaults at 2.5) 
	<beginning position>(optional; defaults at 0)
	<number of dimensions>(optional; defaults to 1)
```

An example using the given problem set for the Module would look like:

```
Module10_RandomWalk.py 100 500
```
I wasn't sure if I could vectorize my code any further, but I decided to just get it to work.  I struggled more than usual with this particular module.  It takes me a bit to get thinking in terms of matrices and vectors.

I didn't do as many bells and whistles in this particular module as I usually do due to time constraints, but it seems to work as intended.

----------

### Module 11 ###
>**Step 01**: Based on the discrete formulation for computing PWS that you developed and posted on the discussion board, write a Python code that:

>Takes as input at the command line the name of a comma-separated text file containing the hourly measured soil moisture values from April 1 at 12am to April 30 at 11pm. The file (linked below) contains a single column and each row is a successive hour of observation. Soil moisture values are in volumetric units, i.e., m3/m3.
Reads the soil moisture values into a numpy array, and
Uses the trapezoidal rule as outlined in section A.1.7 of the text to compute the cumulative PWS during the course of the month. Note, use a value of θ* = 0.17

>**Step 02**: Run the code with for the two years of data provided above. Post a screenshot of your successfully running code and the output of your code as a reply to your initial discussion board post. I would suggest that you organize the output in a simple table in BlackBoard, for example:

>|Year|Value of Plant Water Stress|
|---|---|
|2007|PWS goes here|
|2011|PWS goes here|

**Solution:**
First I utilized a slightly modified version of the CSV import that I used in Modules 5, 6, and 7 to import the csv for each year.  I then ran the soil moisture numbers through a loop to calculate the Plant Water Stress at each hour using the trapezoidal rule formula:

PWS = sum from k=0 to n-1 of 1/2(t at k+1 - t at k) * [(theta(at t k) - theta-star) + (theta(at t at k+1) - theta-star)]

- PWS = Plant Water Stress
- theta(at time k) = soil moisture at each hour (k)
- theta(at time k + 1) = soil moisture at each next hour from k
- n = number of trapezoids
- k = trapezoid number/iteration number
- t at k = time (hour) at given iteration number
- t at k+1 = time(hour at given next iteration number

I wanted to use as much numpy as possible to see how fast I could make it with limited vector experience.  To that end, I chose to use iterators to get some experience with Python iterators, specifically nditer.  They are far less intuitive than Java iterators, but I managed to work through the issues and figure them out. 

----------

### Module 12 ###
>**Step 01**: Based on the centered finite difference approximation for computing PWS2(t) that you developed and posted on the discussion board, write a Python code that:

>- Takes as input at the command line the name of a comma-separated text file containing the hourly measured soil moisture values from April 1 at 12am to April 30 at 11pm. The file (linked above) contains two columns, the date and time in the first and soil moisture in the second. Soil moisture values are in volumetric units, i.e., m3/m3.
- Reads the soil moisture values into a numpy array, and
- Computes the time series of PWS2(t). Note that since you are using a centered-difference approximation, the output time series will have two fewer numbers that the original time series of soil moisture. 
- Creates a labeled plot of PWS2(t)

>**Step 02**: Run the code with for the two years of data provided above. Post the clearly labeled plot of the time series of PWS2(t) for both years (on the same plot) as a reply to your initial discussion board post.

**Solution:**
The requirements called for the loading of two files at once.  For simplicity, I added a -i2 for my argparser.  Ideally, I would make it so I could input a comma-delimited string and load all files in the string; but that's for another day.

I added the PWS2 calculation to speedcalc and created a basic plot for it.  I labeled the axes and added a legend.

There were aspects of this particular module that I would have liked to have done differently or more completely, but ended up just meeting the requirements due to time constraints.

----------

### Module 13 ###
>In preparation for this programming activity, you developed a finite difference solution to the classic Lotka-Volterra model.

>Now you will go about implementing that finite difference solution, running the Lotka-Volterra model for given parameter values, and presenting the results, which was given as follows:

>![](http://i.imgur.com/cz5AxNN.jpg)

>**Step 01**: Proceed to develop a Python script that implements your finite difference solution to the Lotka-Volterra equations for predator-prey interaction. The script should:

>- Allow you to easily define and change the values of the parameters α, β, γ, and δ; different values of the initial conditions N1 and N2; and different numbers of time steps NT.
>- Plot and clearly label the simulated predator and prey density over the simulation time

>**Step 02**: Proceed to run the model for NT = 200 (i.e., 200 time steps), with the following parameter values and initial conditions:

>- α = 0.1
- β = 0.02
- γ = 0.4
- δ = 0.02
- Initial value of N1 = 10
- Initial value of N2 = 10

>**Step 03**: Post the plot of this simulation as a reply to your initial discussion board post for this module. Also post a bulleted list of 3 observations about the interaction between predator and prey in the simulation.

>**Step 04 (Optional)**: Also run the model for different parameter values and initial conditions than those above (you choose). Post the figure for this simulation beneath the figure and observations for the model run described in **Step 02**.

**Solution:**

----------
### Module 14 ###
>In this programming activity you will replicate the spatial autocorrelation analysis of Zhang et al. (2009) using Moran's I, but for an NDVI image from southwest Idaho. Below you will find a link to the NDVI dataset you will be analyzing (available soon).  

>**Step 01**: Use a combination of numpy and PySAL to compute the value of Moran's I at lag distances ranging from 1 pixel (30 m) to 10 pixels (300 m)

>**Step 02**: Your code should create a plot of Moran's I as a function of lag distance from 0 to 300 m.

>**Step 03**: Post the plot of Moran's I as a function of lag distance as a response to your original discussion board post.

**Solution:**