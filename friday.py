'''85. linear search'''
# a = range(1, 20)
# def func(num):
#     if num in a:
#         return True
#     else:
#         return False
#
# print(func(6))
#----------------------------------------------
'''86. wap to count the number of commented lines in the file'''
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\friday.py'
# with open(path) as file:
#     count = 0
#     for line in file:
#         if line.strip():
#             if line.startswith('#'):
#                 count += 1
#     print(count)

#-----------------------------------------------------
'''87. wap to count no of capital letters in the string'''
# str_ = 'PyThoN 123 IS @ PrOgRAmmING 567 LAnGuagE !'
# count = 0
# for ele in str_:
#     if 'A'<= ele <= 'Z':
#         count += 1
#
# print(count)

#------------------------------------------------------
'''87. wap to count no of capital letters in the string'''
# str_ = 'PyThoN 123 IS @ PrOgRAmmING 567 LAnGuagE !'
# spe_char_count = 0
# alpha_count = 0
# num_count = 0
# for ele in str_:
#     if ele.isalpha():
#         alpha_count += 1
#     elif ele.isdigit():
#         num_count += 1
#     else:
#         spe_char_count += 1
#
# print(spe_char_count)
# print(num_count)
# print(alpha_count)

#----------------------------------------
'''88. difference between xrange and range
python2 - xrange
python3 - range

1. xrange donot have start, stop and step attributes
    But range object has start, stop and step attributes

2. range object supports slicing whereas xrange donot support
    slicing

3. range object has __contains__, so it supports membership
    operator
    But xrange doesnot implement __contains__ method
'''

#-----------------------------------------------------
'''89. wap to get the below output'''
# a = [1, 2 ,3, 4, 5, 6, 7, 8, 9]
'''op ---> [1, 2], [3, 4], [5, 6], [7, 8], [9]'''
# for i in range(0, len(a), 2):
#     print(a[i:i+2])

#------------------------------------------------------
'''90. wap to check if the elements in the second list
is series of continuation of the items in the first list'''
# l1 = [2, 4, 6, 8, 10]
# l2 = [12, 14, 16, 18, 20]
#
# diff = l1[1] - l1[0]
# l = [*l1, *l2]  #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# def continuation():
#     for ele in range(0, len(l)):
#         if l[ele + 1] == l[ele] + diff:
#             return True
#         else:
#             return False
#
# print(continuation())
#----------------------------------------------------------
'''91. what is the difference between append method and extend 
method in list'''
'''
append method adds one item at the end of the list
extend method adda all the items of the iterable at the end 
    of the list
Both append and extend will add the elements to the end of the list
'''
# l = [1, 2, 3]
# l.append('hai')
# print(l)
#
# l.extend('100')
# print(l)

#-----------------------------------------
'''92. wap to find the first repeating character in a string'''
# s = 'hai hello universe how are you'
# for ele in s:
#     if s.count(ele) > 1:
#         print(ele)
#         break

#--------------------------------------------
'''93. wap to find the index of nth occurance of a substring
in a string'''
# import re
# s = 'she sells seashells on the seashore'
# def n_occurance(iterable, pat, n):
#     count = 0
#     res = re.finditer(pat, iterable)
#     for ele in res:
#         count += 1
#         if count == n:
#             print(ele)
#
# n_occurance(s, 'e', 7)
#-------------------------------------------
'''write a func to check if the numb is prime or not'''
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             print(f'{n} is not prime')
#             break
#     else:
#         print(f'{n} is a prime number')
# prime(29)

#-------------------------------------------------
'''94. wap to find prime numbers in the range 2-50'''
# def prime(n):
#     for i in range(2, n):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
#
# prime(50)

#--------------------------------------------------------
'''95. wap to sort a list which has a mix of even and odd numbers
, the sorted list should contain odd numbers first and then even 
numbers in a sorted order'''
# num_list = [2, 17, 31, 32, 47, 97, 98, 60, 55, 46, 49]
#
# even_list = [ele for ele in num_list if ele % 2 == 0]
# odd_list = [ele for ele in num_list if ele % 2 != 0]
#
# even_list.sort()
# odd_list.sort()
#
# print([*odd_list, *even_list])

