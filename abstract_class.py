from abc import ABC,abstractmethod
class Emplyee(ABC):
    @abstractmethod
    def cal_salary(self,sal):
        pass

class  Developer(Emplyee):
    def cal_salary(self,sal):
        final_salary=sal * 2.20
        return final_salary

emp_1=Developer()
print emp_1.cal_salary(10000)
    
