# Assignment - 19 Full Stack Web Development using Python MySirG

# Functions

# 1. Write a python program to create a simple function which prints “MySirG” .

def My():
    print("MySirG")
My()


# 2. Write a python program to create a function which expects two arguments and print
# them in the function body.
def f1(a,b):
    print(a,b)
f1(10,20)

# 3. Write a python program to create a function which expects an unknown number of
# arguments.
def f2():
    # i dont know understand this   question

# 4. Write a python program to create a function which expects kwargs arguments.
 def f3(**kwargs):
    print("all data in ",kwargs)

 f3(First_name='rohit',Lost_name='yadav',Mobile_number='53535354')
 f3(Email='rohityadavcsky@gmail.com',village='kadipur_jaunpur')


# 5. Write a python program to create a function which expects a list as an argument.
def li():
    list=[23,45,343,3434,3434,34566]
    



# 6. Write a python program to create a function that finds a maximum of four numbers.
def f4():
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    c=int(input("Enter a third number"))
    d=int(input("Enter four number"))

    num = {a, b, c, d}
    print("Number:",num)
    if(a > b and a > d and a>c):
      print("Maximum 1's number  is greater")  
    elif(b > a and b>c and b>d) :
       print("Maximum 2's number  is greater")
    elif(c>a and c>b and c>d) :
      print("Maximum 3's number  is greater")
    elif(d >a and d>b and d>c) :
       print("Maximum 4's number  is greater")
    else :
      print("done")
      
f4()



# 7. Write a python program to sum all the numbers in a list.
def li():
    list=[1,2,4,5,6,8,37643,48575]
    total=0
    for x in list:
        total+=x
    print(total)
li()

# 8. Write a python program to multiply all the numbers in a list.
def li():
    list=[1,2,4,5,6,8]
    total=0
    for x in list:
        total*=x
    print(total)
li()

# 9. Write a python program to create a function to check whether a number falls in a
# given range.
# 10. Write a python program to create a function to check whether a given number is even
# or odd.
def eve():
    num=int(input("Please enter a number"))
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")
eve()