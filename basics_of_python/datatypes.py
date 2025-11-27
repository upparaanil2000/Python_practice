#to allocate the sufficient amount of memory space for input of the program.
#=======================fundamental data types:To store a single value======================================
#int-->it is predefined,it can store the integers,whole numbers
#and it is stored the number system data
#types
#1decimal number system(by default):
digit=9
print(digit,type(digit))#9 <class 'int'>
#2.binary==>base 2 literals is called as binary(bust be preceded with 0b or 0B)
a=0b101
print(a)#5--->1*4+0+1=5
#b=01234
#print(b)#SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
b=0B100
print(b)#4
#2.Octal==>base 8 literals are called octal number system.==>0o or 0O(0 to 7)
a=0o017
print(a)
b=0O312
print(b)
#hexadecimal ===>base 16 literals called as hexa decimal number system
a=0xF10
print(a)
#convrsions
binary=bin(10)
print(binary)
binary=bin(0o756)
print(binary)
binary=bin(0x898)
print(binary)
binary=bin(0o76)
print(binary)
#=======================
octal=oct(10)
print(octal)
octal=oct(0o77)
print(octal)
octal=oct(0xFA7)
print(octal)
octal=oct(10101)
print(octal)
#============================
hexadecimal=hex(101)
print(hexadecimal)
hexadecimal=hex(0o77)
print(hexadecimal)
hexadecimal=hex(120)
print(hexadecimal)
#===================
#2.float:store the real constant values(numbers with decimals)
a=1.7678877888789899788#take numbers after decimal part 14 digits only
print(a)#1.76788778887899
print(type(a))
#==============================
#3.bool--?To store the true and false values(or 1 or 0)
a=True
print(type(a))
#===complex data type-->to store the imaginary data/complex numbers  ===>a+
a=6+10j
print(a.imag)
print(a.real)
# b=0b1010+0o123j
# print(b)#SyntaxError: invalid octal literal:because of imag part compulsory is decimal part.
b=0b10101+120j
print(b)#(21+120j)
print(type(b),b.real)#<class 'complex'> 21.0

#=========================Sequence category data type================
#to store sequence of values
#=======str==it is a predefined class to treated as sequence category-->it store string/text/alphanumeric data
z='anil'
print(z,type(z))
x="""hello
  boss this is new world"""
print(x)
#============bytes========
""" to store "numerical positiveInteger values range from 0 to 255
there is not symbolic notation to organize the data.but it converts bytes data type by using bytes()
note:it is immutable"""
# a=bytes([1,2,3,156,3])
# print(a,type(a))#b'\x01\x02\x03\x9c\x03' <class 'bytes'>
#b = bytes([256, 66, 67])#ValueError: bytes must be in range(0, 256)
b=bytes([65,66,67])
print(b)           # b'ABC' here 65 ,66,67 are the A,B,C values in ASCII
print(b[0])        # 65
#
#====bytearray---->it is mutable it allows to change the same address

ba=bytearray([1,3,4,66])
print(ba)
ba[0]=66
ba[1]=65
print(ba)#bytearray(b'BA\x04B')
#===============Range()-->to store the numerical  integer values with equal intervals.It is immutable
#Ex:1
a=range(10)
print(a)#range(0, 10)
#ex:2'
a=range(20,50)
# a[2]=100
# print(a)#TypeError: 'range' object does not support item assignment
print(a[2])#22
#here one doubt there, i want to print the range b/w 20 to 50 without using for loop and step parameter
#M1:
x=range(20,50)
print(list(x),type(x))#[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]<class 'range'>
#m2
print(tuple(x))#(20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49)
#m3==>Method 3: Use unpacking operator *
print(*range(20,50))#20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
#ex3:
a=range(20,50,2)
for i in a:
    print(i,end=" ")#20 22 24 26 28 30 32 34 36 38 40 42 44 46 48
print()
#List category Data type:
""" List: to store multiple values  either of same type or different types of or 
both types with unique and duplicates in a single object.
symbol-->[] and syntax===>varname=[value1,value2,value3,etc..]
                        varname=[]#empty list
                        varname=list()#it covert to list data type
1.It maintain Insertion  Order and perform both slicing and index operations
2. It is mutable data type
note:even spaces also consider as value"""

