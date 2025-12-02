"""to perform the certain operation and provide reusability or
A function is a named block of code that you can call (invoke) to perform a task and optionally return a value.
 In Python, functions are first-class objects — you can assign them to variables,
  pass them, return them, attach attributes, etc.
  1.functon definition: it exists only once,we can have one or more function calls.
  2.function call:Every function calls,there must be existed function definition  otherwise will get name error.

  Start
 ↓
Function defined (def)
 ↓
Wait until someone calls it
 ↓
Function is called
 ↓
Parameters receive values
 ↓
Code inside function runs line-by-line
 ↓
return sends output back
 ↓
End


#======================================
Types of Functions in Python
1. Built-in Functions
These are pre-defined by Python and available for immediate use.
Examples: print(), len(), type(), sum()
print("Hello, World!")   # Built-in function
numbers = [1, 2, 3, 4]
print(len(numbers))      # Output: 4
print(sum(numbers))      # Output: 10

2. User-defined Functions
#Functions created by the programmer using the def keyword.
Useful for code reusability and modularity.
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))   # Output: Hello, Alice!
"""
#types of parameters and arguments in the function
"""Parameters vs. Arguments
Parameters → Variables defined inside the function signature (when you create the function).

Arguments → Actual values/data you pass into the function when calling it.
Ex:Think of parameters as placeholders and arguments as the real values that fill those placeholders."""
def example(name):#here name is parameter
    print(f"Hello,{name}")
example("Anil")#here anil is Arguments
#types
"""Python functions support several kinds of parameters:
1. Positional Parameters(The most common type).
Arguments are matched to parameters based on their position."""
def add(x,y):
    return x+y
print(add(1,2))#30
#print(add(10,20,40))TypeError: add() takes 2 positional arguments but 3 were given
"""
2.Default Parameters:You can assign default values to parameters.
If no argument is passed, the default value is used."""
def ex1(name="Anil"):#this is the default parameter no need to pass the arguments
    print(f"My name is {name}")#My name is Anil
ex1()
"""
3. Keyword Parameters:You can specify arguments by name when calling the function.
Order doesn’t matter when using keywords."""
def introduction(name,age):
    return f"my name is {name} and my age is {age}"
print(introduction(name="Anil",age=25))#my name is Anil and my age is 25
#print(introduction(name="Anil",age=25,phone=95456789))#TypeError: introduction() got an unexpected keyword argument 'phone'
#print(introduction(a="A",b=25))#TypeError: introduction() got an unexpected keyword argument 'a'
print(introduction(age=25,name="Anil"))#my name is Anil and my age is 25
"""
4.Variable-length Parameters:Sometimes you don’t know how many arguments will be passed.
Python provides two special symbols:
*args → for variable-length positional arguments
**kwargs → for variable-length keyword arguments"""
def show_numbers(*args):
    for num in args:
        print(num)
show_numbers(1,2,3,4,5,6,7,8,9,10,"anil",89.0,3+5j)#passing no.of values
def show_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is {value}")
show_info(name="Anil",age=25,city="Bangalore",phone=9542890892,salary=58999.89)
"""
5.Positional-only and Keyword-only Parameters (Python 3.8+)
You can enforce how arguments must be passed:
/ → parameters before this must be positional-only
* → parameters after this must be keyword-only"""
def func(a, b, /, c, *, d):
    print(a, b, c, d)

