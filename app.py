import streamlit as st
import joblib


st.title(" House Price Prediction App")


area = st.number_input("Area (in square feet)", min_value=100, max_value=10000, value=100)
bathrooms = st.slider("Number of Bathrooms", 1, 15, 2)
stories = st.slider("Number of Stories", 1, 10, 3)
hotwaterheating = st.selectbox("Hot Water Heating", ['yes', 'no'])
parking = st.slider("Number of Parking Spots", 0, 5, 2)
airconditioning = st.selectbox("Air Conditioning", ['yes', 'no'])
basement = st.selectbox("Basement", ['yes', 'no'])
prefarea = st.selectbox("Preferred Area", ['yes', 'no'])


min_max = {
    'area': (1650, 16200),
    'bathrooms': (1, 4),
    'stories': (1, 4),
    'parking': (0, 3)
}


def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)


def yes_no_to_binary(val):
    return 1.0 if val.lower() == 'yes' else 0.0


if st.button("Predict Price"):
   
    area_norm = normalize(area, *min_max['area'])
    bathrooms_norm = normalize(bathrooms, *min_max['bathrooms'])
    stories_norm = normalize(stories, *min_max['stories'])
    parking_norm = normalize(parking, *min_max['parking'])

    hotwaterheating_bin = yes_no_to_binary(hotwaterheating)
    airconditioning_bin = yes_no_to_binary(airconditioning)
    basement_bin = yes_no_to_binary(basement)
    prefarea_bin = yes_no_to_binary(prefarea)


    loaded_model = joblib.load("House1_price_prediction.pkl")

    
    sample = [[
        area_norm, bathrooms_norm, stories_norm,
        hotwaterheating_bin, parking_norm, airconditioning_bin,
        basement_bin, prefarea_bin
    ]]

    
    predicted_price = loaded_model.predict(sample)[0]

   
    min_price = 1750000
    max_price = 13300000
    actual_price = predicted_price * (max_price - min_price) + min_price

   
    st.success(f" Predicted House Price: {actual_price:,.2f} RS")
