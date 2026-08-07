import pandas as pd

sample = pd.read_csv("dataset/sample_messages.csv")

print(sample.head(15))

print("\nColumns:")
print(sample.columns.tolist())