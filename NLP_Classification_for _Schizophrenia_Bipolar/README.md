# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP

### Project Objectives:
 We are tasked in creating a classification model using NLP based on two subredits, r/bipolar and r/schizophrenia. This model will predict if a post identifies as schizophrenia or bipolar.



## The Modeling Process
1. We are geting raw data from webscraping.
2. The columns consists of title and the text which what we need
3. Generate classification model using from the raw data. This process consists of:
    - Data Cleaning
    - Tokenizing
    - Lemmatizing
    - EDA 
    - Data Visualization (Horizontal Bar chart & WordCloud)
    - Train-test split
    - Vectorizing
    - Grid Search
    - Logistic Regression Model
    - Naive-Bayes Classification Model

3. Predict the values for your target column in the test dataset 
    -  Use of train-test split, vectorize and test data with unknown values for the target to simulate the modeling process

4. Evaluate models!
    - evaluation metrics
    - baseline model/score
    - model inferential
    - confusion matrix

---

### Data used:
This Dataset is an exceptionally detailed with over 4 columns of different words relating to schizophrenia and bipolar.

For the purpose of the analysis, we webscrape our datasets from two subreddits. The  dataset contains 3000 schizophrenia and bipolar posts with text. These raw data will undergo preprocessiong steps before train-test-split. Classification for bipolar and schizophrenia will be predicted using the trained classification model.

Information found in the raw datasets includes information suchs as the title, text.
The full information could be found in the data dictionary below.


---

### Data Dictionary:

<br>**Dataset name: combined.csv**
<br>This dataset contains text data of webscrapes from two subredits post, r/schizophrenia and r/bipolar . 



| Column | Description                                | Data Type             | Example                                          |
|--------|--------------------------------------------|-----------------------|--------------------------------------------------|
| Id     | A unique identifier for each record         | Numeric or alphanumeric | 1, 2, 3, a, b, ...                                     |
| Title  | The title or headline of the text           | Text or string         | "Breaking News: New Discovery in Science"        |
| Text   | The main body of the text or article        | Text or string         | "Scientists have recently made a groundbreaking discovery..." |
| Score  | A numerical score or rating associated      | Numeric (integer or floating-point) | 8.5, 9, 6.2, ...            |
| Label  | A labelling of 0,1 should it be schizophrenia or bipolar | Numeric (interger) | 0,1 |

In the Markdown table above, each column represents a different attribute of the dataset, and each row provides relevant information about that attribute, including its description, data type, and example values.



### Key takeaways from the project:
1. The primary healthcare system would hence greatly benefit from a preliminary alert filtering tool that is anonymous and community based
2. To build a model that will assist clinicians in understanding how mental health can be diagnosed via non-contextual linguistic information.
3. Evaluate effectiveness of Natural-Language Processing (NLP) technologies as a way of converting and understanding mental health conditions.



---

### Future Works:
Future works are focused on targeting to help patients with other mental conditions and to help doctors. The recommendations are as follows: 
1. Further train the model to be able to recognize a wider spectrum of mental health conditions​
2. AI will analyze the conversation with patient to help doctors get insights of their condition before the appointment
