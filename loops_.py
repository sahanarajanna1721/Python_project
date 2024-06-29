# count = 0
# while count < 5:
#     print('hello world')
#     count += 1

# count = 5
# while count > 0:
#     print('hello world')
#     count -= 1

#------------------------------------------------------
'''1. Print numbers from 1-10'''
# count = 1
# while count < 11:
#     print(count)
#     count += 1

#----------------------------------------
'''2. printing numbers from 10-1'''
# count = 10
# while count > 0:
#     print(count)
#     count -= 1

#----------------------------------------
'''3. wap to get even numbers from 1-100'''
# count = 2
# while count <= 100:
#     print(count)
#     count += 2
#
# ##Alternate
# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1

#-----------------------------------------
'''4. wap to get odd numbers from 1-100'''
# count = 1
# while count <= 100:
#     print(count)
#     count += 2
#
# count = 1
# while count <= 100:
#     if count % 2 != 0:
#         print(count)
#     count += 1

#--------------------------------------------
'''5. Iterate over a iterable'''
# a = 'Sanketh Patil'
# index = 0
# while index < len(a):
#     print(a[index])
#     index += 1

#----------------------------------
'''6. iterate over a list'''
# names = ['ashok', 'venkatesh', 'chirag', 'atharv', 'mithun', 'abhishek']
# index = 0
# while index < len(names):
#     print(names[index])
#     index += 1

#-------------------------------------------------------------------
'''7. Reverse the iterable'''
# a = 'lenevo'
# index = -1
# while index >= -len(a):
#     print(a[index], end='')
#     index -= 1
#
# a = 'lenevo'
# index = -1
# rev_str = ''
# while index >= -len(a):
#     rev_str += a[index]
#     index -= 1
# print(rev_str)
#
# a = 'python is awesome'
# index = 0
# rev_str = ''
# while index < len(a):
#     rev_str = a[index] + rev_str
#     index += 1
#
# print(rev_str)

#---------------------------------------------------------------------------
'''8. wap to add even numbers and odd numbers to the seperate lists from 1-50'''
# even_list = []
# odd_list = []
# count = 1
# while count <= 50:
#     if count % 2 == 0:
#         even_list.append(count)
#     else:
#         odd_list.append(count)
#     count += 1
#
# print(even_list)
# print(odd_list)

#----------------------------------------------------------------
'''9. Calculate the first n number sum'''
# num = int(input('Enter the number: '))      #5
# count = 1
# total = 0
# while count <= num:
#     total += count
#     count += 1
# print(total)

#--------------------------------------------------------------------
'''10. wap to calculate the number of alphabets, numbers and special characters in 
the given string'''
# str_ = '$p!d*rM@n 123 % n0 w@Y h0m# 789'
# alpha_count = 0
# num_count = 0
# spe_char_count = 0
#
# count = 0
# while count < len(str_):
#     if str_[count].isalpha():
#         alpha_count += 1
#     elif str_[count].isnumeric():
#         num_count += 1
#     else:
#         spe_char_count += 1
#
#     count += 1
#
# print(f'The str has {alpha_count} alphabets, {num_count} numbers and {spe_char_count} special characters')

## Alternate Solution
# str_ = '$p!d*rM@n 123 % n0 w@Y h0m# 789'
# alpha_count = 0
# num_count = 0
# spe_char_count = 0
#
# count = 0
# while count < len(str_):
#     if 'A'<= str_[count] <= 'Z' or 'a' <= str_[count] <= 'z':
#         alpha_count += 1
#     elif '0' <= str_[count] <= '9':
#         num_count += 1
#     else:
#         spe_char_count += 1
#
#     count += 1
#
# print(f'The str has {alpha_count} alphabets, {num_count} numbers and {spe_char_count} special characters')

#-------------------------------------------------------------------------
'''11. calculate the sum of user input numbers'''
# num = int(input('Enter the num: '))     #918273
# total = 0
# str_num = str(num)          #'918273'
# count = 0
# while count < len(str_num):     #0<6
#     total += int(str_num[count])        #total = 0 + int(str_num[0])--> 0 + int('9')-->0+9 = 9
#     count += 1
#
# print(total)

