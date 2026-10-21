# list is built in data structure used to store an ordered collection of items.they are dynamic,resizable and cabale of storing multiple data types.
# list are defined using square brackets [] and items are separated by commas.
# list are zero indexed and mutable,meaning items can be added,removed or modified.
# list are dynamic,meaning they can grow or shrink as needed.
# list are iterable,meaning they can be looped through using a for loop.
# list are mutable,meaning they can be changed after they are created.

# creating a list there is two ways to create a list one is using square brackets and the other is using list() function.

cafeMenuItems = ["Coffee", "Tea", "Sandwich", "Cake"]
otherItems=cafeMenuItems;
name = 'harish'
nickename =  name;
print(id(name))
print(id(nickename))
#example of creating a list using list() function
cafeMenuItems.append("Ice Cream")
#remove item
cafeMenuItems.remove("Sandwich")
#update item
cafeMenuItems[2] = "Pizza"
name="sunita"
nickename = name
print(name)
print(nickename)
print(id(name))
print(id(nickename))
# #example of creating a list using set
# cafeMenuItems = set(["Coffee", "Tea", "Sandwich", "Cake"])
#example of creating a list using dictionary

#example of creating a list using range
# cafeMenuItems = range(1, 12)
#example of creating a list using generator
# cafeMenuItems = (x for x in range(1, 10))
# #example of creating a list using comprehension
# cafeMenuItems = [x for x in range(1, 10)]

#give me example what can we do with a list like add item remove item update item,read item,sort item,reverse item,count item,find item,etc.
print("What can we do with a list?")

#sort item
for item in cafeMenuItems:
    print(item)
print("*"*10)
for item in otherItems:
    print(item)   
