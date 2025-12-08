
"""OOPs (Object-Oriented Programming System) in Python is a way of structuring code around classes and objects.
The four main concepts are Encapsulation, Inheritance, Polymorphism, and Abstraction.
or python is programming paradigm based on the concepts of objects,which can contains data and methods.
"""
"""
class:class is collection of data members and methods.
Or
A class is a blueprint or template for creating objects.
It defines attributes (data) and methods (behavior) that the objects created from it will have.
Syntax:
class ClassName:
    # attributes (variables)
    # methods (functions)
    def method(self):
        pass
note:every class is programmer defined data type.
Object:when you created an object the memory space  will be allocated.
or allocating the sufficient memory space for data members and methods.
1.An object is an instance of a class.
2.When you create an object, Python allocates memory and binds the class’s attributes and methods to that object.
Syntax:obj = ClassName()   # object creation
"""
#Ex1:Real-world Scenario 1: Car Manufacturing
#Class: Car (blueprint for all cars)
#Objects: Tesla, BMW, Toyota (actual cars built from the blueprint)
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color=color
    def drive(self):
        print(f"{self.brand}  {self.color} is  driving")
car1=Car("BMW","blue")
car2=Car("Honda","yellow")
car1.drive()
car2.drive()
#Ex2:Real-world Scenario 2: Bank Account
#Class: BankAccount (blueprint for accounts)
#Objects: ANIL’s account, Alice’s account
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposite(self,amount):
        self.balance=self.balance+amount
        print(f"{self.owner} deposited {amount} and now available balance {self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{self.owner} withdrawn amount is {amount} and now available balance {self.balance}")
        else:
            print(f"{self.balance} is very low or insufficient balance")
account1=BankAccount("Anil",10000)
account2=BankAccount("Hari",30000)
account1.deposite(1000)
account2.withdraw(5000)
print("====================================================================")
"""Types of Methods in Python Classes: a class can have different types of methods depending on how they interact with the class and its objects:
1.Instance Methods
==================
Operate on object instances.
First parameter is always self (represents the current object).
Used to access or modify object attributes.
Syntax:class MyClass:
          def instance_method(self, arg1, arg2):
            # logic using self
             return arg1 + arg2
"""
class BankAccount:
    def __init__(obj,owner,balance):
        obj.owner=owner
        obj.balance=balance
    def deposite(obj,amount):
        obj.balance=obj.balance+amount
        print(f"{obj.owner} deposited {amount} and now available balance {obj.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{self.owner} withdrawn amount is {amount} and now available balance {self.balance}")
        else:
            print(f"{self.balance} is very low or insufficient balance")
account1=BankAccount("Anil",10000)
account2=BankAccount("Hari",10000)
account1.deposite(1000)
account2.withdraw(1000)
print("===============================================================================")
"""
2.Class Methods
===============
A class method works with the class itself, not just individual objects.
It’s defined using the @classmethod decorator.
The first parameter is cls, which refers to the class.
Common use case: alternative constructors (different ways to create objects).
Syntax:class MyClass:
            @classmethod
            def class_method(cls, arg1):
                  # logic using cls
                return cls
"""
#Ex:Imagine a company where employee records can be created in multiple ways:
#Normally, by passing name and role.
#Alternatively, by parsing a string like "UPPARA-Developer".
class Employee:
    company="PTG"
    def __init__(self,name,role):
        self.name=name
        self.role=role
    #classmethod:alternative constructor
    @classmethod
    def frm_string(cls,emp_string):
        name,role=emp_string.split("-")#Alice-Designer this name should split and stored in name and role.
        return cls(name,role)
    #class method:company wide info
    @classmethod
    def company_info(cls):
        print(f"all employs worked at {cls.company}")

# Normal object creation
emp1 = Employee("UPPARA", "Developer")
# Alternative constructor using class method
emp2 = Employee.frm_string("Alice-Designer")
# Accessing company info via class method
Employee.company_info()
print(emp1.name, emp1.role)
print(emp2.name, emp2.role)

