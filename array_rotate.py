# Function rotate(arr, d, n) that rotaties an array of size n at d

def rotate(arr, d, n):
	temp1 = arr[0:d]
	print temp1

	temp2  = arr[d:]
	print temp2

	new = temp2 + temp1
	print new


	
array = [1,2,3,4,5,6,7]
n = len(array)
d = 4

rotate(array, d, n)
