'''9. wap to swap two numbers without using 3rd variable'''
# num1 = 100
# num2 = 200
# num2, num1 = num1, num2
# print(num1)
# print(num2)

#-----------------------------------------------
'''10. wap to merge two different lists'''
# list_1 = [10, '30', 20, 4.0]
# list_2 = ['hello', 'python', 'selenium']

#Using *
# list_3 = [*list_1, *list_2]
# print(list_3)       #[10, '30', 20, 4.0, 'hello', 'python', 'selenium']

#Using +
# print(list_1 + list_2)      #[10, '30', 20, 4.0, 'hello', 'python', 'selenium']

#Using extend method
# list_1.extend(list_2)
# print(list_1)   #10, '30', 20, 4.0, 'hello', 'python', 'selenium']

# from itertools import chain
# merged_list = chain(list_1, list_2)
# print(merged_list)  #<itertools.chain object at 0x0000024C8C6CD430>
# print(list(merged_list))    #[10, '30', 20, 4.0, 'hello', 'python', 'selenium']

#-----------------------------------------------------------
## To merge dictionaries
# d1 = {'one':1, 'two':2, 'three':3}
# d2 = {1:'one', 2:'two', 3:'three'}
#
# # print({**d1, **d2}) #{'one': 1, 'two': 2, 'three': 3, 1: 'one', 2: 'two', 3: 'three'}
# from itertools import chain
# merged_dict = chain(d1, d2)
# # print(merged_dict)
# print(list(merged_dict))

#-------------------------------------------
'''11. wap to read a random line in a file'''
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def random_line(num):
#     with open(path) as file:
#         for line_no, line in enumerate(file, start=1):
#             if num == line_no:
#                 print(f'{line_no} = {line}')
#
# random_line(9)

## Alternate solution
# from itertools import islice
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def random_line(num):
#     with open(path) as file:
#         ## res = islice(file, line_num, line_num+1)
#         res = islice(file, num, num+1)
#         print(res)  #<itertools.islice object at 0x000001E254E56090>
#         for ele in res:
#             print(ele)
#
# random_line(3)

#---------------------------------------------
'''11. wap to read a random lines in a file'''
# from itertools import islice
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def random_line(start_val, end_val):
#     with open(path) as file:
#         ## res = islice(file, start, end)
#         res = islice(file, start_val, end_val)
#         print(res)  #<itertools.islice object at 0x000001E254E56090>
#         for ele in res:
#             print(ele)
#
# random_line(3, 8)

#-------------------------------------------------
'''wap to print last N lines of a file'''
# from itertools import islice
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def last_n_lines(num):
#     with open(path) as file:
#         line_count = 0
#         for line in file:
#             line_count += 1
#         print(line_count)
#
#         file.seek(0)
#
#         res = islice(file, line_count-num, line_count)
#         # print(res)
#         print(list(res))
#
# last_n_lines(4)

## Alternate method
# from collections import deque
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
#
# def last_n_lines(num):
#     with open(path) as file:
#         res = deque(file, num)
#         print(res)
#
# last_n_lines(3)

#------------------------------------------------------
'''wap to check if the string is palindrome or not'''

# def palindrome(str_):
#     if str_ == str_[::-1]:
#         return f'{str_} is a palindrome'
#     else:
#         return f'{str_} is not a palindrome'
# print(palindrome('racecar'))

## ALternate
# def palindrome(str_):
#     rev_str = ''
#     for ele in str_:
#         rev_str = ele + rev_str
#
#     if str_ == rev_str:
#         return f'{str_} is a palindrome'
#     else:
#         return f'{str_} is not a palindrome'
#
# print(palindrome('malayalam'))
# print(palindrome('python'))
#-------------------------------------------------------
'''wap to search for a particular character in a given string
and return the corresponding index
'''
# def str_index(str_, element):
#     for index, item in enumerate(str_):
#         if element == item:
#             print(f'The index of {item} is {index}')
#
# str_index('welcome to python', 'e')

##Alternate
# def str_index(str_, n):
#     for ele in str_:
#         if str_.find(n) > -1:
#             return str_.find(n)
#
# print(str_index('python', 'p'))

##Alternate
# def string(str_, ele):
#     try:
#         print(str_.index(ele))
#     except ValueError:
#         print('element not found')
#
# string('python', 'l')

#-------------------------------------------------------