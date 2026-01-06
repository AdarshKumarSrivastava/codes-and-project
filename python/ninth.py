# wap in pyhton to ptint if the sum of the cube of the digit is same as no. given by user 
#then the no. is armstrong 
num=int(input("no.="))
sum=0
b=num
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10
if(sum==b):
    print("armstrong number") 
else:
    print("not a armstrong no.")       

#wap in pyhton factorial of given no.
a=int(input("anyno.="))
pro=1
while(a>0):
    pro=pro*a
    a=a-1
print(pro)

#wap in python to find the power. eg(a=2,b=3) a power b 
a=int(input("A ="))
b=int(input("B ="))
c=a**b
print("a power b is =",c)

#wap in pyhton 
#Q1= 0,1,1,2,3,5,8,13,21.........n
#Q2= 1,0,1,0,1,0......n                        
n=int(input("A="))
a=1
b=0
count=0
while(a<=n):
    print("1")
    count=count+1
    print("0")
    a=a+1



