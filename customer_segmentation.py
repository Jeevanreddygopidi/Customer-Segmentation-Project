import pandas as pd

# Load the Excel file
file_path = 'Online Retail.xlsx'  # Adjust the path if necessary
df = pd.read_excel(file_path, engine='openpyxl')

# Explore the first few rows
print(df.head())

# Check for missing values and general information
print(df.info())

# Checking for missing values
print(df.isnull().sum())

# Drop rows with missing values if necessary
df_cleaned = df.dropna()

# Check the structure of the cleaned data
print(df_cleaned.info())

# Get basic statistical description of numerical data
print(df_cleaned.describe())

# Check unique values in relevant columns (e.g., Country, Product, etc.)
print(df_cleaned['Country'].unique())
print(df_cleaned['InvoiceNo'].nunique())  # Example: Checking for unique invoice numbers

# Create a new feature 'TotalPrice' (Quantity * UnitPrice)
df_cleaned['TotalPrice'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']

# Group data by 'CustomerID' and aggregate total spend and frequency
customer_data = df_cleaned.groupby('CustomerID').agg({
    'TotalPrice': 'sum',
    'InvoiceNo': 'nunique',  # Number of unique transactions (invoices)
    'Quantity': 'sum'
}).reset_index()

# Rename columns for clarity
customer_data.columns = ['CustomerID', 'TotalSpend', 'Frequency', 'TotalQuantity']

# Explore the new dataset
print(customer_data.head())

from sklearn.preprocessing import StandardScaler

# Select the features for clustering
features = ['TotalSpend', 'Frequency', 'TotalQuantity']

# Scale the data using StandardScaler
scaler = StandardScaler()
customer_data_scaled = scaler.fit_transform(customer_data[features])

# Check the first few rows of scaled data
print(customer_data_scaled[:5])

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Elbow method to find optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(customer_data_scaled)
    wcss.append(kmeans.inertia_)

# Plot the WCSS to visualize the elbow
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Assuming you choose 3 clusters based on the elbow method
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(customer_data_scaled)

# Check the distribution of customers across clusters
print(customer_data['Cluster'].value_counts())

import seaborn as sns

# Visualizing the clusters based on 'TotalSpend' and 'Frequency'
sns.scatterplot(x='TotalSpend', y='Frequency', hue='Cluster', data=customer_data, palette='Set1')
plt.title('Customer Segments Based on Spend and Frequency')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Visualize clusters using scatterplot
sns.scatterplot(x='TotalSpend', y='Frequency', hue='Cluster', data=customer_data, palette='Set1')
plt.title('Customer Segmentation Based on TotalSpend and Frequency')
plt.show()

cluster_analysis = customer_data.groupby('Cluster').agg({
    'TotalSpend': 'mean',
    'Frequency': 'mean',
    'TotalQuantity': 'mean'
})

print(cluster_analysis)

