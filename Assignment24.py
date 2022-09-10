# Assignment - 24 Full Stack Web Development using Python MySirG

# Classes and Objects

# 1. Write a python program to create a user class with 3 properties : name, age, email.

class user:
    name='rohit'
    age=22
    email='rohityadavcksy@gmail.com'

u1=user()
print(u1.name)
print(u1.age)
print(u1.email)




# 2. Write a python program to create a user class with a method to greet the user.

class user:
    def greet(self):
        print("Congratulations")

u1=user()
print(u1.greet())




# 3. Write a python program to create 2 objects of the user class and assign different
# values.


class user:
    def __init__(self,p,r):
        self.value1=p
        self.value2=r
    def show_data(self):
        print(self.value1,self.value2)

obj=user(30,50)
obj2=user(100,200)
obj.show_data()
obj2.show_data()



# 4. Write a python program to init default values for user object using __init__ method.


class student:
    def __init__(self):
        self.marks=10

    def show(self):
        print(self.marks)

std=student()
std.show()



# 5. Write a python program to delete the age property of the user.

#doubt





# 6. Write a python program to create 3 user objects and find the youngest of all.

#dobut



# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
# values).
class laptop:

    def __init__(self,r,c,h,b):
        self.ram=r
        self.cpu=c
        self.hdd=h
        self.brand=b

    def showconfig(self):
        print(self.ram,self.cpu,self.hdd,self.brand)
        

com1=laptop(16,"i9","1TB","HP")
com2=laptop(32,"i11","2TB","Macbook")
print(com1.showconfig())
print(com2.showconfig())

# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size.

class laptop:
    def __init__(self,r,c,h,b):
        self.ram=r
        self.cpu=c
        self.hdd=h
        self.brand=b

    def showconfig(self):
        print(self.ram,self.cpu,self.hdd,self.brand)
        

com1=laptop(16,"i9","1TB","HP")
com2=laptop(32,"i11","2TB","Macbook")
com3=laptop(64,"i12","5TB","Macbook")

print(com1.showconfig())
print(com2.showconfig())
print(com3.showconfig())
li=[16,32,64]
print(sorted(li))





# 9. Write a python program to create a School class and 3 instance variables and 1 class
# variable.
class school:
    school="ineuron"

    def __init__(self):
        self.name="Rohit"
        self.age=22
        self.email="rohit@gamil.com"

obj=school()
print(school.school)




# 10. Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values


class Employee:
    def __init__(self):
        self.empid=100
        self.name="Maxwell"
        self.salary="1.1b"

    def show_all_data(self):
        print(self.empid,self.name,self.salary)

obj=Employee()
obj.show_all_data()
