# 🧠 Diabetes Prediction App (Streamlit - Local Version)

A simple machine learning web app built with **Streamlit** to predict whether a person is likely to have **diabetes** based on medical input features.

This app uses a trained **TensorFlow model** and **scaler** loaded from the local directory, and runs **locally on VS Code**.

---

## ✨ Features

* ✅ Input-based prediction via user-friendly GUI
* ✅ Uses trained deep learning model (`.h5`) and scaler (`.pkl`)
* ✅ No internet or cloud required — all local
* ✅ Easy to run via Streamlit

---

## 🏗️ Project Structure

```
diabetes-app/
├── app_gui.py              # Main Streamlit app
├── diabetes_model.h5       # Trained TensorFlow model
├── scaler.pkl              # Saved StandardScaler object
├── requirements.txt        # Python dependencies
└── README.md               # You're here!
```

---

## 🧪 How to Run Locally (VS Code)

### 1. Install requirements

Make sure you're using Python 3.10 or similar. Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app_gui.py
```

Then open the provided `localhost` URL in your browser.

---

## 🧠 Model & Data

* **Model:** Trained using TensorFlow and saved as `diabetes_model.h5`
* **Scaler:** StandardScaler (`scaler.pkl`)
* **Storage:** Placed in the same directory as `app_gui.py`

Make sure these files are available before running the app.

---

## 📥 Input Fields (for Prediction)

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

The model outputs:

* `1` → **Diabetes**
* `0` → **No Diabetes**

---

## 📸 Screenshot

<a href="https://ibb.co/GQhMm5jY"><img src="https://i.ibb.co/m5xypc7Z/Annotation-2025-06-01-181412.png" alt="Annotation-2025-06-01-181412" border="0"></a>

---

## 📄 License

MIT License © 2025
Developed by \[Ahmeid Aqeil and Rahmat Afriyanto]