#----------------------------------------------------
'''96.wap to sort a list which has a mix of even and odd numbers
, the sorted list should contain odd numbers first and then even 
numbers in a descending order'''
# num_list = [2, 17, 31, 32, 47, 97, 98, 60, 55, 46, 49]
#
# even_list = [ele for ele in num_list if ele % 2 == 0]
# odd_list = [ele for ele in num_list if ele % 2 != 0]
#
# even_list.sort(reverse=True)
# odd_list.sort()
#
# print([*odd_list, *even_list])

#-------------------------------------------------------
'''97. wap to count the number of occurances of non-special
characters in the given string'''
# s = '123hello @ world ! % ha! Un!verse4567 *()'
# count = 0
# for ele in s:
#     if ele.isalnum():
#         count += 1
#
# print(count)

## alternate
# import re
# s = '123hello @ world ! % ha! Un!verse4567 *()'
# res = re.findall(r'\w', s)
# print(len(res))

#----------------------------------------
# s = '123hello @ world ! % ha! Un!verse4567 *()'
# from collections import defaultdict
# def_dict = defaultdict(int)
#
# for ele in s:
#     if ele.isalnum():
#         def_dict[ele] += 1
# print(def_dict)

#-------------------------------------------------------
'''98. Grouping Flowers and animals in the below list'''
# items = ['lotus-flower', 'lilly-flower', 'dog-animal',
#          'cat-animal', 'sunflower-flower']
# from collections import defaultdict
# def_dict = defaultdict(list)
# for item in items:
#     value, key = item.split('-')
#     def_dict[key] += [value]
# print(def_dict)

#----------------------------------------------------
'''99. Grouping files with same extensions'''
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt',
#          'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# from collections import defaultdict
# def_dict = defaultdict(list)
# for item in files:
#      f_name, ext = item.split('.')
#      def_dict[ext] += [f_name]
# print(def_dict)

#-------------------------------------------------
'''100. Filter only those characters except digits'''
# s = '123@hello4567 world 789 universe !!'
# non_digits = []
# for ele in s:
#     if not ele.isdigit():
#         non_digits.append(ele)
#
# print(''.join(non_digits))

## Alternate
# s = '123@hello4567 world 789 universe !!'
# import re
# res = re.findall(r'[^\d]+', s)
# print(''.join(res))

#-------------------------------------------------
'''101. Count the number of words in a sentence, ignore
 special characters'''
# sentence = 'Hi there! How are you:) How are you doing today!'
# import re
# res = re.findall(r'[\w]+', sentence)
# # print(res)  #['Hi', 'there', 'How', 'are', 'you', 'How', 'are', 'you', 'doing', 'today']
#
# from collections import Counter
# c = Counter(res)
# print(c)    #Counter({'How': 2, 'are': 2, 'you': 2, 'Hi': 1, 'there': 1, 'doing': 1, 'today': 1})

#--------------------------------------------------------
'''102. Grouping even and odd numbers'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ## o/p ---> {1:[1, 3, 5, 7, 9], 0:[2, 4, 6, 8, 10]}
#
# from collections import defaultdict
# def_dict = defaultdict(list)
# for num in numbers:
#     if num % 2 == 0:
#         def_dict[0] += [num]
#     else:
#         def_dict[1] += [num]
#
# print(def_dict)

#---------------------------------------------------
'''103. Find all the max numbers from the below list'''
# l = [1, 2, 2, 5, 6, 7, 8, 9, 4, 9, 9, 8, 9]
# max_ = max(l)
# print(max_)
# print(l.count(max_))

## Alternate
# l = [1, 2, 2, 5, 6, 7, 8, 9, 4, 9, 9, 8, 9]
# max_ = max(l)
# max_list = []
# for ele in l:
#     if ele == max_:
#         max_list.append(ele)
#
# print(max_list)     #[9, 9, 9, 9]

#---------------------------------------------------
'''104. Find all max length words from the below sentence'''
# sentence = 'hello world hi apple hai yahoo'
# res = sentence.split()
# # print(res)      #['hello', 'world', 'hi', 'apple', 'hai', 'yahoo']
#
# max_len = max(res)
# for ele in res:
#     if len(ele) == len(max_len):
#         print(ele)


#----------------------------------------------------------
'''leap year'''
# year = int(input('enter the year: '))
# if year % 4==0 and year != 100:
#     print('leap')
# elif year % 400 == 0:
#     print('leap')
# else:
#     print('not a leap year')






