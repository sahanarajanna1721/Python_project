# count = 1
# while count <= 10:
#     print(count)
#     count += 1

## range(start, end, step)

# for num in range(1, 10):
#     print(num)

# for num in range(10, 0, -1):
#     print(num)

# for num in range(10, 30, 2):
#     print(num)

#--------------------------------------------------------
# print(range(1, 10))     #range(1, 10)

## Typecasting
# print(list(range(1, 10)))       #[1, 2, 3, 4, 5, 6, 7, 8, 9]

## Traverse
# for ele in range(1, 10):
#     print(ele)

#---------------------------------------------------------
'''
for num in range(start, end, step):
    statements

for ele in iterable:
    statements
'''
#--------------------------------------------------------
## Traversing through a string
# a = 'hello'
# for ele in a:
#     print(ele, end=' ')

## Traversing through a list
# names = ['samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel']
# for ele in names:
#     print(ele)

## Traversing through a tuple
# names = ('samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel')
# for ele in names:
#     print(ele)


## Traversing through a set
# names = {'samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel'}
# for ele in names:
#     print(ele)

## Traversing through a dict
# dict_ = {'name':'Ram', 'age':50, 'salary':50000, 'place':'Ayodhya'}
# for ele in dict_:
#     print(ele)        #keys

# dict_ = {'name':'Ram', 'age':50, 'salary':50000, 'place':'Ayodhya'}
# for ele in dict_.keys():
#     print(ele)      #keys

# dict_ = {'name':'Ram', 'age':50, 'salary':50000, 'place':'Ayodhya'}
# for ele in dict_.values():
#     print(ele)      #Values

# dict_ = {'name':'Ram', 'age':50, 'salary':50000, 'place':'Ayodhya'}
# for ele in dict_.items():
#     print(ele)  #Tuple of two elements, where first ele is key and second ele is value

# dict_ = {'name':'Ram', 'age':50, 'salary':50000, 'place':'Ayodhya'}
# for key, value in dict_.items():
#     print(key, value)

# dict_ = {'name':'Ram', 'age':50, 'salary':50000, 'place':'Ayodhya'}
# for ele in dict_.items():
#     print(ele[0], ele[1])

#-----------------------------------------------------------------
'''1. wap to find the sum of n natural numbers'''
# number = int(input('Enter the num: '))     #10
# total = 0
#
# for num in range(1, number+1):
#     total += num        #total = total + num
# print(total)

#------------------------------------------------------------
'''2. Sum of all digits'''
# num = int(input('Enter the num: '))     #345676
# str_num = str(num)      #'345676'
# sum_ = 0
# for ele in str_num:
#     sum_ += int(ele)
#
# print(sum_)

#------------------------------------------------------------
'''3. Wap to fetch the numbers which has 6 in them in the range(1, 100)'''
# list_ = []
# for ele in range(1, 100):
#     if '6' in str(ele):
#         list_.append(ele)
#
# print(list_)

#-------------------------------------------------------------
'''4. create a list where even len elements should be as it is, odd
len elements should be reversed'''
# names = ['samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel']
# res_list = []
#
# for ele in names:
#     if len(ele) % 2 == 0:
#         res_list.append(ele)
#     else:
#         res_list.append(ele[::-1])
#
# print(res_list)

#--------------------------------------------------------------------
'''5. wap to reverse a string'''
# str_ = 'reverse string'
# rev_str = ''
# for ele in str_:
#     rev_str = ele + rev_str
# print(rev_str)

#-----------------------------------------------------------------
'''6. create a dict of ele and its len pair'''
# names = ['samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel']
# dict_ = {}
# for ele in names:
#     dict_[ele] = len(ele)
# print(dict_)

#---------------------------------------------------------
'''6. create a dict, if len of ele is even, retain the same for value, else reverse for value'''
# names = ['samsung', 'oneplus', 'apple', 'vivo', 'oppo', 'nokia', 'googlepixel']
# dict_ = {}
# for ele in names:
#     if len(ele)%2 == 0:
#         dict_[ele] = ele
#     else:
#         dict_[ele] = ele[::-1]
# print(dict_)

#------------------------------------------------------------
'''7. find the factorial of a number'''
# num = int(input('Enter the num: '))     #5
# fact = 1
# for ele in range(1, num+1):
#     fact *= ele     #fact = fact * ele
#
# print(fact)

#---------------------------------------------------------
'''8. wap to count the total number of alphabets, numericals and special characters
in the given string'''
# str_ = '123h#LL0 @ w0rLd pyT#0n'
# alpha_count = 0
# num_count = 0
# spe_char_count = 0
# for ele in str_:
#     if ele.isalpha():
#         alpha_count += 1
#     elif ele.isnumeric():
#         num_count += 1
#     else:
#         spe_char_count += 1
# print(f'There are {alpha_count} alphabets, {num_count} numbers and {spe_char_count} special characters')

