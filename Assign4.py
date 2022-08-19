# 1. Write a python script to take your name as input from the user and then print it.
# input always take str value.

n=input("please enter your name:")
print(n)

# 2. Write a python script to take input from the user. Input must be a number.

n1=int(input("please enter any number:-"))
print(n1)

# 3. Write a python script which takes two numbers from the user, then calculate their sum
# and display the result.

a=int(input("Enter first number:"))
a1=int(input("Enter the second number:"))
s=a+a1
print("Sum of the number",s)

# 4. Write a python script which takes the radius from the user and display area of a circle.

pi=3.14
r=float(input("Enter the area of radius"))
area=pi*r*r
print("Area of the circle is ",area)

# 5. Write a python script to calculate the square of a number. Number is entered by the user.

s=int(input("please enter the any number:"))
s1=s*s
print("square of the number is ",s1)

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
#area of triangle formula is a=1/2*b*h
# b*h/2
b=eval(input("Enter the area breath"))
h=eval(input("Enter the area hight"))
are=(b*h)/2
print("Area of the triangle is",are)

# 7. Write a python script to calculate average of three numbers, entered by the user
# sum of the total number divide by and number of terms.

n1=int(input("Enter first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
avg=(n1+n2+n3)/3
print("Average of the three number is ",avg)

#  8. Write a python script to calculate simple interest
# formula of simple interset is p*r*t/100

p=eval(input("Please enter SI principle amount"))
r=eval(input("please enter SI rate"))
t=eval(input("please enter SI time"))
SI=(p*r*t)/100
print("Sum of the Simple Intrest is",SI)

# 9. Write a python script to calculate the volume of a cuboid.
# formula of volume of cubiod is len,wid,heigh.
len=eval(input("Enter the length of cubiod"))
wid=eval(input("Enter the width of cubiod"))
heigh=eval(input("Enter the heigh of cubiod"))
cubiod=len*wid*heigh
print("Volume of Cuboid is",cubiod)

# 10. Write a python script to calculate area of a rectangle
# rectangle is A = l × w.

l=eval(input("Enter the leng"))
w=eval(input("Enter the width"))
rect=l*w
print("Area of the rectangle is",rect)














