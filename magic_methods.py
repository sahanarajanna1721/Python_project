# ---------------------------------------------------------------------------------------------
# Container Protocol
# ---------------------------------------------------------------------------------------------
"""
1. __contains__(self, obj)
2. __len__(self)
3. __getitem__(self, index)
4. __setitem__(self, index, value)
5. __delitem__(self, name)
"""
names = ['apple', 'google', 'yahoo']
names.__contains__("apple")     # Same as "apple" in names
names.__len__()     # Sames as len(names)
names.__getitem__(0)    # Same as names[0]
names.__setitem__(1, 'facebook')    # Same as names[1] = "facebook"

# Custom class which supports container protocol
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __len__(self):
        return 2
    
    def __contains__(self, value):
        if value == self.a or value == self.b:
            return True
        return False
    
    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise IndexError("Index cannot be > 2")
        
    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            raise IndexError("Index cannot be > 2")

    def __delitem__(self, index):
        raise AttributeError(f"Sorry Cannot delete item at index {index}")
# ---------------------------------------------------------------------------------------------
class PositivePoint(Point):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def __setitem__(self, index, item):
        if item < 0:
            raise Exception(f"Cannot set the negative value at index {index}")
        super().__setitem__(index, item)
# ---------------------------------------------------------------------------------------------        
# Setting range of values to be set for "a" and "b"
# the permissible value for "a" is between 0-100 (both inclusive)
# the permissible value for "b" is between 0-50 (both inclusive)
class RangePoint(Point):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __setitem__(self, index, value):
        if index == 0:
            if value in range(0, 101):
                super().__setitem__(index, value)
            else:
                raise Exception
        elif index == 1:
            if value in range(0, 51):
                super().__setitem__(index, value)
            else:
                raise Exception
# ---------------------------------------------------------------------------------------------         
#Custom Container Object "Point"
# Alternate Implementation
# ---------------------------------------------------------------------------------------------         
class Point:
    def __init__(self, *values):
        self._points = [*values]

    def __len__(self):
        return len(self._points)    # self._points.__len__()
    
    def __contains__(self, value):
        if value in self._points:
            return True
        return False

    def __getitem__(self, index):
        return self._points[index]

    def __setitem__(self, index, value):
        if value < 0:
            raise ValueError("Cannot set negative value")
        self._points[index] = value

    def __delitem__(self, index):
        del self._points[index]
# ---------------------------------------------------------------------------------------------
# Attribute Protocol
# ---------------------------------------------------------------------------------------------
"""
1. __getattribute__(self, name)
2. __getattr__(self, name)
3. __setattr__(self, name, value)
4. __delattr__(self, name)
"""
"""
1. Whenever an attribute is accessed, the __getattribute__() method is invoked.
2. If __getattribute__ method finds the attribute, its value is returned. Otherwise, __getattribute__ method calls __getattr__
   method as fallback mechanism. __getattr__ method is called only for missing attribute.
3. The default behavior of __getattr__() is to raise an AttributeError exception. (we can override this method)
4. The __setattr__() method is always invoked when setting an attribute. 
and the __delattr__() method is always invoked when deleting an attribute.
"""
# ---------------------------------------------------------------------------------------------
# "Point" object which allows only positive values for "a" and "b"
class PositivePoint:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Overriding __setattr__ method
    def __setattr__(self, name, value):
        if value < 0:
            raise ValueError("Cannot set a negative value")
        super().__setattr__(name, value)
# ---------------------------------------------------------------------------------------------
# Converting "fname" and "lname" to upper case using __setattr__ method
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __setattr__(self, name, value):
        super().__setattr__(name, value.upper())
# ---------------------------------------------------------------------------------------------
# Reversing "fname" and "lname" using __setattr__ method
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __setattr__(self, name, value):
        super().__setattr__(name, value[::-1])
# ---------------------------------------------------------------------------------------------
# Validate the values of 'a' and 'b' only for numbers
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __setattr__(self, name, value):
        if name == "a" or name == "b":
            if not isinstance(value, (int, float)):
                raise ValueError
        super().__setattr__(name, value)
    
    def mul(self):
        return self.a * self.b
# ---------------------------------------------------------------------------------------------
# validating 'fname', 'lname' and 'pay'
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def __setattr__(self, name, value):
        # Restricitng "fname" and "lname" to maximum of 5 characters
        if name == "fname" or name == "lname":
            if len(value) > 5:
                raise ValueError(f"{name} cannot be more than 5 characters")
        # Restricting "pay" to minimum of $500
        if name == "pay":
            if value < 500:
                raise ValueError(f"pay cannot be less than 500")
        super().__setattr__(name, value)
