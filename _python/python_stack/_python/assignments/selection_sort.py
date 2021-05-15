__list_to_sort__ = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
def selectionsort(List):
	for min_dfault_from0 in range(len(List)-1):
		Min = min_dfault_from0 #assume that element with min_dfault_from0 index is Min
		for eelment_to_compare_with_after0 in range(min_dfault_from0+1, len(List)): #compare with unsorted the other elements
			if(List[eelment_to_compare_with_after0]<List[Min]):
				Min = eelment_to_compare_with_after0                                #modify Min index with the smaller element
		List[min_dfault_from0],List[Min]=List[Min],List[min_dfault_from0]           #exchange the values of Min and min_default_from0 
	
print("Unsorted list: ", __list_to_sort__)
selectionsort(__list_to_sort__)
print("after selectionsort function:")
print("  sorted list: ", __list_to_sort__)