print("="*80)
"""
3. Static Methods:
==================
Do not depend on self or cls.
Defined using @staticmethod decorator.
Behave like normal functions but live inside the class for logical grouping.
#note:to create own utility functions
Syntax:
        class MyClass:
            @staticmethod
            def static_method(arg1, arg2):
             return arg1 * arg2

"""
#Ex:
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y  #return the value
    @staticmethod
    def is_even(num):
        return num % 2 == 0 #True or False
# Usage
print(MathUtils.add(10, 20))
print(MathUtils.is_even(42))
print("="*80)

"""
Variables:Instance Variables
Variables unique to each object (instance).
Defined inside methods, usually inside __init__.
Characteristics:
Each object gets its own copy.
Changing one object’s variable won’t affect another.
Accessed using self.variable_name."""
class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable
s1 = Student("Anil", 21)
s2 = Student("Rahul", 22)
#print(Student.name)  # AttributeError: type object 'Student' has no attribute 'name'(when you access the instance variable through the class name)
print(s1.name)  # Anil
print(s1.age)#21
print("="*80)
"""
Class Variables (Static Variables):
Variables that belong to the class, not individual objects.
Shared among all objects.
Characteristics:
Defined inside the class but outside methods
All objects use same value unless overridden
Accessed using ClassName.var or self.var
================================================
Shared across all objects of the class.
Defined directly inside the class, outside methods.
Accessed using ClassName.variable or self.variable"""
class Employee:
    company="TCS"
    def __init__(self,name):
        self.name=name#instance variables
        # print(self.company)#note class variables also accessible by using self
        # self.company="RAMRAJ"
        # print(self.company)#RAMRAJ
    @classmethod
    def demo(cls):
        print(cls.company)#TCS
        # cls.company="PTG"
        # print(cls.company)#PTG
emp1=Employee("ANil")
emp1.demo()
#to change the class variable by using object name
emp1.company="Amazon"
print(emp1.company)#Amazon
#to change the class variable name by using class
Employee.company="Surya Company"
print(Employee.company)#Surya Company
"""
Variables created inside a method, accessible only within that method.
Characteristics:
Temporary variables
Scope ends after method execution
Not available outside the method
=======================================
Local Variables:
Declared inside a method.
Exist only while the method is running.
Not accessible outside the method.
"""
class Demo:
    other="I dont know"# class variables
    def __init__(self,name):
        self.name=name#instance variable
    def dispay_data(self):
        age=12#local variables
        phone=788788789#local variables
    def outside_data(self):
        #print(self.age)#AttributeError: 'Demo' object has no attribute 'age'(Because of it is local variable
        print(self.name)
        #print(self.phone)#AttributeError: 'Demo' object has no attribute 'phone'
        print(self.other)#even access class variable by using self
obj1=Demo("Anil")
obj1.outside_data()

#ex:2
class Test:
    def show(self):
        x = 10            # local variable
        print(x)
t = Test()
t.show()
#print(t.x)#AttributeError: 'Test' object has no attribute 'x'
print("="*80)

"""
Properties (Using @property):
===============================
These look like variables but behave like functions.
Used to control access to instance variables.
We use @property to create safe, controlled, flexible, 
and readable access to internal variables—even if Python does not fully block direct modification."""
class Bank:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
obj = Bank(100)
obj._balance=5000
print(obj.balance)
"""
Type-Annotated Variables (Python ≥ 3.6):
==========================================
Used for clarity and static checking (PEP 526)."""
class Demo:
    x: int = 10         # class variable with type hint
    def __init__(self):
        self.y: float = 5.5# instance variable with type hint"""
