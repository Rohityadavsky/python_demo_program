# Assignment - 8 Full Stack Web Development using Python MySirG

# While Loop



# 1. Write a python script to print MySirG 5 times on the screen
i=1
while i<=5:
    print("MySirG",end=" ")
    i+=1


# 2. Write a python script to print first 10 natural numbers

i=1
while i<=10:
    print(i,end=" ")
    i+=1


# 3. Write a python script to print first 10 natural numbers in reverse order
i=10
while i>=1:
    print(i,end=" ")
    i-=1
#another way to create this program 10  natural number in reverse order.
i=1
while i<=10:
    print(11-i,end=" ")
    i+=1


# 4. Write a python script to print first 10 odd natural numbers
n=eval(input("please enter any number:"))
i=1
while i<=n:
    print(i,end=" ")
    i+=2



# 5. Write a python script to print first 10 odd natural numbers in reverse order
n=eval(input("please enter the number:"))
i=1
while i<=n:
    print(n-i,end=" ")
    n=n-2

# 6. Write a python script to print first 10 even natural numbers
n=int(input("Enter number:"))
a=1
while a<=n:
    print(a*2,end=" ")
    a+=1

# 7. Write a python script to print first 10 even natural numbers in reverse order
n=int(input("Enter number"))
a=1
while a<=n:
    print(n*2,end=" ")
    n=n-1
# 8. Write a python script to print squares of first 10 natural numbers
n=int(input("Enter a number"))
a=1
while a<=n:
    print(a**2)
    i=i+1
#another way 
a=1
while a<=10:
    print(a**2,end=" ")
    a=a+1

# 9. Write a python script to print cubes of first 10 natural numbers
n=int(input("Enter number"))
i=1
while i<=n:
    print(i**3,end=" ")
    i=i+1
# another way.
i=1
while i<=10:
    print(i**3,end=" ")
    i=i+1
# 10. Write a python script to print first 10 multiples of 5
i=1
while i<=10:
    print(i*5,end=" ")
    i+=1