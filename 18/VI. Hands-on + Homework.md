## **VI. Hands-on: Working with Data to Prepare 3 Different Plots**

Your task during this hands-on session is to practice combining the plotting skills you've learned.
You’ll work with our car dataset (the extended one from this lesson) and create the following plots.

---

### **A) Line Plot — Sales Trend Over Time**

```python
plt.plot(df['LaunchDate'], df['Sales'], marker='o', color='blue')
plt.title('Sales Trend Over Launch Dates')
plt.xlabel('Launch Date')
plt.ylabel('Sales')
plt.grid(True)

# Add average sales reference line
plt.axhline(y=df['Sales'].mean(), color='red', linestyle='--', label='Average Sales')
plt.legend()
plt.show()
```

** Practice Focus:**

* Time-series plotting
* Adding reference lines and legends
* Using dates as x-axis

---

### **B) Box Plot — Price Distribution by Car Type**

```python
sns.boxplot(x='Type', y='Price', data=df)
plt.title('Price Distribution by Car Type')
plt.grid(True)
plt.show()
```

** Practice Focus:**

* Category-wise distribution
* Understanding spread and outliers
* Using Seaborn with Matplotlib

---

### **C) Pie Chart — Market Share of Car Types**

```python
type_counts = df['Type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Market Share by Car Type')
plt.show()
```

**Practice Focus:**

* Visualizing proportions
* Customizing pie charts (start angle, labels)

---

### **D) BONUS Example — Combined Scatter + Reference + Annotation**

```python
plt.scatter(df['Price'], df['Sales'], color='green', label='Sales Data')
plt.title('Price vs Sales with Annotation')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)

# Reference line for average sales
plt.axhline(y=df['Sales'].mean(), color='red', linestyle='--', label='Average Sales')

# Annotate highest sale
best = df[df['Sales'] == df['Sales'].max()]
plt.annotate('Top Model', xy=(best['Price'].values[0], best['Sales'].values[0]),
             xytext=(best['Price'].values[0]+5000, best['Sales'].values[0]+100),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.legend()
plt.show()
```

** Practice Focus:**

* Combining scatter, reference lines, annotations, and legend

---

##  **VII. Homework Assignment (Optional or To Continue at Home)**

Using **any dataset you have** (or the provided car dataset), prepare the following visualizations:

 **1. Histogram of a Continuous Variable (e.g., Price or Sales)**

```python
plt.hist(df['Price'], bins=6, color='orange', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```

---

**2. Bar Chart Comparing Categories (e.g., Car Type vs Average Sales)**

```python
avg_sales_by_type = df.groupby('Type')['Sales'].mean()

plt.bar(avg_sales_by_type.index, avg_sales_by_type.values, color='purple')
plt.title('Average Sales by Car Type')
plt.xlabel('Car Type')
plt.ylabel('Average Sales')
plt.grid(axis='y')
plt.show()
```

---

**3. Scatter Plot of Two Continuous Variables (e.g., Price vs Sales) with Annotations**

```python
plt.scatter(df['Price'], df['Sales'], color='navy')
plt.title('Price vs Sales')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)

for i in range(len(df)):
    plt.text(df['Price'][i]+200, df['Sales'][i]+5, df['Model'][i], fontsize=8)

plt.show()
```

---

## **Bonus Challenge:**

* Create a function similar to `plot_with_reference()` that allows plotting **any two variables** with optional annotations and reference lines.
* Apply it to your dataset with different pairs of variables.

```python
fig, ax1 = plt.subplots(figsize=(10, 6))


color = 'tab:blue'
ax1.set_xlabel('Model')
ax1.set_ylabel('Price', color=color)
ax1.plot(df['Model'], df['Price'], marker='o', color=color, label='Price')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(df['Model'], rotation=45)


ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Sales', color=color)
ax2.plot(df['Model'], df['Sales'], marker='s', color=color, label='Sales')
ax2.tick_params(axis='y', labelcolor=color)


fig.tight_layout()
plt.title("Price vs Sales by Model")
plt.show()
```