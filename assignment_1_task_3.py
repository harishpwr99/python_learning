# Task 3: Product Pricing (Dictionaries)

# Create a dictionary price_dict where keys are product names and values are prices (integers or floats). Include at least 6 entries.
price_dict={"product_1":{"product_name":"laptop","price":15000},"product_2":{"product_name":"mouse","price":500},"product_3":{"product_name":"pendrive","price":1500},"product_4":{"product_name":"monitor","price":8500},"product_5":{"product_name":"keyboard","price":1500},"product_6":{"product_name":"ups","price":3500}}

# Write small code blocks to:
# Add a new product with price to price_dict.
price_dict["product_7"]={"product_name":"headphone","price":1500}

# Update the price of an existing product.
price_dict["product_7"]['price']=300
# Remove a product by name (handle the case when the product does not exist).
if "product_7" in price_dict:
    del price_dict["product_7"]
print(price_dict)
print("_" * 100)
sumofproducts=sum(details['price'] for details in price_dict.values())
total=len(price_dict)
avegare = sumofproducts / total
print(avegare)
print(max(details['price'] for details in price_dict.values()))
print(min(details['price'] for details in price_dict.values()))
# Sort products by price (low to high)
sorted_products = sorted(price_dict.items(), key=lambda item: item[1]["price"])
print(sorted_products)
# Print the average price of all products (use only dictionary operations and basic arithmetic).
# Extra (optional): Print the product with both the maximum and minimum prices.