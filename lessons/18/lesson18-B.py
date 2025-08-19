# Dataset
data = {
    'Model': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu'],
    'Price': [15000, 18000, 20000, 22000, 25000, 27000, 30000, 32000, 35000, 40000, 28000, 23000],
    'Expenses': [12300, 16700, 19800, 21000, 23500, 20000, 25670, 30040, 32700, 37800, 26000, 22000],
    'Sales': [800, 750, 500, 450, 400, 380, 300, 250, 200, 150, 360, 420],
    'Rating': [4.5, 4.2, 4.8, 4.0, 3.9, 3.8, 3.5, 3.4, 3.2, 3.0, 3.6, 4.1],
    'Type': ['Hatchback', 'Hatchback', 'Sedan', 'Sedan', 'SUV', 'SUV', 'SUV', 'Truck', 'Truck', 'Truck', 'SUV', 'Sedan'],
    'Country': ['Japan', 'Japan', 'Germany', 'Germany', 'USA', 'USA', 'USA', 'USA', 'Japan', 'Germany', 'USA', 'Germany'],
    'LaunchDate': pd.to_datetime(['2021-01-01', '2021-03-01', '2021-05-01', '2021-06-01',
                                   '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01',
                                   '2021-11-01', '2021-12-01', '2022-01-01', '2022-02-01'])
}
 
df = pd.DataFrame(data)


# 1. Multi-axis Plot (Price vs Sales)
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

 
# 2. Boxplot using Matplotlib only
types = df['Type'].unique()
types.sort()
data_to_plot = [df[df['Type'] == t]['Price'] for t in types]


plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=types)
plt.title("Price Distribution by Vehicle Type")
plt.xlabel("Type")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# 3. Heatmap using Matplotlib only
numeric_df = df.select_dtypes(include='number')
corr = numeric_df.corr().values
labels = numeric_df.columns


fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(corr, cmap='coolwarm')
fig.colorbar(cax)


ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha='left')
ax.set_yticklabels(labels)
 

# Annotate correlation values
for i in range(len(labels)):
    for j in range(len(labels)):
        ax.text(j, i, f"{corr[i, j]:.2f}", va='center', ha='center', color='black')
plt.title("Correlation Heatmap", pad=20)
plt.tight_layout()
plt.show()