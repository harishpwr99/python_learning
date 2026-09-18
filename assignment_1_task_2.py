# Task 2: Categories (Sets)

# From your products list, create a set of categories called categories_set. (If product names do not contain categories, create a short parallel list categories = [..] with matching length and use that.)
products=['paneer pizza','veg burger','salted fries','veg momos','black coffee','veg pizza']
categories=['pizza','burger','fries','momos','coffee','pizza']
categories_set=set(products)

# Demonstrate adding a new category to the set and show that duplicates are ignored.
categories_set.add("salted fries")
print(categories_set)

# Show how to check whether a category exists in the set (print a boolean result).
target = "salted fries"
exist = target in categories_set
print(exist)

# Extra (optional): Show how to get the total number of unique categories using a set.
print(len(categories_set))


