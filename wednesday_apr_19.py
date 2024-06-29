#--------------------------------------------------------
'''139. what is the difference between is and == operator '''
#-------------------------------------------------------
# names = ['apple', 'google', 'gmail', 'flipkart', 'yahoo']
# for ele in names:
#     if ele[0] in 'aeiouAEIOU' or ele[-1] in 'aeiouAEIOU':
#         print(ele)

#----------------------------------------------------
# a = [1, 2, 3, 4]
# b = a[:]
# # print(b)
# print(a == b)
#
# print(a is b)

#-----------------------------------------------------
'''140. What is self in the class'''

#-----------------------------------------------------
'''141. What is assert statement. what is the difference between assert
and if/else statement'''
# assert 3==3
# print('hello world')

#-----------------------------------------------------
'''142. What is the difference between a module, a package and a library'''
#------------------------------------------------------
'''143. wap to get the below output using while loop
1
1 2
1 2 3
1 2 3 4
'''
# pat = ''
# count = 1
# while count <=4:
#     pat += str(count) + ' '
#     print(pat)
#     count += 1

#-------------------------------------------------------
'''144. wap to get the below output'''
# items = ['$123.45', '$434.23', '$567.89']
# ## output should be --> [123.45, 434.23, 567.89]
# list_ = []
# import re
# for ele in items:
#     res = re.findall(r'[\d\.]+', ele)
#     for i in res:
#         list_.append(float(i))
# print(list_)

#-------------------------------------------------------
'''145. function should accept a list and if any number is divisible by 3 then
modify that number to 33, else keep it as it is'''

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = []
# for num in l:
#     if num%3==0:
#         res += [33]
#     else:
#         res += [num]
# print(res)


##Alternate Solution
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = [33 if num%3==0 else num for num in l]
# print(result)

#---------------------------------------------------------------
'''146. write a fibonacci series'''
# def fibo(num):
#     n1 = 0
#     n2 = 1
#
#     for i in range(num):
#         yield n1
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#
# res = fibo(10)
# print(res)
# for j in res:
#     print(j)

#----------------------------------------------------------------
'''147. wap to print the following pattern
1 2 3 *
1 2 * 4
1 * 3 4
* 2 3 4
'''
# pat = ''
# index = 4
# for ele1 in range(1, 5):
#     for ele2 in range(1, 5):
#         if ele2 == index:
#             print('*', end=' ')
#         else:
#             print(ele2, end=' ')
#     index -= 1
#     print()

#-------------------------------------------------------------