# XFoil BEM Tool
Python script to quickly extract Re vs. AoA, Cl, and Cd for any given airfoil geometry using XFoil. Made for Blade Element Momentum (BEM) applications with computational fluid dynamics software.

### About
The cycling industry has long relied on expensive wind tunnel testing when designing new aerodynamic products. However, with the recent advent of computational fluid dynamics (CFD), the industry now has an economical tool that supplements this iterative design process. While current CFD methods can reliably simulate static bicycle components, the complex aerodynamics of rotating, spoked wheels make them particularly difficult to efficiently simulate as they consume valuable computational time. My research project investigates a new CFD method that can accurately model a bicycle wheel at a lower computational cost. 

XFoil BEM Tool was specifically made for my research project. While this was its specific application, this script can be useful in any context involving BEM and CFD. It is particularly good with Star-CCM+.

### Requirements
- [XFoil 6.99](https://web.mit.edu/drela/Public/web/xfoil/)
- [Python 3.8.5](https://www.python.org/downloads/)
- [Spyder IDE (preffered)](https://www.spyder-ide.org/)  

### What's in the box
- Installation guide
- Python script
- Example  

## Installation

**1. XFoil**   
Download the latest version of XFoil (I used 6.99). Place the executable as close to your main drive as possible.
```
C/XFoil/xfoil.exe
```  

**2. Python**  
Install with standard settings being sure to add to environment PATH.  

**3. Spyder**  
Install with standard settings.  

**4. XFoil BEM Tool**   
Download xfoil_bem_tool.py and place it in your XFoil directory.
```
C/XFoil/xfoil_bem_tool.py
```  

## Running the script
Open xfoil_bem_tool.py in Spyder and configure your desired parameters.
<img src="https://github.com/drewvigne/xfoil_bem_tool/blob/master/images/parameters.PNG" height="300">
 - re_strt is the starting Reynolds number
 - re_end is the ending Reynolds number
 - XFoil will iterate between this range of Reynolds numbers for your desired step size, re_step
 - alfa_strt, alfa_end, and alfa_step work on the same principle for angle of attacks  
 
For custom airfoils place the .dat file in the same directory as XFoil and XFoil BEM Tool. Instead of typing None type your foil file name 'example.dat'.  

Click the play button. XFoil will run every Reynolds number and for every angle of attack.

## Interpreting data
XFoil will dump save files for every Reynolds number tested called '#_SAVE". In each file the angle of attacks are stored with corresponding Cl and Cd data.  

XFoil BEM Tool automatically sweeps these files and dumps another file called "outfile.csv". This is the main output file containing Re vs. AoA, Cl, and Cd. Use this for your BEM applications with your compatible CFD software. 

<img src="https://github.com/drewvigne/xfoil_bem_tool/blob/master/images/output.PNG" height="300">

When using virtual disks with Star-CCM+'s BEM solver, you are asked to load a CSV file containing this exact data. Simply load this csv file into your CFD software and you should be good to go. BEM computations use this 2D airfoil data to approximate 3D fluid scales, forces, and moments. 

## Acknowledgments
Thank you to this script's co-author, George Loubimov, who accelerated my learning of Python.

## To do
- Clean up code
- Add non-convergence sensing
- Reconfigure using DataFrame and pandas
