'''105. Find the range from the following string'''
# s = '0-0,4-8,20-20,43-45'
# ##[0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
# res = s.split(',')
# # print(res)      #['0-0', '4-8', '20-20', '43-45']
#
# range_list = []
# for ele in res:
#     start, end = ele.split('-')
#     for num in range(int(start), int(end)+1):
#         range_list.append(num)
#
# print(range_list)
#-------------------------------------------------------
'''106. Can we override static method in Python'''
# class Demo:
#
#     @staticmethod
#     def display():
#         print('Demo class display executing')
#
# class Spam(Demo):
#
#     @staticmethod
#     def display():
#         print('Spam class display executing')
#
# spam_obj = Spam()
# spam_obj.display()

#--------------------------------------------------------
'''107. write a func which returns the sum of lengths of all
the iterables'''
# def total_length(*iterables):
#     total = 0
#     for iterable in iterables:
#         total += len(iterable)
#     return total
#
# print(total_length('hai', [1, 2, 3, 4], (2, 3, 4), {1:1, 2:2}))

#----------------------------------------------------------
'''108. Replace whitespaces with newline character in the below 
string'''
# sentence = 'Hello world welcome to python'
# print(sentence.replace(' ', '\n'))

#Alternate
# import re
# sentence = 'Hello world welcome to python'
# res = re.sub(r'\s', '\n', sentence)
# print(res)
#-------------------------------------------------------
'''109. Replace all the vowels with "*" '''
# sentence = 'Hello world welcome to python'
# import re
# res = re.sub(r'[aeiou]', '*', sentence)
# print(res)

##ALternate
# sentence = 'Hello world welcome to python'
# result = ''
# for ele in sentence:
#     if ele in 'aeiouAEIOU':
#         result += '*'
#     else:
#         result += ele
# print(result)
#-------------------------------------------------------
'''110. Replace all the occurances of Java with Python 
in a file'''
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\sample_1.txt'
# with open(path) as file:
#     for line in file:
#         res = re.sub(r'java', 'python', line)
#         print(res)

#----------------------------------------------------------
'''111. wap to find sum of max 3 numbers and min 3 numbers'''
# l = [9, 1, 4, 2, 3, 8, 6, 7, 5]
#
# sorted_list = sorted(l)
# # print(sorted_list)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# min_sum = sum(sorted_list[:3])
# print(min_sum)
#
# max_sum = sum(sorted_list[-3:])
# print(max_sum)

#---------------------------------------------------
'''112. wap to get the below output
input --> 'python@#$%pool'
output --> ['PYTHON', 'POOL']
'''
# s = 'python@#$%pool'
# import re
# res = re.findall(r'\w+', s)
# # print(res)
# result = [ele.upper() for ele in res]
# print(result)

#---------------------------------------------------
'''113. wap to print all the numbers which are ending with 5'''
# numbers = ['1', '12', '123', '12345', '125', '155', '555', '666']
# for num in numbers:
#     if num.endswith('5'):
#         print(num)

## Alternate
# numbers = ['1', '12', '123', '12345', '125', '155', '555', '666']
# for number in numbers:
#     res = re.findall(r'\d+5$', number)
#     if res:
#         print(res)

#---------------------------------------------------
'''114. wap to get the indexes of each item in the below list'''
# names = ['apple', 'google', 'apple', 'gmail', 'yahoo', 'gmail',
#          'microsoft', 'yahoo', 'flipkart']
#
# from collections import defaultdict
# def_dict = defaultdict(list)
#
# for index, item in enumerate(names):
#     def_dict[item] += [index]
# print(def_dict)

#------------------------------------------------------
'''115. wap to print "Bengaluru" for 10 times without using loops '''
# print('Bengaluru\n' * 10)

#--------------------------------------------------------
'''116. wap to print all the words which starts with letter 'h'
 in the given string '''
# s = 'hello world hi universe how are you happy birthday'
# res = re.findall(r'\bh[\w]+', s)
# print(res)

## Alternate
# s = 'hello world hi universe how are you happy birthday'
# l = []
# res = s.split()
# for ele in res:
#     if ele.startswith('h'):
#         l.append(ele)
#
# print(l)

#----------------------------------------------
'''117. wap to find the sum of all even numbers in the given string'''
# s = 'hello 123 world 567 welcome to 9724 python'
# res = re.findall(r'\d', s)
# # print(res)  #['1', '2', '3', '5', '6', '7', '9', '7', '2', '4']
#
# sum_ = 0
# for ele in res:
#     if int(ele) % 2 == 0:
#         sum_ += int(ele)
#
# print(sum_)
#--------------------------------------------------
'''118. wap to add each num in word1 to number in word2'''
# word1 = 'hello 1 2 3 4 5'
# word2 = 'world 5 6 7 8 9'
# ## output --> 1+5, 2+6, 3 +7, 4+8, 5+9
#
# num1 = re.findall(r'\d', word1)
# num2 = re.findall(r'\d', word2)
# # print(num1)     #['1', '2', '3', '4', '5']
# # print(num2)     #['5', '6', '7', '8', '9']
#
# for i, j in zip(num1, num2):
#     print(int(i) + int(j))

#--------------------------------------------------------
'''119. wap to filterout even and odd numbers in the given str'''
# s = 'hello 123 world 567 welcome to 9724 python685645'
# res = re.findall(r'\d', s)
# # print(res)  #['1', '2', '3', '5', '6', '7', '9', '7', '2', '4', '6', '8', '5', '6', '4', '5']
#
# even_list = [int(ele) for ele in res if int(ele)%2==0]
# odd_list = [int(ele) for ele in res if int(ele)%2!=0]
#
# print(even_list)
# print(odd_list)

#----------------------------------------------------
'''120. wap to print all the numbers starting with 8'''
# numbers = ['8', '87', '67', '890', '45', '888', '108', '828']
# for num in numbers:
#     if num.startswith('8'):
#         print(num)

## Alternate
# numbers = ['8', '87', '67', '890', '45', '888', '108', '828']
# for number in numbers:
#     res = re.findall(r'^8\d+', number)
#     if res:
#         print(res)

#--------------------------------------------------------
'''121. wap to remove duplicates from the list without using
empty list or converting to set'''
# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4, 4, 3]
# l2 = l1[:]
# for ele in l2:
#     if l1.count(ele)>1:
#         l1.remove(ele)
# print(l1)

#---------------------------------------------------
'''122. Print all the missing numbers from 1-10 in the below list'''
# l = [1, 3, 6, 8, 10]
# l1 = []
# for num in range(1, 11):
#     if num not in l:
#         l1.append(num)
# print(l1)

#--------------------------------------------------------
'''123. wap to get the below output'''
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# ## 1a, 2a, 3a, 1b, 2b, 3b, 1c, 2c, 3c
# for i in l1:
#     for j in l2:
#         print(str(i)+j)

#-----------------------------------------------------
'''124. wap to get the below output
## o/p ---> [Y3, c2, a2, A4]'''

# words = 'AAAAaaccYYY'
# unique_words= set(words)
# # print(unique_words)
#
# list_ = []
# for ele in unique_words:
#     temp = words.count(ele)
#     list_.append(ele+str(temp))
# print(list_)

#----------------------------------------------------
'''125. what is the output'''
# class Demo:
#     def greet(self):
#         print('hello world')
#
#     def greet(self):
#         print('hello universe')
#
# d = Demo()
# d.greet()       #hello universe