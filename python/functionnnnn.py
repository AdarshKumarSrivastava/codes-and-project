def ab():
    a=1
    sum=0
    while(a<=100):
        if(a%2==0):
            print(a,end=" ")
            sum=sum+a    
        a=a+1    
    print("The sum of the even no. is ",sum)
ab()
print()            
def ab(a):
    sum=0
    while(a<=100):
        if(a%2==0):
            print(a,end=" ")
            sum=sum+a
        a=a+1
    print("the sum of the value is =",sum)
a=1
ab(a)
print()
def abc():
    a=1
    sum=0
    while(a<=100):
        if(a%2==0):
            print(a,end=" ")
            sum=sum+a            
        a=a+1    
    return sum
x=abc()
print("the sum of the no. is =",x)
print()
def abb(a):
    sum=0
    while(a<=100):
        if(a%2==0):
            print(a,end=" ")
            sum=sum+a    
        a=a+1    
    return sum    
a=1
x=abb(a)
print("the sum of the no. is =",x)

