# assignment07_sophia

This repository is intended to capture the work I did for the broadband project as of April 6th 2022. For this assignment I wanted to try and visualize the layers in a way that made sense to me, as a starting point. I also wanted to test out folium and a protoype website.

# Explanation of the folders

The folder <code>/folium_test</code> simply contains a test of folium. It can be ignored for the purposes of this assingment.  

The folder <code>/folium_outputs</code> contains the HTML outputs of the functions that plot the data layers over a folium map. 

The folder <code>/docs</code> contains the test HTML website that uses the folium maps.

# Explanation of the python files
All of these files do roughly the same thing. They all contain code that:
1. Reads in json data
2. Makes a geojson data frame
3. Plots the information, generating a simple matplotlib object
4. Plots the information, generating a folium map
The folium map also has a function that allows the user to turn off and on the layers.
I chose to break up the data files into 4 parts: Tier data (<code>broadband_tier.py</code>), grant data(<code>broadband_grant.py</code>), may be underserved data(<code>broadband_may_under.py</code>), and underserved data (<code>broadband_underserved.py</code>). I am not sure that this is the best approach, but I think it makes sense to visualize some of these layers together. 

#Running the code
From the command line:
```
python broadband_tier.py
```
The code will first generate a matplotlib object. Once you are done viewing it, please close it and the code will generate the folium HTML file.
The same steps can be done for 
```
python broadband_grant.py
python broadband_may_under.py
python broadband_underserved.py
```
#Outputs:
Simple plots:
Tier 0-5
![Teir1](iris.png)
![Teir2](iris.png)
Teir 0-1

Grant
May be underserved
Underserved
![Iris](iris.png)

#Issues
There seems to be a problem with large json layers and folium. For the code <code>broadband_underserved.py</code> and <code>broadband_may_under.py</code>, the folium part is commented out becuase it doesn't quite work. It should work in the same way as the grant and teir code, but I suspect that the layers are just too large
  
   
