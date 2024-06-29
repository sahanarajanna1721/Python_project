'''strings : collecrion of characters'''

'''
1. single quotes, double, or triple
'''

# a = "I'm Ramya. I'm from Bangalore"
# a = '''I'm Ramya. I'm from Bangalore'''
# print(a)

# a = 'I am Ramya. I am from "Bangalore"'
# b = '''I am Ramya. I am from "Bangalore"'''
# print(a)
# print(b)

# a = '''I'm Ramya. I'm from "Bangalore"'''
# print(a)

#-----------------------------------------------------
'''escape sequence'''
# str_1 = 'happy bir\\thday\\'
# print(str_1)

# str_1 = r"happy bir\thday \nithya"
# print(str_1)

# str_1 = ' "happy bir\\thday \\nithya" '
# print(str_1)
#-----------------------------------------------------
'''format strings'''

# print('My name is Ram, I am 45 years old')

### .format()
# print('My name is {}, I am {} years old'.format('Ram', 45))
# print('My name is {}, I am {} years old'.format(45, 'Ram'))
# print('My name is {1}, I am {0} years old'.format(45, 'Ram'))
# print('My name is {name}, I am {age} years old'.format(age=45, name='Ram'))
# print('My name is {name}, I am {age} years old'.format(name, age))

### f-strings
# name = 'Ram'
# age = 45
# print('My name is {name}, I am {age} years old')    #My name is {name}, I am {age} years old
# print(f'My name is {name}, I am {age} years old')   #My name is Ram, I am 45 years old

# day = 24
# minute = 60
# print(f'A day has {day} hours, {day*minute} minutes')

#######################################
'''input() : '''
# name = input('Enter the name : ')
# print(f'My name is {name}')

# num = int(input('Enter the number : '))     #int('10') == 10
# print(f'Entered number is {num}')
## int('10.3') --> Error

# num = float(input('Enter the number : '))
# print(f'Entered number is {num}')

########################################
'''indexing : the process of extracting one character at a time'''
# a = 'python selenium'
# print(a[7])     #s
# print(a[1])     #y
# print(a[13])    #u
# print(a[15])    #IndexError

# print(a[-7])

'''slicing : process of extractimg multiple characters at a time
Syntax : var_name[start index : end index : stepvalue]
default start index = 0
default end index = len(str)
default step value = 1

* The element at the end index will not be considered for slicing

* If step value is positive, traversing takes place in forward direction,
if step value is negative, traversing takes place in reverse direction
'''
# a = 'welcome to Bengaluru'
# print(a[3:9])           #come t
# print(a[2:18:2])        #loet egl
# print(a[::])        #welcome to Bengaluru

# print(a[10:2])  # cant traverse from 10 to 2 if step value is positive, it will not give any error, instaed it will give empty string


# a = 'welcome to Bengaluru'
# print(a[11:20:1])       #Bengaluru
# print(a[11:])           #Bengaluru
# print(a[11:22])

#
# a = 'royal challengers bengaluru'
# print(a[6:17])      #challengers
# print(a[-21:-10])   #challengers
# print(a[6:-10])     #challengers
# print(a[-21:17])    #challengers

# print(a[16:5:-1])       #sregnellahc
# print(a[-11:-22:-1])    #sregnellahc
# print(a[16:-22:-1])     #sregnellahc
# print(a[-11:5:-1])      #sregnellahc

# print(a[::-1])      #urulagneb sregnellahc layor
# print(a[::-2])      #uuanbsenlaclyr

####################################
'''len() : it is an inbuilt function to find the length of iterable'''
# a = 'royal challengers bengaluru'
# print(len(a))

#######################################
# a = 'hello world@1'
# b = 'hey'
# print(id(a))
# print(id(b))

# print(id(a[0]))
# print(id(b[0]))

###############################################
'''ord() : To find the ASCII value
Syntax : ord('character')
'''
# print(ord('A'))
# print(ord('a'))
# print(ord('9'))
# print(ord('*'))
# print(ord(' '))
# print(ord('2'))
# print(ord('10'))        #TypeError
# print(ord(4))           #TypeError

'''chr() : '''
# print(chr(98))
# print(chr(79))
# print(chr(8765))

##############################################
'''string methods'''
'''upper : It will convert all the alphabetical characters of the string to the uppercase
Syntax : var_name.upper()
'''
# a = 'hello @ 123 world'
# print(a.upper())        #HELLO @ 123 WORLD
#
# b = 'HelLO @ 123 WORld'
# print(a.upper())        #HELLO @ 123 WORLD

