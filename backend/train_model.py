import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

regions = ["chennai", "madurai", "coimbatore"]

os.makedirs("models", exist_ok=True)

for region in regions:
    df = pd.read_csv(f"data/{region}.csv")

    X = df[["temperature", "humidity", "windSpeed", "pressure"]]
    y = df["rain"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    with open(f"models/{region}.pkl", "wb") as f:
        pickle.dump(model, f)

    print(f"✅ {region} model trained")

