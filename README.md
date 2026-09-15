# E-Commerce Sales Data Analysis

## Project Overview

This project analyzes e-commerce sales data using Python and popular data analysis and visualization libraries.

The goal is to understand sales performance, profit, customer orders, product performance, and regional trends.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Dataset

The dataset contains e-commerce order information including:

- Order ID
- Order Date
- Customer ID
- Product
- Category
- Region
- Quantity
- Unit Price
- Discount
- Sales
- Profit

## Data Cleaning

The following data cleaning techniques were performed:

- Checked for missing values
- Removed duplicate rows
- Filled missing region values
- Handled missing discount values
- Recalculated missing sales values
- Converted Order Date into datetime format

## Exploratory Data Analysis

The following analyses were performed:

- Total Sales
- Total Profit
- Total Quantity Sold
- Average Order Value
- Category-wise Sales
- Region-wise Sales
- Top 10 Products by Sales
- Monthly Sales Trend
- Sales Distribution
- Category-wise Profit
- Region-wise Profit
- Sales vs Profit
- Discount vs Sales
- Correlation Analysis

## Data Visualization

The project uses:

- Bar Charts
- Line Charts
- Histograms
- Box Plots
- Scatter Plots
- Correlation Heatmaps

## Key Business Insights

- Electronics is the highest-selling category.
- Laptop is the top-selling product.
- The East region has the highest sales.
- Sales and profit show a positive relationship.
- Some high-value orders appear as outliers.

## Project Structure

```text
ecommerce-sales-analysis/
│
├── data/
│   └── ecommerce_sales.csv
│
├── main.py
│
├── requirements.txt
│
└── README.md