import streamlit as st
import joblib

model = joblib.load("House_price_pred.pkl")

st.title("House Price Prediction tool")
st.write("Predict the price of your dream house!")

Square_Feet = st.number_input("enter desired square footage:" )
num_bedrooms = st.number_input("Enter number of bedrooms:")
num_bathrooms = st.number_input("Enter number of bathrooms:")
num_floors = st.number_input("Enter number of floors:")
year_built = st.number_input("Enter year built:")
has_garden = st.number_input("Has Garden (Enter 1 if you need, else input 0")
has_pool = st.number_input("Has Pool (Enter 1 if you need, else input 0")
garage_size = st.number_input("Enter garage size:")
location_score = st.number_input("Enter location score:")
distance_to_center = st.number_input("Enter distance to center:")

if st.button("Predict price"):

     features = [
     Square_feet,
     num_bedrooms,
     num_bathrooms,
     num_floors,
     year_built,
     has_garden,
     has_pool,
     garage_size,
     location_score,
     distance_to_center
     ]

     prediction = model.predict([features])[0]
     st.write(f'your predicted price is: ${prediction}')

