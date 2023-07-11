import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import os
import pickle
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier

# Get the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

#Configurations
st.set_page_config(page_title='West Nile Virus', page_icon='🦟', layout='wide')
st.title('🦟West Nile Virus')
st.markdown('Upload your dataset to get a WNV prediction data. Only upload using the template format, any other format will result in an error. You may download the template below. The template has a sample entry for you to follow.')

#functions
def cleaning(dataset):
    dataset.columns = dataset.columns.str.lower()
    dataset['date'] = pd.to_datetime(dataset['date'])
    dataset['year'] = dataset['date'].dt.year
    dataset['month'] = dataset['date'].dt.month
    dataset['day'] = dataset['date'].dt.day
    weather = dataset[['date', 'station', 'tmax', 'tmin', 'tavg', 'depart','dewpoint','wetbulb','heat','cool','sunrise','sunset','snowfall','preciptotal','stnpressure','sealevel','resultspeed','resultdir','avgspeed']]
    station1 = weather[weather['station'] == 1].drop('station', axis=1)
    station2 = weather[weather['station'] == 2].drop('station', axis=1)
    weather = station1.merge(station2, on=['date'], suffixes=('_stn1', '_stn2'))
    weather = weather.drop(['snowfall_stn2', 'depart_stn2', 'sunrise_stn2', 'sunset_stn2'], axis=1)
    dataset = dataset.merge(weather, on='date')
    dataset = dataset.drop(['date', 'station', 'tmax', 'tmin', 'tavg', 'depart','dewpoint','wetbulb','heat','cool','sunrise','sunset','snowfall','preciptotal','stnpressure','sealevel','resultspeed','resultdir','avgspeed'], axis=1)
    dataset = pd.get_dummies(dataset, columns=dataset.select_dtypes(exclude='number').columns.to_list(), drop_first=True)
    dataset = dataset.drop_duplicates()
    return dataset

template_df_path = os.path.join(dir_path, 'template.csv')
template_df = pd.read_csv(template_df_path)
template_string = template_df.to_csv(index=False)
st.download_button(label="Download Prediction Template", data = template_string, file_name="prediction_template.csv")

uploaded_file = st.file_uploader(label = 'Upload Prediction Information, CSV format only', type='csv', help='Please use the exact same format as the prediction template to prevent error')

if uploaded_file is not None:
    dataset = pd.read_csv(uploaded_file)
    st.header('Uploaded Data')
    st.dataframe(dataset)
    cleaned_dataset = cleaning(dataset)
    ori_df = cleaned_dataset.reset_index()
    ori_df = ori_df.drop('index', axis=1)

    cleaned_dataset['daylight_duration'] = cleaned_dataset['sunset_stn1'] - cleaned_dataset['sunrise_stn1']
    # Convert temperatures from Fahrenheit to Celsius
    cleaned_dataset['tavg_stn2_celsius'] = (cleaned_dataset['tavg_stn2'] - 32) * 5/9
    cleaned_dataset['tavg_stn1_celsius'] = (cleaned_dataset['tavg_stn1'] - 32) * 5/9

    # Calculate actual vapor pressure for each station
    cleaned_dataset['actual_vapor_pressure_stn2'] = 6.11 * 10**((7.5 * cleaned_dataset['tavg_stn2_celsius']) / (237.7 + cleaned_dataset['tavg_stn2_celsius']))
    cleaned_dataset['actual_vapor_pressure_stn1'] = 6.11 * 10**((7.5 * cleaned_dataset['tavg_stn1_celsius']) / (237.7 + cleaned_dataset['tavg_stn1_celsius']))

    # Calculate saturation vapor pressure for each station
    cleaned_dataset['saturation_vapor_pressure_stn2'] = 6.11 * 10**((7.5 * cleaned_dataset['dewpoint_stn2']) / (237.7 + cleaned_dataset['dewpoint_stn2']))
    cleaned_dataset['saturation_vapor_pressure_stn1'] = 6.11 * 10**((7.5 * cleaned_dataset['dewpoint_stn1']) / (237.7 + cleaned_dataset['dewpoint_stn1']))

    # Calculate relative humidity for each station
    cleaned_dataset['relative_humidity_stn2'] = (cleaned_dataset['actual_vapor_pressure_stn2'] / cleaned_dataset['saturation_vapor_pressure_stn2']) * 100
    cleaned_dataset['relative_humidity_stn1'] = (cleaned_dataset['actual_vapor_pressure_stn1'] / cleaned_dataset['saturation_vapor_pressure_stn1']) * 100
    cleaned_dataset.drop(['tavg_stn2', 'dewpoint_stn2', 'dewpoint_stn1', 'tavg_stn1', 'sunset_stn1', 'sunrise_stn1', 'actual_vapor_pressure_stn2','actual_vapor_pressure_stn1','saturation_vapor_pressure_stn2','saturation_vapor_pressure_stn1'], axis=1, inplace=True)
    
    col_path = os.path.join(dir_path, 'columns.csv')
    col = pd.read_csv(col_path)
    cleaned_dataset.columns = cleaned_dataset.columns.str.lower()
    cleaned_dataset[list(set(col.columns.str.lower()) - set(cleaned_dataset.columns))] = 0
    cleaned_dataset = cleaned_dataset.reindex(columns=col.columns.str.lower())
    

    impute_path = os.path.join(dir_path, 'impute.pkl')
    with open(impute_path, 'rb') as file:
        imputer = pickle.load(file)

    model_path = os.path.join(dir_path, 'gb_best_model_updated.pkl')
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)

    proba_wnv = loaded_model.predict_proba(imputer.transform(cleaned_dataset))[:, 1]
    proba_wnv = pd.DataFrame(proba_wnv)
    proba_wnv = proba_wnv.rename(columns={0: 'Chance of WNV Presence'})
    st.header('Prediction')
    st.dataframe(proba_wnv)
    merged_df = pd.concat([proba_wnv, ori_df], axis=1)
    csv_string = merged_df.to_csv(index=False)
    st.download_button(
        label="Download WNV Probability",
        data=csv_string,
        file_name="wnv_probability.csv"
    )
