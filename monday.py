'''27. wap to remove the duplicates from the list without using
inbuilt methods
'''
# items = [1, 2, 1, 3, 5, 4, 3, 6, 7, 4]  ##[1, 2, 3, 5, 4, 6, 7]
# result = set(items)
# print(result)   #{1, 2, 3, 4, 5, 6, 7}
# print(list(result))

##Alternate method
# items = [1, 2, 1, 3, 5, 4, 3, 6, 7, 4]  ##[1, 2, 3, 5, 4, 6, 7]
# unique_list = []
# for ele in items:
#     if ele not in unique_list:
#         unique_list.append(ele)
# print(unique_list)


# items = [1, 2, 1, 3, 5, 4, 3, 6, 7, 4]  ##[1, 2, 3, 5, 4, 6, 7]
# unique_list = []
# for ele in items:
#     if items.count(ele) == 1:
#         unique_list.append(ele)
# print(unique_list)

##Using comprehension
# res = [ele for ele in items if ele in unique_list]
# print(res)

#----------------------------------------------------
'''28. Find the longest word in the sentence'''
# s = 'python is a programming language'
# s_split = s.split()
# # print(s_split)  #['python', 'is', 'a', 'programming', 'language']
#
# longest_word = ''
# for ele in s_split:
#     if len(ele) > len(longest_word):
#         longest_word = ele
#
# print(longest_word)

## Alternate method
# s = 'python is a programming language'
# longest = max(s.split(), key=len)
# print(longest)

'''Program to find the shortest element'''
# s = 'python is a programming language'
# shortest = min(s.split(), key=len)
# print(shortest)

## Alternate method
# s = 'python is a programming language'
# s_split = s.split()
# # print(s_split)  #['python', 'is', 'a', 'programming', 'language']
# shortest_word = s_split[0]
# for ele in s_split:
#     if len(ele) < len(shortest_word):
#         shortest_word = ele
# print(shortest_word)

#-----------------------------------------------------
'''29. wap to reverse the values in a dict if the value is of type
string'''
# d = {'a':'hello', 'b':9.8, 'c':'world', 'd':100}
#d = {'a':'olleh', 'b':9.8, 'c':'dlrow', 'd':100}

# d1 = {}
# for key, value in d.items():
#     if isinstance(value, str):
#         d1[key] = value[::-1]
#     else:
#         d1[key] = value
# print(d1)


## Using Comprehension
# d2 = {key:value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(d2)

#-----------------------------------------------------
'''30. wap to get 1234'''
# t = ('1', '2', '3', '4')        #1234
# print(''.join(t))

## Alternate solution
# t = ('1', '2', '3', '4')        #1234
# res = ''
# for ele in t:
#     res += ele
# print(res)

#------------------------------------------------------------
'''31. How to get the elements that are in list b, but not in
 list a'''
# list_a = [1, 2, 3]
# list_b = [1, 2, 3, 4]
# set_a = set(list_a)
# set_b = set(list_b)
# print(set_b.difference(set_a))

## Alternate solution
# list_a = [1, 2, 3]
# list_b = [1, 2, 3, 4]
#
# for ele in list_b:
#     if ele not in list_a:
#         print(ele)

#-----------------------------------------------------
'''32. A function takes variable number of positional arguments
as input. How to check if the arguments that are passed are more 
than 5
'''
# def func(*args):
#     if len(args) > 5:
#         print('The arguments are greater than 5')
#     else:
#         print('The arguments are lesser than 5')
#
# func('a', 'b', 10, 2, 3, 4, 'python', 'hai')
# func(1, 2)

#----------------------------------------------
'''33. Count the number of occurances of 'CRITICAL', "INFO", 
"ERROR" lines in a log file
'''

lines = '''CRITICAL:Hello world 
INFO: This is an info
ERROR: this is an error
CRITICAL: This is critical
CRITICAL: hello
INFO: hello info
ERROR: This is error
CRITICAl: This is critical
CRITICAL: Critical issue
INFO: hello
ERROR: hello 
'''
# d = {}
# for line in lines.split('\n'):
#     split = line.split(':')
#     for ele in split:
#         if split[0] in d:
#             d[split[0]] += 1
#         else:
#             d[split[0]] = 1
#
# print(d)

#--------------------------------------------------
'''34. wap to reverse a iterable without using reversed func'''
# l = [1, 2, 3, 4, 5]
# rev_l = []
# for ele in range(len(l)-1, -1, -1):
#     rev_l.append(ele)
# print(rev_l)

#-------------------------------------------------------
'''35. Print the numbers in the below list'''
# l = ['abcd', '123', 'xyz', '456']
# for ele in l:
#     if ele.isnumeric():
#         print(ele)

#--------------------------------------------------------
'''36. write a func to print the below output
func('TRACXN', 0)   ---->Should print RCN
func('TRACXN', 1)   ---->Should print TAX
'''
# def func(string, num):
#     if num == 0:
#         print(string[1::2])
#     elif num == 1:
#         print(string[::2])
#     else:
#         print('Invalid Input')
#
# func('TRACXN', 0)       #RCN
# func('TRACXN', 1)       #TAX
# func('TRACXN', 8)

#----------------------------------------------
'''37. Sum of all the numbers in the below string'''
import re

# s = 'Sony12India567Pvt2ltd'
# total = 0
# res = re.findall(r'[\d]', s)
# print(res)  #['1', '2', '5', '6', '7', '2']
# for num in res:
#     total += int(num)
# print(total)

# s = 'Sony12India567Pvt2ltd'
# total = 0
# for ele in s:
#     if '0' <= ele <= '9':
#         total += int(ele)
# print(total)

#--------------------------------------------------
'''38. wap to print sum of all numbers in below string'''
# s = 'Sony12India567Pvt25ltd'     #12 + 567 + 25
# total = 0
# res = re.findall(r'[\d]+', s)
# print(res)      #['12', '567', '25']
# for num in res:
#     total += int(num)
# print(total)

#---------------------------------------------------
'''39. wap to print the number of occurances of characters in 
a string without using inbuilt methods'''
# s = 'hello world'
# d = {}
# for ele in s:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele] = 1
# print(d)

## Using defaultdict
# from collections import defaultdict
# s = 'hello world'
# def_dict = defaultdict(int)
# for ele in s:
#     def_dict[ele] += 1
# print(def_dict)

#-------------------------------------------------
'''40. wap to print only the repeated characters and the count
of the repeated characters'''
# s = 'hello world'
# from collections import defaultdict
#
# def_dict = defaultdict(int)
# for ele in s:
#     def_dict[ele] += 1
# # print(def_dict)
#
# for key, value in def_dict.items():
#     if value > 1:
#         print(key, value)

#--------------------------------------------
'''41. wap to get alternate characetrs of a str in list format'''
# s = 'hello universe'
# res = s[::2]
# print(list(res))        #['h', 'l', 'o', 'u', 'i', 'e', 's']

## Using Comprehension
# s = 'hello universe'
# l = [ele for ele in s[::2]]
# print(l)                #['h', 'l', 'o', 'u', 'i', 'e', 's']

#---------------------------------------------------
'''42. wap to get the square of list of numbers'''
# l = [1, 3, 34, 32, 7, 65, 43, 10]
# def square(iterable):
#     square_list = []
#     for num in iterable:
#         square_list.append(num ** 2)
#     return square_list
#
# print(square(l))

## Using Lambda
# l = [1, 3, 34, 32, 7, 65, 43, 10]
# res = lambda num : num ** 2
# sq_list = [res(ele) for ele in l]
# print(sq_list)
