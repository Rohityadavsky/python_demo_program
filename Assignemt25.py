# Assignment - 25 Full Stack Web Development using Python MySirG

# OOPs and Inheritance

# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).

class profile:
    def __init__(self):
        self.name="rohit"
        self.email="ro@gmail.com"
        self.age=22

    def show_data(self):
        print("Name-",self.name,"Age-",self.age,"Email-",self.email )


obj=profile()
obj.show_data()


    



# 2. Write a python script to update the above Profile class with encapsulation.

class profile:
    def __init__(self):
        self.name="rohit"
        self.age=22
        self.email="ro@gmail.com"
class profile2:
    def __init__(self):
        pass

    



# 3. Write a python script to update 2nd Question, change email and age to __email and
# __age.

# 4. Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.


# 5. Write a python script to create a Calculator class with 2 methods for adding and
# subtracting 2 values.

# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class.

# 7. Write a python script to create a Phone class with 2 methods to print the features
# (calling and sms).

# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
# Phone Class.

# 9. Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
# number and 2nd to add a new entry).

# 10. Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller.
