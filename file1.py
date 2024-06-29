# import keyword
# print(keyword.kwlist)

#---------------
'''isidentifier() :  Will check if the identifier is valid or not
''.isidentifier()'''
# print('var_name'.isidentifier())
# print('1_var'.isidentifier())
# print('while'.isidentifier())
# print('_10'.isidentifier())
# print('G'.isidentifier())

#------------------------------------------------
'''id() : Will give memory address'''
# a = 10
# print(id(a))
#-------
'''dir() : List of attributes'''
# print(dir(int))

'''ord() : Will give ASCII values'''
# print(ord('a'))

'''chr() : Will give the character associated with that number'''
# print(chr(98))

#------------
'''print() : To print data in the console'''
# print('hello', end='*****')
# print('good morning')       #hello*****good morning
#
# print('python','selenium', sep='!!!!!')     #python!!!!!selenium
#
# print('hello', 'hai', sep='^^^', end='%$%')
# print('heyyy', 'wassup', sep='**')
# # hello^^^hai%$%heyyy**wassup
#
# print('hello', 'hai')
# print('heyyy', 'wassup')

#--------------------------
# print(bool(-19))
#
# print(bool(0.00000000000000000000000000000000001))

# print(bool(False))
# print(bool(bool()))


'''
default value of int = 0/int()
default value of float = 0/float()
default value of complex = 0j/0+0j/complex()
default value of bool = False/bool()
'''

#-------------
'''type() = Will give the datatype of the value'''
# a = 10.8
# print(type(a))

#--------------
'''isinstance()  Check if the value belongs to the particular datatype or not'''
# a = 10

#---------------------------
'''strings'''
#
# '' , "", ''''''

# print('hai')
# print("hai")
# print('''hai''')

#---------------
# print('I'm Ramya')      #SyntaxError
# print("I'm Ramya")      #I'm Ramya
# print('''I'm Ramya''')  #I'm Ramya

# print("Hello "Bengaluru"")  #SyntaxError
# print('Hello "Bengaluru"')      #Hello "Bengaluru"
# print('''Hello "Bengaluru"''')  #Hello "Bengaluru"

#------------------
# print('''I'm from "Bengaluru"''')   #I'm from "Bengaluru"

#--------------------
# a =  'python is programming language'
# print(a[10:3:1])

# a = 100
# print(id(a))

#------------------------
'''even or odd'''
# num = float(input('Enter the number: '))
# if num % 2 == 0:
#     print('even')
# else:
#     print('odd')

#-------------------------
# char = input('Enter the alphabet: ')
# if char.isalpha():
#     if char.isupper():
#         print(char.lower())
#     else:
#         print(char.upper())
# elif char.isdigit():
#     print('Entered char is a number')
# else:
#     print('Entered char is special char')

#--------------------------------
# num1 = int(input('Enter the num1: '))
# num2 = int(input('Enter the num2: '))
# num3 = int(input('Enter the num3: '))
#
# if num1 > num2 and num1 > num3:
#     print(f'{num1} is greater')
# elif num2 > num3:
#     print(f'{num2} is greater')
# else:
#     print(f'{num3} is greater')

#--------------------------------------------
# a = 'h@I W0rLd'
# i = 0
# swap = ''
# while i < len(a):
#     if a[i].isalpha():
#         if a[i].isupper():
#             swap += a[i].lower()
#         else:
#             swap += a[i].upper()
#     else:
#         swap += a[i]
#     i += 1
#
# print(swap)

#---------------------------------------------
'''1 -  10'''
# num = 1
# while num < 11:
#     print(num)
#     num += 1

#----------------------------------
'''10 - 1 '''
# num = 10
# while num > 0:
#     print(num)
#     num -= 1

#----------------------------------
# a = 'python is a programming language'
# count = 1
# while count <= 10:
#     print(a)
#     count += 1

#-----------------------------------------
'''wap to reverse string'''
# a = 'python is a programming language'
# rev_ = ''
# index = 0
# while index < len(a):
#     rev_ = a[index] + rev_
#     index += 1
#
# print(rev_)


#-------------------------------------------
'''
for ele in range(start value, end value, step value):
    statements

for ele in iterable:
    statements
'''
#------------------------------
# for num in range(1, 10):
#     print(num)

# for num in range(10, 1, -1):
#     print(num)

# for num in range(-10, -1):
#     print(num)

# a = 'python'
# for ele in a:
#     print(ele)


