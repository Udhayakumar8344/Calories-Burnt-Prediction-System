import pandas as pd
import joblib

def load_data(filepath):
    return pd.read_csv(filepath)

def save_model(model, filepath):
    joblib.dump(model, filepath)

def load_model(filepath):
    return joblib.load(filepath)
