# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: West Nile Virus

## Introduction

The West Nile Virus (WNV) is a mosquito-borne virus that has become a significant global health concern since its emergence in 1999. Originating in East Africa, WNV quickly spread to North America, resulting in a widespread epidemic. Since then, the virus has continued to expand its geographic range, affecting regions across the world. WNV is primarily transmitted through the bite of infected mosquitoes, with birds serving as the primary reservoir hosts. While the majority of infected individuals exhibit mild or no symptoms, approximately 20% may experience severe manifestations, including neurological complications. The elderly and immunocompromised individuals are at a higher risk of severe illness. Control and prevention efforts focus on mosquito control, surveillance, public education, and research for vaccines and treatments. Continued research and interventions are necessary to minimize the impact of WNV and protect vulnerable populations from this mosquito-borne disease.


## Problem Statement

"To address the prevalence of West Nile Virus (WNV), this study aims to identify and analyze the key factors that significantly influence the presence of WNV. The research seeks to generate proactive and preventive solutions at a societal level to combat the spread of WNV. Additionally, the study aims to develop predictive models to forecast the future hotspots of WNV, with the objective of optimizing anti-mosquito measures and efficiently allocating resources to minimize the risk of WNV transmission."


## Modeling Evaluation

|Model|Train Score|Test Score|AUC Score|
|:---:|:---:|:---:|:---:|
|<font color="blue">Gradient Boost (tuned)</font>|<font color="blue">0.967</font>|<font color="blue">0.931</font>|<font color="blue">0.980</font>|
|Logistic Regression (baseline)|0.690|0.716|0.802|
|Random Forest|0.983|0.892|0.952|
|Ada Boost|0.864|0.890|0.960|

## Cost Benefit Analysis

West Nile Virus incurs a large amount of costs including but not limited to hospitalization costs, long-term medical costs, productivity loss, preventive measure costs and analytics cost. Having a predictive model to predict prevalence of West Nile Virus can optimize cost savings by minimizing costs associated with West Nile Virus infection, as well as costs associated with spraying for mosquito control programs.

## Dataset

For the purpose of the analysis, we are provided with the `train`, `test`, `spray` and `weather` datasets. 

The `train` dataset consists of data from 2007, 2009, 2011 and 2013. We will be using this dataset for model building purposes. The `test` dataset consists of data from 2008, 2010, 2012 and 2014. We will be predicting the mosquito population information using this dataset. 

The `spray` dataset consists of Geographic Information Mapping (GIS) data for the spray efforts in 2011 and 2013. Spraying can reduce the number of mosquitos in the area, and therefore might eliminate the appearance of West Nile virus. 

The `weather` dataset consists of weather conditions of 2007 to 2014, during the months of the tests. It is believed that hot and dry conditions are more favorable for West Nile virus than cold and wet. 

Please refer to data dictionaries below for the full infomation found in the datasets.

---

### Data Dictionary:

Three main datasets were used in this project. The data dictionaries of the datasets can be found below.

<br>**Dataset name: `train`**
<br>This dataset contains data from 2007, 2009, 2011, and 2013.

| Feature | Type | Dataset | Description |
|:--|:-:|:-:|:--|
|date|datetime|train| Date that the WNV test is performed.|
|address|string|train| Approximate address of the location of trap. This is used to send to the GeoCoder. |
|species|string|train| The species of mosquitos.|
|block|integer|train| Block number of address.|
|street|string|train| Street name.|
|trap|string|train| Id of the trap.|
|addressnumberandstreet|string|train| Approximate address returned from GeoCoder.|
|latitude|float|train| Latitude returned from GeoCoder.|
|longitude|float|train| Longitude returned from GeoCoder.|
|addressaccuracy|integer|train| Accuracy returned from GeoCoder.|
|nummosquitos|integer|train| Number of mosquitoes caught in this trap.|
|wnvpresent|integer|train| Whether West Nile Virus was present in these mosquitos. 1 means WNV is present, and 0 means not present.|

<br>**Dataset name: `test`**
<br>This dataset contains data from 2007, 2009, 2011, and 2013.

| Feature | Type | Dataset | Description |
|:--|:-:|:-:|:--|
|id|string|test| The id of the record.|
|date|datetime|test| Date that the WNV test is performed.|
|address|string|test| Approximate address of the location of trap. This is used to send to the GeoCoder. |
|species|string|test| The species of mosquitos.|
|block|integer|test| Block number of address.|
|street|string|test| Street name.|
|trap|string|test| Id of the trap.|
|addressnumberandstreet|*string*|test| Approximate address returned from GeoCoder.|
|latitude|float|test| Latitude returned from GeoCoder.|
|longitude|float|test| Longitude returned from GeoCoder.|
|addressaccuracy|integer|test| Accuracy returned from GeoCoder.|

