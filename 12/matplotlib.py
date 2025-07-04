
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Alice'],
    'Age': [25, np.nan, 35, 45, np.nan, 29, 33, 22, 39, 25],
    'Salary': [50000, 60000, 70000, 80000, 90000, 1000000, 65000, np.nan, 72000, 60000],
    'Gender': ['F', 'M', 'M', 'M', 'F', np.nan, 'F', 'M', 'F', 'F'],
    'Email': [
        'alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com',
        'eva@example.com', 'frank@example.com', 'grace@example.com', 'henry@example.com',
        'ivy@example.com', 'alice@example.com'  # duplicate email
    ],
    'Country': ['USA', np.nan, np.nan, np.nan, np.nan, 'Slovenia', 'Slovakia', 'Slovenianstan', np.nan, 'USA']
}

df = pd.DataFrame(data)


plt.boxplot(df['Salary'])
plt.title('Boxplot of Salary')
plt.show()