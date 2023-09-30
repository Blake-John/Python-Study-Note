from math import sqrt

class Triangle () :
    def __init__ (self,a,b,c) :
        self._a = a
        self._b = b
        self._c = c
    
    @staticmethod
    def is_valid (a,b,c) :
        return a + b > c and a + c > b and b + c > a 
    
    def perimeter (self) :
        return self._a + self._b + self._c
    
    def area (self) :
        half = (self._a + self._b + self._c)/2
        return sqrt (
            half * (half - self._a) * (half - self._b) * (half - self._c)
        )

def main () :
    a,b,c =5,6,7
    t = Triangle (a,b,c)
    if t.is_valid (a,b,c) :
        print (f'C={t.perimeter ()}')
        print (f'S={t.area ()}')
    else :
        print ('These data could not make up a triangle.')

if __name__ == '__main__' :
    main ()