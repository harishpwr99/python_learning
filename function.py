def findmaxnumber(x):
    result=0
    for items in x:
        if(result< items):
            result=items 
    return result

print(findmaxnumber([22,54,11,21,83,54,33,2,84,176,33,923,993]))    