# a = ['python', 'selenium', 'java', 'c', 'robot framework', 'c++']
# for ele in a:
#     print(ele)

# a = ('python', 'selenium', 'java', 'c', 'robot framework', 'c++')
# for ele in a:
#     print(ele)


# a = {'python', 'selenium', 'java', 'c', 'robot framework', 'c++'}
# for ele in a:
#     print(ele)

# a = {'python':10, 'selenium':20, 'java':30, 'c':40, 'robot framework':50, 'c++':60}
# for ele in a:
#     print(ele)

# a = {'python':10, 'selenium':20, 'java':30, 'c':40, 'robot framework':50, 'c++':60}
# for ele in a.keys():
#     print(ele)

# a = {'python':10, 'selenium':20, 'java':30, 'c':40, 'robot framework':50, 'c++':60}
# for ele in a.values():
#     print(ele)

# a = {'python':10, 'selenium':20, 'java':30, 'c':40, 'robot framework':50, 'c++':60}
# for ele in a.items():
#     print(ele)

#-------------------------------
'''enumerate'''
# a = 'hello world'
# index = 0
# for ele in a:
#     print(ele, index)
#     index += 1

# a = 'hello world'
# for ele in a:
#     print(ele, a.index(ele))        #drawback is index method will give the index of the firs occuring element

# a = 'hello world'
# print(enumerate(a))     #enumerate object
# for ele in enumerate(a):
#     print(ele)

# a = {1:1, 2:2, 3:3}
# for ele in enumerate(a):
#     print(ele)
#---------------------------------------------------
'''zip'''
# a = 'hai'
# b = ['hello', 'hai', 'python', 'world', 'universe']
# print(zip(a, b))

# for ele in zip(a, b):
#     print(ele)

#---------------------------------------------------
'''zip_longest'''
# from itertools import zip_longest
# a = 'hai'
# b = ['hello', 'hai', 'python', 'world', 'universe']
# for ele in zip_longest(a, b, fillvalue='empty'):
#     print(ele)

#-----------------------------------------------------
# a = 'karnataka'
# d = {}
# for ele in a:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele] = 1
# print(d)        # {k:2, a:4, r:1, n:1, t:1}

# a = 'karnataka'
# from collections import defaultdict
# def_dict = defaultdict(int)
# for ele in a:
#     def_dict[ele] += 1
#
# print(def_dict)

#---------------------------------------------------------
s = 'python is a programming language and programs are fun'
##{p:[python, programming, programs], i:[is], a:[a, and, are], l:[language], f:[fun]}

# d = {}
# for word in s.split():
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         d[word[0]] += [word]
# print(d)
#
# from collections import defaultdict
# def_dict = defaultdict(list)
# for word in s.split():
#     def_dict[word[0]] += [word]
# print(def_dict)


#----------------------------------------------------------------
'''comprehensions
No condition =  [expression for ele in iterable]
                {expression for ele in iterable}
                
Only if condition = [expression for ele in iterable if <condition>]
                    {expression for ele in iterable if <condition>}
                    
Both if-else =   [True block if <condition> else False block for ele in iterable]
                 {True block if <condition> else False block for ele in iterable}
'''
# numbers = []
# for num in range(1, 7):
#     numbers.append(num)
#
# print(numbers)

#-------------------------------------------------------------
# res = [num for num in range(1, 10)]
# print(res)
#
# res = {num for num in range(1, 10)}
# print(res)

# res = [ele for ele in range(1, 20) if ele %2==0]
# print(res)
# res = {ele for ele in range(1, 20) if ele %2==0}
# print(res)

#----------------------------------------------
# names = ['apple', 'google', 'yahoo', 'microsoft', 'facebook']
# res = []
# for name in names:
#     if len(name) % 2 ==0 :
#         res.append(name)
#     else:
#         res.append(name[::-1])
# print(res)
#
# res1 = [ele if len(ele)%2==0 else ele[::-1] for ele in names]
# print(res1)

#----------------
# names = ['apple', 'google', 'yahoo', 'microsoft', 'facebook']
# res = {name:len(name) for name in names}
# print(res)

# names = ['apple', 'google', 'yahoo', 'microsoft', 'facebook']
# res = {name:name if len(name)%2==0 else name[::-1] for name in names}
# print(res)

#----------------------------------------------
# a = ['hello', 'hai']
# for ele in a:
#     for char in ele:
#         print(char)

# res = [char for ele in a for char in ele]
# print(res)