# ---------------------------------------------------------------------------------------------
# Restricting the user from adding new attributes to the class using __setattr__ method
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def __setattr__(self, name, value):
        if not name in ("fname", "lname", "pay"):
            raise AttributeError(f"No Attribute named {name}")
        super().__setattr__(name, value)
# ---------------------------------------------------------------------------------------------
# Making an Immutable Class by customizing __setattr__ and __delattr__ method
class Point:
    def __init__(self, x, y):
        super().__setattr__("x", x)
        super().__setattr__("y", y)

    def __setattr__(self, name, value):
        print('Calling __setattr__')
        raise AttributeError("Cannot set attribute value")

    def __delattr__(self, name):
        print("Calling __delattr__")
        raise AttributeError("Cannot delete an attribute")
# ---------------------------------------------------------------------------------------------
# Alternate method of making class Readonly
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
# Wrapping the Point object inside ReadOnly class
class ReadOnly:
    def __init__(self, point):
        super().__setattr__("point", point)
    
    def __setattr__(self, name, value):
        raise AttributeError()
        
    def __getattr__(self, name):
        return getattr(self.point, name)   

    def __delattr__(self, name):
        raise AttributeError("cannot delete attribute")
# ---------------------------------------------------------------------------------------------
# Comparison Protocol
# ---------------------------------------------------------------------------------------------
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __eq__(self, other):
        if self.age == other.age:
            return True
        return False
    
    def __lt__(self, other):
        if self.age == other.age:
            return True
        return False
    
    def __gt__(self, other):
        if self.age > other.age:
            return True
        return False
# ----------------------------------------------------------
# Alternate Implementation (comparing pay)
# ----------------------------------------------------------
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __eq__(self, other):
        if self.pay == other.pay:
            return True
        return False
    
    def __lt__(self, other):
        if self.pay == other.pay:
            return True
        return False
    
    def __gt__(self, other):
        if self.pay > other.pay:
            return True
        return False
# ---------------------------------------------------------------------------------------------
# Number Protocol
# ---------------------------------------------------------------------------------------------
x = 10
x.__add__(10)
x.__mul__(10)
x.__sub__(10)

