def add():
    a=int(input("no.1="))
    b=int(input("no.2="))
    c=a+b
    print(c)
#
def sub():
    a=int(input("no.1="))
    b=int(input("no.2="))
    c=a-b
    print(c)
#
def multi():
    a=int(input("no.1="))
    b=int(input("no.2="))
    c=a*b
    print(c)

def divi():
    a=int(input("no.1="))
    b=int(input("no.2="))
    if(b!=0):
        c=a%b
        print(c)
    else:
        print("not defined")
#
def qo():
    a=int(input("no.1="))
    b=int(input("no.2="))
    c=a//b
    print(c)    
   
print("There are five type of function")
print("1=additon")
print("2=subtraction")
print("3=multiplication")
print("4=division")
print("5=quotient")
print()
a=int(input("choose any no.="))
if(a==1):
    add()
elif(a==2):
    sub()
elif(a==3):
    multi()
elif(a==4):
    divi()    
else:
    qo()                
############################################################################
def abc(a,b):
    print(a+" "+b)
abc("hello","world")

def the(a,b,c):
    print("the sum of all three no.=",a+b+c)
    print("the multiplication of all three no.=",a*b*c)
the(a=int(input("digit.1=")),b=int(input("no.2=")),c=int(input("no.3="))) 
#
def the(a,b,c):
    print("the sum of all three no.=",a+b+c)
    print("the multiplication of all three no.=",a*b*c)
a=int(input("digit.1="))
b=int(input("no.2="))
c=int(input("no.3="))
the(a,b,c)
#######################################################################
def aa():
    a=1
    while(a<=n):
        print(a,end="")
        a=a+1
n=int(input("any no.=")) 
aa()
print()       
#
def abc():
    n=int(input("no.="))
    p=1
    while(n>0):
        p=n*p
        n=n-1
    print("factorial=",p)    
abc()
print()
#############################
def table():
    n= int(input("table no.="))    
    for i in range(1,11,1):
        p=n*i
        print(n,"*",i,"=",p)
table()    
