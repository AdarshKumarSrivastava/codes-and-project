#wap in pyhton 
#Q1= 0,1,1,2,3,5,8,13,21.........n
#Q2= 1,0,1,0,1,0......n                        
n=int(input("A="))
a=1
while(a<=n):
    if(a%2==0):
        print("0",end=",")
    else:
        print("1",end=",")
    a=a+1    
#Q1
n=int(input("A="))
c=0
b=1
a=0
while(c<=n):
    print(c,end=",")
    a=b
    b=c
    c=a+b

#q3 1,1,0,1,1,0.........n
n=int(input("A="))
while(a<=n):
    if(a%3==0):
        print("0",end=",")
    else:
        print("1",end=",")
    a=a+1        
