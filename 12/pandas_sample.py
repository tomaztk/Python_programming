import pandas as pd
import numpy as np

# Sample data
data = {
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT', 'IT', 'IT', 'Sales', 'HR', np.nan],
    'Employee': ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Salary': [70000, 80000, 50000, 52000, 75000, np.nan, 72000, 68000, 51000, 60000],
    'YearsAtCompany': [3, 2, 5, 4, 3, 2, 5, 1, np.nan, 3],
    'FullTime': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)



# Grouped
grouped = df.groupby('Department').agg({'Salary':'count', 'YearsAtCompany':'mean'})
#print(grouped)

grouped2 = df.groupby('Department').agg({'Salary':'count', 'YearsAtCompany':'mean'}).reset_index()
#print(grouped2)

grouped3 = df.groupby('Department')[['Salary', 'YearsAtCompany']].mean()
#print(grouped3)

dfc = df.copy()
# dfc['Salary'] = dfc['Salary'].fillna(dfc['Salary'].mean(), inplace=True) 
dfc['Salary'].fillna(dfc['Salary'].mean(), inplace=True) 
dfc['YearsAtCompany'] = dfc['YearsAtCompany'].fillna(0)

#print(dfc)

# some shit stats
agg_stats = dfc.groupby('Department').agg({

     'Salary':['mean', 'max','count'],
     'YearsAtCompany':['mean','count']
}).reset_index()

#print(agg_stats)


sort3 = dfc.sort_values(by='Salary', ascending=False).head(3)
print(sort3)



#### Complex sample


import pandas as pd
import numpy as np

np.random.seed(2908)

departments = ['Sales', 'HR', 'IT', 'Finance']
regions = ['North', 'South', 'East', 'West']
titles = ['Analyst', 'Manager', 'Executive', 'Intern']

n = 30
df_complex = pd.DataFrame({
    'EmployeeID': range(1001, 1001 + n),
    'Name': np.random.choice(['Elza', 'Bob', 'Karolina', 'David', 'Eve', 'Frank', 'Blažena', 'Hajdi', 'Ivan', 'Joži'], n),
    'Department': np.random.choice(departments, n),
    'Region': np.random.choice(regions, n),
    'JobTitle': np.random.choice(titles, n),
    'Salary': np.random.randint(45000, 120000, n).astype(float),
    'BonusPercent': np.random.uniform(0.05, 0.2, n),
    'StartDate': pd.to_datetime('2015-01-01') + pd.to_timedelta(np.random.randint(0, 3000, n), unit='D'),
    'FullTime': np.random.choice(['Yes', 'No'], n, p=[0.85, 0.15])
})

#add random shiiiiit
df_complex.loc[np.random.choice(df_complex.index, 3), 'Salary'] = np.nan
df_complex.loc[np.random.choice(df_complex.index, 2), 'Region'] = None

print(df_complex.head())




pivot = pd.pivot_table(df_complex,
                       values='Salary',
                       index='Department',
                       columns='Region',
                       aggfunc='mean')

# print(pivot)


def salary_range(x):
    return x.max() - x.min()



custom_agg = df_complex.groupby('JobTitle').agg(
    Avg_Salary=('Salary', 'mean'),
    Salary_Range=('Salary', salary_range),
    Median_Bonus=('BonusPercent', 'median'),
    Count=('EmployeeID', 'count')
)

# print(custom_agg)


df_cleaned = df_complex.copy()
df_cleaned['Salary'] = df_cleaned['Salary'].fillna(df_cleaned['Salary'].median())
df_cleaned['Region'] = df_cleaned['Region'].fillna('Unknown')
df_cleaned['JobTitle'] = df_cleaned['JobTitle'].str.title().str.strip()

# print(df_cleaned.isnull().sum()) # če je vse 0 potem ok


high_performer = df_complex[(df_complex['BonusPercent'] > 0.10) & (df['Salary'] > 50000)]
# print(list(high_performer['Name']))



df_complex['DeptAvgSalary'] = df_complex.groupby('Department')['Salary'].transform('mean')

# print(df_complex)

df_complex['AboveDeptAvg'] = df_complex['Salary'] > df_complex['DeptAvgSalary']

# print(df_complex[['EmployeeID', 'Department', 'Salary', 'DeptAvgSalary', 'AboveDeptAvg']].head())



today = pd.Timestamp.today()
df_complex['TenureYears'] = (today - df_complex['StartDate']).dt.days / 365

# print(df_complex[['EmployeeID', 'StartDate', 'TenureYears']].head())




## slicing, subsetting, bla bla bla

# print(df_complex[['Name', 'Department', 'Salary']])
# print(df_complex[df_complex['Department'] == 'IT'])
# print(df_complex[df_complex['Salary'] > 100000])
# print(df_complex[(df_complex['Department'] == 'IT') & (df_complex['Region'] == 'North')])
# print(df_complex[(df_complex['FullTime'] == 'Yes') & (df_complex['Salary'].between(80000, 100000))])
# print(df_complex.loc[5:10, ['Name', 'Salary']])
# print(df_complex.iloc[5:10, 1:4])
# print(df_complex[df_complex['Department'].isin(['HR', 'Sales'])])
# print(df_complex[df_complex['JobTitle'].isin(['Manager', 'Analyst'])])
# print(df_complex[~(df_complex['Department'] == 'Finance')])
# print(df_complex[df_complex['Name'].str.startswith('A')])
# print(df_complex[df_complex['JobTitle'].str.contains('exec', case=False, na=False)])

# print(df_complex[df_complex['StartDate'] > '2020-01-01'])
# print(df_complex.nlargest(5, 'Salary')[['Name', 'Department', 'Salary']])
# print(df_complex.nsmallest(3, 'BonusPercent')[['Name', 'BonusPercent']])

print(df_complex[df_complex['Name'].str.match(r'^\w{4}$')])