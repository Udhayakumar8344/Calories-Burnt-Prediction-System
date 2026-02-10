import pandas as pd
import numpy as np
import random

def generate_data(num_samples=5000):
    np.random.seed(42)
    random.seed(42)

    data = {
        'Gender': np.random.choice([0, 1], size=num_samples), # 0: Male, 1: Female
        'Age': np.random.randint(20, 70, size=num_samples),
        'Height': np.random.randint(150, 200, size=num_samples), # in cm
        'Weight': np.random.randint(50, 120, size=num_samples), # in kg
        'Duration': np.random.randint(10, 90, size=num_samples), # in minutes
        'Heart_Rate': np.random.randint(70, 180, size=num_samples), # bpm
        'Body_Temp': np.random.uniform(36.5, 41.0, size=num_samples) # Celsius
    }

    df = pd.DataFrame(data)

    # Synthetic equation for calories burned
    # Base calories + (Duration * Intensity Factor) + (Weight * Factor) - (Age * Factor)
    # Intensity ~ Heart Rate
    
    calories = []
    for i, row in df.iterrows():
        # Metabolic rate approximation
        gender_factor = 10 if row['Gender'] == 0 else 5 # Males burn slightly more
        intensity = (row['Heart_Rate'] - 70) / 110.0 # Normalized intensity 0-1
        
        # Non-linear relationship
        cal = (row['Duration'] * (5 + 10 * intensity)) + (row['Weight'] * 0.5) - (row['Age'] * 0.2) + gender_factor
        
        # Add some random noise
        cal += np.random.normal(0, 5)
        
        # Ensure positive
        cal = max(cal, 10)
        
        calories.append(round(cal, 2))

    df['Calories'] = calories
    
    return df

if __name__ == "__main__":
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df = generate_data()
    df.to_csv('data/calories_data.csv', index=False)
    print("Data generated successfully: data/calories_data.csv")
    print(df.head())