# Custom class which supports Number Protocol
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Point(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Point(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Point(self.a * other.a, self.b * other.b)
# ---------------------------------------------------------------------------------------------
# Truthiness implementation using __bool__ and __len__
"""
By default, an object is considered true unless its class defines either a __bool__() method that 
returns False or a __len__() method that returns zero, when called with the object.
"""
# Point class has not implemented either __bool__ or __len__
# So by default, the boolean value of point object is always considered as True
# --------------------------------------------------------------------------------------
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __bool__(self):
        if self.age < 18:
            return False
        return True

e1 = Employee("steve", 20, 1000)   # bool(e1) -> True
e2 = Employee("jobs", 17, 2000)    # bool(e2) -> False
# --------------------------------------------------------------------------------------
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
    
    # __len__ function is called as fallback mechanism if __bool__ is not defined on the object.
    # an object evaluates to boolean True if __len__ function returns an integer 1, and to False
    # if __len__ function return integer 0
    # If both __bool__ and __len__ are not defined, the object is considered to be evaluated to True
    def __len__(self):
        if self.age < 18:
            return False
        return True
# --------------------------------------------------------------------------------------
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
p1 = Point(0, 0)        # bool(p1) -> True
p2 = Point(1, 2)        # bool(p2) -> True
p3 = Point(1, 0)        # bool(p3) -> True
p4 = Point(0, 1)        # bool(p4) -> True
p5 = Point(-1, 1)       # bool(p4) -> True
p6 = Point(1, -1)       # bool(p6) -> True

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # By default __bool__ is called to evaluate Truthiness of the object.
    def __bool__(self):
        if self.a == 0 and self.b == 0:
            return False
        elif self.a < 0 or self.b < 0:
            return False
        return True

p1 = Point(0, 0)        # bool(p1) -> False
p2 = Point(1, 2)        # bool(p2) -> True
p3 = Point(1, 0)        # bool(p3) -> True
p4 = Point(0, 1)        # bool(p4) -> True
p5 = Point(-1, 2)       # bool(p5) -> False
p6 = Point(1, -3)       # bool(p6) -> False

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # __len__ function is called as fallback mechanism if __bool__ is not defined on the object
    # If both __bool__ and __len__ are not defined, the object is considered to be evaluated to True
    def __len__(self):
        if self.a <= 0 and self.b <= 0:
            return 0
        return 1

p1 = Point(0, 0)        # bool(p1) -> False
p2 = Point(1, 2)        # bool(p2) -> True
p3 = Point(1, 0)        # bool(p3) -> True
p4 = Point(0, 1)        # bool(p4) -> True
p5 = Point(-1, 1)       # bool(p4) -> True
p6 = Point(1, -1)       # bool(p6) -> True
p7 = Point(-1, -3)      # bool(p6) -> False
# ---------------------------------------------------------------------------------------------
# Function Protocol
# ---------------------------------------------------------------------------------------------
"""
1. __call__
"""
class Greeting:
    def __init__(self, name="world"):
        self.name = name
    
    def __call__(self):
        return f"hello {self.name}"
    
class Greeting:
    def __call__(self, name):
        print(f'Hello {name}')

class Spam:
    def __init__(self, a):
        self.a = a

    def __call__(self):
        print('Executing __call__ ',self.a)

class Squares:
    def __call__(self, numbers):
        squares = []
        for number in numbers:
            squares.append(number ** 2)
        return squares

class Evens:
    def __call__(self, number):
        if number % 2 == 0:
            return True
        else:
            return False

# Class implementation of a decorator
class Log:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("You called {self.func.__name__}")
        return self.func(*args, **kwargs)

class Time:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f'Execution Time: {end-start}')
        return result

class Record:
    def __init__(self, func):
        self.func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self.func(*args, **kwargs)

# Using callable classes in sorted() function
# Sorting the list based on the last character of the list item
class LastChar:
    def __call__(self, item):
        return item[-1]

items = ['bv', 'aw', 'dt', 'cu']
last = LastChar()
s = sorted(items, key=last)

# Sorting based on temperatures
class Temperature:
    def __call__(self, item):
        return item[-1]

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
temperature = Temperature()
sorted(temperatures, key=temperature)


portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

class By:
    def __init__(self, key):
        self.key = key

    def __call__(self, item):
        if self.key == "name":
            return item['name']
        elif self.key == "shares":
            return item['shares']
        else:
            return item['price']

# Sorting Based on name
sorted(portfolio, key=By("name"))

# Sorting Based on Shares
sorted(portfolio, key=By("shares"))

# Sorting Based on Price
sorted(portfolio, key=By("price"))
# ---------------------------------------------------------------------------------------------
# string representation of an object
class Employee:
    def __init__(self, fname, lname, age):
        self.fanme = fname
        self.lname = lname
        self.age = age
    
    def __repr__(self):
        return f"({self.fname}, {self.lname}, {self.age})"
# ---------------------------------------------------------------------------------------------
# Iterator Protocol
"""
1. __iter__
2. __next__
* Any object that implements __iter__ method is called as "iterable"
* __iter__ method should return an object instance to the class that implements __next__ method
* __next__ method knows how to give the next value until it hits "StopIteration" exception
"""
class PointIterator:
    def __init__(self):
        self.index = 0

    # __next__ method knows how to give the next value
    def __next__(self):
        if self.index >= 2:
            raise StopIteration
        next_number = self.index
        self.index += 1
        return next_number

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __iter__(self):
        # This should return an object instance to the class which implements __next__ method
        pi = PointIterator()
        return pi
# ---------------------------------------------------------------------------------------------
class PointIterator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._points = (self.a, self.b)
        self.index = 0

    # __next__ method knows how to give the next value
    def __next__(self):
        if self.index >= len(self._points):
            raise StopIteration
        next_number = self._points[self.index]
        self.index += 1
        return next_number

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __iter__(self):
        # This should return an object instance to the class which implements __next__ method
        pi = PointIterator(self.a, self.b)
        return pi
# ---------------------------------------------------------------------------------------------
# Object Protocol
"""
1. __new__
2. __init__
3. __del__
4. __repr__
"""      
# Descriptor Protocol
"""
1. __get__
2. __set__
3. __del__
"""
# ---------------------------------------------------------------------------------------------
# Context Manager Protocol
"""
1. __enter__
2. __exit__
"""
# ---------------------------------------------------------------------------------------------
