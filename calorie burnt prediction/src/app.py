import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd
import numpy as np

class CalorieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calories Burnt Prediction")
        self.root.geometry("400x500")
        
        # Load model
        try:
            self.model = joblib.load('models/xgboost_model.pkl')
        except FileNotFoundError:
            self.model = None
            messagebox.showwarning("Model Error", "Model not found. Please train the model first.")

        self.create_widgets()

    def create_widgets(self):
        # Title
        label_title = tk.Label(self.root, text="Calories Burnt Predictor", font=("Helvetica", 16, "bold"))
        label_title.pack(pady=10)

        # Input Frame
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Gender
        tk.Label(frame, text="Gender:").grid(row=0, column=0, padx=5, pady=5)
        self.gender_var = tk.StringVar(value="Male")
        gender_cb = ttk.Combobox(frame, textvariable=self.gender_var, values=["Male", "Female"], state="readonly")
        gender_cb.grid(row=0, column=1, padx=5, pady=5)

        # Age
        tk.Label(frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        # Height
        tk.Label(frame, text="Height (cm):").grid(row=2, column=0, padx=5, pady=5)
        self.height_entry = tk.Entry(frame)
        self.height_entry.grid(row=2, column=1, padx=5, pady=5)

        # Weight
        tk.Label(frame, text="Weight (kg):").grid(row=3, column=0, padx=5, pady=5)
        self.weight_entry = tk.Entry(frame)
        self.weight_entry.grid(row=3, column=1, padx=5, pady=5)

        # Duration
        tk.Label(frame, text="Duration (min):").grid(row=4, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(frame)
        self.duration_entry.grid(row=4, column=1, padx=5, pady=5)

        # Heart Rate
        tk.Label(frame, text="Heart Rate (bpm):").grid(row=5, column=0, padx=5, pady=5)
        self.heart_rate_entry = tk.Entry(frame)
        self.heart_rate_entry.grid(row=5, column=1, padx=5, pady=5)

        # Body Temp
        tk.Label(frame, text="Body Temp (°C):").grid(row=6, column=0, padx=5, pady=5)
        self.temp_entry = tk.Entry(frame)
        self.temp_entry.grid(row=6, column=1, padx=5, pady=5)

        # Predict Button
        predict_btn = tk.Button(self.root, text="Predict", command=self.predict, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        predict_btn.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"), fg="blue")
        self.result_label.pack(pady=10)

    def predict(self):
        if self.model is None:
            messagebox.showerror("Error", "Model not loaded")
            return

        try:
            gender = 0 if self.gender_var.get() == "Male" else 1
            age = float(self.age_entry.get())
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            duration = float(self.duration_entry.get())
            heart_rate = float(self.heart_rate_entry.get())
            body_temp = float(self.temp_entry.get())

            features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
            
            # Predict
            prediction = self.model.predict(features)[0]
            
            self.result_label.config(text=f"Calories Burnt: {prediction:.2f} kcal")
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalorieApp(root)
    root.mainloop()
