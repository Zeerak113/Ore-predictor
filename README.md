## Project Overview
This project uses a **Random Forest Classifier** to analyze global data. By inputting Latitude and Longitude coordinates, the model predicts whether it is copper, gold or iron.

## The Tech Stack
* **Language:** Python
* **Libraries:** Scikit-Learn, Pandas, Joblib
* **Environment:** Developed in Google Colab, deployed in VS Code

## Repository Contents
* `ore_predictor_notebook.ipynb`: The complete research phase, including data cleaning and model training.
* `app.py`: The production-ready script for running predictions locally.
* `requirements.txt`: The list of dependencies needed to run this project.


> **Note on Model File:** The trained `.pkl` model file exceeds GitHub's 25MB upload limit. To generate the model locally, simply run the provided Notebook.

## How to Use
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the prediction script: `python app.py`

## Note:
This project was born from a desire to move beyond "Tutorial Hell" and apply Machine Learning to my professional field: Geoscience. Using a global dataset of mineral occurrences, I built a Random Forest model to predict three specific ores(copper, gold, iron) based on geographic coordinates.

## Hurdles
As a Geoscientist learning ML, the challenge wasn't just the math but the engineering. This project documents my transition from cloud-based research (Google Colab) to a functional, local Python environment (VS Code).