#methods
#1.append()-->adding end of the list. syntax-->list object.append(value)
list_obj=[10,2,-19,20,"anil",10+5j,89.123]
print(list_obj,type(list_obj))#[10, 2, -19, 20, 'anil', (10+5j), 89.123] <class 'list'>
list_obj.append("new_Append_element")
#list_obj.append([10,20,30]) [10, 2, -19, 20, 'anil', (10+5j), 89.123, 'new_Append_element', [10, 20, 30]]
print(list_obj)#[10, 2, -19, 20, 'anil', (10+5j), 89.123, 'new_Append_element'
#2.insert()-->adding the element for specific position/index  syntax--->listobj.insert(indexvalue,value)
list_obj.insert(1," hey iam a insert element at index value 1")
print(list_obj)#[10, ' hey iam a insert element at index value 1', 2, -19, 20, 'anil', (10+5j), 89.123, 'new_Append_element']
#3.remove()-->It is content based removal,removing first occurrence of specific element.if element is not found it get an error
#syntax--->list_obj.remove(value)
print(list_obj[1])
list_obj.remove(" hey iam a insert element at index value 1")
print(list_obj)#[10, 2, -19, 20, 'anil', (10+5j), 89.123, 'new_Append_element']
#pop()--->to delete the last element of the list. syntax:list_obj.pop()
list_obj.pop()
print(list_obj)#[10, 2, -19, 20, 'anil', (10+5j), 89.123]
#pop(index)-->to delete the index based removal.syntax-->list_obj.pop(index)
list_obj.pop(5)
print(list_obj)#[10, 2, -19, 20, 'anil', 89.123]
#count():count the no.of elements occurrence of specified element. syntax-->listobj.count(value)
x=[10,20,10,10,20,10]
print(x.count(10))#4
#extend()----->to add a list of  values in the list.
list_obj.extend([10,20,30,40])
print(list_obj)#[10, 2, -19, 20, 'anil', 89.123, 10, 20, 30, 40]
#index()--->find the index of the first occurrence of the specific element.
print(list_obj.index("anil"))#4
print(list_obj.index(20))#3
#copy()--->copying the content of the one list object into another list object(shallow copy):not effect on another object when you're changing anything
list_obj2=list_obj.copy()
print(list_obj2)#[10, 2, -19, 20, 'anil', 89.123, 10, 20, 30, 40]
print(list_obj2==list_obj)#True
list_obj2.append("hi iam new element")
print(list_obj2,"  ",list_obj)#[10, 2, -19, 20, 'anil', 89.123, 10, 20, 30, 40, 'hi iam new element']    [10, 2, -19, 20, 'anil', 89.123, 10, 20, 30, 40]
#clear()--->to delete the all elements in the list
list_obj2.clear()
print(list_obj2)#[]
#del()--->object based indexing and slicing and we can call also remove entair object.
del(list_obj[1:3])
print(list_obj)#[10, 20, 'anil', 89.123, 10, 20, 30, 40]
#to delete complete
del list_obj
#print(list_obj)#NameError: name 'list_obj' is not defined.
#reverse method()-->reverse order of the list.
list_obj=[1,2,3,[10,20,30],9,10,[1,[38,67,90]]]
#print(list_obj.reverse())#it shows none
list_obj.reverse()
print(list_obj)#[[1, [38, 67, 90]], 10, 9, [10, 20, 30], 3, 2, 1]
#sort()--->sort the list.note it contains only same dat types
x=[9,1,8,0,-2,10]
x.sort()
print(x)#[-2, 0, 1, 8, 9, 10]

#neasted list
list_obj3=[1,2,3,[10,20,30],9,10,[1,[38,67,90]]]
#to access the 38 number
print(list_obj3[6][1][0])#38
#to access 30
print(list_obj3[3][2])#30

""" tuples:To Store the multiple values either same type 
(or) different types  or both types with unique  and duplicates in Single Object.
syntax===>varname=(value1,value2,value3,etc..), varname=(), varname=tuple()
1.To perform the insertion order
2.Indexing and Slicing Operation
3.It is Immutable"""

