"""Operator is symbol .it is used to perform operation two are more operands
✅ 1. Arithmetic Operators

Used for mathematical operations.

Operator	Meaning
+	Addition
-	Subtraction
*	Multiplication
/	Division
%	Modulus (remainder)
//	Floor division
**	Exponent (power)
✅ 2. Assignment Operators

Used to assign values.

Operator	Meaning
=	Assign
+=	Add & assign
-=	Subtract & assign
*=	Multiply & assign
/=	Divide & assign
//=	Floor-div & assign
%=	Modulus & assign
**=	Power & assign
✅ 3. Comparison / Relational Operators

Used to compare two values.

Operator	Meaning
==	Equal to
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
✅ 4. Logical Operators

Used to combine conditions.

Operator	Meaning
and	True if both conditions true
or	True if any condition true
not	Reverse the result
✅ 5. Bitwise Operators

Used for binary-level operations.

Operator	Meaning
&	AND
`	`
^	XOR
~	NOT
<<	Left shift
>>	Right shift
✅ 6. Membership Operators

To check presence in a sequence.

Operator	Meaning
in	True if value present
not in	True if value not present
✅ 7. Identity Operators

To check object identity (memory address).

Operator	Meaning
is	True if both refer to same object
is not	True if not same object
✅ 8. Ternary (Conditional) Operator

Inline if condition.

a if condition else b

✅ 9. Walrus Operator (Python 3.8+)

Assigns value inside expressions.

if (n := len(data)) > 5:

✅ 10. Operator Overloading (using magic methods)

Used in classes to change operator behavior.

Examples:

__add__

__sub__

__eq__

__len__

(Not an operator itself, but important in Python latest versions.)"""
#Arithmetic operation
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a % b)   # 1
print(a // b)  # 3
print(a ** b)  # 1000
#Assignment operator
x = 5
x += 3   # x = x + 3 → 8
x -= 2   # x = x - 2 → 6
x *= 2   # 12
x /= 3   # 4.0
x //= 2  # 2
x **= 3  # 8
#Comparison operator or Relational operator
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True
#Logical operator
a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False

#Bitwise Operators:It is applicable only the Integer data(because they are varying precision

a = 5     # 0101
b = 3     # 0011

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10(#formula -->a<<b -->a*2 power of b)5<<1===>5*2power of 1=10
print(a >> 1)  # 2(given data/2 power of no.of bits) 5/2 power 1--->5//2--->2

#Membership operators
nums = [1, 2, 3, 4]

print(2 in nums)        # True
print(10 not in nums)   # True
#Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(id(a),id(b),id(c))#2067509655168 2067509655168 2067512131776
print(a is b)      # True (same memory)
print(a is c)      # False (different objects)

#Ternary Operator
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)   # Adult
#9. Walrus Operator (:=)
data = [1, 2, 3, 4]
if (n := len(data)) > 3:
    print("Length:", n)
#Operator Overloading
class Demo:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Demo(self.x + other.x)

d1 = Demo(5)
d2 = Demo(10)
print((d1 + d2).x)   # 15



