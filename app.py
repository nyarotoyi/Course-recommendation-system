# pip install scikit-learn==1.3.2
# pip install numpy
# pip install flask


# load packages==============================================================
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, template_folder=".")


scaler = pickle.load(
    open(
        "Models/scaler.pkl",
        "rb",
    )
)
model = pickle.load(
    open(
        "Model/model.pkl",
        "rb",
    )
)
class_names = [
    "Bachelor of Supply Chain Management",
    "Bachelor of Statistics",
    "Bachelor of Corporate Communications",
    "Bachelor of Human Resouce Management",
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


# Recommendations ===========================================================
def Recommendations(
    gender,
    extracurricular_activities,
    riasec,
    math_score,
    history_score,
    physics_score,
    chemistry_score,
    biology_score,
    english_score,
    geography_score,
    total_score,
    average_score,
):
    # Encode categorical variables
    gender_encoded = 1 if gender.lower() == "female" else 0
    extracurricular_activities_encoded = 1 if extracurricular_activities else 0

    # Create feature array
    feature_array = np.array(
        [
            [
                gender_encoded,
                extracurricular_activities_encoded,
                riasec,
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
        ]
    )

    # Scale features
    scaled_features = scaler.transform(feature_array)

    # Predict using the model
    probabilities = model.predict_proba(scaled_features)

    # Get top five predicted classes along with their probabilities
    top_classes_idx = np.argsort(-probabilities[0])[:3]
    top_classes_names_probs = [
        (class_names[idx], probabilities[0][idx]) for idx in top_classes_idx
    ]

    return top_classes_names_probs


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recommend")
def recommend():
    return render_template("recommend.html")


@app.route("/pred", methods=["POST", "GET"])
def pred():
    if request.method == "POST":
        gender = request.form["gender"]
        extracurricular_activities = (
            request.form["extracurricular_activities"] == "true"
        )
        riasec = int(request.form["riasec"])
        math_score = int(request.form["math_score"])
        history_score = int(request.form["history_score"])
        physics_score = int(request.form["physics_score"])
        chemistry_score = int(request.form["chemistry_score"])
        biology_score = int(request.form["biology_score"])
        english_score = int(request.form["english_score"])
        geography_score = int(request.form["geography_score"])
        total_score = float(request.form["total_score"])
        average_score = float(request.form["average_score"])

        recommendations = Recommendations(
            gender,
            extracurricular_activities,
            riasec,
            math_score,
            history_score,
            physics_score,
            chemistry_score,
            biology_score,
            english_score,
            geography_score,
            total_score,
            average_score,
        )

        return render_template("results.html", recommendations=recommendations)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
