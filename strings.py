"""Most of the questions are from coddingbat.com"""
# Reversing all char in a  string
def charReverse(char):
	reversed_str = char[::-1]

	return reversed_str  

print charReverse('Hello')


#Reverse all word ins string eg Hello world => world Hello
# Using split and reverse 
def stringReversed(words):

	words = words.split(' ')
	
	words.reverse()
	
	return ' '.join(words)

print stringReversed('This is new')

#Using indexing
def stringReversed2(words):
	return ' '.join(words.split()[::-1])

print stringReversed2('This is new')
	

#Using the long method
def stringReversed3(s):
	length = len(s)
	spaces = [' ']
	words = []
	i = 0

	while i < length:
		if s[i] not in spaces:
			word_start = i

			while i < length and s[i] not in spaces:
				i += 1

			words.append(s[word_start: i])

		i += 1

	return "".join(reversed(s))

print stringReversed3('This is new')

# Return the number of times that the string "code" appears 
# anywhere in the given string, except we'll accept any letter for 
# the 'd', so "cope" and "cooe" count.
def count_occurence(string):
	count = 0

	for i in range(0, len(string)-3):
		if string[i:i+2] =='co' and string[i+3]=='e':
			count += 1
	return count

print count_occurence('AAcodeBBcoleCCccoreDD')

# Given a list strings find frequency of the specific query string 
# in that list eg ['aabb', 'abc', 'bba', 'abc'] query= 'abc'
def query_frequency(lst, query):
	freq = {query:0}

	for i in range(len(lst)):
		if lst[i] == query:
			freq[query] += 1

	return freq

print 'The frequnecy of a query is : '
print query_frequency(['aabb', 'abc', 'bba', 'abc'], 'bba')

# Write a program that accepts a sentence and calculate the number of letters and digits
# eg hello 123 => letters:4, numbers:3

def letters_digits(string):
	d = {'digits':0 ,'letters':0}

	for i in string:
		if i.isalpha():
			d['letters'] += 1

		elif i.isdigit():
			d['digits'] += 1
		
		else:
			pass

	return d


string = 'hello! 124'

print letters_digits(string)


# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
	cat_cnt = 0
	dog_cnt = 0

	for i in range(len(str)-1):
		if str[i:i+3] == 'cat':
			cat_cnt = cat_cnt + 1

		if str[i:i+3] == 'dog':
			dog_cnt = dog_cnt + 1

	if dog_cnt == cat_cnt:
		return True
	return False

print cat_dog('catdog') 
print cat_dog('catcat')
print cat_dog('1cat1cadodog')
































