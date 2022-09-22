# Assignment - 5 Full Stack Web Development using Python MySirG

# 1. Write a python script to remove the last digit from a given number. (for example, if
# user enters 2534 then your output should be 253)

n=(input("Enter number"))
print(int(n[:-1]))



# 2. Write a python script to get the last digit from a given number. (for example, if user
# enters 2089 then your output should be 9)

n=int(input("please enter number"))
print(int(str(n)[3]))


# 3. Write a python script to swap data of two variables

a=int(input("Enter number"))
b=int(input("Enter number"))
c=0
a=b
b=c
print("Swap a and b is",a,b)

# another way 

a=int(input("Enter a first number"))
b=int(input("Enter a second number"))
a,b=b,a
print("a",a,"b",b)



# 4. Write a python script to find x power y, where values of x and y are given by user

x=int(input("Enter number"))
y=int(input("Enter number"))
z=x**y
print("Power of x is",z)


# 5. Write a python script which takes a three digit number from the user and displays
# only its first digit.

x=int(input("Enter a three digit  number"))
print(int(str(x)[0]))



# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.

x=int(input("Enter a three digit number "))
print(int(str(x)[1]))



# 7. Write a python script which takes a three digit number from the user and displays
# only its last digit.

x=int(input("Enter the value"))
print(int(str(x)[2]))

# 8. Write a python script to use IN operator to display the data present in the list

list=["mohan","is a good by","but","her friend is","not good"]
print("mohan" in list)

print("MySirG" not in list)
#output is True





# 9. Write a python script to use NOT IN operator to display the data not present in list

list=["mohan","is a good by","but","her friend is","not good"]
print("Rohit" not in list)
#output True


# 10. Write a python script to use IS operator to display if both variables are the same
# object or not?
x=50
y=50

print(id(x),type(x),id(y),type(y))

print(x is y)
print(x is not y)
#output is True.
#output is False.

