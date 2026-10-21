def mymodddal(ttt):
    def check():
        print("before code execution")
        ttt()
        print("after execution")
    return check

@mymodddal
def greet():
    print("execution time")
greet()
#greetnew = mymodddal(greet)  
#greetnew()         

def decorator_name(func):
    def wrapper(*rrr,**jjj):
        print("Before execution")
        result = func(*rrr, **jjj)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b,c,d,**ff):
    for key,value in ff.items():
        print(key)
        print(value)
    return (a + b + c) * d

print(add(5, 3,7,2,name="amit",gender="male"))