#for in built functions
tuple_obj=(1,1,2,2,2,3,"anil","98.20",True,6+9j)
print(tuple_obj,type(tuple_obj)) #(1, 1, 2, 2, 2, 3, 'anil', '98.20', True, (6+9j)) <class 'tuple'>
#index()--->to find the specific index value based on value.It gives first occurrence of the value
print(tuple_obj.index(True))#0 -->because True means 1.so that it gives index value 0.if not in 1 it shows the index value is 6
#cont()--->to count the specific element.
print(tuple_obj.count(2))#3


"""Set Category  datatypes:To store multiple values either of same type or different types or both types 
with unique values in single object.
1.duplicated is not allowed.
2.Set is both mutable and immutable.
3.frozenset is mutable
Syntax--> {},varname={1,2,3,4,6,7,8}, varname=set()
4.Never maintain insertion order.
5.We cant perform indexing and slicing.
*** is mutable---->used to  add() function so that is mutable
***immutable---->set object doesn't support assignment operator
"""
#================methods===========
#add()--> adding the elements to the set object.
set_obj={1,3,1,"anil",98.20,True,8+5j,3}
#print(set_obj,type(set_obj))#{1, 98.2, 3, 'anil', (8+5j)} <class 'set'>(note if give duplicate but take only once)
set_obj.add("new_element")
print(set_obj)#{1, 98.2, 3, (8+5j), 'new_element', 'anil'}
#copy()--->To copy the one set object to another set object
set_obj1=set_obj.copy()
print(set_obj1)#{1, 98.2, 3, 'new_element', (8+5j), 'anil'}
#remove()--->to remove the element of the set object
set_obj1.remove("new_element")
print(set_obj1)#{1, 98.2, 3, 'anil', (8+5j)}
#discard()--->remove the specific element of the set object.
#print(set_obj1.discard(98.2))#none
set_obj1.discard(98.2)
print(set_obj1)#{1, 3, 'anil', (8+5j)}
set_obj1.discard(98.2)
print(set_obj1)#it shows empty if in case element is not found.but in the remove function shows an error
#pop()--->to remove the default any element
set_obj1.pop()
print(set_obj1)#{'anil', 3, (8+5j)}
#clear()-->to remove all the elements in set object
set_obj1.clear()
print(set_obj1)#set()
#====mathematical methods
"""1.isdisjoint():it shows---> True:no common elements between two set objects.
                            False:Other wise
                            syntax--->setobj1.isdisjoint(setobj2)"""
set_obj1={1,2,3,4,6,7,0,2}
set_obj2={10,20,30,10,11}
set_obj3={9,8,1,3,1,2,4,10,20,30,10,11,6,7,0}
print(set_obj1.isdisjoint(set_obj2))#True
print(set_obj1.isdisjoint(set_obj3))#false
""" issuperset():True:set object1 contains all the elements of set object2"""
print(set_obj3.issuperset(set_obj1))#True
print(set_obj2.issuperset(set_obj1))#False
"""issubset():true:all the elements of set object1 present in set object2"""
print(set_obj1.issubset(set_obj3))#True
""" Union() or |-->all the elements of set1 and set2 collect unique elements and store the set3"""
set_obj4=set_obj1.union(set_obj2)
set_obj5=set_obj1|set_obj3
print(set_obj4,set_obj5)#{0, 1, 2, 3, 4, 6, 7, 10, 11, 20, 30},{0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 20, 30}
""" intersection() or & :take a common elements between set1 and set2 and store set3"""
set_obj5=set_obj1.intersection(set_obj2)
print(set_obj5)#it shows set() because of no common elements have
#set_obj5=set_obj1.intersection(set_obj3)
set_obj5=set_obj1&set_obj3
print(set_obj5)#{0, 1, 2, 3, 4, 6, 7}

