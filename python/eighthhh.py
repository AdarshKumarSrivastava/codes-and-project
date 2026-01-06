#1,4,9,........200
a=1
p=1
while(p<=200):
    print(p,end=",")
    a=a+1
    p=a**2

#1+4+9+16........n
n=int(input("no.="))
a=1
p=1
sum=0
while(p<=n):
    sum=sum+p
    a=a+1
    p=a**2
print("the sum of the no.=",sum)    

#1,8,27,64.........200    
a=1
p=1
while(p<=200):
    print(p,end=",")
    a=a+1
    p=a**3

#1+8+27.......n
n=int(input("no.="))
a=1
sum=0
while(p<=n):
    sum=sum+p
    a=a+1
    p=a**3
print("the sum of the no=",sum)    



n=int(input("any no.="))
a=1
sum=0
while(p<=n):
    sum=sum+p
    a=a+1
    p=a**2

a=1
p=1
while(p<=1):
    a=a+1
    p=a**2    