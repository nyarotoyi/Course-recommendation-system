# Course Recommendation System
This project involves building a Course Recommendation System using a Random Forest Classifier. The system is designed to assist post-secondary students in selecting university courses that best align with their academic performance, interests, and RIASEC profiles.

## Features
- Random Forest Classifier: Utilizes machine learning algorithms to provide accurate recommendations.
- Performance-Based Recommendations: Takes into account students' academic performance.
- Personality-Based Matching: Aligns course recommendations with students' RIASEC profiles.
## Objective
The primary goal of this project is to develop a tool that aids students in making informed decisions about their course selection based on a comprehensive analysis of their performance and personalities.

## Instructions
Before using any other files, you need to run the Student Recommendation notebook to generate model.pkl and scaler.pkl.

## Dataset Description
This dataset contains information about students enrolled in an academy, including their personal details, academic scores, extracurricular activities, and career aspirations.

### Features Information
- id: Unique identifier for each student.
- first_name: First name of the student.
- last_name: Last name of the student.
- email: Email address of the student.
- gender: Gender of the student (male/female).
- extracurricular_activities: Indicates whether the student participates in extracurricular activities (True/False).
- riasec: The total Holland's RIASEC score obtained by summing scores from all six profiles.
- career_aspiration: Aspirational course of the student.
- math_score: Score achieved by the student in mathematics.
- history_score: Score achieved by the student in history.
- physics_score: Score achieved by the student in physics.
- chemistry_score: Score achieved by the student in chemistry.
- biology_score: Score achieved by the student in biology.
- english_score: Score achieved by the student in English.
- geography_score: Score achieved by the student in geography.
