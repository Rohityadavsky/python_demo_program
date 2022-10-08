# Assignment - 24 Full Stack Web Development using Python MySirG

# Classes and Objects

# 1. Write a python program to create a user class with 3 properties : name, age, email.
class user:
    name="rohit"
    age=23
    email="rohit@gmail.com"
obj=user()
# print(obj.name)
# print(obj.age)
# print(obj.email)
print(user.name)
print(user.age)
print(user.email)


# 2. Write a python program to create a user class with a method to greet the user.

class user:

    def greet_user(self):
        print("Congratulations")

u1=user()
print(u1.greet_user())

#  or

class user:
    def __init__(self):
        self.user="Greet user"
obj=user()
print(obj.user)




# 3. Write a python program to create 2 objects of the user class and assign different
# values.


class user:

    def data(self):
        print("All Information of user")

obj=user()
obj.name="MysirG"
obj.place="Bhopal"

obj2=user()
obj2.email="mysig@gmail.com"
#object first
print(obj.name)
print(obj.place)
#object second
print(obj2.email)
    




# 4. Write a python program to init default values for user object using __init__ method.

class user:
    def __init__(self):
        self.name="rohit"
        self.age=23
        self.email="rohit@gmail.com"

    def show(self):
        print(self.name,self.age,self.email)

obj=user()
obj.show()

#  or

class user:
    def __init__(self):
        self.name="xyz"
        self.email="xyz@gamilc.com"

obj=user()
print(obj.name,obj.email)




# 5. Write a python program to delete the age property of the user.

class user:
    def __init__(self):
        self.name="mysir"
        self.age=50


    def delete(self):
        print(self.name)
        del self.age
        

obj=user()
obj.delete()



# 6. Write a python program to create 3 user objects and find the youngest of all.

class user:
    def __init__(self,age):
        self.age=age

    def youngest(self):
        if s1.age>s2.age and s1.age>s3.age:
            print("s1 youngest")
        elif s2.age>s1.age and s2.age>s3.age:
            print("s2 youngest")
        else:
            print("s3 youngest")

s1=user(40)
s2=user(43)
s3=user(39)
print(s1.youngest())
        




# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
# values).
# class laptop:

class laptop:
    def __init__(self):
        self.brand="HP"
        self.ram=32
        self.cpu="i9"

    def showconfig(self):
        return self.brand,self.ram,self.cpu


lap=laptop()
print(lap.showconfig())


# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size.


#confusion  




# 9. Write a python program to create a School class and 3 instance variables and 1 class
# variable.

class school:
    school_name="xyz"

    def __init__(self):
        self.principal_name="Gajodhar"
        self.teacher_number=50
        self.all_number_of_student=1000

    def school_data(self):
        print(self.principal_name)
        print(self.teacher_number)
        print(self.all_number_of_student)

    @classmethod
    def show_school_name(cls):
        return cls.school_name

obj=school()
obj.show_school_name()
obj.school_data()



# 10. Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values

class employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary

    def show_employ(self):
        return self.empid,self.name,self.salary

obj=employee(1,"pramod",25000)
print(obj.show_employ())
