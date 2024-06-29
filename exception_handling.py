'''try and except block'''

'''default except block'''
# a = 10
# b = 0
# str_ = 'hello world'
# try:
#     # print(a/b)      #ZeroDivisionError
#     print(str_[100])        #IndexError
# except BaseException as error_msg:
#     # print('division by zero is not possible')
#     print('indexing not possible')
#     print(error_msg)

'''specific except block'''
# try:
#     # print(variable)     #NameError
#     # print(10/0)
#     print('hai'[10])
# except NameError:
#     print('except block handling')

'''multiple'''


# try:
#     print(10/0)     #ZeroDivisionError
# except NameError:
#     print('Variable doesnt exist')
# except IndexError:
#     print('Index num is out of range')
# except TypeError:
#     print('type mismatched')
# except ZeroDivisionError:
#     print('division by zero is not possible')

##############################################
# a = 10
# b = 0
# try:
#     # print('good afternoon')
#     res = a/b
# except:
#     print(z)
# else:
#     print(res)
# finally:
#     print('finally block executing')

#########################################

# a = int(input('Enter the value for a: '))
# if a > 0:
#     print('positive')
# else:
#     raise TypeError('Numbers cannot be negative')

#################################
# a = ['apple', 'google', 'apple', 'gmail', 'yahoo', 'yahoo']
# d = {}
# for ele in a:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele] = 1
# print(d)

#######################################
# a = ['apple', 'google', 'apple', 'gmail', 'yahoo', 'yahoo']
# d = {}
# for ele in a:
#     try:
#         d[ele] += 1
#     except:
#         d[ele] = 1
#
# print(d)

#######################################
# numbers = [(1, 2), (2, 0), (8, 4), (7, 3), (9, 0), (0, 4), (1, 0)]
# for number in numbers:
#     try:
#         result = number[0]/number[1]
#     except ZeroDivisionError:
#         print('Division by zero is not possible')
#     else:
#         print(result)
#     finally:
#         print(f'The numbers are {number[0]} and {number[1]}')
#     print()

##############################################
# import math
# def factorial_(num):
#     if isinstance(num, int) and num > 0:
#         print(math.factorial(num))
#     else:
#         print('cant find factorial for other characters')
# factorial_('8')

# import math
# def fact(num):
#     try:
#         res = math.factorial(num)
#     except:
#         raise TypeError('Invalid data to find factorial')
#     else:
#         print(res)
#
# fact('9')

######################################

# class PersonError(Exception):
#     pass
#
# a = 0
# if a < 1:
#     raise PersonError

###############################
class InsufficientFundError(Exception):
    pass


class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Rs.{amount} successfully deposited')

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            raise InsufficientFundError('withdrawal amount is larger than the balance')

    def statement(self):
        print(f'The available balance is {self.balance}')


b = Bank('Ram', 50000)
b.deposit(10000)
b.statement()
b.withdraw(100000)