import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("House_price_prediction.pkl")
scaler = joblib.load("scaler.pkl")  


price_min =  1750000      
price_max = 13300000   


def encode_yes_no(value):
    return 1 if value.lower() == 'yes' else 0

st.title("🏠 House Price Prediction App")


area = st.slider("Area (sq. ft)", 200, 1000, 500)
bathrooms = st.number_input("Number of Bathrooms", 1, 10, 1)
stories = st.number_input("Number of Stories", 1, 10, 1)
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])
parking = st.slider("Parking Spaces", 0, 10, 1)


hotwaterheating = encode_yes_no(hotwaterheating)
airconditioning = encode_yes_no(airconditioning)
basement = encode_yes_no(basement)
prefarea = encode_yes_no(prefarea)


input_df = pd.DataFrame([[
    area, bathrooms, stories, hotwaterheating, parking,
    airconditioning, basement, prefarea
]], columns=[
    "area", "bathrooms", "stories", "hotwaterheating", "parking",
    "airconditioning", "basement", "prefarea"
])


scaled_input = scaler.transform(input_df)


if st.button("Predict Price"):
    prediction = model.predict(scaled_input)[0]


    actual_price = prediction * (price_max - price_min) + price_min

   
    st.info(f"💰 Estimated Price: ₨ {actual_price:,.2f}")



