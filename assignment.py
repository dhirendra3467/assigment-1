'''  "Write a code to reverse a string."
a = "dhirendra"[::-1]
print(a)'''


''' "Write a code to count the number of vowels in a string"
a  = "dhirendra"
vowels = "aeiou"
count = sum(a.count(vowel)for vowel in vowels)
print(count)'''

'''"Write a code to check if a given string is a palindrome or not"
a  = "dhirendra "
rev = a[::-1]
if a == rev:
    print("it is a palindrome number")
else:
    print("it is not a palindrome")'''

'''"Write a code to check if two given strings are anagrams of each other"
word1 = "thing"
word2 = "night"
if sorted(word1)==sorted(word2):
    print("string is anagrams"  )
else:
    print("strings is not anagrams")'''

'''"Write a code to find all occurrences of a given substring within another string."
a = "Harry potter and the Goblet of fire"
print(a[0:12])'''

'''"Write a code to perform basic string compression using the counts of repeated characters."
strval = "aaaabbbbccdddd"
ch = strval[0]
result = ""
count = 0
strval= strval+" "
for i in strval:
    if i==ch:
        count+=1
    else:
        result= result+str(count)+str(ch)
        ch=i
        count=+1
print(result)'''

'''"Write a code to determine if a string has all unique character."

                                        '''

'''"Write a code to convert a given string to uppercase or lowercase"
a = "dhirendra"
print(a.upper())
b = "HELLO world"
print(b.lower())'''

'''"Write a code to count the number of words in a string"
a = "dhirendar is a good man"
strlist = a.split()
print(strlist)'''

'''"Write a code to concatenate two strings without using the + operator"
a = "dhirendra"
b = "suthar"
print(" ".join([a,b]))'''


'''" Write a code to remove all occurrences of a specific element from a list"
list = [55,33,56,23,32,22,12,22,44]
i = 22 
while i in list:
    list.remove(i)
print(list)'''

'''"Implement a code to find the second largest number in a given list of integers"
list = [23,12,45,67,99,65]
list.sort()
e= list[-2]
print("second largest number:",e)'''

'''"Create a code to count the occurrences of each element in a list and return a dictionary with elements as keys and their counts as values"
list = [11,45,8,11,23,45,23,45]

count = dict()

for i in list:
    if i in count:
        count[i]+=1
    else:
        count[i] = 1
print(count)'''

'''"Write a code to reverse a list in-place without using any built-in reverse functions"
num = [5,6,7,8,9]

for i in range(len(num)):
    print(num.pop())'''

'''"Implement a code to find and remove duplicates from a list while preserving the original order of elements"
list1 = [1,2,4,3,5,1,3,4,]   
print(list(dict.fromkeys(list1)))'''

'''"Create a code to check if a given list is sorted (either in ascending or descending order) or not"
list = [1,2,3,4,5]
flag = 0
for i in range(0,len(list)-1):
    if list[i] >= list[i+1]:
        flag = 1
        break

if flag == 0:
    print("sorted")

else:
    print("not sorted")'''

'''"Write a code to merge two sorted lists into a single sorted list"
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]
def merge_sorted_list(l1,l2):
    return sorted (l1 + l2)
merged = merge_sorted_list(l1,l2)
print(merged)'''

'''"Implement a code to find the intersection of two given lists"
list1 = [11,16,21,26,31,36,41]
list2 = [26,41,36]
intersection_list = []
for i in list1:
    if(i in list2):
        intersection_list.append(i)

print(intersection_list)'''

'''"Create a code to find the union of two lists without duplicates"
list1 = [23,45,65,77]
list2 = [45, 56,77]
list3 = list1 + list2
result = []
for i in list3:
    if i not in result:
        result.append(i)
print(result)'''

'''"Write a code to shuffle a given list randomly without using any built-in shuffle functions"
from random import randint
def shuffle_array(arr):
    n = len(arr)
    for i in range(n):
        rand = randint(i , n-1)
        arr[i],arr[rand] = arr[rand], arr[i]
        return arr 
print(shuffle_array([1,2,3,4,5,6,7]))'''


'''"Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples"
def comman_elements(tuple1,tuple2):
    return tuple(set(tuple1)& set(tuple2))

tuple1 = (1,2,3,4,5)
tuple2 = (4,5,6,7)
comman_elements_tuple = comman_elements(tuple1 , tuple2)
print('comman elements:',comman_elements_tuple)'''

'''"Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the intersection of these two sets"
set1 = {2,4,5,6}
set2 = {4,6,7,8}
print("set1 intersection set2:", set1.intersection(set2))'''

