# Function 
def mergeSort (arr):
	if len(arr) > 1:

		mid  = len(arr) // 2

		lefthalf = arr[:mid]
		righthalf = arr[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = j = k = 0

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				arr[k] = lefthalf[i]
				i  = i + 1
			
			else :
				arr[k] = righthalf[j]
				j = j + 1

			k = k + 1

		# check if any elements are left

		while i < len(lefthalf):
			arr[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		while j < len(righthalf):
			arr[k] =  righthalf[j]

			j = j + 1
			k = k + 1

# call the mergesort function

arr = [5,2,4,6,1]
print arr

mergeSort(arr)
for i in range(len(arr)):
	print arr[i]




