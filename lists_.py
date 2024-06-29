'''LISTS
Collection of homogenous or heterogeneous data.
Separated by comma.
Elements in the lists are ordered.
Lists can hold duplicate elements
It is a mutable type
Boundary: […….]
Syntax: var_name = [ele1, ele2, ele3, ele4……]
Length of a list: len(var_name)
Indexing and Slicing is possibble
'''

'''list methods'''

'''1. append() : To add an element to the list
Can only add one element
The element will be appended to the end of the list
Syntax : var_name.append(element)
'''
# list_ = ['hello', 'python', 'selenium', 'java']
# list_.append('sql')
# print(list_)        #['hello', 'python', 'selenium', 'java', 'sql']
#
# list_.append(10)
# print(list_)

# list_.append(10, 20)
# print(list_)    #TypeError

#----------------------------------------------------------------------
'''extend() : : Extends the existing list with the items of the given sequence.
Syntax : list.extend(iterable)'''
# list_ = ['sql', 'python', 'selenium', 'java']
# list_.extend('ruby')
# print(list_)        #['sql', 'python', 'selenium', 'java', 'r', 'u', 'b', 'y']

# list_.extend(['javascript', 'php', 'pass', 'c', '.net'])
# print(list_)        #['sql', 'python', 'selenium', 'java', 'javascript', 'php', 'pass', 'c', '.net']

# list_.extend(10)
# print(list_)        #TypeError: 'int' object is not iterable


#-------------------------------------------------------------------------------
'''insert() : It adds an element at the specified position
Syntax : var_name.insert(position, value)
'''
# list_ = ['sql', 'python', 'selenium', 'java']
# list_.insert(0, 'javascript')
# print(list_)        #['javascript', 'sql', 'python', 'selenium', 'java']

# l = ['hai', 'hello']
# print(l.insert(10, 'welcome'))
# print(l)
#--------------------------------------------------------------
# list_ = ['javascript', 'sql', 'python', 'selenium', 'java']
# print(list_[0])
# print(list_[1])
# list_[0] = 'python'
# print(list_[0])
# print(list_)

# a = 'python'
# a[4] = 'a'
# print(a)


############################################################
'''pop() : To delete the elements from the list
Syntax : var_name.pop(index_number)
* pop will return the deleted element
* If the index_num is not mentioned, by default it will delete the last element

'''
# list_ = ['red', 'yellow', 'pink', 'black', 'blue', 'red', 'white', 'purple', 'orange']
# print(list_.pop(4))     #blue
# print(list_)        #['red', 'yellow', 'pink', 'black', 'red', 'white', 'purple', 'orange']
# print(list_.pop())      #orange
# print(list_)    #['red', 'yellow', 'pink', 'black', 'red', 'white', 'purple']

# list_ = ['red', 'yellow', 'pink', 'black', 'blue', 'red', 'white', 'purple', 'orange']
# print(list_.pop(-2))        #purple
# print(list_.pop(100))   #IndexError: pop index out of range

#-----------------------------------------------------------
'''remove() : Will remove the specified element from the list
Syntax : var_name.remove(element)
'''
# list_ = ['red', 'yellow', 'pink', 'black', 'blue', 'red', 'white', 'purple', 'orange']
# list_.remove('black')
# print(list_)

# list_.remove()      #TypeError

# list_.remove('red')
# print(list_)

#-------------------------------------------------------------
'''del : It is a keyword to deallocate the memory in an iterable.'''
# list_ = ['red', 'yellow', 'pink', 'black', 'blue', 'red', 'white', 'purple', 'orange']
# print(id(list_))
# del list_[0:4]
# print(list_)
# print(id(list_))

# del list_[5]

#########################################################################
# list_ = ['red', 'yellow', 'pink', 'white', 'purple', 'orange']
# print(id(list_))
# print()
# list_.append('peach')
# print(list_)
# print(id(list_))
# print()
# list_.pop()
# print(list_)
# print(id(list_))


# str_ = 'hello world'
# print(id(str_))
# res = str_.upper()
# print(id(str_))
# print(id(res))

################################################################
'''count() : It gives the number of occurances of a specified element in the list
Syntax : var_name.count(element)
'''
# list_ = ['red', 'blue', 'red', 'red', 'green', 'blue', 'orange', 'purple']
# print(list_.count('red'))       #3
# print(list_.count('green'))     #1
# print(list_.count('violet'))    #0
# print(list_.count())        #TypeError

