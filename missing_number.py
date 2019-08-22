# Find missing number in an array 1 to n
def find_missing(arr, n):
	total = n * (n+1) // 2

	sum_of_array = sum(arr)

	missing = total - sum_of_array

	return missing

arr = [1,2,3,4,6,7,8]
n = len(arr)
result = find_missing(arr, n)
print arr[result]
print result

# assuming is sorted
# for x in range(0,len(arr) -1):
#     if arr[x+1] - arr[x] != 1:
#         print arr[x] + 1