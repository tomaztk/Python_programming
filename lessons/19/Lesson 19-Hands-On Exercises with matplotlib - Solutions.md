### Lesson 19 — Hands-On Exercises with **Matplotlib**


### **Solutions (Code Examples)**

```python
import matplotlib.pyplot as plt

# 1
plt.plot(df['Model'], df['Sales'])
plt.title('Sales Over Models')
plt.xlabel('Model')
plt.ylabel('Sales')
plt.show()

# 2
plt.bar(df['Model'], df['Price'])
plt.title('Price per Model')
plt.show()

# 3
plt.barh(df['Model'], df['Sales'])
plt.title('Sales per Model (Horizontal)')
plt.show()

# 4
plt.scatter(df['Price'], df['Sales'])
plt.title('Price vs Sales')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.show()

# 5
plt.hist(df['Rating'])
plt.title('Histogram of Ratings')
plt.show()

# 6
plt.boxplot(df['Price'])
plt.title('Boxplot of Price')
plt.show()

# 7
df['Type'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Vehicle Type Distribution')
plt.ylabel('')
plt.show()

# 8
df.groupby('Type')['Price'].mean().plot.bar()
plt.title('Average Price per Type')
plt.show()

# 9
plt.plot(df['LaunchDate'], df['Sales'])
plt.title('Sales Over Launch Dates')
plt.show()

# 10
df['Country'].value_counts().plot.bar()
plt.title('Number of Models per Country')
plt.show()

# 11
plt.scatter(df['Price'], df['Sales'], c=pd.factorize(df['Type'])[0])
plt.title('Price vs Sales Colored by Type')
plt.show()

# 12
df.groupby(['Country', 'Type'])['Sales'].sum().unstack().plot(kind='bar')
plt.title('Sales by Country and Type')
plt.show()

# 13
df.groupby(['Country', 'Type'])['Sales'].sum().unstack().plot(kind='bar', stacked=True)
plt.title('Stacked Sales by Type per Country')
plt.show()

# 14
for t, group in df.groupby('Type'):
    plt.plot(group['LaunchDate'], group['Sales'], label=t)
plt.legend()
plt.title('Sales Trends by Type')
plt.show()

# 15
plt.scatter(df['Price'], df['Sales'], s=df['Rating']*20)
plt.title('Scatter with Rating as Marker Size')
plt.show()

# 16
df['Country'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Country-wise Model Share')
plt.ylabel('')
plt.show()

# 17
plt.hist(df['Price'], bins=5)
plt.title('Histogram of Prices (5 Bins)')
plt.show()

# 18
df.boxplot(column='Rating', by='Type')
plt.title('Boxplot of Ratings by Type')
plt.suptitle('')
plt.show()

# 19
plt.scatter(df['Price'], df['Sales'], c=df['Rating'], cmap='viridis')
plt.colorbar(label='Rating')
plt.title('Sales vs Price Colored by Rating')
plt.show()

# 20
df.sort_values('LaunchDate', inplace=True)
plt.plot(df['LaunchDate'], df['Sales'].cumsum())
plt.title('Cumulative Sales Over Time')
plt.show()

# 21
bars = plt.bar(df['Model'], df['Sales'])
plt.title('Sales with Annotations')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
plt.show()

# 22
df['RollingSales'] = df['Sales'].rolling(3).mean()
plt.plot(df['LaunchDate'], df['Sales'], label='Actual')
plt.plot(df['LaunchDate'], df['RollingSales'], label='Rolling Avg')
plt.legend()
plt.title('Sales with Rolling Average')
plt.show()

# 23
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(df['LaunchDate'], df['Price'], 'g-')
ax2.plot(df['LaunchDate'], df['Sales'], 'b-')
ax1.set_xlabel('Launch Date')
ax1.set_ylabel('Price', color='g')
ax2.set_ylabel('Sales', color='b')
plt.title('Dual Axis Plot')
plt.show()

# 24
import seaborn as sns
sns.heatmap(df[['Price', 'Sales', 'Rating']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 25
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].bar(df['Model'], df['Sales'])
axs[0, 0].set_title('Sales per Model')
axs[0, 1].scatter(df['Price'], df['Sales'])
axs[0, 1].set_title('Price vs Sales')
axs[1, 0].hist(df['Rating'])
axs[1, 0].set_title('Histogram of Ratings')
df['Type'].value_counts().plot.pie(ax=axs[1, 1], autopct='%1.1f%%')
axs[1, 1].set_title('Vehicle Type Distribution')
plt.tight_layout()
plt.show()
```


