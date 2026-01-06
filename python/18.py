#Q1
a=int(input("no.="))
b=a+1
c=a-1
for row in range(a):
    for col in range(1,b,1):
        if(row<=c and col<b and row>0 and col>1):
            print(" ",end=" ")
        else:
            print("*",end=" ")        
    print()