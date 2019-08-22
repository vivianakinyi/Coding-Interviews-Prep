# Find pairs in the array that equals sum given
def sum_pairs(nums, sum):
	pairs = []
	
	if nums < 2:
		print "Array too small"

	for i in range(0, len(nums)):
		diff = sum - nums[i]

		if diff in nums:
			pairs.append((diff, nums[i]))
		
	return set(pairs)
		
	# print "No pair adds up to ", sum

nums = [3,4,1,2,9]
# nums = [-11, -20, 2, 4, 10]
# nums = [1, 3, 2, 2]
sums = 10
print sum_pairs(nums, sums)

def printPairs(nums, sums):
	s = set()

	for i in range(0, len(nums)):
		diff = sums - nums[i]

		if diff > 0 and diff in s:
			print "Pair with the sum is ", nums[i], diff

		s.add(nums[i])

nums = [3,4,1,6,9]
# nums = [-11, -20, 2, 4, 10]
# nums = [1, 3, 2, 2]
sums = 10
print printPairs(nums, sums)



## Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  cnt = 0
  
  for i in range(len(nums)):
    if nums[i] % 2 == 0 :
      cnt = cnt + 1
  
  return cnt

print count_evens([2,3,6,7,8])


"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) - 3
centered_average([1, 1, 5, 5, 10, 8, 7]) - 5
centered_average([-10, -4, -2, -4, -2, 0]) - -3
"""


def centered_average(nums):
  nums.sort()
  
  new_nums = nums[1:len(nums)-1]
  
  total = 0
  
  for i in range(len(new_nums)):
    total += new_nums[i]
    
  centered = total // len(new_nums)
  
  return centered
    
print centered_average([1, 2, 3, 4, 100]) 
print centered_average([1, 1, 5, 5, 10, 8, 7])
print centered_average([-10, -4, -2, -4, -2, 0]) 



"""
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) - 6
sum13([1, 1]) - 2
sum13([1, 2, 2, 1, 13]) - 6
"""
# def sum13(nums):
#   total = 0
  
#   if len(nums) < 1:
#     return 0
    
#   else:
#     for i in range(len(nums)):
#       if nums[i] == 13:
#         break
#       else:
#         total = total + nums[i]
        
#     return total

# # Run to test
# print sum13([1, 2, 2, 1]) 
# print sum13([1, 1]) 
# print sum13([1, 2, 2, 1, 13]) 
# print sum13([13, 1, 3, 1, 13])


def sum13(nums):
	if len(nums)==0:
		return 0
	
	sum=0

	for i in range(1,len(nums)):
		if nums[i]==13 or nums[i-1]==13:
			sum = sum
    	else:
      		sum += nums[i]
  	
  	if nums[0]==13:
  		return sum
  	else:
  		return sum + nums[0] 

# Run to test
print sum13([1, 2, 2, 1]) 
print sum13([1, 1]) 
print sum13([1, 2, 2, 1, 13]) 
print sum13([13, 1, 3, 1, 13])


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twosum(nums, target):
    pairs = {}
        
    for i, num in enumerate(nums):
        diff = target - num
            
        if diff not in pairs:
            pairs[num] = i
            print pairs
                
        else:
            return [pairs[diff], i]


print twosum([2, 7, 11, 15], 9)