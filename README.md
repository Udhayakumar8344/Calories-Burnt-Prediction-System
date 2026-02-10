
# 🏃‍♂️ Calorie Pulse - Calorie Burnt Prediction

**Predict your calories burned during exercise with Machine Learning.**

This project leverages Machine Learning (XGBoost) to accurately estimate calorie expenditure based on biometric data and exercise details. It features a modern web interface built with Flask and a classic desktop application using Tkinter.

---

## 🚀 Key Features

*   **📊 Accurate Predictions**: Uses an XGBoost Regressor model trained on synthetic data for reliable calorie estimation.
*   **🌐 Modern Web Interface**: User-friendly, responsive Flask application with "Calorie Pulse" branding.
*   **🖥️ Desktop Application**: Lightweight GUI for offline, quick calculations.
*   **📈 Data Generation**: Includes a custom synthetic data generator based on metabolic formulas.
*   **🧠 Comprehensive Training**: Easy-to-use scripts to regenerate data and retrain the model.

---

## 🛠️ Built With

*   **Python 3.8+**
*   **Flask** (Web Framework)
*   **Tkinter** (Desktop GUI)
*   **XGBoost** (Machine Learning Model)
*   **Pandas & NumPy** (Data Processing)
*   **HTML5, CSS3, JavaScript** (Frontend)
*   **Scikit-Learn** (Model Evaluation)

---

## 📦 Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/calorie-burnt-prediction.git
    cd calorie-burnt-prediction
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 💻 Usage

### 1. Run the Web Application (Recommended)
Launch the modern web interface:
```bash
python web/app.py
```
> Open your browser and navigate to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 2. Run the Desktop Application
Launch the legacy desktop GUI:
```bash
python src/app.py
```

### 3. Generate New Data (Optional)
If you want to create a fresh dataset:
```bash
python src/generate_data.py
```
*   Generates `data/calories_data.csv` with 5,000 samples.

### 4. Train the Model (Optional)
Retrain the XGBoost model on the latest data:
```bash
python src/train_model.py
```
*   Saves the trained model to `models/xgboost_model.pkl`.
*   Prints evaluation metrics (MAE, R2 Score).

---

## 📂 Project Structure

```
calorie-burnt-prediction/
├── data/                   # Generated dataset
│   └── calories_data.csv
├── models/                 # Trained models
│   └── xgboost_model.pkl
├── src/                    # Source code
│   ├── app.py              # Desktop GUI Application
│   ├── generate_data.py    # Synthetic data generator
│   ├── train_model.py      # Model training script
│   └── utils.py            # Utility functions
├── web/                    # Web Application
│   ├── static/             # CSS, JS, Images
│   ├── templates/          # HTML Templates
│   └── app.py              # Flask server
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 🧠 Model Details

The model is trained using **XGBoost Regressor** with the following inputs:
*   Gender (Male/Female)
*   Age
*   Height (cm)
*   Weight (kg)
*   Duration (min)
*   Heart Rate (bpm)
*   Body Temperature (°C)

It learns the non-linear relationships between these factors and calorie burn, providing a customized estimate for each session.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Contact

Project Link: [https://github.com/yourusername/calorie-burnt-prediction](https://github.com/yourusername/calorie-burnt-prediction)
