""" 员工结算系统

某公司有三种类型的员工,分别是部门经理、程序员和销售员。需要设计一个工资结算系统,根据提供的员工信息来计算员工的月薪。
其中,部门经理的月薪是固定15000元;
程序员按工作时间(以小时为单位)支付月薪,每小时200元;
销售员的月薪由1800元底薪加上销售额5%的提成两部分构成。
"""

import abc

class Employee (metaclass=abc.ABCMeta) :
    def __init__  (self,name) :
        self.name = name
    
    @abc.abstractmethod
    def salary (self) :
        pass

class Manager (Employee) :
    def __init__ (self,name) :
        super ().__init__ (name)

    
    @property
    def salary (self) :
        return 15000

class Programmer (Employee) :
    def __init__ (self,name,work_time=0) :
        super().__init__ (name)
        self.wt = work_time
    
    @property    
    def salary (self) :
         return 200 * self.wt
    
class Saler (Employee) :
    def __init__ (self,name,sale_count=0) :
        super ().__init__ (name)
        self.sale_count = sale_count
    
    @property
    def salary (self) :
        return self.sale_count * 0.05 + 1800

def main () :
    ems = [Manager ('A'),Programmer ('B'),Saler ("C")]
    for em in ems :
        if isinstance (em,Programmer) :
            em.wt =int (input ("Please input your work time"))
        elif isinstance (em,Saler) :
            em.sale_count =int (input ("Please input your sale count."))
        print (f"The salary of {em.name} is {em.salary} yuan.")

if __name__ == '__main__' :
    main ()



    