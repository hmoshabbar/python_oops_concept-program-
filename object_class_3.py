# Now i want to print full name using method inside the class how to do see in below (full Program)

class Student:

    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first +"."+last +"@gmail.com"
        #self.full_name=first+" "+last  # we can do like this...also

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
#print stu_2.full_name

# now printing full Name lets see
print stu_1.full_name()   # we should pranticies bracket because its come from self .
print stu_2.full_name()
