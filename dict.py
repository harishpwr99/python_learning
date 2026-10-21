from multiprocessing import Value


studentInfo = {"student_1":{"name":"harish","email":"harishpwr99@gmail.com","age":37},"student_2":{"name":"rishabh","email":"rishabh99@gmail.com","age":3},"student_3":{"name":"rahi","email":"rahi@gmail.com","age":7},"student_4":{"name":"sarika","email":"sarika@gmail.com","age":31},"student_5":{"name":"asish","email":"ashish@gmail.com","age":35},"student_6":{"name":"shubham","email":"shubham@gmail.com","age":30},}

for value in studentInfo.values():
    print(value)

print("*"*20)

for value in studentInfo.popitem():
    print(value)    

print("*"*20)

for items,vala in studentInfo.items():
    print(items)
    print(vala)

print("*"*20)        
#search key by student name and replace age

search_name = 'rishabh'

# Find the specific student ID key by checking the inner 'name' value
student_key = [key for key, info in studentInfo.items() if info['name'] == search_name]

print(student_key)  # Output: ['student_2']
