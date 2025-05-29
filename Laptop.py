import streamlit as st
import numpy as np
import joblib 

# Load the trained model
model = joblib.load("rf_model.pkl")

st.title("Laptop Price Prediction App")

st.divider()

st.write("With this app, you can get the laptop price prediction after entering the values of Processor Speed, RAM Size, and Storage Capacity!")

st.divider()

# Get user inputs
processor_speed = st.number_input("Enter Processor Speed (GHz)", value=2.50, step=0.50)
ram_size = st.number_input("Enter RAM Size (GB)", value=16, step=8)
storage_capacity = st.number_input("Enter Storage Capacity (GB)", value=512, step=256)

# Prepare input for prediction
X = [processor_speed, ram_size, storage_capacity]

st.divider()

# Button to trigger prediction
if st.button("Estimate Price"):
    st.balloons()
    
    X_array = np.array(X).reshape(1, -1)  # reshape for prediction
    prediction = model.predict(X_array)[0]  # get the first result

    st.write(f"Estimated Laptop Price: ${prediction:,.2f}")
else:
    st.write("Please click the button to get a price prediction.")
