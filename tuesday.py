'''43. write a func that accepts two strings and returns True
if the two strings are anagrams of each other '''
# def anagram(str1, str2):
#     if str1 == str2:
#         return False
#     a = sorted(str1)
#     b = sorted(str2)
#     if a == b:
#         return True
#     return False
#
# print(anagram('silent', 'listen'))
# print(anagram('racecar', 'racecar'))

#--------------------------------------------------
'''44. write a program to iterate through list and build a 
new list, only if the items in the list has even number of 
characters'''
# list_ = ['mysore', 'bengaluru', 'bijapura', 'hubli', 'dharwad', 'badami']
# even_list = []
# for ele in list_:
#     if len(ele)%2 == 0:
#         even_list.append(ele)
#
# print(even_list)
#---------------------------------------------------
'''45. write a program to iterate through list and build a 
dict of even length ele as key and its len as value'''
# list_ = ['mysore', True, 'bengaluru', 10, 'bijapura', 'hubli', 'dharwad', 'badami']
# dict_ = {}
# for ele in list_:
#     if isinstance(ele, str):
#         if len(ele)%2 == 0:
#             dict_[ele] = len(ele)
#
# print(dict_)

#------------------------------------------------------
'''46. wap which squares the numbers in a list using map object '''
# l = [1, 2, 3, 4, 5]
# ## map = map(func, iterable)
# res = map(lambda num : num ** 2, l) #[1, 4, 9, 16, 25]
# print(res)  #<map object at 0x0000025A57CCD5B0>
# print(list(res))

## Using normal func
# l = [1, 2, 3, 4, 5]
# def square(num):
#     return num ** 2
#
# res = map(square, l)
# print(list(res))
#----------------------------------------------------

# ele = 'bengaluru'
# res = lambda element : len(element) % 2 == 0
# print(res(ele))

# ele = 'bengaluru'
# res = lambda element : 'even length' if len(element) % 2 == 0 else 'odd length'
# print(res(ele))

# list_ = ['mysore', 'bengaluru', 'bijapura', 'hubli', 'dharwad', 'badami']
# res = map(lambda element : len(element) % 2 == 0, list_)
# print(res)
# print(list(res))    #[True, False, True, False, False, True]


# list_ = ['mysore', 'bengaluru', 'bijapura', 'hubli', 'dharwad', 'badami']
# res = filter(lambda element : len(element) % 2 == 0, list_)
# print(res)
# print(list(res))

#-----------------------------------------------------
'''47. wap to count the number of lines  in a file without loading'
the file to the memory'''
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
# with open(path) as file:
#     line_count = 0
#     for line in file:
#         line_count += 1
#     print(line_count)

#------------------------------------------------------
'''48. Printing line and line numbers'''
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, '-', line)

#----------------------------------------------------
'''49. wap to print the sum of entire list and sum of internal list'''
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
## [6, 15, 24]
## 45
# sum_list = []
# for ele in l:
#     sum_list.append(sum(ele))
# print(sum_list)
# print(sum(sum_list))


# l1 = []
# total = 0
# for ele in l:
#     for item in ele:
#         total += item
#
# print(total)
#------------------------------------------------------
'''50. wap to reverse the list as below'''
# words = ['hi', 'hello', 'python']
#op --> ['nohtyp', 'olleh', 'ih']
# rev_list = []
# for ele in words:
#     rev_list.append(ele[::-1])
# print(rev_list[::-1])

#-------------------------------------------------------
'''51. wap to merge the tuples'''
# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# print(t1 + t2)  #(1, 2, 3, 4, 100, 200, 300)
# print((*t1, *t2))       #(1, 2, 3, 4, 100, 200, 300)

#------------------------------------------------------
'''52. wap to replace the value present in nested dictionary'''
# d = {'a':100, 'b':{'m':'man', 'n':'nose', 'c':'cat'}}
# ## Replace nose with net
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]['n'] = 'net'
# print(d)    #{'a': 100, 'b': {'m': 'man', 'n': 'net', 'c': 'cat'}}

#-----------------------------------------------------
'''53. write a list comprehension to get list of even numbers 
from 1-50'''
# even_ = [ele for ele in range(1, 51) if ele%2==0]
# print(even_)

# odd_ = [ele for ele in range(1, 51) if ele%2 != 0]
# print(odd_)

#-------------------------------------------------------
'''54. wap to count number of white spaces in a file'''
# import re
# path = r'C:\Users\QSP\PycharmProjects\PythonRevision\files\f1.txt'
# count = 0
# with open(path) as file:
#     for line in file:
#         match = re.findall(r'\s', line)
#         if match:
#             count += len(match)
#
# print(count)

#-------------------------------------------------
'''55. difference between default dict and normal dict'''
'''
default dict :
1. When each key is encountered for the first time, it will not 
be there  in the mapping
2. So an entry is automatically created with default value
3. Whem keys are encountered again, the look-up proceeds normally
 like a normal dictionary
4. So, in default dict, creation of the key, initialisation will 
happen simultaneously

Normal dict : In case of normal dict, if the key doesnot exist,
    'KEY ERROR' is raised
2. So, we first create the keys and initialise the values

'''
#------------------------------------------------