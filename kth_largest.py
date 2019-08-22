# Find kth largest elements in an unsorted array

def kth_largest(arr, k):
	print "In kth largest"
	mergeSort(arr)
	
	# Split the array to kth item
	print arr[:k]


	# for i in range(k):
	# 	print arr[i]


# Descending order i.e from largest to smallest
def mergeSort(arr):
	if len(arr) > 1:
		
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]

		mergeSort(left)
		mergeSort(right)

		i = j = k = 0

		while i < len(left) and j <len(right):
			if left[i] > right[j]:  # Store the largest value first
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j = j + 1

			k = k + 1

		# Check if more values are left on the lefthalf
		while i < len(left):  
			arr[k] =  left[i]
			i += 1
			k += 1

		# Check if more values are left on the righthalf
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1



arr = [1,23,12,9,30,2,50]
kth_largest(arr, 3)

