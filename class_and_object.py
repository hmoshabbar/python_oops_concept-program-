# create a class:
# Class:: Class is a blue Print of which object we are created.

# METHOD 1:
class Student:    # its a class 
    pass


stu_1=Student()   # its a object of Student Class
stu_2=Student()   # its a object of Student Class

# Now he have to create instance Variable for object....(for obj 1)
# instance Variable: is a variable we are create for object

stu_1.first="Moshabbar"
stu_1.last="Hussain"
stu_1.email="moshabbar.hussain@gmail.com"
stu_1.marks=60

# Now he have to create instance Variable for object....(for obj 1)

stu_2.first="Rahul"
stu_2.last="Amin"
stu_2.email="rahul.amin@gmail.com"
stu_2.marks=98

# Now Print Statement use for display result purpose(for stu_1)
print stu_1.first
print stu_1.last
print stu_1.email
print stu_1.marks

# Now Print Statement use for display result purpose(for stu_2)
print stu_2.first
print stu_2.last
print stu_2.email
print stu_2.marks


# For above Exaple for class it tooks lots of code for all so i am going to do same things using intitilization
# Methods is  : def __init__(self,instance variable )

# METHOD 2:
class Student: # its a class

    # i am creating initialization Methods for that class with that methods i am putting instance varible name

    def __init__(self,first,last,marks):  # here (self) is a instance [stu_2.first="Rahul" and self.first=first is same]
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first +"."+last +"@gmail.com"
        
        
# now no need to create instance variable which have mentioned in above
# now just create object and give inside your instance variable like below
stu_1=Student("Moshabbar","Hussain",60)
stu_2=Student("Rahul","Amin",98)
# Now Print Statement use for display result purpose(for stu_1)
print stu_1.first
print stu_1.last
print stu_1.email
print stu_1.marks

# Now Print Statement use for display result purpose(for stu_2)
print stu_2.first
print stu_2.last
print stu_2.email
print stu_2.marks

# Now i want to print full name of both two student ....like below
print "{} {}" .format(stu_1.first,stu_1.last)
print "{} {}" .format(stu_2.first,stu_2.last)


# Now i want to print full name using method inside the class how to do see in below (full Program)

class Student:

    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first +"."+last +"@gmail.com"
        #self.full_name=first+" "+last
    # i am creting another method to print full name already i mentioned in above
    def full_name(self):  # it self means it will inherit from that  class Student
        return "{} {}" .format(self.first,self.last)


    
stu_1=Student("Moshabbar","Hussain",60)
stu_2=Student("Rahul","Amin",98)

# Now Print Statement use for display result purpose(for stu_1)
print stu_1.first
print stu_1.last
print stu_1.email
print stu_1.marks
#print stu_1.full_name

# Now Print Statement use for display result purpose(for stu_2)
print stu_2.first
print stu_2.last
print stu_2.email
print stu_2.marks

# now printing full Name lets see
print stu_1.full_name()   # we should pranticies bracket because its come from self .
print stu_2.full_name()


# Now Class Variable and how to do it and declare it.....
# class Variable:: its a variable and its share among with all instance variable class variable we are declared
# below the class only ......see example

class Student:
    per_raise=1.90  # its a class variable 

    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first +"."+last +"@gmail.com"

    def full_name(self):
        return "{} {}".format(self.first,self.last)

    # now method for class variable ..
    def apply_raise(self):
        self.marks=int(self.marks*1.90)

stu_1=Student("Rahul","Amin",90)
print stu_1.marks
stu_1.apply_raise()# stu_1 its a object and apply_raise its a name of the method
print stu_1.marks

# now for dictionary format for student .......
print stu_1.__dict__
print stu_2.__dict__
        







