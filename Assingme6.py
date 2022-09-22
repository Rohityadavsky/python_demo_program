#Assignment - 6 Full Stack Web Development using Python MySirG

#Decision Control

# 1. Write a python script to check whether a given number is positive or non-positive

n=int(input("Enter a given number"))
if n>0:
    print("Positive")
elif n==0:
    print("Not Positive and Not Non-Positive")
else:
    print("Non-Positive")

# 2. Write a python script to check whether a given number is divisible by 5 or not

n1=int(input("Enter a number:"))
if n1%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

# 3. Write a python script to check whether a given number is even or odd.

n2=int(input("Enter the given number is:"))
if n2%2==0:
    print("Even")
else:
    print("Odd")

#4. Write a python script to print greater between two numbers. Print number only once
#even if the numbers are the same.

num=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

if num>num2:
    print("Greater then num2",num)
elif num>num:
    print("Greter then num",num2)
else:
    print("It's not correct")

#5. Write a python script to print two given words in dictionary order
dic=["mysirg","rohit"]
print(dic)
#6. Write a python script to check whether a given number is a three digit number or not.
my=int(input("please enter number")
if my<1000 and my>99:
       print("three number")
 else:
       print("not three number")
# 7. Write a python script to check whether a given number is positive, negative or zero.
a=int(input("Enter the given number"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
elif a==0:
    print("Zero")
else:
    print("Incorecct number")

#8. Write a python script to check whether a given quadratic equation has two real &
#distinct roots, real & equal roots or imaginary roots

# 9. Write a python script to check whether a given year is a leap year or not.

year=int(input("Enter the year:"))
if year%4==0:
    print("leap year")
else:
    print("Not leap year")

# 10. Write a python script to print greater among three numbers. Print number only once
#  if the numbers are the same.

num1=int(input("Enter first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
       
print((a if a>c else c) if a>b else (b if b>c else c))
       
# if num1>num2>num3:
#     print("Grater num1")
# elif num2>num1>num3:
#     print("Grater num2")
# elif num3>num2>num1:
#     print("Greater num3")

# 11. Write a python script to take the month value in numeric format and display the
#number of days in it.
       
 month=int(input("Enter the month"))
 if month in (1,3,5,7,8,10,12):
       print("31 days")
  elif month in (4,6,9,11):
       print("30 days")
  elif month==2:
       print(" 28 or 29 days")
  else:
       print("Invalid number")
       
# 12. Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part

 num=complex(input("Enter a complex number"))
 print(num.real) if num.real>num.img else print(num.img)