temp=Demo()
print(temp.x)#10
print(temp.y)#5.5
print("="*80)
"""| Variable Type | Where defined?                           | Scope                   | Shared?           | Stored In         |
| ------------- | ---------------------------------------- | ----------------------- | ----------------- | ----------------- |
| **Instance**  | inside methods (`__init__`) using `self` | Object-level            | ❌ No              | Object dictionary |
| **Class**     | inside class (not method)                | Class-level             | ✔ Yes             | Class dictionary  |
| **Local**     | inside methods                           | Method only             | ❌ No              | Stack frame       |
| **Property**  | using `@property` decorator              | Object-level            | Controlled access | Object            |
| **Annotated** | anywhere                                 | Same as respective type | -                 | Same              |
"""

"""Constructor:
Definition: A constructor is a special method used to initialize an object when it is created.
In Python, the constructor is the __init__() method.
It runs automatically when you create an object from a class.
Purpose: Assign initial values to instance attributes.
class ClassName:
    def __init__(self, parameters):
        # initialization code
        self.attribute = parameters
"""
class BankAccount:
    def __init__(self, owner, balance=0):   # Constructor
        self.owner = owner
        self.balance = balance
        print(f"Account created for {self.owner} with balance {self.balance}")
# Usage(here no need to call any method)
acc1 = BankAccount("ANIL", 1000)
acc2 = BankAccount("HARI", 500)
print(acc1.owner)
print("="*80)
"""
Destructor in Python:
Definition: A destructor is a special method used to clean up resources when an object is deleted or goes out of scope.
In Python, the destructor is the __del__() method.
It runs automatically when the object is destroyed by the garbage collector.
Purpose: Release resources (like closing files, database connections, etc.).
Syntax:class ClassName:
    def __del__(self):
        # cleanup code
        print("Destructor called")
"""
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "w")
        print(f"File {filename} opened.")

    def write_data(self, data):
        self.file.write(data)

    def __del__(self):  # Destructor
        self.file.close()
        print("File closed and resources released.")
# Usage
handler = FileHandler("test.txt")
handler.write_data("Hello, UPPARA!")
del handler  # Explicitly deleting object (calls destructor)
print("="*80)
"""
| Feature      | Constructor          | Destructor           |
| ------------ | -------------------- | -------------------- |
| Method name  | `__init__()`         | `__del__()`          |
| Called when  | Object created       | Object destroyed     |
| Main purpose | Initialize variables | Free/clean resources |
| Arguments    | Can have             | Cannot have          |
| Automatic?   | Yes                  | Yes (GC-based)       |
"""
#===========================================================================================
"""Inheritance in Python:
Inheritance allows one class (child/subclass) to acquire the properties and methods of another class (parent/superclass).
It helps in:
1.Code reusability
2.Removing duplication
3.Extending functionality
4.Maintaining clean structure
Types of Inheritance in Python
=================================
1️⃣ Single Inheritance
2️⃣ Multilevel Inheritance
3️⃣ Multiple Inheritance
4️⃣ Hierarchical Inheritance
5️⃣ Hybrid Inheritance
(Also: Super() concept)"""
#Single inheritance:A class inheritance from the one parent class.
"""Syntax:
class Parent:
    pass
class Child(Parent):
    pass
"""
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print(f"{self.brand} is driving")
class Car(Vehicle):  # Single inheritance
    def honk(self):
        print("Car honks!")
car = Car("Tesla")
car.drive()
car.honk()
print("="*80)
"""
2.Multiple Inheritance
=====================
Definition: A child class inherits from more than one parent class.
class A:
    pass
class B:
    pass
class C(A, B):
    pass
"""
class Employee:
    def __init__(self, name):
        self.name = name
    def work(self):
        print(f"{self.name} is working")
class Developer:
    def develop(self):
        print("Writing and reviewing code")

class Tester:
    def test(self):
        print("Testing the software for bugs")

class TechLead(Employee, Developer, Tester):   # Multiple inheritance
    def lead(self):
        print("Leading the team and assigning tasks")
