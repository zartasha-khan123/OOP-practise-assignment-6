#1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor.
# Add a method display() that prints student details.


class Student():
    def __init__(self,name:str,marks:int):
        self.name =name
        self.marks = marks
        
    def display(self):
        print (f"Name:{self.name} Marks:{self.marks}")
 
 
student = Student("zartash\n",95)
student.display() 



# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.


class Counter():
    counter = 0 
    @classmethod
    def count(cls):
      cls.counter += 1
      return cls.counter
    
counts1 = Counter()
counts2 = Counter()
print(counts1.count())
print(counts2.count())




# 3 - Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.



class Car():
    def __init__ (self,brand):
        self.brand = brand
        
        
    def start(self):
        print(f"car brand is {self.brand}")
        
car = Car("toyata")
car.start()            
        
        
        
        
        
# 4 - Class Variables and Class Methods

# Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.        


class Bank():
   
    bank_name ="metro bank"
    
    @classmethod 
    def change_bank_name(cls,name):
        cls.bank_name = name
        print(f"our bank name is {cls.bank_name} which is change by class method")
        
        
# Show that it affects all instances.      
bank1= Bank()
bank2 = Bank()
bank1.change_bank_name("habib bank limited") 


print(bank1.bank_name)
print(bank2.bank_name)
print(Bank.bank_name)
       
       
       

# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. 
# No class or instance variables should be used.


class MathUtils():
    
    @staticmethod  # static na cls ko na self ko layta hain independent logic build krta hain
    def add(a,b):
      return a + b
  
print(MathUtils.add(3,2))




# 6-  Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and 
# another message when it is destroyed (destructor).
    
       
class Logger():
    def __init__(self,message):
        self.message = message
        print(f"Constructor : {self.message}")
        
        
    def __del__(self):
        print(f"Destructor: Object is destroyed")   
        
        
logger = Logger("Object is Created")       
  
  
del logger
        
        
      
      
      
#7- Access Modifiers: Public, Private, and Protected


# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee():
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
        
        
        
    def detail(self):
        print(f"Name: {self.name} , Salary: {self._salary} , Ssn: {self.__ssn}")
        
        
employee= Employee("zartasha", 100000, 1234567) 
print(employee.name)       #public variable
print(employee._salary)   # protected variable
# print(Employee.__ssn)   # public variable can not be access directly
print(employee._Employee__ssn)  # This will work but it's not recommended -Python name mangling karta hai private variables ke liye.
employee.detail()      
    
    
    
    
# 8 - The super() Function
# Assignment:

# Create a class Person with a constructor that sets the name.
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.


class Person():
    def __init__(self,name):
        self.name = name
        
        
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        
    def inherit(self):
        return f"Person name is : {self.name} and subject is : {self.subject}"  
            
    
person = Teacher("zartasha", "Python")
print(person.name)
print(person.subject)
print(person.inherit())
        
        
       

# 9 -  Abstract Classes and Methods

# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().        
        

from abc import ABC , abstractmethod


class Shape (ABC):
    
    
    @abstractmethod
    def area(self):
        pass

    
    
class Rectangle(Shape):
    def __init__(self,height,width):
       self.height = height
       self.width = width
       
       
    def area(self):
        return self.height * self.width   
    
    
shape = Rectangle(5,3)   
print(shape.area())
    
    
    
    
# 10 - Instance Methods

# Assignment:
# Create a class Dog with instance variables name and breed. 
# Add an instance method bark() that prints a message including the dog's name.


class Dog ():
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
    
    
  def bark(self,sound="wooff"):
      self.sound = sound
      print (f"My dog name is {self.name} and he is a {self.breed} and he is barking like {self.sound}")
      
      
      
dog = Dog("bilwee","German-Shepherd") 

print(dog.bark())     
      


  
  
# 11 - Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count()
# to increase the count when a new book is added.


class Book():
    total_books = 0
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        return cls.total_books
    
print(Book.increment_book_count())    
print(Book.increment_book_count())
print(Book.increment_book_count())
        
        
        
        
# 12 -  Static Methods
# Assignment:
# Create a class TemperatureConverter with a static 
# method celsius_to_fahrenheit(c) that returns the Fahrenheit value.    


class TemperatureConverter():
    
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        
        return (c * 9/5) + 32
    
temp_c = 25    
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c) 

print(temp_f) 






# 12 - . Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.
    
    
class Engine():
    def __init__(self, speed):
        self.speed = speed
        
    def start(self):
       return f"Engine with {self.speed} HP started."
        
            
