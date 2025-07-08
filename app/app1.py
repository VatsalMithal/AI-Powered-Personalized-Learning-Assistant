import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Saved Model & Scaler
model = joblib.load('D:/FinalProject/use_case_1/model/random_forest.pkl') 
scaler = joblib.load('D:/FinalProject/use_case_1/model/scaler.pkl')

#  Load Label Encoders
encoders = {}
for col in ['tutor_mode', 'answer_type', 'skill_id']:
    encoders[col] = joblib.load(f'D:/FinalProject/use_case_1/model//encoder_{col}.pkl')

#  App Title
st.title("🎓 Student Pass/Fail Prediction App")

st.write("Predict whether a student will pass or fail a quiz/exam based on their historical activity.")

#  User Input Form
st.header("🔧 Enter Student Activity Data")

attempt_count = st.number_input("Attempt Count", min_value=0, value=1)
ms_first_response = st.number_input("Milliseconds to First Response", min_value=0, value=5000)
hint_count = st.number_input("Hint Count", min_value=0, value=0)
hint_total = st.number_input("Hint Total", min_value=0, value=3)
overlap_time = st.number_input("Overlap Time (ms)", min_value=0, value=10000)
first_action = st.number_input("First Action Code", min_value=0, value=0)
opportunity = st.number_input("Opportunity", min_value=0, value=1)
opportunity_original = st.number_input("Opportunity Original", min_value=0, value=1)
position = st.number_input("Position in Assignment", min_value=0, value=1)

# Dropdowns for categorical inputs
tutor_mode = st.selectbox("Tutor Mode", encoders['tutor_mode'].classes_)
answer_type = st.selectbox("Answer Type", encoders['answer_type'].classes_)
skill_id = st.selectbox("Skill ID", encoders['skill_id'].classes_)

#  Encode categorical inputs
tutor_mode_encoded = encoders['tutor_mode'].transform([tutor_mode])[0]
answer_type_encoded = encoders['answer_type'].transform([answer_type])[0]
skill_id_encoded = encoders['skill_id'].transform([skill_id])[0]

#  Prepare input for prediction
input_data = np.array([[
    attempt_count, ms_first_response, hint_count, hint_total, overlap_time,
    first_action, opportunity, opportunity_original, position,
    tutor_mode_encoded, answer_type_encoded, skill_id_encoded
]])

#  Scale numeric features
input_scaled = scaler.transform(input_data)

#  Make Prediction
if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    result = "✅ Student is likely to PASS!" if prediction == 1 else "❌ Student is likely to FAIL."
    st.subheader(result)
