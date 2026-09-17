# python data structure - list and tuple
# Task 1: Product Collections (Lists & Tuples)
# Create a list named products containing at least 6 product names (strings).
# Create a tuple named sample_product that stores (product_name, price, category) for one product.
# Print the 2nd and last product from the products list.
# Append two new product names to products and then print the updated list.
# Extra (optional): Convert sample_product into a list, change its price, and convert it back to a tuple.

# product list name
products=['paneer pizza','veg burger','salted fries','veg momos','black coffee','veg pizza']
#tuple list
sample_product=('onion pizza',150,'pizza')
print(products[1])
print(products[-1])
count=1
for i in products:
    print(f"{count}.{i}")
    count +=1
count=1    
addProduct=str(input("This is your current menu.Do you want to add prodcut in your list then type y : "))
if addProduct == 'y' or addProduct == 'yes' or addProduct == 'YES':
    print("Note : You can add product if you done then add done and you can see your all menu")
    while True:
        newProduct = str(input("Product name: "))
        if newProduct == 'done' or newProduct == '':
            break
        products.append(newProduct)
for i in products:
    print(f"{count}.{i}")
    count +=1
#convert touple to list
sample_product= list(sample_product)
sample_product[1]=200
sample_product = tuple(sample_product)
print(sample_product)    