func(1, 2, 3, d=4)   # ✅ valid
#func(a=1, b=2, c=3, d=4) #→ ❌ error (a and b must be positional)TypeError: func() got some positional-only arguments passed as keyword arguments: 'a, b'
func(1,2,c=123,d=67)#here observed this after / we can use as keyword argument also.
#func(10,20,30,45)#TypeError: func() takes 3 positional arguments but 4 were given.(because of d is keyword arguments)
#####################################
"""
3.Recursive Functions:Functions that call themselves to solve problems step by step.
Commonly used in problems like factorial, Fibonacci, etc."""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(int(input("Enter the number:"))))#720
#here if enter the negative number it shows :RecursionError: maximum recursion depth exceeded
def febonnaci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        print(a,end=" ")
febonnaci(int(input("Enter the number:")))
print()
"""
4.Lambda Functions (Anonymous Functions)
Small, one-line functions defined using the lambda keyword.
Syntax: lambda parameters: expression
No statements: Only expressions (no assignments, loops, or return lines).
Scope: Captures variables from the enclosing scope (like closures).

When to use: Tiny, throwaway functions passed to other functions.
When to avoid: Complex logic—prefer def with a named function for readability and debugging.
Often used for short operations or with functions like map(), filter(), reduce()."""
#Ex:1
squres=lambda x:x*x
print(squres(4))
#Ex:2(with multiple parameters
add=lambda a,b:a+b
print(add(10,20))
#ex:3:Lambda used immediately (without naming)
print((lambda s: s.strip().upper())("hello"))  # HELLO
#clouser behviour
def multplication(k):
    return lambda x:x*x
#print(multplication(3))#it give the object address
#double=multplication()#TypeError: multplication() missing 1 required positional argument: 'k'
double=multplication(5)
print(double(10))
"""Map:Map applies a function to each item of an iterable, returning a new iterator of results.
"""
#x1:
numbers=[1,2,3,4]
double=map(lambda x:x*x,numbers)
print(list(double))#it used list because numbers are passing through the list
"""Common patterns
1.Transform types: Convert strings to ints, format data, etc."""
data=["1","2","3","4"]
print(data)#['1', '2', '3', '4']
intdata=list(map(int,data))
print(intdata)#[1,2,3,4]
#2.Map with multiple iterables: Applies the function pairwise.
a=[1,2,3]
b=[10,20,30]
answer=list(map(lambda x,y:x+y,a,b))
print(answer)#[11, 22, 33]
#3.Alternatives and guidance
#List comprehensions are often clearer:
nums=[1,2,4,6,8]
print([x ** 2 for x in nums]) #[1, 4, 16, 36, 64]
#Use map when: You already have a function (like str, int) or you need lazy iteration in pipelines.
"""2.Filter:Filter selects items from an iterable for which a predicate (boolean function) returns True."""
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
filter_values=filter(lambda x:x%2==0,a)
print(list(filter_values))#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""Truthiness and None
Any truthy/falsy return works: Non-zero numbers, non-empty strings are truthy; 
zero, empty strings, None are falsy."""
names=["anil","surya"," ","Rajesh"," "]
cleaned=list(filter(lambda s:s and s.strip(),names))
print(cleaned)#['anil', 'surya', 'Rajesh']
"""Alternatives and guidance:Comprehensions often read better:"""
nums=[1,2,3,4,5]
a=[x for x in nums if x%2==0]
print(a)#[2,4]
#Use filter when: You already have a predicate function or want lazy evaluation.
"""Reduce:
Reduce aggregates an iterable into a single value by repeatedly applying a binary function.
 It lives in functools.
How reduce works:
Function signature: reduce(func, iterable, initializer=None)
Process: Start with initializer (if provided) or the first element; 
then apply func(accumulator, current) sequentially"""
from functools import reduce
a=[1,2,3,4,5]
reduce_value=reduce(lambda x,y:x*y,a,1)#here 1 means how many times like if put 2 instead of 1 it gives value 240(because of multiplication)
print(reduce_value)#120
#sum of numbers
sum=reduce(lambda acc,x:x+acc,a,0)
print(sum)#15
#find maxium value
maximum=reduce(lambda m,x:m if x<m else x,a,0)
print(maximum)#5
#concat string
a=["hello","anil"]
concat=reduce(lambda x,y:x+" "+y,a)#hello anil
print(concat)
"""Lambda: Anonymous, single-expression function.

Map: Transform items → iterator of results.

Filter: Keep items meeting a condition → iterator of items.

Reduce: Collapse items into a single value via accumulation."""
from functools import reduce

data = [" 10", "20 ", "  ", "30", "forty", "50"]
pipeline = map(lambda s: s.strip(), data)
numeric_only = filter(lambda s: s.isdigit(), pipeline)
print(list(numeric_only))#['10', '20', '30', '50']
to_ints = map(int, numeric_only)#it converts to the int type
total = reduce(lambda acc, x: acc + x, to_ints, 0)
print(total)  # 110
