class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def reset(self):
        self.a = 0
        self.b = 0
    
    def swap(self):
        temp = self.a
        self.a = self.b
        self.b = temp
    
    def move(self, dx, dy):
        self.a = self.a + dx
        self.b = self.b + dy
    
    def sum(self):
        return self.a + self.b

# creating an instance of Point class or creating Point object or saving data inside Point class
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(4, 5)


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b


c1 = Calculator(2, 3)
c2 = Calculator(3, 6)
c3 = Calculator(4, 5)


class Employee:
    def __init__(self, fname, lname, age, pay):
        # instance variables
        self.fname = fname
        self.lname = lname
        self.age = age
        self.pay = pay
    
    def email(self):
        return f"{self.fname}.{self.lname}@comapny.com"

    def hike(self, percentage):
        hike_amount = self.pay * percentage
        self.pay = self.pay + hike_amount


e1 = Employee("steve", "jobs", 26, 1000)
e2 = Employee("bill", "gates", 27, 2000)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
    
    def attack(self, pts):
        print("attacking the player")
        self.health = self.health - pts
        if self.health <= 0:
            print("Game Over!!!!")

p1 = Player(1, 2)
p2 = Player(3, 4)
p3 = Player(5, 6)


class Point:
    # over-loaded constructor
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c

p1 = Point()
p2 = Point(1)
p3 = Point(1, 2)
p4 = Point(1, 2, 3)