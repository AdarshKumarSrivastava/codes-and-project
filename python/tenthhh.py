#5,0,10,0,15......n
n=int(input("A="))
a=1
b=1
while(a<=n):
    if(a%2!=0):
        print(5*b,end=",")
        b=b+1
    else:
        print("0",end=",")
    a=a+1        

#Q2 1,0,1,1,1,0,1,1,1,0........n
n=int(input("no.="))
a=1
while(a<=n):
    if(a%2==0 and a%4==0):
        print("1")
    elif(a%2==0):
        print("0",end=",")
    else:
        print("1",end=",")    
    a=a+1    