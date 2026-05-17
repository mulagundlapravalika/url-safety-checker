import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample dataset (URL features)
data = {
    "has_https": [1,0,1,0,1,0],
    "has_ip": [0,1,0,1,0,1],
    "has_at_symbol": [0,1,0,1,0,1],
    "label": [0,1,0,1,0,1]  # 0 = Safe, 1 = Malicious
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "url_model.pkl")

print("Model trained successfully")