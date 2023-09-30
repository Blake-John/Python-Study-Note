"""设计一个程序
1.有一个窗口，窗口中有两个按钮 下载 和 关于
2.点击下载会等待10s,下载完成后弹出提示
3.点击关于会弹出作者信息
"""

import tkinter
import tkinter.messagebox
import threading
import time

# class Download (threading.Thread) :
#     def __init__ (self) :
#         super ().__init__ ()
#         self._downloadtime = random.randint(5, 6)
    
#     def run (self) :
#         print ("Start to download.")

def main () :
    class Download (threading.Thread) :
        def run (self) :
            time.sleep (10)
            tkinter.messagebox.showinfo ('Prompt','Download Successfully!')
            # 启用下载按钮
            button1.config (state=tkinter.NORMAL)
    
    def download () :
        button1.config (state=tkinter.DISABLED)
        # 设置守护进程，主程序结束后不再运行
        Download (daemon=True).start ()
    
    def show_about () :
        tkinter.messagebox.showinfo ('About','Writer:Blake John')
    
    top = tkinter.Tk ()
    top.title ('单线程')
    top.geometry ('200x150')
    top.wm_attributes ('-topmost',True)
    
    pannel = tkinter.Frame (top)
    button1 = tkinter.Button (pannel,text='Download',command=download)
    button2 = tkinter.Button (pannel,text='About',command=show_about)
    button1.pack (side='left')
    button2.pack (side='right')
    pannel.pack (side='bottom')
    
    tkinter.mainloop ()

if __name__ == '__main__' :
    main ()