import pandas as pd
df = pd.read_csv("Task-2/train.csv")
# print(df)
# I have already checked the data in powerBi by using of an Dax an queries
print(df.duplicated().any())

print(df.isnull().sum())
# but it contains null data in Postal Code     >> 11

df.fillna({"Postal Code": "Unknown"}, inplace=True)

df.to_csv("Cleaned_Superstore_Data.csv", index=False)