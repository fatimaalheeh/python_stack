from random import randint
from time import time

unsorted_list = [20, 7, 3, 4, 12, 15, 2, 1]

def bubbleSort(a):
	update=True
	while(update):
		update = False
		for i in range(len(a)-1):
			if a[i]>a[i+1]:
				a[i],a[i+1]=a[i+1],a[i]
				update = True
	return a

print(bubbleSort(unsorted_list))

def optimizedBubbleSort(a):
	update=True
	n=len(a)
	while(update==True and n>1):
		update = False
		for i in range(len(a)-1):
			if a[i]>a[i+1]:
				a[i],a[i+1]=a[i+1],a[i]
				update = True
		n-=1
	return a

print(optimizedBubbleSort(unsorted_list))

#random array generator
def generate_random_array(n):
	a=[]
	for i in range(n):
		a.append(randint(1,10000))
	return a

unsorted_list = generate_random_array(3000)
unsorted_list_backup = unsorted_list

#Calculate execution times

start1 = time()
bubbleSort(unsorted_list)
end1 = time()-start1

print("Bubble Sort ends in "+str(end1)+" seconds.")


start2 = time()
optimizedBubbleSort(unsorted_list_backup)
end2 = time()-start2

print("Optimized Bubble Sort ends in "+str(end2)+" seconds.")
