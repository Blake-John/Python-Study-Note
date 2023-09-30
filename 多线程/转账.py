import time
import threading

class Account () :
    def __init__ (self) :
        self._balance = 0
        self._lock = threading.Lock ()
        
    def deposit (self,money) :
        # 先获取锁才能执行后续的代码
        self._lock.acquire ()
        try :
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理业务需要0.01秒时间
            time.sleep (0.01)
            # 修改账户余额
            self._balance = new_balance
        finally :
            self._lock.release ()
        
    @property
    def balance (self) :
        return self._balance
    
class AddMoneyThread (threading.Thread) :
    def __init__ (self,account,money) :
        super ().__init__ ()
        self._account = account
        self._money = money
    
    def run (self) :
        self._account.deposit (self._money)
    
def main () :
        account = Account ()
        threads = []
        # 创建一百个存钱线程向用户中存钱
        for _ in range (100) :
            t = AddMoneyThread (account,1)
            threads.append (t)
            t.start ()
        # 等待所有存钱的线程都执行完毕
        for t in threads :
            t.join ()
        print (f"The account has the possession of {account.balance}")
        
if __name__ == '__main__' :
    main ()
    
        