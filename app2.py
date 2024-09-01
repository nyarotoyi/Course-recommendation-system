import streamlit as st
import pickle
import numpy as np

# Load the scaler and model
caler = pickle.load(open("Models/scaler.pkl", 'rb'))
model = pickle.load(open("Models/model.pkl", 'rb'))
scaler = pickle.load(
    open(
        "Models/scaler.pkl",
        "rb",
    )
)
model = pickle.load(
    open(
        "Models/model.pkl",
        "rb",
    )
)

# Define the class names for the courses
class_names = [
    "Bachelor of Supply Chain Management",
    "Bachelor of Statistics",
    "Bachelor of Corporate Communications",
    "Bachelor of Human Resource Management",
    "Bachelor of Development Studies",
    "Bachelor of Procurement and Contract Management",
    "Bachelor of Project Management",
    "Bachelor of Business Administration",
    "Bachelor of Journalism",
    "Bachelor of Business and Office Management",
    "Bachelor of Economics and Statistics",
    "Bachelor of Mass Communication",
    "Bachelor of Commerce",
    "Bachelor of Procurement and Logistics",
    "Bachelor of Finance",
    "Bachelor of Business Information Technology",
    "Bachelor of Technology and Entrepreneurship Management",
]

# Streamlit App
st.title("Course Recommendation System")

st.write("""
    Welcome to the Course Recommendation System.
    This system is a test project designed to explore the potential of recommending university courses based on student profiles. 
    The dataset used was sourced from Kaggle and tailored to fit the objectives of this proof of concept.

    Currently, we have focused on 14 courses offered by JKUAT COHRED, aiming to demonstrate how academic performance and RIASEC profiles 
    can be used to suggest the most suitable courses for students.
""")

st.write("Fill the form below to get your course recommendations:")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
extracurricular_activities = st.selectbox("Extracurricular Activities", ["Yes", "No"])
riasec_score = st.number_input("RIASEC Score", min_value=0, max_value=100)
math_score = st.number_input("Math Score", min_value=0, max_value=100)
history_score = st.number_input("History Score", min_value=0, max_value=100)
physics_score = st.number_input("Physics Score", min_value=0, max_value=100)
chemistry_score = st.number_input("Chemistry Score", min_value=0, max_value=100)
biology_score = st.number_input("Biology Score", min_value=0, max_value=100)
english_score = st.number_input("English Score", min_value=0, max_value=100)
geography_score = st.number_input("Geography Score", min_value=0, max_value=100)

# Encode categorical variables
gender_encoded = 1 if gender == "Female" else 0
extracurricular_activities_encoded = 1 if extracurricular_activities == "Yes" else 0

# Calculate total and average score
total_score = sum(
    [
        math_score,
        history_score,
        physics_score,
        chemistry_score,
        biology_score,
        english_score,
        geography_score,
    ]
)
average_score = total_score / 7

# Create feature array with 12 features
feature_array = np.array(
    [
        gender_encoded,
        extracurricular_activities_encoded,
        riasec_score,
        math_score,
        history_score,
        physics_score,
        chemistry_score,
        biology_score,
        english_score,
        geography_score,
        total_score,
        average_score,
    ]
).reshape(1, -1)

# Scale features
scaled_features = scaler.transform(feature_array)

# Make prediction
if st.button("Get Course Recommendation"):
    probabilities = model.predict_proba(scaled_features)
    top_classes_idx = np.argsort(-probabilities[0])[:3]
    top_classes_names_probs = [
        (class_names[idx], f"Probability: {float(probabilities[0][idx]):.2f}") for idx in top_classes_idx
    ]

        st.write("### Recommended Courses and Probabilities")
        for idx, (course, probability) in enumerate(recommendations, 1):
            st.write(f"{idx}. **{course}**: {probability}")
