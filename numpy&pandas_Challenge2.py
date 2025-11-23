import numpy as np
import pandas as pd

data = {
    "OrderId": [101,102,103,104,105],
    "CustomerId": [1,2,3,4,1],
    "Product": ["موبایل", "تلویزیون", "موبایل", "هدفون", "لبتاب"],
    "Price": [1500, 200, 800, 12500, 800],
    "Quantity": [1,2,3,2,1],
    "OrderDate": ["2023-01-15", "2023-01-16", "2023-01-16", "2023-01-17", None]
}
df = pd.DataFrame(data, index=[1,2,3,4,5])
# print(df)
# print('---------------------')
# print(df.head(2))
# print('---------------------')
# print(df.tail(2))
# print('---------------------')
# print(df.info())
# print('---------------------')
df.describe(include="all")
# print('---------------------')
# print(df.isna())
# print('---------------------')
# print(df.isna().sum())
# print('---------------------')
df["OrderDate"] = df["OrderDate"].fillna("2023-01-18")
# print(df.head())
# print('---------------------')
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
# print(df.info())
# print('---------------------')
# df = df.drop_duplicates("Product")
# print('---------------------')
df = df.rename(columns= {"Product": "ProductName"})
# print(df.head())
# print('---------------------')
# print(df["Price"])
# print('---------------------')
# print(df.loc[1])
# print('---------------------')
# print(df.iloc[1])
# print('---------------------')
# print(df.loc[df["ProductName"] == "لبتاب" , ["Price", "Quantity"]])
# print('---------------------')
# print(df.loc[df["Price"] > 800])
# print('---------------------')
# print(df.loc[df["Price"] > 800, ["OrderDate"]])
# print('---------------------')
# print(df['Price'] > 800)
# print('---------------------')
# print(df[df['Price'] > 800]['OrderDate'])
# print('---------------------')
df["TotalSales"] = df["Price"] * df["Quantity"]
# print('---------------------')
df["OrderMonth"] = df["OrderDate"].dt.month
# print('---------------------')
df['ProductName'] = df['ProductName'].replace({"موبایل" : "تلفن هوشمند"})
# print('---------------------')
df_sorted = df.sort_values(by="Quantity", ascending=False)
df_sorted.head()
# print('---------------------')
df.groupby('ProductName')['Quantity'].sum()
# print('---------------------')
df.groupby('ProductName')['Quantity'].count()
# print('---------------------')
df.groupby('ProductName')['TotalSales'].mean()
# print('---------------------')
df.groupby('ProductName').agg({
    "TotalSales": ["mean", "count", "sum", "std"],
    "CustomerId": "nunique"
})
# print('---------------------')
customers = pd.DataFrame({
    "CustomerId": [1,2,3,4],
    "CustomerName": ["Ali", "Zahra", "Amir", "Neda"],
    "City": ["Tehran", "Yazd", "Tehran", "Sari"],
    "Age": [20,38,16,58]
})
# print(customers)
# print('---------------------')
merged_df = pd.merge(df, customers, on="CustomerId")
print(merged_df)
print('---------------------')
print(df.join(customers, lsuffix='_caller', rsuffix='_other'))