lead = TechLead("Anil")
lead.work()     # from Employee
lead.develop()  # from Developer
lead.test()     # from Tester
lead.lead()     # from TechLead
print("="*80)
"""
In Python multiple inheritance, if parent classes have the same method name,
Python resolves conflicts using MRO (Method Resolution Order).
The method belonging to the parent class listed first in the child class definition is called first."""
class A:
    def show(self):
        print("Show from A")
class B:
    def show(self):
        print("Show from B")
class C:
    def show(self):
        print("Show from C")
class D(A,B,C):# multiple inheritance
    def show(self):
        print("Show from D")
        #B.show(self)#to call after Class D method call
        #super().show()#show from A calling the parent class
obj = D()
obj.show()
print("="*80)
"""output:            
Show from D
note:class D(A,B,C): ---->D--->A---->B--->C---->object
note:class D(C,B,A):----->D---->C---->B---->A--->object"""

"""
Multilevel inheritance :
=============================
Class A → Class B → Class C
Each class inherits from the class above it, forming a chain of inheritance.
or 
Multilevel inheritance allows one class to inherit from another derived class, forming a chain of inheritance.
It is useful for creating step-by-step specialization.
Example: GrandFather → Father → Son, or Employee → TeamLeader → Manager.
or 
Definition: A chain of inheritance where a class inherits from another child class, forming a hierarchy.
Each level adds new features, and the last child inherits everything from its ancestors.
Syntax:
class Grandparent:
    pass
class Parent(Grandparent):
    pass
class Child(Parent):
    pass
"""
class Employee:
    def Work(self):
        print("Employee doing work")
class TeamLeader(Employee):
    def Lead_team(self):
        print("Lead the team and assigning tasks")
class Manager(TeamLeader):
    def manage_team(self):
        print("Manage the team and assigning tasks")
task=Manager()
task.Work()#Employee doing work
task.Lead_team()#Lead the team and assigning tasks
task.manage_team()#Manage the team and assigning tasks
print("="*80)
"""
Hierarchical Inheritance:
===========================
What: One parent, multiple children.
When to use: Several specialized classes share a common base.
Definition: When multiple child classes inherit from the same parent class.
Each child gets the parent’s properties and methods, but can also define its own.
Useful when you have a common base class and multiple specialized subclasses
Syntax:
class Parent:
    # common features
    pass
class Child1(Parent):
    # specialized features
    pass
class Child2(Parent):
    # specialized features
    pass
"""
#Ex:
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def show_balance(self):
        print(f"{self.owner} have current balance is {self.balance}")
class SavingAccount(BankAccount):
    def add_interest(self):
        self.balance*=1.5
        print(f"Interest added now current balance is {self.balance}")
class CurrentAccount(BankAccount):
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"the withdraw amount is {amount} after current balance is {self.balance}")
        else:
            print(f"the insufficient balance.so check current balance is {self.balance}")
x=SavingAccount("Anil",50000)
y=CurrentAccount("Hari",10000)
x.show_balance()#Anil have current balance is 50000
x.add_interest()#Interest added now current balance is 75000.0
y.show_balance()#Hari have current balance is 10000
y.withdraw(5000)#the withdraw amount is 5000 after current balance is 5000
print("="*80)
"""
Rules:
When you create a child class object, it inherits all methods and attributes from its parent class.
But it does not inherit methods from sibling classes (other child classes of the same parent).
Each child has access to the parent’s methods, plus its own, but not the other children’s."""

"""
Definition: 
Hybrid inheritance is a combination of two or more types of inheritance (like single, multiple, multilevel, or hierarchical).
It often creates complex relationships, and Python resolves them using Method Resolution Order (MRO).
Syntax:
class A:
    pass
class B(A):   # Single inheritance
    pass
class C(A):   # Hierarchical inheritance
    pass
class D(B, C):   # Multiple inheritance (Hybrid)
    pass
"""
# Base class
class Bank:
    def __init__(self, name):
        self.name = name
    def bank_info(self):
        print(f"Welcome to {self.name} Bank")