#---------------------------------------------------
'''lower() : It will convert the uppercase alphabets to the lowercase
Syntax : var_name.lower()
'''
# a = 'HELLO @ 12 UNIVERSE'
# print(a.lower())        #hello @ 12 universe
#
# a = 'HellO @ 567 UnIvErSE'
# print(a.lower())        #hello @ 567 universe

#-----------------------------------------------------
'''swapcase () : All the uppercase will be converted to lowercase and lowercase will be 
converted to uppercase. Numbers and special characters remains the same'''
# a = 'HellO @ 567 UnIvErSE'
# print(a.swapcase())     #hELLo @ 567 uNiVeRse

#_____________________________________________________
'''capitalize() : Will convert the first character of string to uppercase, and the rest of 
alphabetical characters to the lowercase
Syntax : var_name.capitalize()
'''
# a = 'python is fun'
# print(a.capitalize())       #Python is fun
#
# b = '@ python is fun'
# print(b.capitalize())       #@ python is fun
#
# c = '123 @ PYthOn'
# print(c.capitalize())       #123 @ python

#----------------------------------------------------
'''title() : It will convert the immediate alphabets after special character or a number to the uppercase
Synatx : var_name.title()
'''
# a = 'hello world hello universe'
# print(a.title())    #Hello World Hello Universe

# b = 'hello@w0rld 5hai'
# print(b.title())        #Hello@W0Rld 5Hai

# c = 'hello @WORLD'
# print(c.title())        #Hello @World

#-----------------------------------------------------
'''index : Will give the index number of the first occurance of the character specified
Will throw ValueError if the character is not found
Syntax : var_name.index('character', [start index= 0], [end index = len(str)])
'''
# a = 'python is a programming language'
# print(a.index('r'))
# print(a.index('o'))
# print(a.index('p', 7, 15))      #12
# print(a.index('p', 7))
# print(a.index('p', , 10))       # SyntaxError. We cant skip the start index
# print(a.index('z'))     #ValueError
# print(a.index('l', 7, 15))  #ValueError

#------------------------------------------------------
'''rindex : Will give the index number of the last occurance of the character specified
Will throw ValueError if the character is not found
Syntax : var_name.rindex('character', [start index= 0], [end index = len(str)])'''
# a = 'python is a programming language'
# print(a.rindex('p'))        #12
# print(a.rindex('o', 3, 17))     #14
# print(a.rindex('z'))        #ValueError

#--------------------------------------------------------
'''find and rfind'''
# a = 'python is a programming language'
# print(a.find('o'))
# print(a.find('z'))
# print(a.rfind('a'))     #29
# print(a.find('a', 3, 17))
# print(a.rfind('e', 24, 28))
# print(a.rfind('e'))

#----------------------------------------------
'''replace() : To replace the old string with the new string, we will use replace() method
Syntax : var_name.replace('old value', 'new value', [count])
'''
# a = 'achievement'
# print(a.replace('e', '*'))      #achi*v*m*nt
# print(a.replace('e', '*', 2))       #achi*v*ment
# print(a.replace('e', 'm', '*')) #TypeError: 'str' object cannot be interpreted as an integer
# print(a.replace('e', '*', 10000))       #achi*v*m*nt
# print(a.replace('ie', '*'))     #ach*vement
# print(a.replace('ei', '*'))     #achievement

#--------------------------------------------------------------
'''05 April 2023'''

'''startswith() : It will check if the string is starting with the character 
specified or not
Syntax : var_name.startswith('character', [start_value=0], [end_value=len(str)])

* The return type of startswith() is boolean
'''
# a = 'hello universe'
# print(a.startswith('h'))
# print(a.startswith('H'))
# print(a.startswith('h', 2, 7))

# a = '123 hello'
# print(a.startswith(1))      #TypeError

#--------------------------------------------
'''endswith() : It will check if the string is ending with the character specified
Syntax : var_name.endswith('character', [start_value=0], [end_value=len(str)])

* Return type is booelan
'''
# a = 'hello python'
# print(a.endswith('N'))      #False
# print(a.endswith('o', 0, 5))

