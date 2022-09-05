# Assignment - 11 Full Stack Web Development using Python MySirG

# loops

# 1. Write a python script to calculate sum of first N natural numbers
n=int(input("Enter a number is:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    print(i,end=" ")
    i+=1
print()
print("sum of the number is =",sum)






# 2. Write a python script to calculate sum of squares of first N natural numbers
n=int(input("Enter a number is:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    print(i*i,end=" ")
    i+=1
print()
print("Sum of the n square natural number is =",sum)    


# 3. Write a python script to calculate sum of cubes of first N natural numbers
n=eval(input("Please enter a number :"))
i=1
sum=0
while i<=n:
    sum=sum+i**3
    print(i**3,end=" ")
    i+=1
print("sum of the cube natural number is=",sum)

# 4. Write a python script to calculate sum of first N odd natural numbers
n=int(input("Enter a number is:"))
i=1
while i<=n:
    print(i,end=" ")
    i+=2

# 5. Write a python script to calculate sum of first N even natural numbers
n=int(input("Enter a number is:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    print(i*2,end=" ")
    i+=1
print()
print("sum of the n even natural number is =",sum)
# 6. Write a python script to calculate factorial of a given number

import math
math.factorial(5)


n=int(input("Enter a number is:"))
i=1
fact=1
while i<=n:
    fact=fact*n
    print(fact,end=" ")
    n-=1


# 7. Write a python script to count digits in a given number
n=int(input("Enter a given number is:"))
count=0
while n>0:
    count=count+1
print(count)
    # doute

# 8. Write a python script to calculate sum of digits of a given number
# 9. Write a python script to print binary equivalent of a given decimal number. (do not
# use bin() method)
n=int(input("Enter a number"))

# 10. Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)