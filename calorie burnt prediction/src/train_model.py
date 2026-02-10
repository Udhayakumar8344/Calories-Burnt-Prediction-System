import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
from utils import save_model

def train():
    # Load data
    data_path = 'data/calories_data.csv'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Run generate_data.py first.")
        return

    df = pd.read_csv(data_path)
    
    X = df[['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']]
    y = df['Calories']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train XGBoost
    print("Training XGBoost...")
    xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
    xgb_model.fit(X_train, y_train)
    
    # Evaluate XGBoost
    y_pred_xgb = xgb_model.predict(X_test)
    mae_xgb = mean_absolute_error(y_test, y_pred_xgb)
    r2_xgb = r2_score(y_test, y_pred_xgb)
    
    print(f"XGBoost MAE: {mae_xgb:.2f}")
    print(f"XGBoost R2 Score: {r2_xgb:.4f}")
    
    # Save model
    if not os.path.exists('models'):
        os.makedirs('models')
    
    save_model(xgb_model, 'models/xgboost_model.pkl')
    print("Model saved to models/xgboost_model.pkl")

    # Optional: Compare with others
    print("\nComparing with other models (for reference):")
    
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    print(f"Linear Regression R2: {r2_score(y_test, lr.predict(X_test)):.4f}")
    
    rf = RandomForestRegressor(random_state=42)
    rf.fit(X_train, y_train)
    print(f"Random Forest R2: {r2_score(y_test, rf.predict(X_test)):.4f}")

if __name__ == "__main__":
    train()
