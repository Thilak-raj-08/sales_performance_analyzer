import pandas as pd

df = pd.read_csv("sales_performance_data.csv")
print(df.head(5))
print(df.shape)
print(df.dtypes)
df.info()

region_revenue = df.groupby("Region")["Revenue"].sum()
print(region_revenue)

category_revenue = df.groupby("Category")["Revenue"].sum()
print(category_revenue)

salesperson_profit = df.groupby("Salesperson")["Profit"].sum()
print(salesperson_profit)

top_salesperson = salesperson_profit.idxmax()
print(top_salesperson)
print(salesperson_profit.loc[top_salesperson])

best_region = region_revenue.idxmax()
print(best_region)
print(region_revenue.loc[best_region])

best_category = category_revenue.idxmax()
print(best_category)
print(category_revenue.loc[best_category])

region_profit = df.groupby("Region")["Profit"].sum()
print(region_profit)
ranked_regions = region_profit.sort_values(ascending=False)
print(ranked_regions)