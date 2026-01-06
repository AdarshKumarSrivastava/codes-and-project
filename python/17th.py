#Q1
for row in range(5):
    for col in range(1,6,1):
        if(row<=3 and col<=4 and row>0 and col>1):
            print(" ",end=" ")
        else:
            print("*",end=" ")        
    print()
    
#Q2   
for row in range(5):
    for col in range(1,5,1):
        if(row<=0 and col>1 and col<4):
            print(" ",end=" ")
        elif(row==1 and col>1 and col>3 and col<3):
            print("*",end=" ")
        elif(row==2 and col>2):
            print(" ",end=" ")
        elif(row==3 and col>3 and col<3 and col>3 and col>1):
            print("*",end=" ")
        elif(row==4 and col>1 and col<4):
            print(" ",end=" ")
        else:
            print("*",end=" ") 
    print()    