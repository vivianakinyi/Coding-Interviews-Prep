# def splitInteger(num,parts):
#     array  = []
#     #if can be completely even
#     if num % parts == 0:

#     	index = num / parts

#     	for i in range(parts):
#     		array.append(index)

#     	return array

#     if num % parts != 0:
#     	quotient = num / parts

#     	remaining_parts = parts - (num % parts)


#     	for i in range(parts):
#     		if i >= remaining_parts:
#     			array.append(quotient +1)
#     		else:
#     			array.append(quotient)
#     	return array

        

# print splitInteger(2, 2)
# print splitInteger(10, 1)
# print splitInteger(20, 5)
# print splitInteger(20, 6)
# print splitInteger(5, 4)


# def minimum_swaps(ratings):
#   swap = 0
#   if len(ratings) > 1:
#     # merge sort - divide array , merge and keep count of merges i.e swaps
    
#     mid = len(ratings) // 2
#     left = ratings[:mid]
#     right = ratings[mid:]

#     # divide recursively
#     minimum_swaps(left)
#     minimum_swaps(right)

#     i=j=k=0

#     while i < len(left) and j < len(right):
#       if left[i] > right[j]:
#         ratings[k] = left[i]
#         i = i + 1
#         # swap = swap + j
#       else:
#         ratings[k] = right[j]
#         j = j + 1
#         # increase swap count
#         swap = swap + 1
#       k = k + 1

#     # Check if any element is on the left
#     while i < len(left):
#       ratings[k] = left[i]
#       i = i + 1
#       k = k + 1
     
#     while j < len(right):
#       ratings[k] = right[j]
#       j = j + 1
#       k = k + 1
      
#   return swap
      
# # ratings = [3,1,2,4]
# ratings = [3,1,2]
# # ratings = [5, 8, 10, 2, 4, 6]

# print minimum_swaps(ratings)
# for i in range(len(ratings)):
# 	print ratings[i]
      

# def minimum_swaps2(ratings):
# 	swaps = 0
# 	for i in range(1, len(ratings)):
# 		key = ratings[i]
		
# 		j= i-1
# 		while j>=0 and key > ratings[j]:
# 			ratings[j+1] = ratings[j]
# 			j=j-1
# 			swaps = swaps + 1 
		
# 		ratings[j+1] = key

# 	return swaps

# ratings = [3,1,2]
# # ratings = [5, 8, 10, 2, 4, 6]

# print minimum_swaps2(ratings)
# for i in range(len(ratings)):
# 	print ratings[i]



# def minimum_swaps3(arr):
# 	swaps = 0

# 	for i in range(len(arr)):
# 		while (arr[i] != i + 1):
# 			temp = arr[i]
# 			arr[i] = arr[arr[i]-1]
# 			arr[temp-1] = temp
# 			swaps =swaps + 1

# 	return swaps
# # ratings = [3,1,2,4]
# ratings = [5, 8, 10, 2, 4, 6]

# print minimum_swaps3(ratings)
# for i in range(len(ratings)):
# 	print ratings[i]

def minimum_swaps4(A):
# Traverse through all array elements 
	swap = 0
	for i in range(len(A)): 
	      
	    # Find the minimum element in remaining  
	    # unsorted array 
	    min_idx = i 
	    for j in range(i+1, len(A)): 
	        if A[min_idx] < A[j]: 
	            min_idx = j 
	              
	    # Swap the found minimum element with  
	    # the first element         
	    A[i], A[min_idx] = A[min_idx], A[i]
	    swap = swap + 1  
	
	return swap
	  
ratings = [3,1,2]
# ratings = [5, 8, 10, 2, 4, 6]
print minimum_swaps4(ratings)
for i in range(len(ratings)):
	print ratings[i]      