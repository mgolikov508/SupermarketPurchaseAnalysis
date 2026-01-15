import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
NUM_PURCHASES = 1000

# Data lists
categories = [
    "Fruits & Vegetables", "Dairy & Eggs", "Meat & Seafood", "Bakery",
    "Beverages", "Snacks", "Frozen Foods", "Household", "Personal Care"
]

products = {
    "Fruits & Vegetables": ["Apples", "Bananas", "Tomatoes", "Carrots", "Lettuce", "Oranges"],
    "Dairy & Eggs": ["Milk", "Cheese", "Yogurt", "Butter", "Eggs"],
    "Meat & Seafood": ["Chicken Breast", "Ground Beef", "Salmon", "Pork Chops", "Shrimp"],
    "Bakery": ["Bread", "Croissants", "Bagels", "Muffins", "Cake"],
    "Beverages": ["Water", "Juice", "Soda", "Coffee", "Tea"],
    "Snacks": ["Chips", "Cookies", "Nuts", "Chocolate", "Crackers"],
    "Frozen Foods": ["Ice Cream", "Pizza", "Vegetables", "French Fries", "Chicken Nuggets"],
    "Household": ["Detergent", "Paper Towels", "Trash Bags", "Dish Soap", "Sponges"],
    "Personal Care": ["Shampoo", "Toothpaste", "Soap", "Deodorant", "Tissues"]
}

payment_methods = ["Cash", "Credit Card", "Debit Card", "Mobile Payment"]
customer_types = ["Regular", "Member", "New"]

# Generate data
data = []
start_date = datetime.now() - timedelta(days=90)

for i in range(NUM_PURCHASES):
    category = random.choice(categories)
    product = random.choice(products[category])
    
    # Price based on category
    base_prices = {
        "Fruits & Vegetables": (1, 8),
        "Dairy & Eggs": (2, 12),
        "Meat & Seafood": (8, 25),
        "Bakery": (2, 10),
        "Beverages": (1, 6),
        "Snacks": (2, 8),
        "Frozen Foods": (3, 12),
        "Household": (3, 15),
        "Personal Care": (3, 18)
    }
    
    price_range = base_prices[category]
    unit_price = round(random.uniform(price_range[0], price_range[1]), 2)
    quantity = random.randint(1, 5)
    total = round(unit_price * quantity, 2)
    
    payment = random.choice(payment_methods)
    customer_type = random.choice(customer_types)
    
    # Random date within last 90 days
    purchase_date = start_date + timedelta(days=random.randint(0, 90))
    
    data.append({
        "Purchase ID": f"PUR{i+1:05d}",
        "Date": purchase_date.strftime("%Y-%m-%d"),
        "Time": f"{random.randint(8, 21):02d}:{random.randint(0, 59):02d}",
        "Category": category,
        "Product": product,
        "Unit Price": unit_price,
        "Quantity": quantity,
        "Total": total,
        "Payment Method": payment,
        "Customer Type": customer_type
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = "supermarket_data.xlsx"
df.to_excel(output_file, index=False, sheet_name="Purchases")

print(f"✅ Generated {NUM_PURCHASES} purchase records")
print(f"📁 Saved to: {output_file}")
print(f"\n📊 Summary:")
print(f"  - Categories: {df['Category'].nunique()}")
print(f"  - Products: {df['Product'].nunique()}")
print(f"  - Total revenue: ${df['Total'].sum():,.2f}")
print(f"  - Average purchase: ${df['Total'].mean():.2f}")
print(f"  - Date range: {df['Date'].min()} to {df['Date'].max()}")
