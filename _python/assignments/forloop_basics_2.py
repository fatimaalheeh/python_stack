#Biggie Size - 
for x in range(len(arr)):
        if arr[x]>0:
            arr[x]='big'
return arr
print(biggie_size([-3,1,4,-1,2]))


#Count Positives - 
def count_positives(arr):
    counter = 0
    for val in arr:
        if val > 0:
            counter += 1
    arr[len(arr)-1] = counter
    return arr
print([-5,-9,0,32,-6,22])
print(count_positives([1,-1,1,-2,-3]))

# 3 Sum Total - 
def sum_total(array):
    sum = 0
    for i in array:
        sum += i
    return sum
print(sum_total([1,1,1,1]))
print(sum_total([100,3,6,10]))


#Average
def avg(list):
    sum = 0
    for x in list:
        sum += x
    return (sum/len(list))
print(avg([2,10,4,5]))

#Length
def lengthFun(arr):
    return len(arr)
print(lengthFun([1,1,1,1,1,4]))
print(lengthFun([1,1]))

# minimum
def minimum(arr):
    if len(arr)<0:
        return False
    minInt = arr[0]
    for x in arr:
        if x<minInt:
            minInt = x
    return minInt
print(minimum([600,80,99,26,3,5]))

#ultimate_analysis 
def ultimate_analysis(arr):
    myDictonary = {'sumTotal': 0, 'average': 0, 'minimum': array[0], 'maximun': array[0], 'length': len(array)}
    for x in arr:
        if myDictonary['minimum']<x:
            myDictonary['minimum'] = x
        if myDictonary['maximun']>x:
            myDictonary['maximun'] = x
        myDictonary['sumTotal']+= x
        myDictonary['average']=myDictonary['sumTotal']/len(array)
    return myDictonary
print(ultimate_analysis([2,8,3,2,10,5]))


# reverse list
def reverse_list(arr):
    for i in range(0, (len(arr)-1)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
print(reverse_list([11,12,13]))