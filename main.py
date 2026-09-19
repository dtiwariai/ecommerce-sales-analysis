import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/ecommerce_sales.csv")

# Display the first few rows of the dataset
print(df.head())

# Display the last few rows of the dataset
print(df.tail())

# Display the shape of the dataset
print("Shape:", df.shape)

# Display the column names
print("Columns:", df.columns)

# Display the data types and missing values
print(df.info())

# Display basic statistics
print("Basic Statistics:")
print(df.describe())

# Data Cleaning

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates rows
print("\nDuplicates Rows:")
print(df.duplicated().sum())

# Check unique values in important columns
print("\nCategories:")
print(df['Category'].unique())

print("\nRegions:")
print(df['Region'].unique())

# Remove duplicates rows
df = df.drop_duplicates()

print("Duplicates after removal:", df.duplicated().sum())

# Fill missing region values
df['Region'] = df['Region'].fillna('Unknown')

# Fill missing discount values
df['Discount'] = df['Discount'].fillna(0)

# Recalculate missing sales values
df["Sales"] = df["Sales"].fillna(df["Unit_Price"] * df["Quantity"] * (1 - df["Discount"]))

# Check missing values again
print("\nMissing Values after cleaning:")
print(df.isnull().sum())

# ==============================
# Data Analysis
# ==============================

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Total Quantity Sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# Average Sales Per Order
average_sales = df["Sales"].mean()
print("Average Sales Per Order:", average_sales)

# Highest Sales
highest_sales = df["Sales"].max()
print("Highest Single Order Sales:", highest_sales)

# Lowest Sales
lowest_sales = df["Sales"].min()
print("Lowest Single Order Sales:", lowest_sales)

# ==============================
# Category-Wise Analysis
# ==============================

# Category-Wise Sales
category_sales = df.groupby("Category")["Sales"].sum()
print("\nCategory-Wise Sales:")
print(category_sales)

# ==============================
# Region-Wise Analysis
# ==============================

# Region-Wise Sales
region_sales = df.groupby("Region")["Sales"].sum()
print("\nRegion-Wise Sales:")
print(region_sales)

# ==============================
# Top 10 Products by Sales
# ==============================

# Top 10 Products by Sales
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Sales:")
print(top_products)

# ==============================
# Category-Wise Sales Chart 
# ==============================

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(10, 6))

plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ==============================
# Monthly sales analysis 
# ==============================

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Month column
df["Month"] = df["Order_Date"].dt.to_period("M")

# Calculate monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Line chart
plt.figure(figsize=(12, 6))

plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ==============================
# Sales Distribution 
# ==============================

plt.figure(figsize=(10, 6))

sns.histplot(df["Sales"], bins=30, kde=True)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()

# ==============================
# Category-Wise Sales Box Plot 
# ==============================

plt.figure(figsize=(10, 6))

sns.boxplot(x="Category", y="Sales", data=df)

plt.title("Sales Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ==============================
# Discount vs Sales
# ==============================

plt.figure(figsize=(10, 6))

sns.scatterplot(x="Discount", y="Sales", data=df)

plt.title("Discount vs Sales")
plt.xlabel("Discount")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ==============================
# Numpy Statistics Analysis
# ==============================

sales = df["Sales"].dropna().to_numpy()

print("\nNumpy Analysis:")

print("Mean Sales:", np.mean(sales))

print("Median Sales:", np.median(sales))

print("Minimum Sales:", np.min(sales))

print("Maximum Sales:", np.max(sales))

print("Standard Deviation:", np.std(sales))

print("25th Percentile:", np.percentile(sales, 25))

print("50th Percentile:", np.percentile(sales, 50))

print("75th Percentile:", np.percentile(sales, 75))

# ==============================
# Category-Wise Profit 
# ==============================

category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("\nCategory-Wise Profit:")
print(category_profit)

plt.figure(figsize=(10, 6))

sns.barplot(x=category_profit.index, y=category_profit.values)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ==============================
# Region-Wise Profit 
# ==============================

region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

print("\nRegion-Wise Profit:")
print(region_profit)

plt.figure(figsize=(10, 6))

sns.barplot(x=region_profit.index, y=region_profit.values)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.tight_layout()
plt.show()

# ==============================
# Category vs Sales and Profit 
# ==============================

category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()

print(category_summary)

plt.figure(figsize=(10, 6))

sns.barplot(data=category_summary.reset_index(), x="Category", y="Sales")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=category_summary.reset_index(), x="Category", y="Profit")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# Sales vs Profit Relationship 
# ==============================

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x="Sales", y="Profit")

plt.title("Sales vs Profit")
plt.xlabel("Sales") 
plt.ylabel("Profit")

plt.tight_layout()
plt.show()

# ==============================
# Sales Distribution by Category 
# ==============================

plt.figure(figsize=(10, 6))

sns.boxenplot(data=df, x="Category", y="Sales")
plt.title("Sales Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# Correlation Heatmap 
# ==============================

numeric_df = df.select_dtypes(include="number")

print(numeric_df.columns)

correlation = numeric_df.corr()

print(correlation)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

# ==============================
# Region + Category Analysis 
# ==============================

plt.figure(figsize=(12, 6))

sns.barplot(data=df, x="Region", y="Sales", hue="Category")

plt.title("Sales by Region and Category")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ==============================
# Final Seaborn Dashboard-Style Figure 
# ==============================

plt.figure(figsize=(12, 6))

sns.countplot(data=df, x="Category")

plt.title("Number of Orders by Category")
plt.xlabel("Category")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n===== BUSINESS INSIGHTS =====")

# Top Category
top_category = df.groupby("Category")["Sales"].sum().idxmax()
print("1. Top Sales Category:", top_category)

# Top Region
top_region = df.groupby("Region")["Sales"].sum().idxmax()
print("2. Top Sales Region:", top_region)

# Top Product
top_product = df.groupby("Product")["Sales"].sum().idxmax()
print("3. Top Selling Product:", top_product)

# Most Profitable Category
top_profit_category = df.groupby("Category")["Profit"].sum().idxmax()
print("4. Most Profitable Category:", top_profit_category)

# Average Order Value
average_order_value = df["Sales"].mean()
print("5. Average Order Value:", round(average_order_value, 2))

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

profit_margin = (total_profit / total_sales) * 100

print("Profit Margin:", round(profit_margin, 2), "%")

category_data = df.groupby("Category")[["Sales", "Profit"]].sum()

category_data["Profit_Margin"] = (
    category_data["Profit"] / category_data["Sales"]
) * 100

print("\nCategory-wise Profit Margin:")
print(category_data.sort_values("Profit_Margin", ascending=False))

# ==============================
# Export Clean Data For Power BI  
# ==============================

output_path = "data/ecommerce_sales_clean.csv"

df.to_csv(output_path, index=False)

print("\nClean dataset exported successfully")
print("File:", output_path)
print("Final Shape:", df.shape)