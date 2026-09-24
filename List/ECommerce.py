#Filtering Expensive Products (Data Slicing & Comprehensions)

all_prices = [12.99, 23.50, 5.99, 45.00, 15.75, 9.99, 29.99, 49.95, 19.99]
budget_limit = 20.00

affordable_prices = [price for price in all_prices if price <= budget_limit]
print("Affordable Prices:", affordable_prices)