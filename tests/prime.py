import time
import math
import sys
import os
import random
import queue
import threading
# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 
	for j in range(low , high): 

		# If current element is smaller than the pivot 
		if arr[j] < pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arrs,low,high=int): 
	
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

# Driver code to test above 
s = time.time()
size = 10000000
arr = [random.randint(0,size) for i in range(0,size)]
#arr = np.random.randint(0,high=size,size=(1,size))
#arr = np.sort(arr[0])

quickSort(arr,0,size-1) 
print(str(time.time()-s))
#print(arr)

# This code is contributed by Mohit Kumra 

