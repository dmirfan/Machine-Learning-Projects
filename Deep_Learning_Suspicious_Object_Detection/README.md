# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone: Suspicious Object Detection on Train Cabins and Public Spaces

## Background

Singapore's urban landscape is characterized by its high-density environment, necessitating the development and maintenance of robust public transportation systems, particularly the Mass Rapid Transit (MRT) system. Serving millions of residents and visitors each day, the MRT system is the lifeblood of Singapore's transit infrastructure. However, the same density and dependence make it susceptible to various safety and security concerns, including the potential for crime, loss of personal items, and issues related to cleanliness.

The current security measures in place largely involve traditional video-based surveillance in train cabins and other public spaces. While these systems have served as a deterrent and means of post-incident investigation, their efficiency is limited when it comes to real-time detection and tracking of suspicious objects. Manual monitoring of surveillance footage is labor-intensive and prone to human errors, such as oversight or misinterpretation. Moreover, the existing systems are inadequate in providing real-time alerts, which are critical in situations requiring immediate attention.

Beyond security, Singapore, with its reputation for cleanliness and order, also faces challenges related to waste management and lost items in public spaces. An effective object detection system could assist in these areas, contributing to the city's overall cleanliness and helping in the retrieval of lost items. 

The limitations of the existing surveillance methods highlight a crucial gap in Singapore's safety and security measures, particularly in the MRT system. They underscore the need for a more advanced, intelligent, and autonomous system capable of detecting, classifying, and tracking objects, particularly those that are suspicious, in real-time. This new system should not only enhance accuracy and reliability but also address privacy concerns that come with increased surveillance. The development and implementation of such a system can significantly contribute to the enhancement of security, overall safety, and orderliness in Singapore's public spaces.


## Problem Statement

In the densely populated city-state of Singapore, where the Mass Rapid Transit (MRT) system is a primary mode of transportation, the critical importance of public safety and security cannot be overstated. The current surveillance methods, primarily conventional video-based monitoring in train cabins and other public spaces, have proved to be less efficient in real-time object detection and tracking, especially for suspicious objects that could pose significant risks and security threats. This limitation is particularly concerning in high-density spaces like train cabins, where quick identification and resolution of such threats are crucial. Moreover, given Singapore's emphasis on public cleanliness and order, an effective object detection system can also contribute to better waste management and retrieval of lost items. The existing surveillance systems suffer from labor-intensive and error-prone manual monitoring, lack of real-time alerts, and absence of advanced features like object classification. Therefore, there is a pressing need for an intelligent, autonomous object detection surveillance system capable of detecting, classifying, and tracking objects, including suspicious ones, in real-time. The successful development and implementation of such a system, while ensuring high accuracy, reliability, and addressing privacy concerns, could significantly enhance the security and overall safety in Singapore's public spaces.


## Modeling Score

|Model|mAP|Precision|Recall|
|:---:|:---:|:---:|:---:|
|<font color="blue">Best Model (tuned)</font>|<font color="blue">0.940</font>|<font color="blue">0.927</font>|<font color="blue">0.904</font>|
|Baseline Model|0.721|0.702|0.688|


## Model Evaluation

<img src="/image/model_eval1.jpeg" width="800" height="600">
<img src="/image/model_eval2.jpeg" width="800" height="600">
<img src="/image/model_eval3.jpeg" width="800" height="600">


## Dataset

For the purpose of the analysis, I have captured images on train cabins, caps , sunglasses and mask. 

The train cabin images dataset consists of data from 2023. I will be using this dataset for model building purposes. We will be using the train cabin setting to have a better accuracy on suspicious objects in the cabins itself. 

The cap images dataset consists of different type and colours of caps that will be used to identify caps in an image which will be classified as suspicious objects. Cap identification is one of the top suspicious object for a person to be wearing and it helps to improve the True Positives. 

The sunglasses images dataset consists of different type and colours of caps that will be used to identify caps in an image which will be classified as suspicious objects. Cap identification is one of the top suspicious object for a person to be wearing and it helps to improve the True Positives. 

The mask images dataset consists of weather conditions of 2007 to 2014, during the months of the tests. It is believed that hot and dry conditions are more favorable for West Nile virus than cold and wet. 

Please refer to data dictionaries below for the full infomation found in the datasets.

---
## Images with annotations using Roboflow

The below images are some of the samples of the datasets used.
<img src="/annot1.jpeg" width="800" height="600">
<img src="/image/annot2.jpeg" width="800" height="600">
<img src="/image/annot3.jpeg" width="800" height="600">