# Single Inheritance
class Account(Bank):
    def __init__(self, name, owner, balance=0):
        super().__init__(name)#it calls the Bank constructor
        self.owner = owner
        self.balance = balance
    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")
# Hierarchical Inheritance
class SavingsAccount(Account):
    def add_interest(self):
        self.balance *= 1.05
        print(f"Interest added! New balance: {self.balance}")
class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}, Remaining balance: {self.balance}")
        else:
            print("Insufficient funds!")
# Hybrid Inheritance (Multiple + Hierarchical)
class PremiumAccount(SavingsAccount, CurrentAccount):
    def premium_features(self):
        print("Premium account offers free international transactions!")
# Usage
premium = PremiumAccount("TechBank", "UPPARA", 5000)
premium.bank_info()  # From Bank
premium.show_balance()  # From Account
premium.add_interest()  # From SavingsAccount
premium.withdraw(1000)  # From CurrentAccount
premium.premium_features()  # From PremiumAccount
#==============================================================================
"""Encapsulation:
Definition: Encapsulation is the concept of wrapping data (variables) and methods (functions) into a single unit (class).
It also involves restricting direct access to some attributes/methods to protect data.
In Python, encapsulation is achieved using access modifiers:
=============================================================
Public (self.var) → accessible everywhere.
Protected (self._var) → accessible within class and subclasses (convention).
Private (self.__var) → accessible only within the class (name mangling).
✔ Protect data
✔ Restrict direct access
✔ Provide controlled access using methods (getter, setter)
✔ Hide implementation details
Syntax:
class ClassName:
    def __init__(self):
        self.__private_var = value      # private variable
        self._protected_var = value     # protected variable
    def get_value(self):                # getter
        return self.__private_var
    def set_value(self, val):           # setter
        if val > 0:
            self.__private_var = val
        else:
            print("Invalid value")
✔ Getter = "Tell me the current value."
✔ Setter = "Update the value, but only if it is valid."
"""
print("="*80)
#Ex:
class BankAccount:
    # Public attribute (accessible everywhere)
    bank_name = "TechBank"

    def __init__(self, owner, balance=0):
        self.owner = owner  # Public instance variable
        self._account_type = "Savings"  # Protected instance variable
        self.__balance = balance  # Private instance variable
    # Public method
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")
    # Protected method (by convention, used inside class or subclasses)
    def _change_account_type(self, new_type):
        self._account_type = new_type
        print(f"Account type changed to {self._account_type}")
    # Private method (accessible only inside the class)
    def __show_balance(self):
        print(f"Balance: {self.__balance}")
    # Public method to safely access private data
    def get_balance(self):
        return self.__balance
    # Public method that internally calls private method
    def show_balance_secure(self):
        self.__show_balance()
# Usage
acc = BankAccount("UPPARA", 1000)

# Public access
print(acc.bank_name)  # ✅ Public class variable
print(acc.owner)  # ✅ Public instance variable
acc.deposit(500)  # ✅ Public method
# Protected access
print(acc._account_type)  # ⚠️ Accessible, but meant for internal/subclass use
acc._change_account_type("Current")  # ⚠️ Works, but not recommended outside class
# Private access
#print(acc.__balance)      # ❌ Error: private variable not directly accessible
# acc.__show_balance()      # ❌ Error: private method not directly accessible
# Safe access to private data
print(acc.get_balance())  # ✅ Access private variable via public method
acc.show_balance_secure()  # ✅ Calls private method internally