#-------------------------------------------------------------------------
'''12. wap to get the count of total num of vowels and consonants in the string'''
# str_ = 'Karnataka is beautiful 1234'
# vowel_count = 0
# consonant_count = 0
#
# count = 0
# while count < len(str_):
#     if str_[count].isalpha():
#         if str_[count] in 'aeiouAEIOU':
#             vowel_count += 1
#         else:
#             consonant_count += 1
#
#     count += 1
# print(vowel_count)
# print(consonant_count)

#---------------------------------------------------------------------
'''13. wap to find the sum of all the numbers in the list'''
# list_ = [10, 22, 'hai', 0, 9.9, 88, 'hello', 7, 'python']
# count = 0
# sum_ = 0
# while count < len(list_):
#     if isinstance(list_[count], (int, float)):
#         sum_ += list_[count]
#     count += 1
#
# print(sum_)

#--------------------------------------------------------------
'''14. wap to print the even length elements in the list'''
# names = ['apple', 'google', 'gmail', 'microsoft', 'yahoo', 'flipkart', 'myntra', 'amazon']
# even_len_elements = []
# count = 0
# while count < len(names):
#     if len(names[count]) % 2 == 0:
#         even_len_elements.append(names[count])
#     count += 1
#
# print(even_len_elements)
#--------------------------------------------------------------
'''15. wap to reverse the str if it is odd, else keep it as it is'''
# names = ['apple', 'google', 'gmail', 'microsoft', 'yahoo', 'flipkart', 'myntra', 'amazon']
# result_list = []
# count = 0
# while count < len(names):
#     if len(names[count]) % 2 == 0:
#         result_list.append(names[count])
#     else:
#         result_list.append(names[count][::-1])
#     count += 1
#
# print(result_list)
#---------------------------------------------------------------
'''16. wap to reverse the list elements'''
# names = ['apple', 'google', 'gmail', 'microsoft', 'yahoo', 'flipkart', 'myntra', 'amazon']
# rev_list = []
# count = 0
#
# while count < len(names):
#     rev_list = [names[count]] + rev_list
#     count += 1
#
# print(rev_list)

#------------------------------------------------------------
'''17. create a dict where elements of the list will be key and its len will be the value'''
# names = ['apple', 'google', 'gmail', 'microsoft', 'yahoo', 'flipkart', 'myntra', 'amazon']
# dict_ = {}
# count = 0
#
# while count < len(names):
#     dict_[names[count]] = len(names[count])
#     count += 1
#
# print(dict_)
#--------------------------------------------------------------
'''18. wap to find the factorial of a number'''
# fact = 1
# num = int(input('Enter the number: '))
# count = 1
# while count <= num:
#     fact *= count       #fact = fact * count
#     count += 1
#
# print(fact)

#----------------------------------------------------------------
'''19. wap to find the average of the numbers present in the list'''
# num_list = [10, 24, 6, 4, 5, 7, 34, 89, 98, 67, 55, 43, 7, 9]
# sum_ = 0
# index = 0
# while index < len(num_list):
#     sum_ += num_list[index]
#     index += 1
#
# print(sum_/len(num_list))

#--------------------------------------------------------------
'''20. wap to print the filenames ending with pdf'''
# files = ['apple.in', 'google.co.in', 'yahoo.pdf', 'gmail.pdf', 'flipkart.in']
# index = 0
# while index < len(files):
#     res = files[index].split('.', maxsplit=1)
#     index += 1
#     if res[-1] == 'pdf':
#         print(res[0])

#------------------------------------------------------------
'''21. wap to print the extensions'''
# files = ['apple.in', 'google.com', 'yahoo.pdf', 'gmail.com', 'flipkart.in']
# index = 0
# while index < len(files):
#     res = files[index].split('.')
#     index += 1
#     print(res[-1])

# files = ['apple.in', 'google.com', 'yahoo.pdf', 'gmail.com', 'flipkart.in']
# index = 0
# while index < len(files):
#     file_name, extension = files[index].split('.')
#     index += 1
#     print(extension)

##
# files = ['apple.in', 'google.co.in', 'yahoo.pdf', 'gmail.com', 'flipkart.in']
# index = 0
# while index < len(files):
#     res = files[index].split('.', maxsplit=1)
#     index += 1
#     print(res[-1])

#--------------------------------------------------------------------------
'''22. wap to reverse the number'''
# num = int(input('Enter the num: '))     #9456723        ##3276549
# str_num = str(num)
# count = 0
# rev_num = ''
# while count < len(str_num):
#     rev_num = str_num[count] + rev_num
#     count += 1
#
# print(rev_num)











