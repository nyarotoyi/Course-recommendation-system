# Course Recommendation System
This project focuses on developing a Course Recommendation System utilizing a Random Forest Classifier. The system aims to guide post-secondary students in choosing university courses that align most effectively with their academic performance, personal interests, and RIASEC profiles.

## Overview
This system is a test project designed to explore the potential of recommending university courses based on student profiles. The dataset used was sourced from Kaggle and tailored to fit the objectives of this proof of concept. Currently, the focus is on 14 courses offered by JKUAT COHRED. This demonstrates how academic performance and RIASEC profiles can be used to suggest the most suitable courses for students.

## How It Works
The system leverages a Random Forest Classifier to analyze students' academic scores and RIASEC profiles. By inputting various academic and personal details, students receive recommendations for courses that align with their strengths and interests.

## Why It Matters
- Personalized Guidance: Helps students make informed decisions about their educational paths.
- Efficient Course Matching: Utilizes advanced machine learning techniques to provide relevant recommendations.
- Data-Driven Insights: Demonstrates the potential of using data science to improve educational outcomes.
  
## Future Enhancements
Building a robust and accurate system will require additional data and testing. Expanding the dataset and integrating comprehensive RIASEC assessments will enhance the system's effectiveness and reliability.
## Try the App

### Streamlit Cloud

Click the button below to access the Course Recommendation System on Streamlit Cloud

<a href="https://courserecommendationsytem.streamlit.app/" target="_blank">
  <img src="https://img.shields.io/badge/Try%20the%20App%20on%20Streamlit%20Cloud-blue?style=for-the-badge&logo=streamlit" alt="Try the App on Streamlit Cloud" />
</a>

### Deploy Locally

You can also deploy the app locally. Choose between the Streamlit app or the Flask app

#### Streamlit App

1. **Clone the repository**
    ```bash
    git clone https://github.com/nyarotoyi/Course-recommendation-system.git
    cd Course-recommendation-system
    ```

2. **Install dependencies**
    ```bash
    pip install streamlit scikit-learn numpy
    ```

3. **Run the Streamlit app**
    ```bash
    streamlit run app2.py
    ```

#### Flask App

1. **Clone the repository**
    ```bash
    git clone https://github.com/nyarotoyi/Course-recommendation-system.git
    cd Course-recommendation-system
    ```

2. **Install dependencies**
    ```bash
    pip install flask scikit-learn numpy
    ```

3. **Run the Flask app**
    ```bash
    python app.py
    ```
## What is RIASEC?

RIASEC, also known as the Holland Code, is a theory of personality and career development. It classifies people into six personality types and matches them with compatible careers and educational paths. The six types are:

- Realistic (R): Practical, hands-on, and physical tasks.
- Investigative (I): Analytical, intellectual, and problem-solving activities.
- Artistic (A): Creative, original, and expressive endeavors.
- Social (S): Helping, nurturing, and interacting with others.
- Enterprising (E): Leadership, persuasion, and entrepreneurial activities.
- Conventional (C): Organizational, detail-oriented, and structured tasks.
Understanding your RIASEC profile helps in selecting career paths and educational opportunities that match your interests and strengths.


## Features
- Random Forest Classifier: Utilizes machine learning algorithms to provide accurate recommendations.
- Performance-Based Recommendations: Takes into account students' academic performance.
- Personality-Based Matching: Aligns course recommendations with students' RIASEC profiles.
- 
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

 ## Acknowledgment
Building a working concept will require more accurate data and a reliable method for assessing RIASEC profiles. This project serves as a proof of concept, and future developments will focus on improving data accuracy and enhancing the assessment process for better recommendations.

## Contact Information

For inquiries, collaborations, or more information about the Course Recommendation System, please feel free to reach out

Email: [zianaodero@gmail.com](mailto:zianaodero@gmail.com).
LinkedIn: [Marice Ziana](https://www.linkedin.com/in/marice-ziana-a51442146/)
