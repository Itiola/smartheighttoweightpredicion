import streamlit as st
import pickle

# Load the saved linear regression model
loaded_model = pickle.load(open('smartweightpredictionmodel.pkl', 'rb'))

def predict_weight(height):
  """
  Function to predict weight based on height using the loaded model
  """
  prediction = loaded_model.predict([[height]])[0]
  return prediction

# Streamlit App

st.title("Smart Weight Prediction")
st.subheader("Predict your weight based on height")

# Get user input for height
user_height = st.number_input("Enter your height (cm):", min_value=0)

# Button to trigger prediction
if st.button("Predict Weight"):
  # Make prediction using the function
  predicted_weight = predict_weight(user_height)
  
  # Display the prediction result
  st.write(f"Your predicted weight is: {predicted_weight:.2f} pounds")