"""Explanation:
Public (self.owner, bank_name, deposit)
Accessible everywhere.
Protected (self._account_type, _change_account_type)
Accessible in class and subclasses. By convention, not meant for outside use.
Private (self.__balance, __show_balance)
Hidden from outside. Can only be accessed inside the class.
Accessed safely via public methods (get_balance, show_balance_secure)."""
"""| Concept                | Example               | Explanation                                   |
| ---------------------- | --------------------- | --------------------------------------------- |
| **Public variable**    | `self.name`           | Accessible anywhere                           |
| **Protected variable** | `self._balance`       | Accessible but should not be modified outside |
| **Private variable**   | `self.__pin`          | Hidden from outside (name-mangled)            |
| **Public method**      | `show_details()`      | Callable by anyone                            |
| **Protected method**   | `_show_balance()`     | Use inside class/subclass                     |
| **Private method**     | `__verify_pin()`      | Accessible only inside class                  |
| **Getter**             | `@property` → `pin()` | Safe read                                     |
| **Setter**             | `@pin.setter`         | Validation before updating                    |
| **Encapsulation**      | access via methods    | Hides internal details                        |
"""
print("="*80)
#================================================================
# Encapsulation encourages controlled access. While Python allows bypassing with name mangling,
# the best practice is to use getter/setter methods or @property decorators.
# Ways to Access Private Variables/Methods in Python
# 1. Using Public Methods (Getter/Setter)
# The recommended way: expose controlled access through methods.
class Student:
    def __init__(self, name):
        self.__name = name
    def get_name(self):   # getter
        return self.__name
    def set_name(self, name):   # setter
        self.__name = name
s = Student("UPPARA")
print(s.get_name())   # UPPARA
s.set_name("Anil")
print(s.get_name())   # ANil
# 2. Name Mangling (_ClassName__variable)
# Python internally renames private variables with _ClassName__variable.
# You can access them directly (not recommended, but possible).
class Student:
    def __init__(self, name):
        self.__name = name
s = Student("UPPARA")
print(s._Student__name)   # Access via name mangling
# 3.Using property() Decorator
# Provides a Pythonic way to define getters and setters.
class Student:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):   # getter
        return self.__name
    @name.setter
    def name(self, value):   # setter
        self.__name = value
s = Student("UPPARA")
print(s.name)   # UPPARA
s.name = "ANil"
print(s.name)   # Ravi
# 4. Accessing Private Methods
# Use a public method to call the private one.
# Or use name mangling.
class Student:
    def __init__(self, name):
        self.__name = name
    def __display(self):   # private method
        print("Name:", self.__name)
    def show(self):   # public method calling private
        self.__display()
s = Student("UPPARA")
s.show()              # Safe way
s._Student__display() # Direct access via name mangling

print("="*80)
"""
Polymorphism
============
Definition: Polymorphism allows the same method or function name to perform different tasks depending on the object or data type.
Python supports both compile-time polymorphism (via method overloading,
 though Python handles it differently than Java/C++) and runtime polymorphism (via method overriding).
Types of Polymorphism in Python:
=================================================
Method Overloading
===================
In languages like Java, you can define multiple methods with the same name but different parameters.
Python doesn’t support true overloading; instead, you can use default arguments or *args to simulate it.
Method Overriding
==================
A child class provides a specific implementation of a method already defined in its parent class.
This is the most common form of polymorphism in Python.
Operator Overloading
======================
Python allows operators like +, *, etc., to behave differently depending on the operands.
Example: 2 + 3 adds numbers, "Hello" + "World" concatenates strings
Duck Typing
Method Overriding
Operator Overloading
Method Overloading (not fully supported, but can be done in Python way)"""
# Methods in Polymorphism
#==================================================
# 1. Method Overloading (Compile-time Polymorphism)
# Definition: Multiple methods with the same name but different parameters.
# Note: Python doesn’t support true method overloading like Java/C++; instead, we simulate it using default arguments or *args.
# Syntax:
# python
# class Math:
#     def add(self, a=0, b=0, c=0):
#         return a + b + c
#way1:Using Default Arguments
class Calculator:
    def add(self,a=0,b=0,c=0):
        return a+b+c
