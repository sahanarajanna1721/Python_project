class Spam:
    def __init__(self, value):
        self.value = value
    
    def apple(self):
        print(f"running Parent class apple method {self.value}")
    
    def google(self):
        print(f"running Parent class google method")
        self.apple()

# case-1 (Child inherits from parent and child having completely independent method)
class Demo(Spam):
    def __init__(self, value):
        # calling parent class constructor or __init__ method
        super().__init__(value)

    def yahoo(self):
        print("running Demo class Yahoo method")

# case-2 (child completely over-riding parent class method)
class Demo1(Spam):
    def __init__(self, value):
        super().__init__(value)

    # re-defining "apple" method in child class
    # over-riding the parent class's apple method in child class (over-riding parent class attribute in child class)
    def apple(self):
        print("running Demo1 apple method")

# case-3 ()
class Demo2(Spam):
    def __init__(self, value):
        super().__init__(value)

    # adding extra func in child class apple and re-using parent class apple method
    def apple(self):
        print('some extra func in Demo2 apple') # extra functionality in child class
        super().apple()     # giving a call to parent class apple method

# case-4 (Child class having its own attributes inside __init__ method)
class Demo3(Spam):
    def __init__(self, value, a, b):
        super().__init__(value)
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

class Spam2:
    def __init__(self, name):
        self.name = name

    def facebook(self):
        print("running Spam2 facebook")
        print(self.name)

# case-5 (Child inehriting from multiple parents "Multiple Inheritance")
class Demo4(Spam, Spam2):
    def __init__(self, value, name):
        Spam.__init__(self, value)
        Spam2.__init__(self, name)
    
    def watsapp(self):
        print("watsapp")

# multi-level inheritance
class A:
    def demo(self):
        print("A")

class B(A):
    def demo(self):
        print("B")
        super().demo()

class C(B):
    def demo(self):
        print("C")
        super().demo()


class Spam:
    # class variable
    a = 10

    def apple(self):
        print(self.__class__.a)

class Apple(Spam):
    # re-defning class attribute or class variable 'a'
    a = 100