#------------------------------------------------------------
'''functions'''

# a = 'python'
# b = 'selenium'
# def reverse_iterable(iterable):
#     rev_ = ''
#     for ele in iterable:
#         rev_ = ele + rev_
#     return rev_
#
# res1 = reverse_iterable(a)
# res2 = reverse_iterable(b)
# print(res1)
# print(res2)

#--------------------------------------------
'''loop control statements
1. pass
2. continue
3. break
'''

# for ele in range(1, 10):
#     pass

# for ele in range(1, 8):
#     if ele == 5:
#         continue
#     print(ele)

## 1, 2, 3, 4, 6, 7

# for ele in range(1, 8):
#     if ele == 5:
#         break
#     print(ele)

## 1, 2, 3, 4

#--------------------------------------------
'''
def func_name(arguments):       #func defn
    statement 1
    statement 2
    statement 3
    .
    .
    statement n
    return values

func_name(arguments)        #func call
'''

#----------------------------------------

# a = 'python is a programming language'
# def length_(iterable):
#     length = 0      #32
#     for ele in iterable:
#         length += 1
#
#     return length
#
# res = length_(a)
# print(res)

# #-------------------------
# def spam():
#     return 'hai'
#
# print(spam())

#-------------------------
# def spam():
#     return 'hai', 'hello', 'python', 10, 20, True, 0, [1, 2, 3]
#
# print(spam())
#
# ## the return type of return statement is a tuple

#-------------------------
# def spam():
#     return 'hai'
#     return 'hello'
#     return 'python'
#
# print(spam())

#--------------------------------
# def even_odd(n):
#     if n % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
#
# print(even_odd(9))
# print(even_odd(90))

#--------------------------------
'''positional arguments'''
# def greet(name, age):
#     print(f'My name is {name} and I am {age} years old')
#
# greet('Raavan', 55)
# greet(55, 'Raavan')

#-------------------------------
'''keyword arguments'''
# def greet(name, age, place):
#     print(f'My name is {name}, I am {age} years old and I am from {place}')
#
# greet(name='Raavan', age=55, place='Lanka')
# greet(age=55, place='Lanka', name='Raavan')

#---------------------------------
'''combination of positional and keyword arguments'''
# def add(a, b, c, d, e):
#     print(a + b + c + d + e)
#
# add(1, 2, 3, d=4, e=5)
# # add(a=1, b=2, 3, 4, 5)      #SyntaxError: positional argument follows keyword argument
# add(1, 2, 3, a=1, b=2)      #TypeError

#--------------------------------
'''positional only arguments : /
 Before /, the elements should be positional '''
# def add(a, b, c, /, d, e):
#     print(a + b + c + d + e)
#
# add(1, 2, 3, 4, 5)
# add(1, 2, 3, d=4, e=5)
# add(1, 2, c=3, d=4, e=5)

#--------------------------------------------------
'''keyword only arguments : * '''
# def add(a, b, *, c, d, e):
#     print(a + b + c + d + e)
#
# add(1, 2, c=3, d=10, e=0)
# add(a=1, b=2, c=3, d=4, e=5)
# add(1, 2, 3, d=4, e=5)

#------------------------------------------
'''combination of mandatory positional and mandatory keyword arguments'''
# def add(a, b , /, c, d, *,  e, f):
#     print(a + b + c + d + e + f)
#
# ## a,b--> positional.   e,f-->keyword.      c,d-->can be positional or keyword
# add(1, 2, 3, d=4, e=5, f=6)
# add(1, 2, 3, 4, e=5, f=6)
# add(1, 2, c=3, d=4, e=5, f=6)

#----------------------------------------
# def add(a, b , *, c, d, /,  e, f):
#     print(a + b + c + d + e + f)
#
# add(1, 2, 3, 4, 5, 6)       #SyntaxError: / must be ahead of *

#----------------------------------------------------------
# def spam(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# spam(1, 2, 3, 4, 5, 6, a=7, b=9)

#----------------------------------------------------------
# a = [1, 2, 3, 4, 5, 6]
# def spam(*n):
#     print(n)
#
# spam(*a)

#------------------------------------------------
'''default parameters'''
# def add(a, b, c=0):
#     print(a + b + c)
#
# add(1, 2)
# add(1, 2, 3)

#------------------------------------------------
'''function annotations'''
# def add(a:int, b:int):
#     print(a + b)
#
# add(1, 2)
# add(1.1, 2.2)
# add('hai', 'hello')





































































