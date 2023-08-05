import os
import json

import requests
import streamlit as st
from dotenv import load_dotenv
from requests.exceptions import HTTPError

# fmt: off
from src.entities.enums import (
    District,
    Condition,
    EnergyCertify,
    ResidenceType
)

# fmt: on
load_dotenv()
API_ENDPOINT = os.getenv('API_ENDPOINT', 'http://127.0.0.0:8000/predict')


st.set_page_config(
    page_title="MLOps House Price Rent Predictor",
    page_icon="🏠",
    initial_sidebar_state="expanded",
)

# Create the header page content
st.title("")
st.markdown(
    "<h1 style='text-align: center; color: white;'> 🏠 House Price Rent Predictor</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: grey;'>Predict the rent value of your residence</h1>",
    unsafe_allow_html=True,
)

condition_values = [condition.value for condition in Condition]
district_values = [district.name for district in District]
energy_values = [energy.value for energy in EnergyCertify]
residence_values = [str(residence.value) for residence in ResidenceType]


with st.form("predict_form"):
    selected_residence = st.selectbox('What type of residence?', residence_values)

    selected_condition = st.selectbox(
        'What is the condition of the house?', condition_values
    )

    selected_district = st.selectbox('What is the location?', district_values)

    selected_energy = st.selectbox('What is the Energy certificate?', energy_values)

    selected_metric = st.number_input(
        'How many square meters does the house have?', format='%f', step=0.5
    )

    selected_rooms = st.number_input(
        'How many rooms does the house have?', format='%d', step=1
    )

    selected_bathroom = st.number_input(
        'How many bathrooms does the house have?', format='%d', step=1
    )

    submitted = st.form_submit_button("Submit")


def predict(residence, condition, district, energy, metric, rooms, bathroom):
    data = {
        'district': district,
        'property_type': residence,
        'bathroom': bathroom,
        'metric': metric,
        'room': rooms,
        'energy_certify': energy,
        'condition': condition,
    }

    response = requests.post(API_ENDPOINT, json=data, timeout=30)

    if response.status_code != 200:
        raise HTTPError(f"Status: {response.status_code}")

    return response.json()


def main():
    if submitted:
        with st.spinner("Predicting..."):
            try:
                prediction = predict(
                    selected_residence,
                    selected_condition,
                    selected_district,
                    selected_energy,
                    selected_metric,
                    selected_rooms,
                    selected_bathroom,
                )
                pred = json.loads(prediction["predictions"])["price_predicted"]["0"]
                st.success(f'The suggested price is: {pred} Є')
            except HTTPError as error:
                st.error(f'Something went wrong... {error}')


if __name__ == "__main__":
    main()