#-----------------------------------------------
'''9. Calculate the sum of all the numbers present in the string'''
# str_ = 'h3ll0 123 w0rld9769 w3lc0m3'
# sum_ = 0
# for ele in str_:
#     if ele.isnumeric():
#         sum_ += int(ele)
#
# print(sum_)

#----------------------------------------------------------
'''10. wap to get the maximum number'''
## Method 1
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 28, 99, 87, 11.8]
# max_num = 0
# for num in num_list:
#     if num > max_num:
#         max_num = num
#
# print(max_num)

## Method 2
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 28, 99, 87, 11.8]
# num_list.sort()
# print(num_list)     #[2, 4, 9.8, 10, 11, 11.8, 28, 43.9, 55, 56, 87, 99]
#
# print(num_list[-1])     #99

## Method 3 using max func
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 28, 99, 87, 11.8]
# print(max(num_list))

#---------------------------------------------------------------------
'''10. wap to get the minimum number'''
## Method 1
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 1, 99, 87, 11.8]
# min_ = num_list[0]
# for num in num_list:
#     if num < min_:
#         min_ = num
#
# print(min_)

## Method 2
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 1, 99, 87, 11.8]
# num_list.sort()
# print(num_list)
# print(num_list[0])

## Method 3 using min func
# num_list = [10, 2, 11, 4, 9.8, 56, 55, 43.9, 1, 99, 87, 11.8]
# print(min(num_list))

#-------------------------------------------------------------
'''11. Create a dict with ele of a string as a key and its ASCII value as value '''
# str_ = 'hello world'
# dict_ = {}
# for ele in str_:
#     dict_[ele] = ord(ele)
# print(dict_)

#-------------------------------------------------------------------
'''12. Check if the number is prime or not'''
# num = int(input('Enter the number : '))
# for ele in range(2, num):
#     if num % ele == 0:
#         print('Composite number')
#         break
# else:
#     print('Prime number')

#---------------------------------------------------------------
'''13. wap to get the prime numbers from 2-50'''
# for i in range(2, 50):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

#----------------------------------------------------------------
'''14. wap to get the below output'''
# s = 'python is a programming language and programs are fun'
## {p:[python, programming, programs], i:[is], a:[a, and, are], l:[language], f:[fun]}

# s_ = s.split()
# # print(s_)   #['python', 'is', 'a', 'programming', 'language', 'and', 'programs', 'are', 'fun']
# d = {}
# for ele in s_:
#     if ele[0] not in d:
#         d[ele[0]] = [ele]
#     else:
#         d[ele[0]] += [ele]      #d[ele[0]] = d[ele[0]] + [ele]
#
# print(d)

#--------------------------------------------------------------
# a = 'hello world'
# for ele in a:
#     print(ele, a.index(ele))


'''enumerate()'''
# a = 'hello world'
# print(enumerate(a))     #<enumerate object at 0x000001E1ABBC2610>
# print(list(enumerate(a)))

#----------------------------------------------------------


#-------------------------------


#--------------------------------------------------------
'''default dict : In Normal dictionaries a key cannot be updated without initialization that is updation can only be done after initialization.
In default dict, updation as well as initialization can be done simultaneously'''

# from collections import defaultdict
# a = 'karnataka'
# def_dict = defaultdict(int)
# for ele in a:
#     def_dict[ele] += 1
#
# print(def_dict)

#------------------------------------------
# s = 'python is a programming language and programs are fun'
# {p:[python, programming, programs], i:[is], a:[a, and, are], l:[language], f:[fun]}

# s_ = s.split()
# # print(s_)   #['python', 'is', 'a', 'programming', 'language', 'and', 'programs', 'are', 'fun']
# d = {}
# for ele in s_:
#     if ele[0] not in d:
#         d[ele[0]] = [ele]
#     else:
#         d[ele[0]] += [ele]      #d[ele[0]] = d[ele[0]] + [ele]
#
# print(d)

#------------------
# s = 'python is a programming language and programs are fun'
# from collections import  defaultdict
#
# def_dict = defaultdict(list)
# for ele in s.split():
#     def_dict[ele[0]] += [ele]
#
# print(def_dict)

#------------------------------------------
'''enumerate : It will return the enumerate object
Upon traversing or typecasting, we will get the tuple consistng of two elements
where thw first ele is index and second element is item
'''
# a = 'hello world'
# print(enumerate(a))     #object
# print(list(enumerate(a)))

# for ele in enumerate(a):
#     print(ele)

## Enumerate will give the tuple consisting of two elements, where
## the first ele is the index and the second ele is the item

# a = 'hello world'
# for index, item in enumerate(a):
#     print(index, item)

# a ='hello world'
# for ele in enumerate(a):
#     print(ele[0], ele[1])
#-------------------------------------------------------------
'''create a dict where the elements will be the key and its index
is the value'''
# names = ['puma', 'nike', 'sketchers', 'levis', 'adidas', 'bata']
# dict_ = {}
# for ele in enumerate(names):
#     dict_[ele[1]] = ele[0]
#
# print(dict_)

