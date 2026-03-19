# 🚀 Fraud Detection System (Flask + Machine Learning)

A web-based **Fraud Detection Dashboard** built using Machine Learning and Flask that analyzes transaction risk in real-time.  

This project uses anomaly detection techniques like **Isolation Forest** and heuristic-based **Local Outlier Factor (LOF)** to classify transactions into risk categories.

---

## 📌 Features

- 🔍 Real-time fraud prediction  
- 📊 Risk score (0–100)  
- 🟢 Low / 🟠 Medium / 🔴 High risk classification  
- 💻 Interactive web dashboard (Flask + HTML/CSS)  
- ⚡ Lightweight & fast predictions  
- 🧠 Hybrid ML approach  

---

## 🛠️ Tech Stack

- **Backend:** Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Machine Learning:** scikit-learn  
- **Data Processing:** NumPy, Pandas  
- **Visualization:** Seaborn, Matplotlib  
- **Model Storage:** Pickle  

---

## 🧠 Machine Learning Models Used

### 1. Isolation Forest
- Detects anomalies by isolating data points  
- Works well for fraud detection in imbalanced datasets  

### 2. Local Outlier Factor (LOF)
- Detects density-based anomalies  
- Helps identify unusual behavior patterns  

### 3. Hybrid Scoring System
- Combines multiple model outputs  
- Produces a final fraud risk score  

---

---

## 📊 Input Features

The model uses 5 key features:

- `V2` → Behavior Score  
- `V4` → Location Risk  
- `V11` → Frequency Score  
- `V17` → Device Risk  
- `Amount` → Transaction Amount  

---

## ⚙️ How It Works

1. User inputs transaction data  
2. Data is sent to Flask backend  
3. Model predicts anomaly score  
4. Risk score is calculated  
5. UI displays fraud level  

---

## 🧪 Model Training

- **Dataset:** Credit Card Fraud Dataset  
- **Sample size:** 40,000 rows  
- **Preprocessing:**  
  - Scaling (StandardScaler)  
  - Feature engineering  
- **Models trained:**  
  - Isolation Forest  
  - LOF  
  - DBSCAN (experimental)  

---


