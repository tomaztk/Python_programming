# Part I
import pandas as pd

data = [10, 20, 30, 40]
labels = ['a', 'b', 'c', 'd']



data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}

df = pd.DataFrame(data)
print(df)





import pandas as pd
import polars as pl
           
dfp = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NYC", "LA", "Chicago"]
})

print(dfp)


dfp2 = pl.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NYC", "LA", "Chicago"]
})

print(dfp2)
