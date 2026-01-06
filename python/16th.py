for row in range(5):
    for space in range(4,row,-1):
        print("  ",end="")
    for col in range(1,row+2,1):
        print(col,end=" ")
    print()        
    
#Q2
a=1
for row in range(5):
    for space in range(4,row,-1):
        print("  ",end="")
    for col in range(1,row+2,1):
        print(a,end=" ")
    print()
    a=a+1
    
#Q3
c=4
for row in range(5):
    for space in range(4,row,-1):
        print("  ",end="")
    for col in range(5,c,-1):
        print(col,end=" ")
    print()       
    c=c-1

#Q4
a=5
for row in range(5):
    for space in range(4,row,-1):
        print("  ",end="")
    for col in range(a,6,1):
        print(col,end=" ")
    a=a-1
    print()
    
#Q5
a=5
c=4
for row in range(5):
    for space in range(4,row,-1):
        print("  ",end="")
    for col in range(a,6,1):
        print(col,end=" ")
    for b in range(4,c,-1):
        print(b,end=" ")    
    a=a-1
    c=c-1   
    print()
    
#Q6
for row in range(5):
    for col in range(1,6,1):
        if(row<=3 and col<=4 and row>0 and col>1):
            print(" ",end=" ")
        else:
            print("*",end=" ")        
    print()
    
        