""" update() or |=   -->To update the current set,by adding items from another set(or any iterables)"""
#set_obj1.update({10,20,30})
set_obj1|={10,20,30}
print(set_obj1) #{0, 1, 2, 3, 4, 6, 7, 10, 20, 30}
""" intersection_update() or &=  -->Remove the items in the set that are not present to the another set or specified set"""
#set_obj1.intersection_update(set_obj2)
#print(set_obj1,set_obj2)#{0, 1, 2, 3, 4, 6, 7, 10, 20, 30} {10, 11, 20, 30}
set_obj1&=set_obj2
print(set_obj1)#{10,20,30}
""""difference or -  --> to remove common elements between two sets and remaining elements takes from set1 to stored in set3"""
set_obj1={1,2,3,4,6,7,0,2}
#set_obj1.difference(set_obj2)
set_obj1-set_obj2
print(set_obj1)#{0, 1, 2, 3, 4, 6, 7}
""" symmetric_difference  or ^  --->
To remove the  common elements from set1 and set2 and remaining elements both set1 and set2 elements stored in set3"""
set_obj1={1,2,3,4,6,7,0,2,10,20}
#print(set_obj2)#{10, 11, 20, 30}
set3=set_obj1.symmetric_difference(set_obj2)
print(set3)#{0, 1, 2, 3, 4, 6, 7, 11, 30}
""" Frozen set: we have any symbolic notation for storing the elements in frozenset
but we can convert any tuple or list or set type elements to frozen set by using frozenset()
syntax:Frozenset_obj=frozenset({value1,value2,value3,etc})
It is immutable
| Method                        | Supported in frozenset | Meaning                        |
| ----------------------------- | ---------------------- | ------------------------------ |
| add()                         | ❌ No                   | Not allowed (immutable)        |
| remove()                      | ❌ No                   | Cannot remove                  |
| discard()                     | ❌ No                   | Cannot remove                  |
| pop()                         | ❌ No                   | Cannot pop                     |
| clear()                       | ❌ No                   | Cannot clear                   |
| update()                      | ❌ No                   | Cannot modify                  |
| intersection_update()         | ❌ No                   | Cannot modify                  |
| difference_update()           | ❌ No                   | Cannot modify                  |
| symmetric_difference_update() | ❌ No                   | Cannot modify                  |
| union()                       | ✔ Yes                  | Read-only union                |
| intersection()                | ✔ Yes                  | Read-only intersection         |
| difference()                  | ✔ Yes                  | Read-only difference           |
| symmetric_difference()        | ✔ Yes                  | Read-only symmetric difference |
| issubset()                    | ✔ Yes                  | Check subset                   |
| issuperset()                  | ✔ Yes                  | Check superset                 |
| isdisjoint()                  | ✔ Yes                  | Check disjoint                 |
| copy()                        | ✔ Yes                  | Return same frozenset          |
"""


"""Dictionary data type:A dictionary is a collection of key–value pairs.
student = {
    "name": "Anil",
    "age": 22,
    "marks": 95
}    
Key points:
1.Keys are unique
2.Keys must be immutable (str, int, tuple…)
3.Values can be anything
Order is preserved (Python 3.7+)"""
#How to create a dictionary
d = {"a": 10, "b": 20, "c": 30} #or
#d = dict(a=10, b=20)#{'a': 10, 'b': 20}
print(d,type(d))#{'a': 10, 'b': 20, 'c': 30} <class 'dict'>
#Accesing the values
print(d["a"])      # 10
print(d.get("b"))#20
#to return keys and values
print(d.keys(),d.values()) #dict_keys(['a', 'b', 'c']) dict_values([10, 20, 30])
#to print the iteams:Returns (key, value) pairs.
print(d.items())#dict_items([('a', 10), ('b', 20), ('c', 30)])
#get(key, default):Safely access a value.
print(d.get("x", "Not found"))#if not there is shows not found
#update()-->Add or modify key–value pairs.
student = {
    "name": "Anil",
    "age": 22,
    "marks": 95
}
student.update({"age":25,"name":"surya"})
print(student)#{'name': 'surya', 'age': 25, 'marks': 95}
#pop():Removes the key and returns its value.
student.pop("marks")
print(student)#{'name': 'surya', 'age': 25}
#popitem():Removes last inserted key–value pair.
student.popitem()
print(student)#{'name': 'surya'}
"""setdefault(key, default)
If key exists → return value
If key does NOT exist → add key with default value."""
student.setdefault("city", "Hyderabad")
print(student)#{'name': 'surya', 'city': 'Hyderabad'}
#copy()
new_dict=student.copy()
print(new_dict)#{'name': 'surya', 'city': 'Hyderabad'}
#clear
new_dict.clear()
print(new_dict)#{}
#fromkeys:Create dictionary from keys with default value.
x = dict.fromkeys(["a", "b", "c"], 0)#
print(x)# {'a': 0, 'b': 0, 'c': 0}





