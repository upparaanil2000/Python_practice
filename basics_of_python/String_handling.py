"""string:In Python, strings are sequences of characters enclosed in quotes,
and the language provides a rich set of built-in methods and operations to handle them efficiently.
 You can create, manipulate, search, format, and transform strings using simple syntax and powerful functions.
"""
#1.Basics of Strings
#Creation: Strings can be defined with single ('...') or double ("...") quotes
str1="anil"
str2='anil'
str3="""anil
            how are you?"""
print(str1,type(str1),str2,type(str2),str3,type(str3))
"""output:anil <class 'str'> anil <class 'str'> anil
            how are you? <class 'str'>"""
"""
Note:Multi-line Strings: Use triple quotes ('''...''' or """ """) for text spanning multiple lines.
Immutability: Strings in Python are immutable, meaning operations return new strings without altering the original"""
#====================Common String Operations=========================
#1.Concatenation: Combine strings with +.
a="anil"
b="surya"
print(a+b)#anilsurya
print(a+" "+b)#anil surya
print("hello" +" "+"surya")#hello surya
#2.Repetition: Repeat strings with *
print(a*3)#anilanilanil
print((a+" ")*3)#anil anil anil
#3.Indexing & Slicing: Access parts of a string.
str_obj="anil surya"
#indexing
print(str_obj[0])#a
print(str_obj[-3])#r
#slicing
print(str_obj[1:])#nil surya
print(str_obj[:2])#0,1,==?an
print(str_obj[:])#anil surya
print(str_obj[-2:])#-2,-1-->ya
print(str_obj[:-2])#anil sur
print(str_obj[2:-1])#il sury
print(str_obj[-2:3])#empty
print(str_obj[-3:-1])#ry
print(str_obj[1:5:2])#nl
print(str_obj[1:5:-1])#empty
print(str_obj[1::2])#nlsra
print(str_obj[::-1])#to reverse the string ===ayrus lina
print(str_obj[-8:8:2])#i u
#===================methods===========
#lower():Converts all characters to lowercase.
print("HELLO".lower())#hello
#upper():Convert all characters to uppercase.
print("hello anil".upper())#HELLO ANIL
#title() → Converts to title case (first letter of each word uppercase).
print("anil surya".title())#Anil Surya
#capitalize() → Capitalizes the first character.
print("anil surya".capitalize())#Anil surya (here title method first letter upper case after space of the letter also,but capitalize only first letter capitalize if after have space.
#swapcase() → Swaps case of each character.
print("AnIl SuRYA".swapcase())#aNiL sUrya
#casefold() → Aggressive lowercase (better for comparisons).
print("ß".casefold())  # "ss"
"""# Example 1: Turkish dotted and dotless 'i'
print("İ".lower())       # "i̇" (i + dot)
print("İ".casefold())    # "i̇" (same here, but casefold ensures consistency)

# Example 2: Greek sigma
print("Σ".lower())       # "σ"
print("Σ".casefold())    # "σ"
print("ΟΣ".casefold())   # "ος" (handles final sigma correctly)

# Example 3: Comparing across cases
s1 = "Python"
s2 = "PYTHON"
print(s1.casefold() == s2.casefold())  # True
"""
#===============Searching & Finding==================
#find(sub) → Returns index of first occurrence, or -1
#note:if data is found -->it returns index number otherwise return -1
print("anilsurya anil".find("l"))#3
print("anilsurya anil".find("su"))#4 because of s start index 4
print("anilsurya anil".find("x"))#-1 because of x not found
#index(sub) → Like find(), but raises error if not found.
print("anilsurya anil".index("l"))#3
#print("anilsurya anil".index("x"))#ValueError: substring not found
#rfind(sub) / rindex(sub) → Search from the right.
"""rfind(sub):
Searches for a substring from the right side of the string.
Returns the highest index where the substring is found.
If not found → returns -1.
rindex(sub):
Works like rfind(), but if the substring is not found, it raises a ValueError instead of returning -1.
"""
#rfind:
print("anilsurya anil".rfind("l"))#13-->means right side of first occurrence value index
print("anilsurya anil".rfind("a"))#10
print("anilsurya anil".rfind("x"))#-1
#rindex:
print("anilsurya anil".rindex("l"))#13
#print("anilsurya anil".index("x"))#ValueError: substring not found
#startswith():Boolean checks.
print("anilsurya anil".startswith("anil"))#True
print("anilsurya anil".startswith("Anil"))#False
#endswith():
print("anilsurya anil".endswith("nil"))#True
print("anilsurya anil".endswith("Nil"))#false
#====================Counting & Measuring================
#count(sub)-->Counts occurrences.
print("anilsurya anil".count("anil"))#2
print("anilsurya anil".count("a"))#3
print("anilsurya anil".count("x"))#0 -->if element not found
#len(string) → Length of string (not a method, but essential).
print(len("anil surya"))#10 with space also included
#==============Splitting & Joining==================
"""split() → Splits into list by whitespace or delimiter.
Syntax:split([separator[, maxsplit]])
separator → optional, default is whitespace (" ").
maxsplit → optional, limits number of splits."""
string="anil surya"
print(string.split(" "),type(string))#['anil', 'surya'] <class 'str'>
print(string.split(","),type(string.split(" ")))#['anil surya']
print("Anil,surya,rakesh".split(","))#['Anil', 'surya', 'rakesh']
text = "one two three four five"
print(text.split(" ", 2))# ['one', 'two', 'three four five']

