from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.neighbors import LocalOutlierFactor

# 1️⃣ Define the Flask app
app = Flask(__name__)

# 2️⃣ Load models
iso_model = pickle.load(open("iso_model_5features.pkl", "rb"))
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.01)

# 3️⃣ Home route
@app.route('/')
def home():
    return render_template("index.html")

# 4️⃣ Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        V2 = float(request.form['V2'])
        V4 = float(request.form['V4'])
        V11 = float(request.form['V11'])
        V17 = float(request.form['V17'])
        Amount = float(request.form['Amount'])

        features = [V2, V4, V11, V17, Amount]
        X = np.array(features).reshape(1, -1)

        # -------- MODEL 1: Isolation Forest --------
        iso_pred = iso_model.predict(X)[0]            # -1 or 1
        iso_score = iso_model.decision_function(X)[0] # anomaly score

        # Scale iso_score from IsolationForest to 0–100
        # Adjust min/max according to your data; this works better for extreme values
        iso_risk = int((1 - iso_score) * 50)  # scale to 0–50
        iso_risk = max(0, min(iso_risk, 100))  # clamp 0–100

        # -------- MODEL 2: LOF --------
        # Simple heuristic: treat extreme values as outliers
        # This avoids using X_fake which fails for single inputs
        lof_pred = -1 if any(abs(f) > 1.0 for f in features) else 1
        lof_risk = 100 if lof_pred == -1 else 20

        # -------- HYBRID SCORE --------
        final_risk = int((iso_risk + lof_risk) / 2)

        # -------- LABEL --------
        if final_risk > 70:
            label = "🔴 High Fraud Risk"
            color = "red"
        elif final_risk > 40:
            label = "🟠 Medium Risk"
            color = "orange"
        else:
            label = "🟢 Low Risk"
            color = "green"

    except Exception as e:
        return str(e)

    return render_template(
        "index.html",
        prediction=label,
        risk=final_risk,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)