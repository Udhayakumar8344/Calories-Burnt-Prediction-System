# Calories Burnt Prediction

This project uses machine learning (XGBoost) to predict the number of calories burned during exercise based on user metrics.

## Features
- **Synthetic Data Generation**: Simulates realistic exercise data.
- **Machine Learning**: detailed XGBoost model to estimate calories.
- **Web Interface**: Modern, professional Flask application.
- **Desktop GUI**: Legacy Tkinter-based user interface.

## Installation

1.  Clone the repository or download the files.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Generate Data** (Optional, data already provided if you run this):
    ```bash
    python src/generate_data.py
    ```

2.  **Train Model**:
    ```bash
    python src/train_model.py
    ```

3.  **Run Web Application** (Recommended):
    ```bash
    python web/app.py
    ```
    Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

4.  **Run Desktop App** (Legacy):
    ```bash
    python src/app.py
    ```

## Project Structure
- `src/`: Core logic and desktop app.
- `web/`: Flask application (frontend/backend).
- `data/`: Dataset.
- `models/`: Trained model.
