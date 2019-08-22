# def mergeSortInversions(arr):
#     if len(arr) == 1:
#         return arr, 0
#     else:
#         a = arr[:len(arr)/2]
#         b = arr[len(arr)/2:]
#         a, ai = mergeSortInversions(a)
#         b, bi = mergeSortInversions(b)
#         c = []
#         i = 0
#         j = 0
        
#         inversions = 0 + ai + bi
#     while i < len(a) and j < len(b):
#         if a[i] >= b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#             inversions += (len(a)-i)
#     c += a[i:]
#     c += b[j:]
#     return c, inversions

# ratings = [3,1,2]
# # ratings = [5, 8, 10, 2, 4, 6]
# print mergeSortInversions(ratings)
# for i in range(len(ratings)):
#   print ratings[i]



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
#         swap = swap + (len(right)-i)
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
      
# ratings = [3,1,2]
# print minimum_swaps(ratings)
# for i in range(len(ratings)):
#   print ratings[i]


def minimum_swaps(ratings):
  #sorting in descending order
  # n = len(ratings)

  #new array with the enumerated value, position
  arrpos = list(enumerate(ratings)) 
  print(arrpos)

  #sort the array
  arrpos.sort(reverse = True, key = lambda lst:lst[1]) 
  print(arrpos)

  # vis = {k:False for k in range(n)}
  # Iniialize all visited to false
  visited = {}
  for k in range(len(ratings)):
    visited[k] = False

  
  #initialiaze the value of swaps
  swaps = 0

  #loop through checking if already visited or if value doesnt need to be swapped
  for i in range(len(ratings)):
    if visited[i] or arrpos[i][0] == i: 
      continue
     #finding the number of nodes in the cycle
    size = 0
    j = i
    
    while not visited[j]:
      visited[j] = True
      j = arrpos[j][0] 
      size += 1
     #adding no of nodes to swap
    if size > 0: 
      swaps += (size - 1) 
  return swaps


ratings = [1,2,3,4]
print minimum_swaps(ratings)
# for i in range(len(ratings)):
#   print ratings[i]



def minimum_swaps1(ratings):
 
  #new array in enum value, position
  arrpos = list(enumerate(ratings))
  
  #sort in descending order
  arrpos.sort(reverse = True, key = lambda lst:lst[1])

  
  #initialize all to False
  visited = {}
  
  for k in range(len(ratings)):
    visited[k] = False
    
    #initialize swaps
  swaps = 0
    
  #loop throuh to check if visited or if swap is needed
  for i in range(len(ratings)):
    if visited[i] or arrpos[i][0] == i:
      continue
    
    size = 0
    j = i
    
    while not visited[j]:
      visited[j] = True
      j = arrpos[j][0]
      size = size + 1

      
    if size > 0:
      swaps = swaps + (size -1)
      
  return swaps
ratings = [1,2,3,4]
print minimum_swaps1(ratings)
    