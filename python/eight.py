a=int(input("any no.="))
count=0
while(a>0):
    count=count+1
    a//10
print("total count of the no.=",count) 

#wap sum of no.

a=int(input("any no.="))
count=0
sum=0
while(a>0):
    rem=a%10
    count=count+1
    sum=sum+rem
    a=a//10
print("the count of digit ",count)
print("the sum of the digit ",sum)

#wap reverse of the no.
a=int(input("any no.="))
rev=0
while(a>0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
print("reverse of the no. is ",rev)

#wap find the series
# 1+2+3+4.......20
a=1
sum=0
while(a<=20):
    sum=sum+a
    a=a+1
print("sum of the no.=-",sum)

#Q2
# 1+3+5+7........50
a=1
sum=0
while(a<=50):
    sum=sum+a
    a=a+2
print("sum of the no.=-",sum)

#Q3
#1,2,4,8,16.........n
n=int(input("any no.="))
a=1
while(a<=n):
    print(a,end=",")
    a=a*2
    
#WAP IN PYTHON TO PRINT THE TABLE OF A GIVEN NO. (FROM USER) THROUGH WHILE LOOP
num=int(input("table of ="))
a=1
while(a<=10):
    pro=a*num
    print(pro,end=",")
    a=a+1      