#countdown
def  countdown(num):
    mylist = []
    for i in range(num, -1, -1):
        mylist.append(i)
    return mylist
print(countdown(5))

#Print the first in the list and Return the second

def printfirst_returnsecond(list):
    print(list[0])
    return list[1]
frst=input("first:")
scnd=input("second")
print (printfirst_returnsecond([frst,scnd]))

#First in the list Plus list'sLength -
def first_plus_length(list):
    print(list[0])
    print(len(list))
    return list[0]+len(list)
print("first plus length: "+first_plus_length([13,20,156]))

#Values Greater than Second - 
def values_greater_than_second(list):
    newList = []
    if len(list)<2:
        return False
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))



#a list on a given length with a given value for all it's components 
def length_value(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_and_value(3,8))

