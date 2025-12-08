"""
Exception handling in Python lets you manage runtime errors gracefully using try, except, else, finally, and raise.
It prevents program crashes and allows you to respond to unexpected situations like invalid input, missing files, or division by zero
Exception Handling in Python
🔹 What is an Exception?
Exception: An error that occurs during program execution (e.g., dividing by zero, accessing a missing file).
Difference between Errors and Exceptions: Errors are usually unrecoverable (like syntax errors), while exceptions can be caught and handled
🔹 Core Components
Topic			            Explanation						                     Real-Time Example
try block		            Code that may raise an exception is placed here.	try: result = 10/0
except block		        Handles the exception if it occurs.			        except ZeroDivisionError: print("Cannot divide by zero!")
multiple excepts	        Catch different exceptions separately.			    Handling ValueError vs FileNotFoundError.
else block		            Runs if no exception occurs.				        else: print("Division successful")
finally block		        Always executes (cleanup code).				        Closing a file connection.
raise keyword		        Manually trigger an exception.				        raise ValueError("Invalid age entered")
custom exceptions	        Define your own exception classes.			        class InsufficientFunds(Exception): pass
"""
# 1. try block
# Purpose: Wraps code that might raise an exception.
try:
    amount=int(input("enter the withdraw amount: "))
    balance=1000
    print("Remaining balance is :",balance-amount)
# 2.except block
# Purpose: Handles the exception gracefully
except ValueError:
    print("Invalid input enter valid a number:")
print("="*80)
# 3. multiple excepts
# Purpose: Handle different exceptions separately.
try:
    filename = input("Enter file name: ")
    f = open(filename, "r")
    data = f.read()
except FileNotFoundError:
    print("File not found. Please upload the correct file.")
except PermissionError:
    print("You don’t have permission to access this file.")
#Handles both missing file and permission issues differently.
# 4. else block
# Purpose: Runs only if no exception occurs.
try:
    amount = float(input("Enter payment amount: "))
except ValueError:
    print("Invalid amount entered.")
else:
    print("Payment of", amount, "processed successfully.")
# 5.finally block
# Purpose: Always executes (cleanup code).
try:
    print("Connecting to database...")
    # simulate error
    raise ConnectionError("Database not reachable")
except ConnectionError as e:
    print(e)
finally:
    print("Closing database connection.")
# 6. raise keyword
# Purpose: Manually trigger exceptions.
balance = 500
withdraw = 600
if withdraw > balance:
    raise ValueError("Insufficient funds for withdrawal!")

# 7. custom exceptions
# Purpose: Define domain-specific errors.
class InvalidGrade(Exception):
    pass

grade = "Z"

try:
    if grade not in ["A", "B", "C", "D", "F"]:
        raise InvalidGrade("Grade entered is not valid.")
except InvalidGrade as e:
    print(e)
