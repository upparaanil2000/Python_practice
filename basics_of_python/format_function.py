#supplies the specified variables to the empty cruelly braces{}.
#ex:1
a=10
b=20
c=a+b
print("the sum is :{}".format(sum))
#note :if you don't have any format specifiers then those values converted into str and use %s
"""%d, %f, %s only change how the value is displayed, not the actual data type of c.
So type(c) always shows <class 'int'>."""
a=10
b=20
c=a+b
print("sum=%d"%c,type(c))#sum=30 <class 'int'>
print("sum=%0.2f"%c,type(c))#sum=30.000000 <class 'int'>#30.00
print("sum=%s"%c,type(c))#sum=30 <class 'int'>
print("sum of %f and %f=%f"%(a,b,c))
"""name = "Anil"
age = 22
print("My name is %s and age is %d" % (name, age))"""
name = "Anil"
age = 22
print("My name is {} and age is {}".format(name, age))
#new format
name = "Anil"
age = 25
print(f"My name is {name} and age is {age}")
print(f"Next year age = {age + 1}")

pi = 3.14159
print(f"Pi value = {pi:.2f}")#3.14


