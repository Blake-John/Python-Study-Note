import time

print ("Hello world!")
print ("Helo man!")
time.sleep (2)
name=input ("What is your name?")
print ("Hello",name,"!")
print ("Let's play a game！")
a=int (input ("How long do you want if there is a ▲?"))
print ("Look!")
for i in range (1,a+1) :
    for x in range (i) :
        print ("*",end=" ")
    print(" ")
anwser=input ("Is it beautiful?('Y'or'N')")
if anwser=="Y" :
    time.sleep (2)
    print ("And look this!")
    for s in range (1,10) :
        y=1
        for c in range (s) :
            print (s,"*",y,"=",s*y,end="  ")
            y=y+1
        print (" ")
    print ("Wow!Could you find the amazement?")
else :
    if a<=9 :
        time.sleep(1)
        print ("Oh!I am so sad!")
    elif a>9 and a<=99 :   
        print ("You are a bad man!!!")
    elif a>99 and a<=999 :
        print ("Oh!My god! Here is a foolish man,he is so stupid!")
    else :
        print ("Oh!Shit! Fucker man! Fucker son! Fuck you!! !@^@$#^@!%!")
time.sleep(5)
