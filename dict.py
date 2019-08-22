""" DICTIONARY """

dicts = {1:'one', 2:'two', 3:'three'}
print dicts.keys() 		# returns a list of keys
print dicts.values() 	# returns a list of values
print dicts.items() 	# returns list of key, value tuples

list_of_tuples = [(1, 'one'), (2,'two'), (3, 'three')]
print dict(list_of_tuples)	# Converts list of tuples to a dict

# Find the second largest value in a dictionary
num_dict = {'one':5, 'two':1, 'three':6, 'four':10}
val = num_dict.values()
val.sort()
print 'Second largest value: ',val, val[-2]




""" Given a list of names find the name that appies twice in a list eg ['Tom, 'Mary', 'Tom', 'Dick, 'John'] """
def appears_twice(given_list):
	names_dict = {}

	for name in given_list:
		if name in names_dict:
			return name
		else:
			names_dict[name] = 1
	return ''


names = ['Mary', 'Tom', 'Dick','Mary', 'John']
print 'The name that appears twice: ',  appears_twice(names)




""" Given a list find the frequency of how many time each name appears """

def frequency_names(given_list):
	names_dict = {}
	
	for name in given_list:
		name = name.lower()

		if name in names_dict:
			names_dict[name] += 1
		
		else:
			names_dict[name] = 1

	return names_dict

names = ['Tom','Mary', 'Tom', 'Dick','Mary', 'John']
print 'frequency of names is : ', frequency_names(names)


""" Find the most frequent element in an array eg [1,2,2,2,3,4,4,7] => 2 """

def most_frequent(arr):
	freq = {}


	for i in range(len(arr)):
		if arr[i] in freq:
			freq[arr[i]] += 1
		else:
			freq[arr[i]] = 1

	# print freq

	max_val = max(freq.values())
	
	
	for k, v in freq.items():
		if max_val == v:
			return k
			

arr = [1,2,2,2,3,4,4,5,7]
print 'The most frequent is : ', most_frequent(arr)


""" Check if the string given has unique characters """
def unique(string):
	freq = {}
	string = string.replace(' ', '')

	for i in string:
		if i in freq:
			freq[i] +=1
			return False
		else:
			freq[i] = 0

	return True

print unique('abc d ')

def unique2(string):
	string = string.replace(' ', '')
	return len(set(string)) == len(string)

print unique('abc d ')

""" Non-repeat element: return the characters that never repeats multiple time"""
def non_repeat(string):
	freq = {}
	string = string.replace(' ', '').lower()
	unique = []
	
	for i in string:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1

	for i in string:
		if freq[i] == 1:
			unique.append(i)

	return unique

print "Non repeat: "
print non_repeat('aab cd')



""" Check if arr1 is a subset of arr2 """

def subset(arr1, arr2):
	dict_arr = {}
	print "In subset"

	if len(arr2) > len(arr1):
		return False

	for i in arr1:
		dict_arr[i] = 0

	print dict_arr

	for j in arr2:
		if j not in dict_arr:
			return False
	return True

arr1 = [1,11,13,7,2]
arr2 = [13, 0, 9]

print subset(arr1, arr2)
	


"""
Given a string return the first repeated word in a string
eg 
Input : "he had had he"
Output : he
"""
def repeatedstr(string):
	freq = {}
	strList = string.split(' ')

	for word in strList:
		if word in freq:
			freq[word] += 1
			return word
			
		else:
			freq[word] = 1

	# return msg if no repetition 
	return "No repetition"

# string = "he had had he"
string ="Ravi had been saying that"
print repeatedstr(string)


def squares(n):
	sq = {}

	for i in range(n):
		sq[i] = i*i





"""Using counter to return the first repeated word in a string"""
from collections import Counter

def firstReapeat(string):
	wordList = string.split(' ')

	#convert list into a dict using Counter
	dicts = Counter(wordList)

	# check which first word has frequency more than 1
	for key in wordList:
		if dicts[key] > 1:
			return key

string = "he had had he"
print firstReapeat(string)


""" Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence. 
eg
Input : {"geeks", "for", "geeks", "for", 
          "geeks", "aaa"}
Output : for

"""

def secondRepeated(lst):
	# Use counter to get freq of each word
	dicts = Counter(lst)

	#sort the frequency counts in descending order
	values = sorted(dicts.values(), reverse=True)

	secondLarge = values[1]

	for key, val in dicts.items():
		if val == secondLarge:
			return key

strList = ["geeks", "for", "geeks", "for", "geeks", "aaa"]
print secondRepeated(strList)