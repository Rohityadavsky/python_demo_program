# Assignment - 10 Full Stack Web Development using Python MySirG

# For loop and range



# 1. Write a python script to print MySirG N times on the screen
n=int(input("Enter a number"))
for i in range(1,n+1):
    print(i,"MySirG")
# 2. Write a python script to print first N natural numbers
n=int(input("Enter a number"))
for k in range(1,n+1):
    print(k,end=" ")
# 3. Write a python script to print first N natural numbers in reverse order
for x in range(int(input("Enter a number")),0,-1):
    print(x,end=" ")
# 4. Write a python script to print first N odd natural numbers

for a in range(int(input("Enter a number"))):
    print((a*2)+1,end=" ")

# 5. Write a python script to print first N odd natural numbers in reverse order

for a in range(int(input("Enter a number")),0,-1):
    print((a*2)+1,end=" ")


# 6. Write a python script to print first N even natural numbers

for a in range(int(input("Enter a number"))):
    print(a*2,end=" ")

# 7. Write a python script to print first N even natural numbers in reverse order

for a in range(2*int(input("Enter a number")),0,-2):
    print(a,end=" ")


# 8. Write a python script to print squares of first N natural numbers

for a in range(int(input("Enter a number"))):
    print((a+1)**2,end=" ")

# 9. Write a python script to print cubes of first N natural numbers
for a in range(int(input("Enter a number"))):
    print((a+1)**3,end=" ")
#10. Write a python script to print first 10 multiples of Nq
n=int(input("Enter a number"))
for a in range(n):
    print((a+1)*10,end=" ")