##################################################################
'''partition() and rpartition(): It will partition the string at the specified element.
partition and rpartition will always give the tuple consisting of three elements, 
where the middle element is the partitioned element, 
first element is the elements before partition and the last element is the elements 
after partition
Syntax : var_name.partition('character')
         var_name.rpartition('character')

'''
# a = 'universe'
# print(a.partition('v'))     #('uni', 'v', 'erse')
# print(a.partition('e'))     #('univ', 'e', 'rse')
# print(a.partition('u'))     #('', 'u', 'niverse')
# print(a.partition('z'))     #('universe', '', '')
#
# print(a.rpartition('e'))    #('univers', 'e', '')

###################################################
'''strip() and rstrip() : It’s an inbuilt method which strips the specified char from both the ends of
original string
Syntax : var_name.strip('characters')

lstrip will remove only the leading characters
rstrip will remove only the trailing characters

* The return type of strip is str
* If the character is not mentioned, by deafult strip methpd will remove the whitespaces
'''
# a = '*********hello******'
# print(a.strip('*'))     #hello

# a = '*&#*$ %hello %^#**'
# print(a.strip('*&^#'))      # $ %hello %
# print(a.strip())        #*&#*$ %hello %^#**

# a = '*&#*$ %hello %^#**'
# print(a.strip('*&^#'))      #$ %hello %
# print(a.lstrip('*&^#$ %'))      #hello %^#**
# print(a.rstrip('*&^#$ %'))      #*&#*$ %hello

#############################################
'''split() : Splits the string at the specified separator, and returns a list.
Syntax : var_name.split([character], [maxsplit])

The return type of split is list.
If the character is not specified, by default it will split at the spaces
'''
# a = 'python'
# print(a.split('yt'))        #['p', 'hon']
# print(a.split('ty'))        #['python']

# a = 'she sells seashells on the seashore'
# print(a.split('h'))     #['s', 'e sells seas', 'ells on t', 'e seas', 'ore']
# print(a.split('s'))     #['', 'he ', 'ell', ' ', 'ea', 'hell', ' on the ', 'ea', 'hore']

# print(a.split('e'))     #['sh', ' s', 'lls s', 'ash', 'lls on th', ' s', 'ashor', '']
# print(a.split('e', maxsplit=3))     #['sh', ' s', 'lls s', 'ashells on the seashore']

# print(a.rsplit('e'))    #['sh', ' s', 'lls s', 'ash', 'lls on th', ' s', 'ashor', '']
# print(a.rsplit('e', maxsplit=3))    #['she sells seashells on th', ' s', 'ashor', '']

# a = 'she sells seashells on the seashore'
# print(a.split())

# a = 'hey there I am using whatsapp'
# print(a.split())    #['hey', 'there', 'I', 'am', 'using', 'whatsapp']

#################################################
'''join() : It’s an inbuilt method which will join the elements of iterables (collection data
type) with a specified string.
Syntax: “string”.join(iterable)

It takes only one argument and it’s a required argument.
Return type is string
'''

# a = 'hello'
# print('*'.join(a))      #h*e*l*l*o
#
# b = ['hey', 'there', 'I', 'am', 'using', 'whatsapp']
# print(' '.join(b))      #hey there I am using whatsapp

########################################################
'''
isalnum() : Returns True if all characters in the string are alphanumeric.
isalpha() : Returns True if all characters in the string are in the alphabet.
isdigit() : Returns True if all characters in the string are digits.
islower() : Returns True if all alpha characters in the string are lower case.
isnumeric() : Returns True if all characters in the string are numeric.
isspace() : Returns True if all characters in the string are whitespaces.
istitle() : Returns True if the string follows the rules of a title.
isupper() : Returns True if all alpha characters in the string are upper case.

'''
#################################
# a = 'hello'
# print(a.isalpha())      #True
#
# b = 'hello world'
# print(b.isalpha())

#-----------------------------------
'''isnumeric()/isdigit()'''
# a = '1234'
# print(a.isnumeric())
#
# b = '12 34'
# print(b.isdigit())

##########################
'''isalnum() : '''
# print('123'.isalnum())
# print('abc'.isalnum())
# print('123abc'.isalnum())
# print('123 abc'.isalnum())

#-------------------

# print(bool('1'))        #True
# print(bool(''))     #False
# print(bool(str()))  #False

'''NOTE : ''(empty string) and str() are the default values of a string'''

# a = 10
# b = str(a)
# print(b, type(b))       #10 <class 'str'>

######
# a = '100'
# b = int(a)
# print(b, type(b))       #100 <class 'int'>

# a = '9.8'
# print(int(a))       #ValueError
# b = float(a)
# print(b, type(b))       #9.8 <class 'float'>

#--------------------------------------------------------------------------



















