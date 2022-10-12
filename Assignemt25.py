# Assignment - 25 Full Stack Web Development using Python MySirG

# OOPs and Inheritance

# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).
class profile:
    def __init__(self):
        self.name="ineuron"
        self.email="xyz@gmail.com"
        self.age=30

    def show_data(self):
        print( self.name)
        print(self.email)
        print(self.age)

p1=profile()
p1.show_data()

# 2. Write a python script to update the above Profile class with encapsulation.
class profile:
    def __init__(self):
        self.name="mysir"
        self.email="xyz@gmail.com"
        self.age=20

    def get_data(self):
        print(self.name)
        print(self.email)
        print(self.age)

    def set_data(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

p1=profile()

p1.set_data("rohit","rohit@gmail.com",23)

print(p1.get_data())

# 3. Write a python script to update 2nd Question, change email and age to __email and
# __age.




class profile:
    def __init__(self):
        self.name="mysir"
        self.__email="xyz@gmail.com"
        self.__age=20

    def get_data(self):
        print(self.name)
        print(self.__email)
        print(self.__age)

    def set_data(self,name,email,age):
        self.name=name
        self.__email=email
        self.__age=age

p1=profile()

p1.set_data("rohit","rohit@gmail.cim",50)
print(p1.get_data())






# 4. Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.

class profile:
    plateform="Ineuron"

    def __init__(self):
        self.name="rohit"
        self.email="rohit@gmail.com"
        self.age=23

    def get_data(self):
        return self.name,self.email,self.age

    def set_data(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    @classmethod
    def pro_file(cls):
        return cls.plateform

pro=profile()
print(profile.pro_file())
pro.set_data("pratima","pratima@gmail.com",23)


print(pro.get_data())



# 5. Write a python script to create a Calculator class with 2 methods for adding and
# subtracting 2 values.

class calculator:
    def __init__(self):
        self.a=50
        self.b=90

    @staticmethod
    def add(x,y):
        print(x+y)

    @staticmethod
    def subtract(a,b):
        print(a-b)

cal=calculator()
calculator.add(30,60)
calculator.subtract(50,20)


# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class.

class calculator:

    @staticmethod
    def add(x,y):
        print(x+y)

    @staticmethod
    def subtract(a,b):
        print(a-b)



class calculator_new_version(calculator):

    @staticmethod
    def multi(x,y):
        print(x*y)

    @staticmethod
    def divi(x,y):
        print(x//y)


cal=calculator_new_version()
calculator_new_version.multi(20,10)
calculator_new_version.divi(50,10)
calculator_new_version.add(40,40)
calculator_new_version.subtract(100,50)



# 7. Write a python script to create a Phone class with 2 methods to print the features
# (calling and sms).

class phone:
    def call(self):
        print("calling feautre")

    def sms(self):
        print("sms feature")

obj=phone()
obj.call()
obj.sms()


# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
# Phone Class.

class calculator:

    @staticmethod
    def add(x,y):
        print(x+y)

    @staticmethod
    def subtract(a,b):
        print(a-b)



class calculator_new_version(calculator):

    @staticmethod
    def multi(x,y):
        print(x*y)

    @staticmethod
    def divi(x,y):
        print(x//y)

class phone(calculator_new_version):
    def call(self):
        print("calling feautre")

    def sms(self):
        print("sms feature")

class smartphone(phone):
    def smtp(self):
        print("smartphone feature 5G support")

obj=smartphone()
obj.add(30,50)
obj.smtp()
    

# 9. Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
# number and 2nd to add a new entry).
# class Truecaller:

#     def fetch_name_number(self):

#dout  
    

# 10. Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller.
#dout
