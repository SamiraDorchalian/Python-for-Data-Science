# import libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\ziggurat\\Desktop\\python for data science\\data.csv")

# print(df.head())
# print('---------------------')
# print(df.info())
# print('---------------------')
# print(df.describe())
# print('---------------------')
print("میانگین کرایه :", round(df["fare_amount"].mean(), 3))
print('---------------------')
print("میانگین مسافت :", df["trip_distance"].mean())
print('---------------------')
print("بیشترین کرایه :", df["fare_amount"].max())
print('------------------------------------------------------')
corr = df['trip_distance'].corr(df['fare_amount'])
print("میزان همبستگی بین کرایه و مسافت:", corr)
print('------------------------------------------------------')
#همبستگی ماتریسی بین چندستون
matrix_corr = df[["passenger_count", "trip_distance", "fare_amount", "tip_amount", "tolls_amount"]].corr()
print(matrix_corr)
print('---------------------')
plt.figure(figsize=(10,6))
sns.heatmap(matrix_corr, annot=True, cmap="coolwarm")
plt.title("Correlation")
# plt.show()
print('------------------------------------------------------')
# نمودار میله ای
sns.countplot(df, x="passenger_count")
plt.title("Count of passenger")
# plt.show()
print('---------------------')
# نمودار پراکندگی
sns.scatterplot(df, x='trip_distance', y='tip_amount')
plt.title('Scatter Plot')
# plt.show()
print('---------------------')
df['tpep_dropoff_datetime'] = pd.to_datetime(df["tpep_dropoff_datetime"])
df['tpep_pickup_datetime'] = pd.to_datetime(df["tpep_pickup_datetime"])
print(df.info())
print('------------------------------------------------------')
df["duration_minutes"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds() / 60
print(df)
print('---------------------')
df["speed"] = df["trip_distance"] / df["duration_minutes"]
print(df)
print('---------------------')
# sns.boxplot(df, x="pickup_location", y="speed")
# plt.show()
sns.boxplot(df, x="payment_type", y="fare_amount")
# plt.show()
# sns.pairplot(df, hue="payment_type")
# df["pickup_location"].value_counts().plot(kind="bar")
print('------------------------------------------------------')
avr_tips = df.groupby("dropoff_longitude")["tip_amount"].mean().sort_values(ascending=False)
print(avr_tips)
print('---------------------')
high_fare = df[df["total_amount"] > 50]
print(high_fare)
print('---------------------')
df["passenger_number"] = df["passenger_count"]
df.rename(columns={"passenger_count": "passenger_number"})
df[df["passenger_count"] == 1]
sns.histplot(df["fare_amount"], bins=60, color="pink", kde=True)
df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
print(df)
sns.countplot(df, x="pickup_hour", palette="coolwarm")
plt.title("Count of Hour")
# plt.show()
print('---------------------')
total_incom = df["total_amount"].sum()
round(total_incom)
print('---------------------')
total_tip = df["tip_amount"].sum()
print(total_tip)
print('---------------------')
df["payment_type"]= df["payment_type"].replace({"Cash": 0, "App Payment": 1, "Credit Card": 2})
print(df)
df['payment_type'].corr(df["tip_amount"])
print('---------------------')
df.groupby("payment_type")['tip_amount'].mean()


