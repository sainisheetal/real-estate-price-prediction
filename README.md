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

!) Data Cleaning: performed all the task to clean the data to analysie
2) Data Analysing: Done as per the details defined and checked all the variables
3) Data Interpretation: worked on questions and plot 
_______________________________________________________________________________________________

Part III: Machine Learning Model

Used more data to predict the price for houses. As i was not getting the required result on my previous data. So I have started my project with cleaning the data:

Step 1: Data cleaning and preprocessing:
To ensure that my data will predict good model and give good acurracy. I have done cleaning and 
created some more column based upon region to narrow down my result.

Step 2: Model selection and training:
After analysing the data I have divided the dataset for training and testing.
I have done testing some of Model to select the best one.

Step 3: Model evaluation:
We have achieved maximum accuracy of 81% with my model, by testing different models and making adjustments to the preprocessed data and features. 

Usage: It is necessary to repeat steps 1-3 multiple times in order to achieve an optimal accuracy outcome. However, our majority of the time will be spent on preprocessing the data.