#-----------------------------------------------------------
'''sort() : In order to sort, the list should be homogenous.
* Modifies the original list itself  returns None
* Syntax: var_name.sort([reverse= True], [key=func_name])'''
# list_num = [3, 1, 10, 0, 65, 79, 97, 4, 8, 4, -5]
# list_num.sort()
# print(list_num)     #[-5, 0, 1, 3, 4, 4, 8, 10, 65, 79, 97]
#
# list_num = [3, 1, 10, 0, 65, 79, 97, 4, 8, 4, -5]
# list_num.sort(reverse=True)
# print(list_num)     #[97, 79, 65, 10, 8, 4, 4, 3, 1, 0, -5]

# list_str = ['flipkart', 'zudio', 'amazon', 'myntra', 'nykaa', 'pantaloons', 'ajio', 'zara']
# list_str.sort()
# print(list_str)

# list_str = ['flipkart', 'zudio', 'amazon', 'myntra', 'nykaa', 'pantaloons', 'ajio', 'zara']
# list_str.sort(reverse=True)
# print(list_str)     #['zudio', 'zara', 'pantaloons', 'nykaa', 'myntra', 'flipkart', 'amazon', 'ajio']

# list_str = ['flipkart', 'zudio', 'amazon', 'zara', 'nykaa', 'pantaloons', 'ajio', 'myntra', 'ola']
# list_str.sort(key=len)
# print(list_str)
# list_str.sort(key=len, reverse=True)
# print(list_str)

#------------------------------------------------------------------
'''index : Returns the index of the first element with the specified value.
Syntax : list.index(element)'''
# list_str = ['nykaa', 'zudio', 'amazon', 'myntra', 'nykaa', 'pantaloons', 'ajio', 'zara']
# print(list_str.index('nykaa'))
# print(list_str.index('zara'))
# print(list_str.index('snapdeal'))       #ValueError

#-----------------------------------------------------------------
'''reverse() : It reverses the original list irrespective of the order
* Modifies the original list.
Syntax : var_name.reverse()
'''
# list_str = ['flipkart', 'zudio', 'amazon', 'myntra', 'nykaa', 'pantaloons', 'ajio', 'zara']
# list_str.reverse()
# print(list_str)


# list_str = ['flipkart', 'zudio', 'amazon', 'myntra', 'nykaa', 'pantaloons', 'ajio', 'zara']
# print(list_str[::-1])
# print(list_str)

'''
NOTE : We can reverse the list by using reverse() method as well as slicing
i. reverse() method will reverse the original list only
ii. Slicing will not affect the original list
'''

#---------------------------------------------------------------------
'''
Shallow copy(): 
A Shallow copy constructs a new compound object and then inserts
references to it. If a list has a nested list then the nested list will be shared by both
original as well as copied list.
Shallow copy can be done by using slicing syntax or copy method.'''
a = [1, 2, 3, 4, 5]
b = a[:]
print(id(a))
print(id(b))
#
# a[0] = 100
# print(a)
# print(b)

# a = [1, 2, 3, [4, 5]]
# b = a[:]
# # print(b)        #[1, 2, 3, [4, 5]]
#
# print(id(a[3]))
# print(id(b[3]))
#
# a[3][0] = 400
# print(a)
# print(b)

##--------------------------------
'''Deepcopy copies everything and stores it in different memory location, that
means the changes made in the original object will not be reflected in the copied object'''
# from copy import deepcopy
# a = [1, 2, 3, [4, 5]]
# b = deepcopy(a)
# a[3][0] = 100
# print(a)        #[1, 2, 3, [100, 5]]
# print(b)        #[1, 2, 3, [4, 5]]


#--------------------------------------------------------
'''copy():  Returns a copy of the list
It follows Shallow copy principle
The memory allocation will be different for both references
If there is a nested copy in the list then it has same memory location for both references
'''
# list_str = ['flipkart', 'zudio', 'amazon', 'myntra', 'nykaa', 'pantaloons', 'ajio', 'zara']
# res = list_str.copy()
# print(res)

#----------------------------------------------
'''Converting a list to string'''
# s = 'hello'
# list(s) # [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]
# s.split() #[‘hello’]
# ''.join(['h', 'e', 'l', 'l', 'o']) # 'hello'
# ' '.join(['h', 'e', 'l', 'l', 'o']) # 'h e l l o'
# ''.join(['hello']) # ‘hello’
#
#
# sentence = 'hello world'
# list(sentence) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# sentence.split() # [‘hello’, ‘world’]
# ''.join(['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']) # ‘hello world’
# ' '.join(['hello', 'world']) # 'hello world'
# ''.join(['hello', 'world']) # 'helloworld'


###########################################################################

'''Immutable:
* Immutable object can’t be changed or modified once after it is created.
* In other words it’s the ability of the data type which hold the values as it its
    once after it is created

Mutable:
* Mutable objects can be modified or changed even after it is created.
* In other words it’s the ability of the data type which allows its values to be
    changed even after created.
* In mutable data type if we make any changes in values, adding element, removing
    element etc. it is reflected in the original object.
'''
























