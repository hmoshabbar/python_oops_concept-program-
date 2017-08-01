class Emplyee:
    def __init__(self,id,name,sex,email,salary,address,join_date,com_name):
        self.id=id
        self.name=name
        self.sex=sex
        self.email=email
        self.salary=salary
        self.address=address
        self.join_date=join_date
        self.com_name=com_name

    def displayEmp(self):
        list=[]
        #print "Emplyee ID------------->:",self.id
        #print "Emplyee Name----------->:",self.name
        #print "Emplyee sex------------>:",self.sex
        #print "Emplyee E-Mail--------->:",self.email
        #print "Emplyee salary--------->:",self.salary
        #print "Emplyee address-------->:",self.address
        #print "Emplyee Join Date------>:",self.join_date
        #print "Emplyee Company Name--->:",self.com_name
        list.append(self.id)
        list.append(self.name)
        list.append(self.sex)
        list.append(self.email)
        list.append(self.salary)
        list.append(self.address)
        list.append(self.join_date)
        list.append(self.com_name)
        print list
        for i in list:
            print i


tab1=Emplyee(101,"Rahul","Male","rahul@hotmail.com",35000,"hyderabad","11-apr-2017","Externetworks India Pvt Ltd")
tab2=Emplyee(102,"Moshabbar","Male","mos@hotmail.com",25000,"hyderabad","11-apr-2017","Externetworks India Pvt Ltd")
tab1.displayEmp()
tab2.displayEmp()
if __name__=="__main__":
    main()


    O/P:
[101, 'Rahul', 'Male', 'rahul@hotmail.com', 35000, 'hyderabad', '11-apr-2017', 'Externetworks India Pvt Ltd']
101
Rahul
Male
rahul@hotmail.com
35000
hyderabad
11-apr-2017
Externetworks India Pvt Ltd


[102, 'Moshabbar', 'Male', 'mos@hotmail.com', 25000, 'hyderabad', '11-apr-2017', 'Externetworks India Pvt Ltd']
102
Moshabbar
Male
mos@hotmail.com
25000
hyderabad
11-apr-2017
Externetworks India Pvt Ltd


    
        

       
