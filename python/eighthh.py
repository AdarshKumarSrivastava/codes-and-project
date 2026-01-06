  #WAP IN PYHTON TO PRINT THE SUM OF  N ODD NO.
num=int(input("any no.="))
a=1
sum=0
while(a<=num):
    sum=sum+a
    a=a+2
print("the sum of odd no.=",sum)

#WPIN PYTHON TO PRINT SERIES OF THE N EVEN NO.
num=int(input("no.="))
a=2
while(a<=num):
    print(a,end=",")
    a=a+2
  
#WAP IN PYHTON TO PRINT THE SUM OF first N ODD NO.
num=int(input("any no.="))
num2=num+num
a=1
sum=0
while(a<=num2):
    sum=sum+a
    a=a+2
print("the sum of the series",sum)

#Wap PYTHON TO PRINT SERIES OF THE first N EVEN NO.
num=int(input("no.="))
num2=num+num
a=2
while(a<=num2):
    print(a,end=",")
    a=a+2


    
#WAP IN PYTHON TO PRINT THE TABLE OF A GIVEN NO. (FROM USER) THROUGH WHILE LOOP
num=int(input("table of ="))
a=1
while(a<=10):
    pro=a*num
    print(num,"*",a,"=",pro)
    a=a+1