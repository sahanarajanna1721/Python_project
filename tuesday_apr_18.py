'''126. In the list below, find all the number pairs which results in 10 either
when added or subtracted'''
# l = [3, 5, -4, 8, 11, 1, -1, 6, 14]
# for ele1 in l:
#     for ele2 in l:
#         if ele1 + ele2 == 10:
#             print(f'Upon adding {(ele1, ele2)} we get the op 10')
#         elif ele1-ele2==10:
#             print(f'Upon subtracting {(ele1, ele2)} we get the op 10')

#------------------------------------------------------
'''127. write a decorator to print prefix +91 to the original phone num'''
# numbers = [9876543211, 8907654123, 8790456321]
#
# def prefix_code(func):
#     def wrapper(*args, **kwargs):
#
#     return wrapper
#
# @prefix_code        #ph_num = prefix_code(ph_num)
# def ph_num(iterable):
#     for num in iterable:
#         return num
#
# print(ph_num(numbers))
#--------------------------------------------------------------
'''128, wap to get the below output'''
# d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# ## output should be ['b', 'd']
# key_list = [ele for ele in d]
# print(key_list[1::2])       #['b', 'd']

##Alternate
# d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# l = []
# for ele in d.keys():
#     l.append(ele)
# print(l[1::2])
#-------------------------------------------------------------
'''129. Can we have multiple init methods in a class'''
# class Sample:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
# sample_obj = Sample(1, 2, 3)
# print(sample_obj.a)     #1
# print(sample_obj.b)     #2
# print(sample_obj.c)     #3
#
# sample_obj_2 = Sample(1, 2)     #TypeError: __init__() missing 1 required positional argument: 'c'

#----------------------------------------------------------------
'''130. Why python is object oriented
        Because in Python, everything is an object(defined as class)
'''
#---------------------------------------------------------------
'''131. what are .pyc files '''
#---------------------------------------------------------------
'''132. reverse a list without using any inbuilt funcs and slicing'''
# a = [1, 2, 3, 4, 5]
# rev_list = []
# for ele in a:
#     rev_list = [ele] + rev_list
# print(rev_list)


##Alternate
# a = [10, 20, 30, 40, 50]
# rev_list = []
# for ele in range(len(a)-1, -1, -1):
#     rev_list.append(a[ele])
# print(rev_list)

##Alternate
# a = [10, 20, 30, 40, 50]
# rl = [a[ele] for ele in range(len(a)-1, -1, -1)]
# print(rl)

#-------------------------------------------------------------
'''134. Difference between while and for loop'''

#-------------------------------------------------------------
'''135. What are magic methods'''

#-------------------------------------------------------------
'''136. Swap two variables without using 3rd variable'''
# a = 10
# b = 20
# b, a = a, b
# print(a)
# print(b)

#--------------------------------------------------------------
'''137. What is pylint'''

#-----------------------------------------------------
'''138. What is the output of the following'''
# print([1, 2, 3, 4] * 2)     #[1, 2, 3, 4, 1, 2, 3, 4]

#--------------------------------------------------------
'''139. what is the difference between is and == operator '''












