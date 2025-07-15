# ZomEats Product Information System

print("Welcome to ZomEats Product Information System\n")

# Task 1: Take Product Details as Input

product_id = int(input("Enter Food Item ID: "))
product_name = input("Enter Food Item Name: ")
price = float(input("Enter Price (₹): "))

categories_input = input("Enter Categories (comma-separated): ")
categories = [cat.strip() for cat in categories_input.split(',')]

available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)

discount_percentage = float(input("Enter Discount Percentage: "))

features_input = input("Enter Food Features (comma-separated): ")
product_features = set(feat.strip() for feat in features_input.split(','))

supplier_name = input("Enter Restaurant Name: ")
supplier_contact = input("Enter Restaurant Contact Number: ")
supplier_location = input("Enter Restaurant Location: ")
supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

print("\n" + "="*50)
print("              ZomEats Product Summary ")
print("="*50 + "\n")

# Task 2: Display Using Different Formatting Methods

# 1. Using Comma Separation (sep=',')
print("Food ID, Name, Price:", product_id, product_name, price, sep=',')

# 2. Using Percentage Formatting (% operator)
print("Discount on Product: %.2f" % discount_percentage)

# 3. Using f-strings (f"")
print(f"\n Food Item: {product_name}")
print(f" Price: ₹{price}")
print(f" Stock Available: {stock_details[0]}")
print(f" Stock Sold: {stock_details[1]}")
print(f" Discount: {discount_percentage}%")
print(f" Categories: {', '.join(categories)}")
print(f" Features: {', '.join(product_features)}")

# 4. Using .format() method
print("\n Restaurant Info: Name - {name}, Contact - {contact}, Location - {location}".format(
    name=supplier_details["name"],
    contact=supplier_details["contact"],
    location=supplier_details["location"]
))

print("\n" + "="*50)
print("            Product Data Entry Complete  ")
print("="*50)

