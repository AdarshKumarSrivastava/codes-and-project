for a in range(5):
    for i in range(1,a+2):
        print(i,end="")
    print() 

#Q2
b=1  
for a in range(5):
    for i in range(1,a+2):
        print(b,end="")
    print() 
    b=b+1
print()
#Q3
b=a
for a in range(5):
    for i in range(1,a+2):
        if(a%2!=0):
            print("0",end="")
        else:
            print("1",end="")    
    print() 
print()
#Q4
b=5  
for a in range(5):
    for i in range(1,a+2):
        print(b,end="")
    print() 
    b=b-1
print()    
#Q5 
b=5
for a in range(5):
    for i in range(1,a+2,1):
        print(b,end="")
        b=b-1
    print()
    b=5
    
#Q6 
n=int(input("any no.="))
c=n
for i in range(n):
    for a in range(1,i+2):
        print(c,end=" ")
        c=c-1
    print()
    c=n    


        