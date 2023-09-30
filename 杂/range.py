import random


class Ran (object) :
    def __init__(self) -> None:
        self.repeat_num1 = []
        self.repeat_num2 = []
    
    def ran (self,num1,num2) :
        result_1 = random.randint (1,num1 + 1)
        result_2 = random.randint (1,num2 + 1)

        while result_1 in self.repeat_num1 :
            result_1 = random.randint (1,num1 + 1)
        
        while result_2 in self.repeat_num2 :
            result_2 = random.randint (1,num2 + 1)
        
        self.repeat_num1.append (result_1)
        self.repeat_num2.append (result_2)

        return result_1 and result_2
    
    def delete (self) :
        self.repeat_num1 = []
        self.repeat_num2 = []

    def exits () :
        exit ()