<br>**Dataset name: `spray`**
<br>This dataset contains the GIS data of spraying efforts in 2011 and 2013.

| Feature | Type | Dataset | Description |
|:--|:-:|:-:|:--|
|date|datetime|spray|The date and time of the spray.|
|time|string|spray|The date and time of the spray.|
|Latitude|string|spray|The Latitude of the spray.|
|Longitude|string|spray|The Longitude of the spray.|


<br>**Dataset name: `weather`**
<br>This dataset contains the weather data from 2007 to 2014.

| Feature | Type | Dataset | Description |
|:--|:-:|:-:|:--|
|station|integer|weather|Station ID.|
|date|datetime|weather|Date of the weather data.|
|tmax|integer|weather|Maximum temperature in Degrees Fahrenheit.|
|tmin|integer|weather|Minimum temperature in Degrees Fahrenheit.|
|tavg|integer|weather|Average temperature in Degrees Fahrenheit.|
|depart|integer|weather|Departure from normal temperature in Degrees Fahrenheit.|
|dewpoint|integer|weather|Average dew point in Degrees Fahrenheit.|
|wetbulb|integer|weather|Average wet bulb in Degrees Fahrenheit.|
|heat|integer|weather|Absolute temperature difference of average temperature (Tavg) from base 65 deg Fahrenheit for Tavg >=65|
|cool|integer|weather|Absolute temperature difference of average temperature (Tavg) from base 65 deg Fahrenheit for Tavg <=65|
|sunrise|string|weather|Sunrise timing in 24H format. (Calculated, not observed)|
|sunset|string|weather|Sunset timing in 24H format. (Calculated, not observed)|
|codesum|string|weather|Significant weather types.|
|depth|integer|weather|Snowfall in inches.|
|water1|integer|weather|Amount of water equivalent from melted snow.|
|snowfall|float|weather|Snowfall in precipitation.|
|preciptotal|float|weather|Water equivalent(Inches & Hundredths(2400 Local Standard Time). Rainfall & melted snow.|
|stnpressure|float|weather|Average station pressure. Inches of HG.|
|sealevel|float|weather|Average sea level pressure. Inches of HG.|
|resultspeed|float|weather|Resultant wind speed. Speed in miles per hour.|
|resultdir|float|weather|Resultant wind direction. To tens of degrees. Whole degrees.|
|avgspeed|float|weather|Average wind speed. Speed in miles per hour.|

---

### Key takeaways from the project:
1. The analysis reveals that years 2007 and 2013 had higher prevalence of West Nile Virus (WNV), as evident from the bar plot. Consequently, the corresponding plots show sharper peaks and declines in WNV activity during these years.


2. Temperature emerges as a significant factor influencing the spread of WNV. Higher temperatures (>60 degrees Fahrenheit) contribute to increased prevalence of WNV and the presence of infected mosquitoes.


3. Lower average and resultant wind speeds (<10 mph) are associated with a higher abundance of mosquitoes and increased prevalence of WNV.

4. Decreased total precipitation (<1.0 inch) is linked to higher prevalence of WNV and a greater number of mosquitoes carrying the virus.

---

### Recommendations
1. Utilize the model as a preliminary tool to determine spray areas. By utilizing weather and trap data collected by the surveillance team, the model can predict the potential presence of WNV. This will assist in identifying hotspots by narrowing down the search area.

2. Target spraying efforts in community areas of Chicago that are densely populated and have a higher predicted probability of WNV, considering that costs are proportional to the sprayed area.

3. Launch educational campaigns to raise public awareness about effective prevention practices. Emphasize the importance of community-government collaboration in combating such viruses.
---

## Future Works

1. The current dataset used for analysis and model development focuses solely on weather features and trap-based data. Including additional data, such as reports on dead birds, which serve as incubators for WNV, could enhance the predictive capabilities of the model.


2. The insights gained from this project can be incorporated into educational materials to educate the general public about the favorable conditions for culex mosquito breeding and the propagation of WNV.


3. While this project primarily focuses on spraying programs, it is worthwhile to explore and research other methods of mosquito control that can complement these efforts.