class Car():
    def __init__(self,brand,speed):
        self.brand = brand
        self.engine = Engine(speed)  # Composition: Car HAS-A Engine
        
        
    def drive(self):
        return f"Car with this name {self.brand}  is driving , {self.engine.start()}" 
        
        
        
my_car = Car("toyata carola", 150)    
print(my_car.drive())
        
               
               
               
# 14 -Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object 
# store a reference to an Employee object that exists independently of it.


class Department():
   def __init__(self,course_name):
       self.course_name = course_name
       
       

class Employee():
    def __init__(self,name,age,department):
        self.name = name
        self.age = age
        self.department = department #  # Aggregation: using existing Department object


    def details(self):
         return f"Employee name is {self.name} , age is {self.age} and course is {self.department.course_name}"
     
     
department = Department("Python Programming")   # Pehle Course ka object bana

employee= Employee("zartasha", 27 ,department)    

print(employee.details())  # Aggregation: Employee has-a Department object

   
   
   
# 15 - Method Resolution Order (MRO) and Diamond Inheritance

# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.   
                      
        
class A ():
    def __init__(self):
        pass
    
    def show(self):
        return f"hello from class A"  
    
    
class B (A):
    def __init__(self):
        pass
    
    
  #override show () method from class A
  
    def show(self):
        return f"hello from class B"
    
    
class C (A):
    def __init__(self):
        pass
    
    
    
    #override show () method from class A
    
    
    def show(self):
        return f"hello from class C"
    
    
    
class D (B,C):
    def __init__(self):
        pass
    
    
   
  
classD = D()
print(classD.show())# prints: hello from class D hello from class B
#Explanation: The MRO of D is B, C, A. So it first calls show

print(D.__mro__)




# 16 -  Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes.
# Apply it to a function say_hello().


def log_function_call(func):
     def wraper():
      print("Function is being called")
      return func()
     return wraper 
 
# Applying decorator to a function 
@log_function_call

def say_hello():
     print ("hello from decorator" )
 
 
say_hello()   



# 17 - Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!".
# Apply it to a class Person.
   
    
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls


@add_greeting
class Person():
    def __init__(self,name):
        self.name = name
        
     
p = Person("zartasha")
print(p.greet())               
        



# 18 - Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price,
# @price.setter to update it, and @price.deleter to delete it.        
        
    
class Product():
    
    def __init__(self,price):
        self._price = 20000
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value < 0:
            print("Price can not be negative")
            
        else:
            self._price = value
        
    
    @price.deleter
    def price(self):
        print (f"Product price is deleted")
        del self._price 
    
    
p= Product(20000)
print("Price is:" , p.price) 

p.price = 30000
print("updated price is:" , p.price)

p.price = -1000

del p.price



# 19 - callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input
# by the factor. Test it with callable() and by calling the object like a function.


class Multiplier():
    def __init__(self,factor):
        self.factor = factor
        
        
    def __call__(self,value):
        self.value = value
        return self.factor * value  # multiply input value by factor
    
 #create object (instance)   
call = Multiplier(4)    

#access factor
print("factor :" , call.factor)


## Check if object is callable
print("Is callable : " ,callable(call))


## Call object like function

print("Result of call(2) :"  ,call(2))




# 20 -  Creating a Custom Exception

# Assignment:
# Create a custom exception InvalidAgeError.
# Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be atleast 18")
    
    else:
        print("age is valid!")
        
  #Try...except to handle the exception      
try:
    user_age = int(input("Enter your age : "))
    check_age(user_age)
    
    
except InvalidAgeError as e:
    print ("custom Exception caused as ", e)    
    
    
except ValueError:
    print("Please Enter a valid number")   
    
    
    
    
# 21 -  Make a Custom Class Iterable
# Assignment:

# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the
# object iterable in a for-loop, counting down to 0.    
    
    
class Countdown():
    def __init__(self, start):
        self.current = start
        
        
    def __iter__(self):
        return self    # Return the iterator itself
    
    def __next__(self):   # 
        if self.current  < 0:
            raise StopIteration
        else:
            val=self.current 
            self.current -= 1
            return val
        
        
        
for number in Countdown(6):
    print(number)
        
            
    
    
 
    
              


    
    
    
    
    
  
            
        
    



    
    
    
       
        
       
       

           
           
             
        
        
    
    
    

  
    
        
    




