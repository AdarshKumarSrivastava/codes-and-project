#wap in python to find greatest among three numbers...
a=int(input("no.1="))
b=int(input("no.2="))
c=int(input("no.3="))
if(a>b>c):
    print("no.1 is greatest among three=",a)
elif(b>a>c):
    print("no.2 is greatest among three=",b)
else:
    print("no.3 is greatest among three=",c)    

#alternate method
a=int(input("no.1="))
b=int(input("no.2="))
c=int(input("no.3="))
if(a>b):
    if(a>c):
        print("no.1 is greatest among three =",a)
    else:
        print("no.3 is greatest among three =",c)
else:
    if(b>c):
        print("no.2 is the greatest among three =",b)
    else:
        print("no.3 is the greatest among three =",c)                
