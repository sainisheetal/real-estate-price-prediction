# real-estate-price-prediction
`06/01/2023 04:00 PM`
Description
The goal of this project was to collect information from the immoweb website. We had to gather information about at least 10,000 properties all over Belgium and create a CSV file with the following columns.

Locality
Type of property (House/apartment)
Subtype of property (Bungalow, Chalet, Mansion, ...)
Price
Type of sale (Exclusion of life sales)
Number of rooms
Living Area
Fully equipped kitchen (Yes/No)
Furnished (Yes/No)
Open fire (Yes/No)
Terrace (Yes/No) -If yes: Area
Garden (Yes/No) -If yes: Area
Surface of the land (is none for each line, the information is given in the line : Surface area of the plot of land)
Surface area of the plot of land
Number of facades
Swimming pool (Yes/No)
State of the building (New, to be renovated, ...)
The dataset had to be clean in the sense of recording only numerical values.

_________________________________________________________________________________
PART I: Collecting data:
Program consists of three different parts.
1) The first part of the program is responsible for gathering all the necessary links that will be used for data collection. 
2) The second part of the program uses the collected links to scrape information from those webpages and cleaned the data that has been collected. 
3) The third part save all data in csv. All csv files are stored with the name "date & time"
__________________________________________________________________________________
PART II: Analysing data:
Dataset Details: 
1) Building condition: True if building in Good, New, Just renovated.
2] Kitchen Type: True if kitchen equipped(no matter what type)
3) Furnished: Trues if 'Yes'
4) Swimming pool: True if 'Yes'
5) Garden: True if 'Yes' or given the area
6) Terrace: True if 'Yes' or given the area
