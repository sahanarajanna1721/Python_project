'''56. Property decorator'''

#-------------------------------------------------
'''57. Mutable and immutable datatypes'''

#---------------------------------------------------
'''58. Explain get() method in dict'''
# dict_ = {'India':'Delhi', 'Srilanka':'Colombo', 'Pakistan':'Islamabad'}
# print(dict_['India'])       #Delhi
# print(dict_['USA'])
## In the above method, if the key is not found, it will throw
##  KeyError.

# print(dict_.get('India'))
# print(dict_.get('USA'))     #None
# print(dict_.get('USA', 'key not found'))
## In case of get method, if the key is not found, get() method will
## not give any error, instead it will give None. Incase, we want
##any other value, we can pass the value as a second parameter
# print(dict_)

'''setdefault'''
# dict_ = {'India':'Delhi', 'Srilanka':'Colombo', 'Pakistan':'Islamabad'}
# print(dict_.setdefault('India'))
# print(dict_.setdefault('USA', 'Washington DC'))
# print(dict_)
#------------------------------------------------------
'''60. Find the longest non-repeated substring in the below string'''
# s = 'python is a programming language and programming is very easy'
# words = s.split()
# ele = words[0]
# for word in words:
#     if words.count(word) == 1:
#         if len(word) > len(ele):
#             ele = word
# print(ele, len(ele))

## Alternate
# s = 'python is a programming language and programming is very easy'
# dict_ = {}
# words = s.split()
# for ele in words:
#     if words.count(ele) == 1:
#         dict_[ele] = len(ele)
# # print(dict_)
#
# res = sorted(dict_.items(), key=lambda item : item[-1])
# print(res[-1])

#----------------------------------------------------------
'''61. write a program to find the duplicate elements in the list
without using inbuilt functions'''
# list_ = ['apple', 'google', 'apple', 'gmail', 'google', 'kia']
# s1 = set(list_)
# # print(s1)
#
# for item in s1:
#     count = 0
#     for ele in list_:
#         if item == ele:
#             count += 1
#     if count > 1:
#         print(item)
#--------------------------------------------------
'''62. wap to count the number of occurances of each item in the
list without using inbuilt functions
'''
# list1 = ['duster', 'seltos', 'kiger', 'ritz', 'kiger', 'duster']
# d = {}
# for ele in list1:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele] = 1
#
# print(d)
#-----------------------------------------------------
'''63. write a func to check if the number is prime'''
# def is_prime(num):
#     for i in range(2, num):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#     else:
#         print('prime')
# is_prime(7)

# def is_prime(num):
#     return not any(num % ele == 0 for ele in range(2, num))
#
# print(is_prime(9))
# print(is_prime(7))
# print(is_prime(17))
#------------------------------------------------------
'''64. create a tuple using range'''
# print(range(1, 10))     #range(1, 10)
# print(tuple(range(1, 10)))  #(1, 2, 3, 4, 5, 6, 7, 8, 9)

#---------------------------------------------------
'''65. wap to find the largest number in the list without using
any inbuilt func'''
# l = [1, 4, 10, 32, 8, 4, 2]
# large = l[0]
# for i in l:
#     if i> large:
#         large = i
# print(large)
#-----------------------------------------------------
'''66. write a func that returns the last digit of an integer.
For Eg. if user input is 3716, output should be 6.
'''
# def is_last_digit(num):
#     if num %10 !=0:
#         temp = num % 10
#         print(temp)
#
# is_last_digit(4568709)

## Alternate
# def is_last_digit(num):
#     temp = str(num)
#     print(int(temp[-1]))
#
# is_last_digit(4568709)
#-------------------------------------------------------
'''67. wap to find the most common words in given list'''
# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
# 'eyes', "don't", 'look', 'around', 'the', 'eyes'
# ]
# d = {}
# for word in words:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
# print(sorted(d.items(), key=lambda item:item[-1])[-1])

# from collections import Counter
# c = Counter(words)
# print(c)    #Counter({'eyes': 7, 'the': 5, 'look': 3, 'into': 2, 'my': 2, 'around': 2, 'not': 1, "don't": 1})
# print(c.most_common())  #[('eyes', 7), ('the', 5), ('look', 3), ('into', 2), ('my', 2), ('around', 2), ('not', 1), ("don't", 1)]
# print(c.most_common()[0])

#-------------------------------------------------
'''68. Make a func named tail that takes the sequence
(like list, str, tuple) and a number, and returns the last n 
elements from the given sequence as a list'''
# def tail(iterable, n):
#     if not isinstance(n, int):
#         return 'Only integers'
#     if n < 0:
#         return []
#     return list(iterable[-n:])
#
# print(tail('programming', -4))
#-------------------------------------------------------
'''69. write a func that accepts a number and returns True
if its a perfect square, else False
'''
# from math import sqrt
# def is_perfect_square(num):
#     return num == sqrt(num)**2
#
# print(is_perfect_square(8))     #False
# print(is_perfect_square(9))     #True

#-------------------------------------------------------
'''70. wap to get all the duplicate items and the number of times
the item is repeated in the list'''
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook',
#          'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# words = set(names)
# for ele in words:
#     res = names.count(ele)
#     if res > 1:
#         print(ele)

#--------------------------------------------------------
'''71. wap to count the number of occurances of each word in file'''
from collections import defaultdict
path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\sample_1.txt'
with open(path) as file:
    d = defaultdict(int)
    for line in file:
        if line.strip():
            res = line.split()
            for ele in res:
                d[ele] += 1

            print(d)
