from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os
import sys

# Add src to path to import utils if needed, though we just need model here
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

app = Flask(__name__)

# Load Model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'xgboost_model.pkl')
try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model from {MODEL_PATH}: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.get_json()
        
        # Extract features in correct order
        # ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
        gender = int(data['gender']) # 0 or 1
        age = float(data['age'])
        height = float(data['height'])
        weight = float(data['weight'])
        duration = float(data['duration'])
        heart_rate = float(data['heart_rate'])
        body_temp = float(data['body_temp'])
        
        features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
        
        prediction = model.predict(features)[0]
        
        return jsonify({
            'success': True,
            'calories': float(prediction)
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
