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
