import pandas as pd

df = pd.read_csv("data/raw/final_shop_6modata.csv")

print(df.head())
print("\nColumns:", df.columns.tolist())
print("\nShape:", df.shape)
