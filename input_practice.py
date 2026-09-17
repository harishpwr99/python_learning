first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
age=input("Enter your age: ")

print(f"Hello {first_name} {last_name}! You are {age} years old.")
print("Are you ready to use calculator here")
print("here is the steps like first add number then operator and then enter you will have final answer")
first_number=int(input("enter first number: "))
operator=str(input("enter operator: "))
second_number=int(input("enter second number: "))
result=input("are you ready to see the result then type yes: ")
if result=="yes":
    if operator == "+":
        answer = first_number + second_number
    elif operator == "-":
        answer = first_number - second_number
    elif operator == "*":
        answer = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            print("cannot divide by zero")
            answer = None
        else:
            answer = first_number / second_number
    else:
        print(f"unknown operator: {operator}")
        answer = None

    if answer is not None:
        print(f"the result is {first_number} {operator} {second_number} = {answer}")
else:
    print("okay then you can try again")








