import pandas as pd
import os

# Load dataset
df = pd.read_csv("weather.csv")

print("Total rows:", len(df))

os.makedirs("data", exist_ok=True)

# Split by index (SAFE)
n = len(df)
third = n // 3

df_chennai = df.iloc[:third]
df_madurai = df.iloc[third:2*third]
df_coimbatore = df.iloc[2*third:]

# Save
df_chennai.to_csv("data/chennai.csv", index=False)
df_madurai.to_csv("data/madurai.csv", index=False)
df_coimbatore.to_csv("data/coimbatore.csv", index=False)

print("Chennai rows:", len(df_chennai))
print("Madurai rows:", len(df_madurai))
print("Coimbatore rows:", len(df_coimbatore))

