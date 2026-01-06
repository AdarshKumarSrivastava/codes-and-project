#Q1 
a=1
for i in range(5):
    for b in range(3,i-2,-1):
        print(a,end=" ")
    print()
    a=a+1    

print()
#Q2
a=5
for i in range(5):
    for b in range(3,i-2,-1):
        print(a,end=" ")
    print()
    a=a-1
print()
print()
#Q4
for i in range(5):
    for b in range(5,i,-1):
        print(b,end=" ")
    print()
    
print()    
#Q4    
c=6
for i in range(5):
    for b in range(1,c,1):
        print(b,end=" ")
    print()
    c=c-1
print()     
print() 
#Q5
c=6
for i in range(5):
    for b in range(1,c,1):
        if(i%2!=0):
            print("0",end=" ")
        else:
            print("1",end=" ")    
    print()
    c=c-1
print()     
print() 
#Q6
c=6
z=1
for i in range(5):
    for b in range(1,c,1):
        if(i%2!=0):
            print("0",end=" ")
        else:
            print(z,end=" ")    
    print()
    c=c-1
    z=z+1
print()     
print() 
#Q7
c=6
z=1
for i in range(5):
    for b in range(1,c,1):
        if(i%2!=0):
            print("0",end=" ")
        else:
            print(z,end=" ")    
    print()
    c=c-1
    if(i%2!=0):
     z=z+1        
    else:
        z=z
        