cal=Calculator()
print(cal.add(10,20,30))#60    Same method add(), different number of arguments.
print(cal.add(10,20))#30
#way2:Using Variable-Length Arguments (*args)
class Calculator2:
    def add(self,*args):
        return sum(args)
cal=Calculator2()
print(cal.add(10,30))#40
#Way3:Using Type Checking
class Printer:
    def print_data(self, data):
        if isinstance(data, int):
            print("Printing number:", data)
        elif isinstance(data, str):
            print("Printing string:", data)
        else:
            print("Unsupported type")

p = Printer()
p.print_data(100)       # Printing number: 100
p.print_data("Hello")   # Printing string: Hello
#example
class Discount:
    def apply(self,price,discount=0,coupon=None):
        if coupon:
            print(f"applying coupon: {coupon}")
            return price*0.9
        else:
            return price-discount
d=Discount()
print(d.apply(10000))#10000
print(d.apply(1000,coupon="New"))
print("="*80)
#2Method Overriding (Runtime Polymorphism)
#=========================================
#Definition: A child class redefines a method from its parent class.
#Decision: Which method runs is decided at runtime based on the object type.
# class Parent:
#     def show(self):
#         print("Parent method")
#
# class Child(Parent):
#     def show(self):
#         print("Child method")
#Example:
class Transaction:
    def process(self):
        print("Processing generic transaction")

class CreditTransaction(Transaction):
    def process(self):
        print("Adding money to account")

class DebitTransaction(Transaction):
    def process(self):
        print("Deducting money from account")
txn1 = CreditTransaction()
txn2 = DebitTransaction()
txn1.process()  # Adding money to account
txn2.process()  # Deducting money from account
print("="*80)
# 3. Operator Overloading
#==========================
# Definition: Redefining how operators (+, -, *, etc.) behave for user-defined objects.
# Python Special Methods: __add__, __sub__, __mul__, etc.
# Syntax:
# class ClassName:
#     def __add__(self, other):
#         # custom logic
class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages
book1 = Book(100)
book2 = Book(200)
print(book1 + book2)  # 300
print("="*80)
# 4. Duck Typing (Python-specific Polymorphism)
#================================================
# Definition: If an object implements the required method, it can be used, regardless of its actual class.
#
# Phrase: “If it looks like a duck and quacks like a duck, it’s a duck.”
# def func(obj):
#     obj.method()
class CreditCard:
    def pay(self):
        print("Paid using Credit Card")
class UPI:
    def pay(self):
        print("Paid using UPI")
def make_payment(payment_method):
    payment_method.pay()
make_payment(CreditCard())  # Paid using Credit Card
make_payment(UPI())         # Paid using UPI

#Ex:2
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()
make_sound(Dog())
make_sound(Cat())

print("="*80)
# The function doesn’t care if it’s Dog or Cat
# ➡ Only checks if sound() exists
# ➡ This is duck typing polymorphism
"""| Type of Polymorphism     | Meaning                               | Simple Example               |
| ------------------------ | ------------------------------------- | ---------------------------- |
| **Duck Typing**          | Same method name in unrelated classes | Dog & Cat have sound()       |
| **Method Overriding**    | Child class changes parent method     | Father → Son work()          |
| **Operator Overloading** | Same operator acts differently        | 10+20, "a"+"b"               |
| **Method Overloading**   | Same method, diff arguments           | add(a), add(a,b), add(a,b,c) |
"""
#============================================================================================
# Definition: Data Abstraction is the process of hiding implementation details and showing only the essential features to the user.
# It focuses on what an object does, not how it does it.
# In Python, abstraction is mainly achieved using Abstract Base Classes (ABC) and the abc module

