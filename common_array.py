# Find the common elements in two sorted arrays

def common(arr1, arr2):
	merged = arr1 + arr2

	freq = {}
	common = []

	for i in range(len(merged)):
		
		if merged[i] in freq:
			freq[merged[i]] += 1
			common.append(merged[i])
		else:
			freq[merged[i]] = 1

	return common

l1 = [1, 3, 4, 6, 7, 9]
l2 = [1, 2, 4, 5, 9, 10]

print common(l1, l2)

# Using sets to find common
def common2(arr1, arr2):
	a = set(arr1)
	b = set(arr2)

	return (a & b)

l1 = [1, 3, 4, 5, 7, 9]
l2 = [1, 2, 4, 5, 9, 10]

print common2(l1, l2)
