# E-Commerce Sales Data Analysis

## Project Overview

This project analyzes e-commerce sales data using Python, data analysis libraries, and Microsoft Power BI.

The goal is to understand sales performance, profit, customer orders, product performance, and regional trends through data analysis and an interactive dashboard.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Microsoft Power BI
- Power Query
- DAX

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

The following data cleaning techniques were performed using Python and Pandas:

- Checked for missing values
- Removed duplicate rows
- Filled missing region values
- Handled missing discount values
- Recalculated missing sales values
- Converted Order Date into datetime format
- Exported the cleaned dataset for Power BI analysis

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
- Profit Margin Analysis

## Data Visualization

The Python analysis uses:

- Bar Charts
- Line Charts
- Histograms
- Box Plots
- Scatter Plots
- Correlation Heatmaps

## Power BI Dashboard

The cleaned dataset was imported into Microsoft Power BI to create an interactive sales dashboard.

### Power BI Features

- Data transformation using Power Query
- Date table creation
- Data modeling
- Relationship between Date Table and Sales Data
- DAX measures
- KPI Cards
- Interactive charts
- Slicers and filters
- Top 10 Products analysis

### DAX Measures

The dashboard includes measures for:

- Total Sales
- Total Profit
- Total Orders
- Total Quantity
- Average Order Value
- Profit Margin %

## Key Business Insights

- Electronics is the highest-selling category.
- Laptop is the top-selling product.
- The East region has the highest sales.
- Sales and profit show a positive relationship.
- Some high-value orders appear as outliers.
- The overall profit margin is approximately 17.6%.

## Project Structure

```text
ecommerce-sales-analysis/
│
├── data/
│   ├── ecommerce_sales.csv
│   └── ecommerce_sales_clean.csv
│
├── powerbi/
│   └── ecommerce_sales_dashboard.pbix
│
├── main.py
│
├── requirements.txt
│
└── README.md