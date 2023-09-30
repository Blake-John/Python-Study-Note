# 1.实例方法 —— 方法内部需要访问 实例属性
#    *实例方法 内部可以使用 类名. 访问类属性
# 2.类方法 —— 方法内部 只 需要访问 类属性
# 3.静态方法 —— 方法内部，不需要访问 实例属性 和 类属性


class Game (object) :
    top_score = 0
    def __init__ (self,player_name) :
        self.player_name = player_name
    @staticmethod # 定义静态方法
    def show_help () :
        print ("Help information : Let zombies enter the gate.")
    @classmethod # 定义类方法
    def show_top_score (cls) :
        print ("The historical record : %d." % cls.top_score)
    def start_game (self) :
        print ("%s starts the game." % self.player_name)
def start_game () :
    print ("Welcoome to the game : Plants VS Zombies")
    print ("Well,now,you have three choices.")
    while True :
        choice = input ("0.Exit the game.\n1.Check the help information.\n2.Check the historical record.\n3.Start the game.\n")
        if choice == "1" :
            # 查看帮助信息
            Game.show_help ()
        elif choice == "2" :
            # 查看历史最高分
            Game.show_top_score ()
        elif choice == "3" :
            # 创建游戏对象，开始游戏
            a = input ("Please input your name.")
            player1 = Game (a)
            player1.start_game ()
        elif choice == "0" :
            print ("Well,Bye!")
            break 
        else :
            print ("Please input right selection.")

start_game ()




