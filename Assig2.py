
# Assignment-2: Python Basics


# 1. Write a python script to add comments and print “Learning Python” on screen.
print('"Learning python"')

# 2. Write a python script to add multi line comments and print values of four variables,
# each in a new line. Variable contains any values.
"""
this is the multi line comments why using multi line comments i think this comments for the user to understand
code for easely 

"""
# string data
a="rohit"
# integer data
b=24234
# float data
c=2342.42342
#complex data
d=4+3j

print(a,b,c,d,sep="\n")


 




# 3. Write a python script to print types of variables. Create 5 variables each of them
# containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

a="MySirG"
b=342442
c=4324.54342
d=4+3j
e=True
print(a,b,c,d,e,sep="\n")
print(type(a),type(b),type(c),type(d),type(e))



# 4. Write a python script to print the id of two variables containing the same integer
# values.


x=42342
y=42342
print(id(x),id(y))
#output  3141162885360 3141162885168



# 5. Create four variables in a Python script and assign values of different data types to
# them. Write a Python script to print value, its type and id of each variable

a=42434
b="mysirg"
c=35435.34345
d="A"
e=ord(d)
print(a,id(a),type(a))
print(b,id(b),type(b))
print(c,id(c),type(c))
print(e,id(e),type(e))





# 6. Write a python script to print all the keywords

import keyword
#from keyword import kwlist
# from keyword import kwlist as kw
print(keyword.kwlist)

# 7. On Python shell use help() function and display the list of keywords
help()


# 8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
# value to it. Write a python script to import A1 module in A0 and print value of the
# variable created in A0.py

#ok
#A0.py file import 
import A1
print(A1.x)
print(A1.p)


# A1.py source file create two variable 

x="MySirG"
p="Welcome to computer world"
print( x, p,sep=",")


# 9. Name the keywords, used as data in the Python script.
#many keyword just like that 
if,class,def,

# 10. Write a python script to display the current date and time. First create variables to
# store date and time, then display date and time in proper format (like: 13-8-2022 and
# 9:00 PM)

import datetime
now=datetime.datetime.now()
