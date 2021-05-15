def bubble_sort (List):
    print("Current values are: ",List)
    countswaps=0
    for i in range(0,len(List)-1):
        for j in range(0,len(List)-1):
            if List[i] > List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
                countswaps +=1
                print("swap",countswaps,"is: ",List)
    print("Array is sorted in ",countswaps,"swaps.")
    return List
    
count_the_swaps = 0
myList = [1,10,2,5,4]
bubble_sort(myList)
print(myList)
print("First Element: ",myList[0])
print("First Element: ",myList[len(myList)-1])