"""
rsplit():Works like split(), but starts splitting from the right.
Syntax:rsplit([separator[, maxsplit]])
Same as split(), but starts splitting from the right.
"""
data = "one:two:three:four"
print(data.rsplit(":", 2))  # ['one:two', 'three', 'four']
print("a,b,c,d,e".rsplit(",",1))#['a,b,c,d', 'e']
#splitlines():Splits a string into a list at line breaks.
poem = "Roses are red\nViolets are blue\nPython is fun"
print(poem.splitlines())  # ['Roses are red', 'Violets are blue', 'Python is fun']
#Joining means combining a list of strings into one string using a separator.
#join():Takes a list (or iterable) of strings and joins them with a separator.
words = ["Python", "is", "awesome"]
print(" ".join(words))  # "Python is awesome"
letters = ["a", "b", "c"]
print("-".join(letters))  # "a-b-c"
row = "John,Anil,25,Engineer"
fields = row.split(",")
print(fields)  # ['John', 'Anil', '25', 'Engineer']
new_row = ";".join(fields)
print(new_row)  # "John;Anil;25;Engineer"

#=============Formatting========
#format() → Inserts values.
print("my name is {}".format("Anil"))#my name is Anil
#f-strings (Python 3.6+) → Inline formatting.
name="anil"
print(f"My name is {name}")#My name is anil
#format_map(dict) → Uses dictionary for formatting.
person = {
    "name": "Alice",
    "age": 25,
    "city": "Hyderabad"
}
# Use format_map with the dictionary
sentence = "My name is {name}, I am {age} years old, and I live in {city}.".format_map(person)
print(sentence)
"""Testing String Properties
isalnum() → True if all characters are alphanumeric.
isalpha() → True if all are letters.
isdigit() → True if all are digits.
isnumeric() → Includes Unicode numbers.
isspace() → True if only whitespace.
islower() / isupper() / istitle() → Case checks"""
print("anil123".isalnum())#True(digits or characters)
print("anil123".isalpha())#False
print("anil".isalpha())#True
print("123".isdigit())#True
"""Checks if all characters in a string are numeric.
Returns True for:
Standard digits (0–9)
Unicode digits (like superscripts, subscripts)
Fractions and Roman numerals in Unicode
Returns False if any character is not numeric."""
print("123".isnumeric())     # True
print("²".isnumeric())       # True (superscript 2)
print("Ⅷ".isnumeric())       # True (Roman numeral 8)
print("½".isnumeric())       # True (fraction one-half)
print("ten".isnumeric())     # False (letters)
print("12a".isnumeric())     # False (mixed with letter)
#================
"""isspace() checks if all characters in a string are whitespace.
Whitespace includes:
Space (" ")
Tab ("\t")
Newline ("\n")
Carriage return ("\r")
Form feed ("\f")
Vertical tab ("\v")"""
print("   ".isspace())     # True (only spaces)
print("".isspace())        # False (empty string)
print(" a ".isspace())     # False (contains a non-space character)
print(" \t\n".isspace())   # True (space + tab + newline)
#==========
print("anil".islower())#True
print("ANIL".isupper())#True
print("Anil".istitle())#True
"""Stripping Methods:Stripping removes unwanted characters (usually whitespace) from the beginning and/or end of a string.
1. strip([chars]):Removes whitespace by default, or specific characters if provided."""
print(" hello ".strip())        # "hello"
print("--hello--".strip("-"))   # "hello"
#lstrip([chars]):Removes whitespace/characters from the left side only.
print("---Anil--".lstrip("-"))#Anil--
#rstrip([chars]):Removes whitespace/characters from the right side only.
print("....Anil...".rstrip("."))#....Anil
print("--ANil-..--".rstrip(".,-"))#--ANil
"""Padding & Alignment Methods:
Padding adds characters to make strings fit a certain width."""
#center(width[, fillchar]):Centers the string in a field of given width.
print("42".center(6))           # "  42  "
print("42".center(6, "*"))      # "**42**"
print("anil".center(10,"$"))#$$$anil$$$
#ljust(width[, fillchar]):Left-aligns the string, padding on the right.
print("Anil".ljust(10,"x"))#Anilxxxxxx
#rjust(width[, fillchar]):Right-aligns the string, padding on the left.
print("anil".rjust(10,"x"))#xxxxxxanil
#zfill(width):Pads with zeros on the left, preserving sign.
#print("anil".zfill("#"))#TypeError: 'str' object cannot be interpreted as an integer
print("anil".zfill(8))#0000anil
print("-45".zfill(8))#-0000045
#=====================Encoding & Expanding==============
#encode([encoding[, errors]]):Converts a string into bytes using a specified encoding.
print("café".encode("utf-8"))          # b'caf\xc3\xa9'
print("café".encode("ascii", "ignore"))# b'caf'
print("café".encode("ascii", "replace"))# b'caf?'
#expandtabs(tabsize):Replaces tabs (\t) with spaces.
print("col1\tcol2".expandtabs(8))      # "col1    col2"
print("col1\tcol2".expandtabs(4))      # "col1 col2"
#===================new-=====
#removeprefix(prefix) (Python 3.9+)
#Removes a prefix if present, otherwise returns the string unchanged.
print("unhappy".removeprefix("un"))    # "happy"
print("unhappy".removeprefix("re"))    # "unhappy"
#removesuffix(suffix) (Python 3.9+):Removes a suffix if present.
print("walking".removesuffix("ing"))   # "walk"
print("walking".removesuffix("ed"))    # "walking"




