# define a class with name
class student:
    def __init__(self,name,roll_no,email): # define initialization that class
        self.name=name
        self.roll_no=roll_no
        self.email=email
    def display_student(self):
        print "Student Name:",self.name
        print "Student Roll_no:",self.roll_no
        print "Student email:",self.email



d1= student("Rahul",56,"rahu@gmail.com")
d1.display_student()
if __name__=="__main__":
    Main()


    O/P:
Student Name: Rahul
Student Roll_no: 56
Student email: rahu@gmail.com


