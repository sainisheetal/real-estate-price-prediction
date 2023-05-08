![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) ![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)  ![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)

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

Question:

1) Comparing which type of property is expensive as per provinces ?![question1](https://user-images.githubusercontent.com/120012675/215512301-b5d1a580-ec2b-4bde-a4d3-5baff71cae89.png)


2) does living area impact the price of the property type?
![question2](https://user-images.githubusercontent.com/120012675/215512336-46c35574-c369-4140-b45d-27760c92993c.png)

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
I have achieved maximum accuracy of 81% with my model, by testing different models and making adjustments to the preprocessed data and features. 
![random forest](https://user-images.githubusercontent.com/120012675/215513072-53b217f5-e4d7-4406-9731-df938675bbe1.png)

Usage: It is necessary to repeat steps 1-3 multiple times in order to achieve an optimal accuracy outcome. However, our majority of the time will be spent on preprocessing the data.
_______________________________________________________________________________________________
Part VI: Deployment:

