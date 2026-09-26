import pandas as pd
import matplotlib.pyplot as plt

# Load Superstore dataset
df = pd.read_csv("Sample_Superstore_Top10.csv")

# Calculate total sales for each product
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Display Top 10 products
print("Top 10 Products by Sales:")
print(top_products)

# Create chart
plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.tight_layout()

# Save chart
plt.savefig("top_10_products.png")
plt.show()
