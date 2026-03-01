import joblib
import pandas as pd


model = joblib.load("foundation_ore_predictor.pkl")

mine=pd.DataFrame([[40.9,-116.3]],  columns=['latitude','longitude'])

name={0:"Copper", 1:"Gold", 2:"Iron"}

result = model.predict(mine)

print(f"Prediction is {name[result[0]]}")