import asyncio
# find max number function
def findmaxnumber(x=[54,27,33,24,86,57]):
    result=0
    for items in x:
        if(result < items):
            result=items 
    return result

#find odd number function
def findoddnumber(x):
    result=[]
    for items in x:
        if(items % 2 != 0):
            result.append(items)
    return result

async def fetch_user(user_id):
    await asyncio.sleep(1)
    return {"id": user_id, "name": "Harish"}

async def main():
    users = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3)
    )
    print(users)

#functions with n number parameter and argument

def noIdeaAboutparam(*param):
    print("type:", type(param))
    print("first argument", param[0])
    print("second argument",param[1])
    print(" all argument",param)

noIdeaAboutparam("harish",32,"harishpwr99@gmail.com","29 oct 1988")


# asyncio.run(main())

# print(findmaxnumber()) 
# print(findmaxnumber([22,54,11,21,83,54,33,2,84,176,33,923,993]))  
# print(findoddnumber([22,54,11,21,83,54,33,2,84,176,33,923,993]))