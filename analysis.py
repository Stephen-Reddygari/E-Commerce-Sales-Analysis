# =========================
# 1. Import Libraries
# =========================

import pandas as pd
import matplotlib.pyplot as plt


# =========================
# 2. Load Data
# =========================

orders = pd.read_csv("List of Orders.csv")
order_details = pd.read_csv("Order Details.csv")
sales_target = pd.read_csv("Sales target.csv")

# =========================
# 3. Data Cleaning
# =========================

orders = orders.dropna(how="all")

orders["Order Date"] = pd.to_datetime(
    orders["Order Date"],
    dayfirst=True
)

sales_target["Month of Order Date"] = pd.to_datetime(
    sales_target["Month of Order Date"],
    format="%b-%y"
).dt.to_period("M")

# =========================
# 4. Overall Business Performance
# =========================

total_sales = order_details["Amount"].sum()
total_profit = order_details["Profit"].sum()
total_quantity = order_details["Quantity"].sum()

profit_margin = (total_profit / total_sales) * 100

print("\nOverall Business Performance")
print("Total Sales: ₹", total_sales)
print("Total Profit: ₹", total_profit)
print("Total Quantity Sold:", total_quantity)
print("Profit Margin:", round(profit_margin, 2), "%")

# =========================
# 5. Category Analysis
# =========================

category_performance = order_details.groupby(
    "Category"
)[["Amount", "Profit", "Quantity"]].sum()

category_performance["Profit Margin (%)"] = (
    category_performance["Profit"] /
    category_performance["Amount"]
) * 100

print("\nCategory Performance")
print(category_performance.round(2))

plt.figure(figsize=(8, 5))

ax = category_performance["Amount"].plot(kind="bar")

for i, value in enumerate(category_performance["Amount"]):
    ax.text(i, value + 3000, f"₹{value:,.0f}", ha="center")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# =========================
# 6. Sub-Category Analysis
# =========================

subcategory_performance = order_details.groupby(
    "Sub-Category"
)[["Amount", "Profit", "Quantity"]].sum()

subcategory_performance["Profit Margin (%)"] = (
    subcategory_performance["Profit"] /
    subcategory_performance["Amount"]
) * 100

print("\nSub-Category Performance")
print(subcategory_performance.sort_values("Profit", ascending=False).round(2))

top_subcategories = subcategory_performance.sort_values(
    "Profit", ascending=False
).head(10)

plt.figure(figsize=(10, 6))

ax = top_subcategories["Profit"].plot(kind="bar")

for i, value in enumerate(top_subcategories["Profit"]):
    ax.text(i, value + 100, f"₹{value:,.0f}", ha="center")

plt.title("Top 10 Sub-Categories by Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit (₹)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

loss_subcategories = subcategory_performance[
    subcategory_performance["Profit"] < 0
].sort_values("Profit")

print("\nLoss-Making Sub-Categories")
print(loss_subcategories.round(2))

# =========================
# 7. State and City Analysis
# =========================

state_performance = orders.merge(
    order_details,
    on="Order ID"
)

state_performance = state_performance.groupby(
    "State"
)[["Amount", "Profit"]].sum()

print("\nState Performance")
print(state_performance.sort_values("Profit", ascending=False))

city_performance = orders.merge(
    order_details,
    on="Order ID"
)

city_performance = city_performance.groupby(
    "City"
)[["Amount", "Profit"]].sum()

print("\nCity Performance")
print(city_performance.sort_values("Profit", ascending=False))

city_profit = city_performance["Profit"].sort_values()

plt.figure(figsize=(10, 8))

city_profit.plot(kind="barh")

plt.title("Profit by City")
plt.xlabel("Profit (₹)")
plt.ylabel("City")

plt.tight_layout()
plt.show()

# =========================
# 8. Monthly Analysis
# =========================

orders["Month"] = orders["Order Date"].dt.to_period("M")

monthly_performance = orders.merge(
    order_details,
    on="Order ID"
)

monthly_performance = monthly_performance.groupby(
    "Month"
)[["Amount", "Profit"]].sum()

print("\nMonthly Sales and Profit")
print(monthly_performance)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_performance.index.astype(str),
    monthly_performance["Amount"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_performance.index.astype(str),
    monthly_performance["Profit"],
    marker="o"
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit (₹)")
plt.xticks(rotation=45)

plt.axhline(0, linewidth=1)

plt.tight_layout()
plt.show()

# =========================
# 9. Sales Target Analysis
# =========================

monthly_target = sales_target.groupby(
    "Month of Order Date"
)["Target"].sum()

monthly_comparison = monthly_performance.copy()

monthly_comparison["Target"] = monthly_target

monthly_comparison["Target Achievement (%)"] = (
    monthly_comparison["Amount"] /
    monthly_comparison["Target"]
) * 100

print("\nActual Sales vs Target")
print(monthly_comparison.round(2))

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_comparison.index.astype(str),
    monthly_comparison["Target Achievement (%)"],
    marker="o"
)

plt.title("Monthly Target Achievement")
plt.xlabel("Month")
plt.ylabel("Target Achievement (%)")
plt.xticks(rotation=45)

plt.axhline(100, linewidth=1)

plt.tight_layout()
plt.show()

# =========================
# 10. Customer Analysis
# =========================

customer_performance = orders.merge(
    order_details,
    on="Order ID"
)

customer_performance = customer_performance.groupby(
    "CustomerName"
)[["Amount", "Profit"]].sum()

print("\nTop 10 Customers by Sales")
print(
    customer_performance
    .sort_values("Amount", ascending=False)
    .head(10)
)

customer_orders = orders.groupby(
    "CustomerName"
)["Order ID"].count()

print("\nTop 10 Customers by Number of Orders")
print(
    customer_orders
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Profit")
print(
    customer_performance
    .sort_values("Profit", ascending=False)
    .head(10)
)

print("\nBottom 10 Customers by Profit")
print(
    customer_performance
    .sort_values("Profit")
    .head(10)
)

top_customers = customer_performance.sort_values(
    "Profit", ascending=False
).head(10)

plt.figure(figsize=(10, 6))

ax = top_customers["Profit"].plot(kind="bar")

for i, value in enumerate(top_customers["Profit"]):
    ax.text(i, value + 50, f"₹{value:,.0f}", ha="center")

plt.title("Top 10 Customers by Profit")
plt.xlabel("Customer")
plt.ylabel("Profit (₹)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# =========================
# 11. Final Business Insights
# =========================

best_category = category_performance["Profit"].idxmax()
worst_category = category_performance["Profit"].idxmin()

best_state = state_performance["Profit"].idxmax()
worst_state = state_performance["Profit"].idxmin()

best_city = city_performance["Profit"].idxmax()
worst_city = city_performance["Profit"].idxmin()

best_month = monthly_performance["Profit"].idxmax()
worst_month = monthly_performance["Profit"].idxmin()

best_target_month = monthly_comparison[
    "Target Achievement (%)"
].idxmax()

worst_target_month = monthly_comparison[
    "Target Achievement (%)"
].idxmin()

print("\nFinal Business Insights")

print("Best Category:", best_category)
print("Worst Category:", worst_category)

print("Best State:", best_state)
print("Worst State:", worst_state)

print("Best City:", best_city)
print("Worst City:", worst_city)

print("Most Profitable Month:", best_month)
print("Least Profitable Month:", worst_month)

print("Best Target Achievement Month:", best_target_month)
print("Worst Target Achievement Month:", worst_target_month)