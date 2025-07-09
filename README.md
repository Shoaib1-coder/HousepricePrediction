
# 🏠 House Price Prediction App

This is a Streamlit web application that predicts house prices based on user input features such as area, number of bathrooms, stories, and more. The model was trained using a normalized dataset and saved using `joblib`.

---

## 🚀 Demo

[![Open in Streamlit](https://housepriceprediction12.streamlit.app/)  


---

## 📦 Features

- Interactive UI to input:
  - Area (in sq. ft)
  - Number of Bathrooms
  - Number of Stories
  - Parking spots
  - Hot Water Heating
  - Air Conditioning
  - Basement
  - Preferred Area
- Normalizes input based on training range
- Loads and uses a pre-trained model (`House1_price_prediction.pkl`)
- Predicts and displays house price in Pakistani Rupees (₨)

---

## 🧠 Model

- Model used: Xgboost 
- Trained on normalized features
- Price output is **scaled back** to actual price range: `1,750,000 – 13,300,000 RS`

---

## 🛠 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Shoaib1-coder/HousepricePrediction.git
cd HousepricePrediction
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py                       # Main Streamlit app
├── House1_price_prediction.pkl  # Trained ML model
├── requirements.txt             # Python dependencies
├── runtime.txt                  # Python version for deployment
├── data/                        # Dataset folder (optional)
├── EDA.ipynb                    # Exploratory Data Analysis notebook
└── README.md                    # Project documentation
```

---

## 🌐 Deployment

This app is compatible with **Streamlit Cloud**. Make sure the following files are in your root folder:

- `app.py`
- `requirements.txt`
- `runtime.txt` (with `python-3.10`)
- `House1_price_prediction.pkl`

Then push to GitHub and deploy from the Streamlit Cloud dashboard.

---

## ✍️ Author

**Muhammad Shoaib Sattar**  
[GitHub](https://github.com/shoaib1-coder) | [Email](mailto:mshoaib3393@gmail.com)

---

## 📜 License

This project is licensed under the MIT License.
