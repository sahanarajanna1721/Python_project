'''72. wap to count the number of vowels'''
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\sample_1.txt'
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             vowel_count = 0
#             for ele in line:
#                 if ele in 'aeiouAEIOU':
#                     vowel_count += 1
#             print(f'{line.strip()} has {vowel_count} vowels')

#--------------------------------------------------------
'''73. wap to print all numeric values in a list'''
# l = ['apple', 1.2, 'google', '26', 100, 78]
# for ele in l:
#     if isinstance(ele, (int, float)):
#         print(ele)

#--------------------------------------------------------
'''Traingle patterns'''
'''
*
* *
* * *
* * * *
'''
# for ele in range(1, 5):
#     print(ele * '* ')

#-------------------------------------------------------
'''
* * * *
* * *
* *
*
'''
# for i in range(4, 0, -1):
#     print(i * '* ')

#-----------------------------------------------------
## Right justified triangle
'''
      *
    * *
  * * *
* * * *
'''
# for i in range(1, 5):
#     print(f'{"* " * i:>8}')

#---------------------------------------------------
'''
* * * *
  * * *
    * *
      *
'''
# for i in range(4, 0, -1):
#     print(f'{"* " * i:>8}')

#----------------------------------------------------
'''
   *
  * *
 * * *
* * * *
'''
# for i in range(1, 5):
#     print(f'{"* " * i:^8}')

#-----------------------------------------------
'''
* * * *
 * * *
  * *
   *
'''
# for i in range(4, 0, -1):
#     print(f'{"* " * i:^8}')

#-----------------------------------------------
'''
*
*
* *
*
* * *
*
* * * *
*
'''
# for ele in range(1, 5):
#     print(ele * '* ')
#     print('*')

#----------------------------------------------
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# pat = ""
# for i in range(1, 6):
#     pat += str(i) + ' '      #pat = pat + str(i)
#     print(pat)

#---------------------------------------------
'''
        1
      1 2
    1 2 3
  1 2 3 4 
1 2 3 4 5
'''
# pat = ''
# for i in range(1, 6):
#     pat += str(i) + ' '
#     print(f'{pat :>10}')

#-------------------------------------------------
'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''
# pat = ''
# for i in range(1, 6):
#     pat += str(i) +' '
#     print(f'{pat :^10}')

#----------------------------------------------
'''
a 
a b 
a b c
a b c d
'''
# pat = ""
# for ele in range(ord('a'), ord('e')):  #for ele in range(97, 101)
#     pat += chr(ele) +' '
#     print(pat)

#----------------------------------------------------
'''75. wap that counts the occurances of a paticular word in file'''
path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\sample_1.txt'

# def _count(word):
#     with open(path) as f1:
#         count = 0
#         for line in f1:
#             words = line.split()
#             for i in words:
#                 if i == word:
#                     count += 1
#         print(count)
#
# _count('hello')

#----------------------------------------------------
'''76. wap to map a product to a company and build a dict with
company and list of products pair'''
# all_products = ['iPhone', 'mac', 'gmail', 'maps', 'iWatch',
#                 'windows', 'google drive', 'one drive']
#
# apple_products = ['iphone', 'mac', 'iwatch']
# google_products =  ['gmail', 'maps', 'googledrive']
# msft_products = ['windows', 'onedrive']
#
# from collections import defaultdict
# def_dict = defaultdict(list)
#
# for ele in all_products:
#     if ele in apple_products:
#         def_dict['apple'] += [ele]
#     elif ele in google_products:
#         def_dict['google'] += [ele]
#     elif ele in msft_products:
#         def_dict['msft'] += [ele]
#
# print(def_dict)

#----------------------------------------------------
'''77. wap to rotate the items of the list'''
# names = ['apple', 'google', 'gmail', 'yahoo', 'microsoft']
# def _rotate(iterable, n):
#     for i in range(0, n):
#         res = iterable.pop()
#         iterable.insert(0, res)
#     print(iterable)

# _rotate(names, 2)
# _rotate(names, 3)

#----------------------------------------------------------
'''78. wap to rotate characters in a string'''
# s = 'hello world'
# print(s[-3:] + s[:-3])

#-----------------------------------------------------
'''79. wap to count the number of white spaces in a given string'''
# s = 'hello world welcome to python'
# import re
# print(len(re.findall(r'\s', s)))

#---------------------------------------------------------
'''80. wap to print only non repeated characters in a string'''
# s = 'hello world'
# for ele in s:
#     if s.count(ele) == 1:
#         print(ele)

#-------------------------------------------------------------
'''81. what is the difference between list and tuple'''

#-------------------------------------------------------------
'''82. wap to print all the consonants in a given string'''
# s = 'hello world'
# res = [ele for ele in s if ele not in 'aeiouAEIOU ']
# print(res)

#------------------------------------------------------------
'''83. wap to check if the year is leap year or not'''
# import calendar
# print(calendar.isleap(2020))
# print(calendar.isleap(2023))

#-----------------------------------------------
'''85. linear search'''
a = range(1, 20)
