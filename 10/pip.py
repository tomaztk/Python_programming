import pandas as pd

data = {
    "Product": ["A", "B", "C"],
    "Region": ["East", "West", "North"],
    "Sales": [1000, 850, 920]
}
df = pd.DataFrame(data)

df.to_excel("data/sales_data_v2.xlsx", sheet_name="Quarter1", index=False)