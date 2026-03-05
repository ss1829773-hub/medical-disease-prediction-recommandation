import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Example dataset
data = {
    "fever": [1,1,0,1],
    "cough": [1,0,1,1],
    "headache": [0,1,1,1],
    "disease": ["Flu","Malaria","Cold","Dengue"]
}

df = pd.DataFrame(data)

# Split symptoms and disease
X = df.drop("disease", axis=1)
y = df["disease"]

# Train model
model = DecisionTreeClassifier()
model.fit(X,y)

# Save model
joblib.dump(model, "model/disease_model.pkl")

print("Model trained successfully!")