import pywifi
from pywifi import const
import time


def gic () :
    wifi=pywifi.PyWiFi ()
    ifaces=wifi.interfaces () [0]
    print (ifaces.status ())
    if ifaces.status ()==const.IFACE_CONNECTED :
        print ("已连接")
    else :
        print ("未连接")

gic ()





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