"""Why Abstraction?
Provides security by hiding sensitive implementation details.
Makes code modular and easier to maintain.
Encourages reusability and flexibility.
Helps in designing blueprints for classes.
How to Implement Abstraction in Python
===========================================
Python uses the abc module (Abstract Base Class) to implement abstraction
Syntax:
from abc import ABC, abstractmethod

class ClassName(ABC):   # Inherit from ABC
    @abstractmethod
    def method_name(self):
        pass
ABC: Base class for defining abstract classes.
@abstractmethod: Decorator to declare a method as abstract (must be implemented in child classes).
"""
#ex1
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        print(f"Deposited {amount} into Savings Account")
    def withdraw(self, amount):
        print(f"Withdrew {amount} from Savings Account")
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        print(f"Deposited {amount} into Current Account")
    def withdraw(self, amount):
        print(f"Withdrew {amount} from Current Account")
# Usage
s = SavingsAccount()
s.deposit(1000)
s.withdraw(500)
c = CurrentAccount()
c.deposit(2000)
c.withdraw(1000)
#ex2
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")
class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")
# Usage
p1 = CreditCard()
p1.pay(500)

p2 = UPI()
p2.pay(300)


"""
Additional OOP Concepts in Python
1. Association
Definition: A relationship between two classes where both can exist independently.

Example: A Teacher teaches a Student.

python
class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} is teaching {student.name}")

class Student:
    def __init__(self, name):
        self.name = name

t = Teacher("Ravi")
s = Student("UPPARA")
t.teach(s)   # Ravi is teaching UPPARA
2. Aggregation
Definition: A "whole-part" relationship, but the part can exist independently.

Example: A Library has Books. Even if the library is closed, books still exist.

python
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books):
        self.books = books   # aggregation

    def show_books(self):
        for book in self.books:
            print("Book:", book.title)

b1 = Book("Python Basics")
b2 = Book("OOP Concepts")
lib = Library([b1, b2])
lib.show_books()
3. Composition
Definition: Stronger form of aggregation. The part cannot exist without the whole.

Example: A Car has an Engine. If the car is destroyed, the engine ceases to exist.

python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started")

class Car:
    def __init__(self, horsepower):
        self.engine = Engine(horsepower)   # composition

    def drive(self):
        self.engine.start()
        print("Car is driving")

c = Car(120)
c.drive()
4. Constructor & Destructor
Constructor (__init__): Initializes object state.

Destructor (__del__): Cleans up resources when object is deleted.

python
class Demo:
    def __init__(self):
        print("Constructor called: Object created")

    def __del__(self):
        print("Destructor called: Object destroyed")

d = Demo()
del d
5. Message Passing
Definition: Objects communicate by calling each other’s methods.

Example: A Remote sends a message to a TV.

python
class TV:
    def turn_on(self):
        print("TV is ON")

class Remote:
    def __init__(self, tv):
        self.tv = tv

    def press_button(self):
        self.tv.turn_on()

tv = TV()
remote = Remote(tv)
remote.press_button()
6. Dynamic Binding (Late Binding)
Definition: Method resolution happens at runtime.

Example: Calling draw() on a Shape object that could be a Circle or Rectangle.

python
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

shapes = [Circle(), Rectangle()]
for s in shapes:
    s.draw()   # Decided at runtime
7. Interfaces (via Abstract Base Classes)
Python doesn’t have interfaces directly, but we use abc module.

python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

p = CreditCard()
p.pay(500)
📊 Summary
Concept	Python Implementation	Example
Association	Independent classes interacting	Teacher ↔ Student
Aggregation	Whole-part, part independent	Library → Books
Composition	Whole-part, part dependent	Car → Engine
Constructor/Destructor	__init__, __del__	Demo class
Message Passing	Objects calling methods	Remote → TV
Dynamic Binding	Runtime method resolution	Shape → Circle/Rectangle
Interfaces	Abstract Base Classes	Payment system
✅ Key Insight: These concepts extend the OOP pillars and are crucial for designing scalable systems in Python."""



