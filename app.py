import streamlit as st
import pickle
import numpy as np
import os

# Load the trained model
model_path = r"C:\Users\test\OneDrive\Desktop\ML project\ad_click_model.pkl"

# Check if the model file exists
if os.path.exists(model_path):
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    model_loaded = True
else:
    model_loaded = False

# Streamlit UI
def main():
    # Set page title and icon
    st.set_page_config(page_title="Ad Click Prediction", page_icon="📊", layout="centered")

    # Add a header and introduction text
    st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #4CAF50;">Ad Click Prediction</h1>
        <p style="font-size: 18px; color: #555;">Enter the details below to predict whether the ad will be clicked.</p>
    </div>
    """, unsafe_allow_html=True)

    # Use a sidebar for a cleaner layout
    st.sidebar.title("Input Details")

    # User inputs
    age = st.sidebar.number_input("Age", min_value=10, max_value=100, step=1)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Non-Binary"])
    device_type = st.sidebar.selectbox("Device Type", ["Tablet", "Mobile", "Desktop"])
    ad_position = st.sidebar.selectbox("Ad Position", ["Bottom", "Top", "Side"])
    time_of_day = st.sidebar.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
    browsing_history = st.sidebar.selectbox("Browsing History", ["News", "Education", "Social Media", "Shopping", "Entertainment"])

    # Encoding user input
    gender_dict = {"Male": 0, "Female": 1, "Non-Binary": 2}
    device_dict = {"Tablet": 0, "Mobile": 1, "Desktop": 2}
    ad_position_dict = {"Bottom": 0, "Top": 1, "Side": 2}
    time_dict = {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3}
    browsing_dict = {"News": 0, "Education": 1, "Social Media": 2, "Shopping": 3, "Entertainment": 4}

    input_data = np.array([[
        age,
        gender_dict[gender],
        device_dict[device_type],
        ad_position_dict[ad_position],
        time_dict[time_of_day],
        browsing_dict[browsing_history]
    ]])

    # Predict button with enhanced styling
    st.markdown("""
    <div style="text-align: center;">
        <p style="font-size: 20px; font-weight: bold;">Click below to predict if the ad will be clicked:</p>
    </div>
    """, unsafe_allow_html=True)

    # Predict button with more style
    if st.button("Predict Click", key="predict_button", help="Click to predict if the ad will be clicked based on the details entered"):
        if model_loaded:
            prediction = model.predict(input_data)
            result = "Clicked" if prediction[0] == 1 else "Not Clicked"
            
            # Display result with a professional message
            st.markdown(f"""
            <div style="text-align: center; font-size: 24px; font-weight: bold; color: #4CAF50;">
                Prediction: {result}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Error: Model file not found. Please check the file path.")

    # Add a footer
    st.markdown("""
    <div style="text-align: center; margin-top: 40px;">
        <p style="font-size: 14px; color: #999;">Powered by Streamlit | Ad Click Prediction Model</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