---

### Data Dictionary:

Three main datasets were used in this project. The data dictionaries of the datasets can be found below.

<br>**Dataset classifier: `suspicious-objects`**


| Feature | Type | Dataset | Description |
|:--|:-:|:-:|:--|
|etection|object|cap| Series of cap images to be used to train the model|
|detection|object|sunglass| Series of sunglass images to be used to train the model|
|detection|object|mask| Series of mask images to be used to train the model|
|context|environment|train cabins| Series of train cabin images that may contain any of the above suspicious objects to be used to train the model|

---
## Detection Images

<img src="/image/detect1.jpeg" width="800" height="600">
<img src="/image/detect2.jpeg" width="800" height="600">
<img src="/image/detec1.jpeg" width="800" height="600">

---

### Deployment:

I have deployed and integrate the model on to my personal domain page. On my own iniative I bought the domain page and hosting altogether before configuring the SSL certificate into the site. The SSL certificate is required to facilitate the ease of use for the live webcam application. Besides, the web application, the static application can be used to infer suspicious images to test out the model I have created with YOLOv8. Please find the link below.

https://dmirfan.online

<img src="/image/webpage1.jpeg" width="800" height="600">
<img src="/image/webpage2.jpeg" width="800" height="600">
<img src="/image/webpage3.jpeg" width="800" height="600">


---

### Key takeaways from the project:
1. The analysis reveals that years 2007 and 2013 had higher prevalence of West Nile Virus (WNV), as evident from the bar plot. Consequently, the corresponding plots show sharper peaks and declines in WNV activity during these years.


2. Temperature emerges as a significant factor influencing the spread of WNV. Higher temperatures (>60 degrees Fahrenheit) contribute to increased prevalence of WNV and the presence of infected mosquitoes.


3. Lower average and resultant wind speeds (<10 mph) are associated with a higher abundance of mosquitoes and increased prevalence of WNV.

4. Decreased total precipitation (<1.0 inch) is linked to higher prevalence of WNV and a greater number of mosquitoes carrying the virus.

---

### Recommendations
1. Implement in Train Cabins and Platforms

The first and most logical place to implement suspicious object detection would be within the train cabins and platforms of the Mass Rapid Transit (MRT) system. These areas see a significant flow of passengers every day, making them potential targets for security threats. By integrating the system within these high-traffic areas, it can help identify and alert the authorities of any suspicious objects in real-time, thus mitigating potential risks. 

2. High-Density Public Spaces

High-density public spaces such as shopping centers, parks, and tourist attractions should also be prioritized. These are places where large numbers of people gather, increasing the potential risk. Additionally, due to the sheer number of objects and activities in these areas, manual surveillance can be challenging, making the need for an intelligent detection system even more crucial.

3. Transportation Hubs 

Transportation hubs, including bus terminals, MRT interchanges, and airports, should also be considered. These places are not only high traffic but also serve as critical infrastructure. Implementing a suspicious object detection system in these areas can enhance overall security and create a safer environment for both travelers and staff.

In each case, the surveillance cameras should be positioned strategically to cover the maximum area and reduce blind spots. The aim is to ensure a comprehensive view of the surroundings, providing the AI system with the necessary data to identify and track suspicious objects effectively.
---

## Future Works

1. Increase in Object Diversity Recognition

While the current generation of object detection systems is promising, there's scope for further enhancement, particularly in recognizing a more diverse range of objects. Future systems could be trained to identify not only larger items like luggage or parcels but also smaller or less common objects that could be suspicious. Such advancements would require extensive machine learning training with diverse datasets and continuous updating of the system as new object types are introduced.

2. Detecting and Interpreting Body Language

The addition of body language interpretation to object detection systems could significantly improve their efficacy. For instance, detecting unusual or suspicious behavior in individuals carrying or leaving behind objects can be an additional layer of security. Training AI models to analyze body language would involve complex machine learning and require extensive, diverse datasets of human behaviors. Ethical considerations, such as privacy and the risk of bias, would also need to be carefully managed.

3. Enhancing Performance in Crowded Spaces

Detecting suspicious objects or activities in crowded spaces is a significant challenge due to the number of objects and individuals present. Future work could focus on improving the systems' ability to function effectively in such environments. Techniques such as crowd segmentation, which involves separating individual members of a crowd for analysis, and multi-object tracking, could be further developed. These advancements will require sophisticated algorithm development and extensive testing to ensure accuracy and reliability.

### Profiles:

LinkedIn -https://www.linkedin.com/in/dmirfan/
