"""To perform certain operation either once or perform operations repeatedly for finite number of times until condition is false"""
#conditional or branching statements or selection statements
"""to perform the certain operation  only once depends on condition evaluations"""
#simple if statement
age = 20

if age >= 18:
    print("Adult")

#if else
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
#elif
num = 0

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
#Neasted if
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive Even Number")
#MATCH–CASE (Python 3.10+)
#Used when you want cleaner branching instead of many elif.
"""match value:
    case pattern1:
        statements
    case pattern2:
        statements
    case _:
        statements   # default
"""
n=int(input("please enter a number:"))
match n:
    case 1 | 3 | 5 | 7:
        print("Odd")
    case 2 | 4 | 6 | 8:
        print("Even")
value=input("please enter a value:")
match value:
    case int():
        print("Integer")
    case str():
        print("String")
    case list():
        print("List")

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
"""For loop:for loop is that to retrieve the data from ay iterable object
syntax: for varname in iterable_object:
            ---------
        else:others statements
note:for iterable objects for using for loop statement,otherwise use to whileloop
"""
#ex1:
for i in range(10):
    print(i)
#ex2:
names=["anil","surya","mahesh"]
for name in names:
    print(name)
#ex:3
for index, item in enumerate(["A", "B", "C"]):
    print(index, item)
#ex:4
names = ["Ravi", "Kiran"]
marks = [80, 90]

for n, m in zip(names, marks):
    print(n, m)

"""while loop:Repeating until a condition becomes False"""
x = 1
while x <= 5:
    print(x)
    x += 1
"""Loop Control Statements:
break — stops the loop completely"""
for i in range(10):
    if i == 5:
        break
    print(i)
#continue — skips current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
#pass — does nothing (placeholder)
if x > 10:
    pass   # we will implement later
"""for-else:else runs only if loop completes without break."""
for i in range(5):
    if i == 10:
        break
else:
    print("No break happened")   # prints
#while loop
x = 1
while x < 3:
    print(x)
    x += 1
else:
    print("Loop finished normally")

"""Innerloop or nested loop:An inner loop is a loop inside another loop.
✔ Inner loop runs COMPLETELY for every single outer loop iteration
✔ Inner loops increase time complexity (good for practice, careful in real apps)
✔ Used in:
patterns
matrices
multiplication tables
comparing items
searching in 2D data structures"""
for i in range(3):      # outer loop
    for j in range(2):  # inner loop
        print(i, j)
#========================================
for i in range(1, 4):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
#=========================================
for i in range(1, 5):        # outer loop → rows
    for j in range(i):       # inner loop → print i stars
        print("*", end="")
    print()                  # new line
"""Iteration details:
i = 1 → j = 0 → *
i = 2 → j = 0,1 → **
i = 3 → j = 0,1,2 → ***
i = 4 → j = 0,1,2,3 → ****"""