#---------------------------------------------------------------------
'''create a dict where the ele is the key and its indices will be the value in the form 
of list'''
# a = 'hello world'
# ## {'h':[0], e:[1], l:[2, 3, 9], o:[4, 7], ' ':5, ...]
# d = {}
# for ele in enumerate(a):
#     if ele[1] not in d:
#         d[ele[1]] = [ele[0]]
#     else:
#         d[ele[1]] +=[ele[0]]
#
# print(d)

#--------------------------------------------------------------------
'''zip: 
* The zip() function takes iterables(can be zero or more), arranges them in a tuple and return it.
* The zip() function returns a zip object which has a list of tuples.
* If the passed iterators have different lengths, the iterator with least items decides the length of the new iterator.
SYNTAX : zip(iterator1, iterator2,…)
'''
# brand = ['oneplus', 'samsung', 'iphone', 'nokia']
# tag_lines = ['never settle', 'together for tomorrow', 'think different', 'connecting people']
# print(zip(brand, tag_lines))    #<zip object at 0x000002128A8F0380>
#
# for ele in zip(brand, tag_lines):
#     print(ele)
#
# print(list(zip(brand, tag_lines)))

# for ele in zip(tag_lines, brand):
#     print(ele)

#-----------------
# cities = ['bangalore', 'mandya', 'kolar', 'dharwad', 'bijapur']
# pincode = [560098, 571401, 563121, 580001]
# for ele in zip(cities, pincode):
#     print(ele)

#-------------------
# a = [1, 2, 3 ,4]
# b = [10, 20, 30]
# c = [100, 200, 300, 400, 500]
# for ele in zip(a, b, c):
#     print(ele)

#-------------
# a = ['hai', 'hello', 'hey']
# b = 'python'
# c = {2, 3, 4, 5}
# for ele in zip(a, b, c):
#     print(ele)

#----------------
# a = 'python'
# b = {'India':'Delhi', 'SouthKorea':'Seoul', 'Srilanka':'Colombo'}
# for ele in zip(a, b.items()):
#     print(ele)

#----------
# a = 'hello'
# b = 'hai'
# for ele in zip(a, b):
#     print(ele)
#--------------------------
'''
NOTE: To include all the elements of iterables of different length, we can use zip_longest of itertools module.
It will map to the extra element with None by default.
SYNTAX: zip_longest(iterator1, iterator2,……….., fillvalue = None)
'''
# from itertools import zip_longest

# a = 'hello'
# b = 'hai'
# for ele in zip_longest(a, b):
#     print(ele)

# a = 'hello'
# b = 'hai'
# for ele in zip_longest(a, b, fillvalue=100):
#     print(ele)
#-----------------
'''create a dict of ele and its count pair'''
# a = 'abracadabra'   #{a:5, b:2,...}
# d = {}
# for ele in a:
#     d[ele] = a.count(ele)
#
# print(d)

## Alternate solution
# a = 'abracadabra'   #{a:5, b:2,...}
# d = {}
# for ele in a:
#     if ele not in d:
#         d[ele] = 1
#     else:
#         d[ele] += 1
# print(d)

#--------------------------------
# num_list = [5, 3, 9, 7, 18, 2, 26]
# for index, item in enumerate(num_list):
#     print(item ** index)

# d = {}
# num_list = [5, 3, 9, 7, 18, 2, 26]
# for index, item in enumerate(num_list):
#     d[item] = item**index
# print(d)

#--------------------------------------------
'''reversed() : Returns iterator object
Will reverse the given sequence'''

# a = 'hello'     #olleh
# print(reversed(a))      #<reversed object at 0x00000233D71AABC0>
# rev_ = list(reversed(a))        #['o', 'l', 'l', 'e', 'h']
# print(''.join(rev_))      #olleh

# a = 'hello'
# for ele in reversed(a):
#     print(ele, end='')

# names = ['puma', 'nike', 'sketchers', 'levis', 'adidas', 'bata']
# print(list(reversed(names)))

# names = ['puma', 'nike', 'sketchers', 'levis', 'adidas', 'bata']
# names.reverse()
# print(names)

'''
reverse method in the list will modify the original list, whereas reversed class
will not modify the original list, it will give a new list

reverse method is a method of a list, whereas reversed is a class and can be applied on
other iterables
'''

#-------------------------------------------------------
'''loop control statements'''
'''pass : It performs no operation'''
# for ele in range(1, 10):
#     pass

'''continue : Will skip the current iteration and continues with the next one'''
# for ele in range(1, 7):
#     if ele == 5:
#         continue
#     print(ele)            ##1, 2, 3, 4, 6

'''break :  break will stop the execution of loop and comes out of it'''
# for ele in range(1, 10):
#     if ele == 4:
#         break
#     print(ele)      #1, 2, 3,









