# E-Commerce Sales Analysis

## Project Overview

This project analyzes e-commerce sales data to understand sales performance, profitability, customer behavior, location-wise performance, and monthly sales trends.

The analysis was performed using Python and common data analysis libraries.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL (Basic)

## Dataset

The dataset contains e-commerce order information including:

- Order details
- Customer information
- Location
- Product categories
- Sales amount
- Profit
- Quantity
- Monthly sales targets

## Analysis Performed

### 1. Data Cleaning
- Removed completely empty rows
- Converted order dates into datetime format
- Converted sales target dates into monthly periods
- Checked for duplicate records

### 2. Business Performance
Calculated:

- Total sales
- Total profit
- Total quantity sold
- Overall profit margin

### 3. Category Analysis
Analyzed sales, profit, quantity, and profit margin by product category.

### 4. Sub-Category Analysis
Identified the most profitable and loss-making sub-categories.

### 5. Location Analysis
Analyzed sales and profit by:

- State
- City

### 6. Monthly Analysis
Analyzed monthly sales and profit trends.

### 7. Sales Target Analysis
Compared actual monthly sales with the assigned sales targets.

### 8. Customer Analysis
Analyzed:

- Top customers by sales
- Customers with the highest number of orders
- Most profitable customers
- Loss-making customers

## Key Insights

- Total sales were approximately ₹4.32 lakh.
- Total profit was approximately ₹23,955.
- Overall profit margin was 5.55%.
- Clothing was the most profitable category.
- Furniture had the lowest category profit margin.
- Tables were the biggest loss-making sub-category.
- Maharashtra generated the highest state-level profit.
- Tamil Nadu had the lowest state-level profit.
- Pune was the most profitable city.
- November 2018 was the most profitable month.
- June 2018 was the least profitable month.
- January 2019 had the highest sales target achievement at 141.24%.

## Project Files

- `analysis.py` — Python analysis code
- `List of Orders.csv` — Order information
- `Order Details.csv` — Product sales and profit information
- `Sales target.csv` — Monthly sales targets

## Conclusion

The analysis shows that sales volume does not always result in higher profitability. Certain categories, products, customers, and locations generated significantly better profits than others.

The analysis can help a business identify profitable products and customers while investigating loss-making areas.