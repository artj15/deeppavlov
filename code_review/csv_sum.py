import pandas as pd

df = pd.read_csv("data.csv", header=None)
print(df.values.sum() == 10)
