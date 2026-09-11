import pandas as pd
df=pd.read_csv('orders.csv')
ch = [~df["country"].isin(["USA","Sweden","Brazil"])]
df["Country"] = df["Country"].str.upper()
df.rename(columns={"OrderID": "Order ID"},inplace=True)
df[~df["Product"].isin(["Headphones", "Laptop"])]


print(ch)

#py = [(df["Category","product"])]