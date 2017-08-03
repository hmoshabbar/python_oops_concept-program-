# inheritance how to do program using inheritance ....

class Student(object):
    per_raise=1.05
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first +"."+last +"@gmail.com"
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def apply_raise(self):
        self.marks=int(self.marks*1.05)


# Now i am going to create another class and i will inherit from superclass(Student) see below how
# i want to find (Dump Student) and i will inherit from above class

class Dumps(Student):  # i am inheriting from student in my Dump class
    # now i am going to initilizing the method and i will inherit all those thins like first,last,marks...ect
    def __init__(self,first,last,marks,pro_lang): # i am adding another instance varible pro_lang
        # now i am going to inherit all those thing ......see below
        #super().__init__(first,last,marks) #python 3.4 using
        super(Dumps,self).__init__(first,last,marks)
        
        self.pro_lang=pro_lang

        
#stu_1=Student("Moshabbar","Hussain",90,"Python")  # adding new pro_lang

# now since i m inheriting from student so i have to give object name Dumps  like below
stu_1=Dumps("Moshabbar","Hussain",90,"Python")
print stu_1.fullname()
print stu_1.email
print stu_1.marks
print stu_1.pro_lang

    
