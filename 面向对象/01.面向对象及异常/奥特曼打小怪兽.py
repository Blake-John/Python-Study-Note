import random
import abc

class Fighter (abc.ABC) :
    __slots__ = ('_name','_hp')

    def __init__ (self,name,hp) :
        self._name = name
        self._hp = hp
    
    @property
    def name (self) :
        return self._name
    
    @property
    def hp (self) :
        return self._hp
    
    @hp.setter
    def hp (self,hp) :
        self._hp = hp if hp >= 0 else 0
    
    @property
    def is_alive (self) :
        return self._hp > 0
    
    @abc.abstractmethod
    def attack (self,other) :
        pass

class Ultraman (Fighter) :
    __slots__ = ('_name','_hp','_mp')

    def __init__ (self,mp) :
        super ().__init__ ()
        self._mp = mp
    
    def attack (self,other) :
        other._hp -= random.randint (15,26)
    
    def huge_attack (self,other) :
        if self._mp >= 50 :
            self._mp -= 50
            injury = other._hp / 4 * 3
            injury = injury if other._hp > 50 else 50
            other._hp -= injury
            return True
        else :
            self.attack (other)
            return False
    
    def magic_attack (self,others) :
        if self._mp >= 20 :
            self._mp -= 20
            for temp in others :
                if is_alive (temp) :
                    temp._hp -= random.randint (10,21)
            return True
        else :
            return False

    def resume (self) :
        point = random.randint (10,31)
        self._mp += point
        return True
    


    
