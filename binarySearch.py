# Recursive Binary Search
def binarySearch(arr, start, end, item):
	if end >= start :		# check base

		mid =  (start + end) // 2
		
		# if middle is greater than item check left
		if arr[mid] > item :
			return binarySearch(arr, start, mid, item)
			

		# if middle is less than item check righ
		elif arr[mid] < item :
			return binarySearch(arr, mid+1, end, item)
			
		# If mid == item return mid
		else:
			return mid
			

arr = [2,4,6,8,10,13, 15, 18]
item = 13

result  = binarySearch(arr, 0, len(arr)-1, item)
print item, "Was found at index ", result


# # Iterative Binary Search a string
def binarySearch_iterative(strings, item):
	start = 0
	end = len(strings) - 1

	index = -1

	while start <= end and index == -1:
		mid = (start + end) // 2
		if strings[mid] == item:
			index = mid
		else:
			if item < strings[mid]:
				end = mid - 1
			else:
				start = mid + 1

	return index

strings =  ["contribute", "geeks", "ide", "practice"]
key = 'geeks'
print key , 'fount at index ' , binarySearch_iterative(strings, key)