'''"Write a code to concatenate two tuples. The function should take two tuples as input and return a new tuple containing elements from both input tuples"
tup1 = eval(input("enter first tuple:"))
tup2 = eval(input("enter second tuple:"))
tup3 = tup1 + tup2
print(tup3)'''

'''"Develop a code that prompts the user to input two sets of strings. Then, print the elements that are present in the first set but not in the second set"
usr_str_1 = input("enter string1:")
usr_str_2 = input("enter string:")
string1 = set(usr_str_1)
string2 = set(usr_str_2)
lst = list(string1-string2)
print('left out elements: {}' .format(lst))'''

'''"Create a code that takes a tuple and two integers as input. The function should return a new tuple containing elements from the original tuple within the specified range of indices"
def get_sub_tuple(original_tuple,start_index, end_index):
    if start_index < 0 or end_index > len(original_tuple) or start_index >= end_index:
        return()
        return
        original_tuple[start_index:end_index]
    my_tuple = (1,2,3,4,5)
    start_index = 1
    end_index = 4
    sub_tuple = get_sub_tuple(my_tuple,start_index, end_index)
    print(sub_tuple)'''
'''"Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets"
s1 = {1,2,3,4}
s2 = {4,5,6,7}
print(s1|s2)'''

'''"Develop a code that takes a tuple of integers as input. The function should return the maximum and minimum values from the tuple using tuple unpacking"
t1 = (11,34,54,78,45)
print(min(t1))
print(max(t1))'''

'''"Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these two sets"
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
print(union)
print(intersection)
print(difference)'''

'''"Write a code that takes a tuple and an element as input. The function should return the count of occurrences of the given element in the tuple"
def count_occurrences(tuple_,element):
    return tuple_.count(element)
my_tuple = (1,2,3,2,1,4,2)
element_to_count = 2
occurrences = count_occurrences(my_tuple,element_to_count)
print(f"the number of occurrences of {element_to_count} in the tuple is: {occurrences}")'''

'''"Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of these two sets"
def get_symmetric_difference():
    set1_str = input("enter the first set of strings (comma-separated):")
    set2_str = input("enter the second set of strings (comma-separated):")
    set1 = set(set1_str.split(","))
    set2 = set(set2_str.split(","))
    symmetric_diff = set1.symmetric_difference(set2)
    print("symmetric difference:",symmetric_diff)
if  __name__ == "__main__":
    get_symmetric_difference()'''

'''"Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list"
def word_frequency(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1 
        else:
            word_count[word] = 1
    return word_count
word_list = ["apple","banana","apple","cherry","banana","apple"]
word_frequency_dict = word_frequency(word_list)
print(word_frequency_dict)'''

'''"Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are common keys, the values should be added together"
def merge_dictionaries(dict1,dict2):
    merged_dict = {}
    for key in set(dict1.keys()).union(dict2.keys()):
        merged_dict[key] = (dict1.get(key,0)+dict2.get(key,0))
    return merged_dict



dict1 = {'a':1,'b':2,'c':3}
dict2 = {'b':4,'c':5, 'd':6}
merged_dict = merge_dictionaries(dict1,dict2)
print(merged_dict)'''

'''"Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the function should return None"
def get_nested_value(d,keys):
    for k in keys:
        if k not in d:
            return None
        d = d[k]
    return d
my_dict  = {'a':{'b':{'c':'value'}}}
keys1 = ['a','b','c']
keys2 = ['a','b','d']
print(get_nested_value(my_dict,keys1))
print(get_nested_value(my_dict,keys2))'''

'''"Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You can choose whether to sort in ascending or descending order"
def sort_dict_by_value(d,reverse=False):
    return dict(sorted(d.items(),key=lambda item: item[1], reverse=reverse))
my_dict = {'apple':3,'banana':1,'cherry':2}
sorted_dict_asc = sort_dict_by_value(my_dict)
print("sorted in ascending order:",sorted_dict_asc)
sorted_dict_desc = sort_dict_by_value(my_dict,reverse=True)
print("sorted in descending order :",sorted_dict_desc)'''

'''"Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary correctly handles cases where multiple keys have the same value by storing the keys as a list in the inverted dictionary"
from collections import defaultdict
def invert_dict(d):
    inverted_dict = defaultdict(list)
    for key , value in d.items():
        inverted_dict[value].append(key)
    return dict(inverted_dict)
my_dict = {'apple':1,'banana':2,'cherry':1,'date':2}
invert_dict = invert_dict(my_dict)
print(invert_dict)'''