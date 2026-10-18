df2 = pd.read_excel("/content/Sales_Analysis_Final_Project_RAW.xlsx")

df2 = df2.drop_duplicates()

df2.rename(columns={"ï»¿OrderID" : "OrderID"}, inplace=True)

df2["Region"] = df2["Region"].fillna("Unknown")
df2["Customer"] = df2["Customer"].fillna("Unknown")
df2["UnitPrice"] = df2["UnitPrice"].fillna(df2["UnitPrice"].mean())
df2["Discount"] = df2["Discount"].fillna(df2["Discount"].mean())
df2["Region"] = df2["Region"].str.title()
df2["Category"] = df2["Category"].str.title()
df2.sort_values("Date", inplace=True)

df2["Cost"] = df2["Sales"] - df2["Profit"]

df2.to_excel("clean_sales.xlsx")
