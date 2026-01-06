#wap in python to find smallest among three no.
a=int(input("no.1="))
b=int(input("no.2="))
c=int(input("no.3="))
if(a<b<c):
    print("no.1 is smallest among three =",a)
elif(b<a<c):
    print("no.2 is smaleest among three=",b)
else:
    print("no.3 is smallest among three=",c)        

#alternate

if(a<b and a<c):
    print("no.1 is the smallest among three=",a)
elif(b<c and b<a):
    print("no.2 is the smallest among three=",b)
else:
    print("no.3 is the smallest among three=",c)

#another method
a=int(input("no.1="))
b=int(input("no.2="))
c=int(input("no.3="))
if(a<b):
    if(a<c):
        print("no.1 is the smallest among three=",a)
    else:
        print("no.3 is the smallest among three=",c)
else:
    if(b<c):
        print("no.2 is the smallest among three=",b)
    else:
        print("no.3 is the smllest among three=",c)                            