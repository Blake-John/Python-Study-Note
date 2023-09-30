import time

def main () :
    # try :
    #     f = open ('D:/install.log','r')
    #     print (f.read ())
    # except FileNotFoundError :
    #     print ("There is not such a file!")
    # except LookupError :
    #     print ("Useing the wrong encoding method!")
    # except UnicodeDecodeError :
    #     print ("There is an error while unencoding!")
    # finally :
    #     if f :
    #         f.close ()

    with open ('D:/install.log','r',encoding='utf-8') as f :
        for line in f :
            print (line,end='')
            time.sleep (0.5)
if __name__ == '__main__' :
    main ()