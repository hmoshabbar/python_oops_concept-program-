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
