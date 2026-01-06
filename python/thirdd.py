a=int(input("any no."))
if(a%2==0):
    print("the no. is even and its square is ",a**2)
else:
    print("the no. is odd and its cude is ",a**3)





# wap in python to input no. of 5 sub of a students find the percentage. if the percentage is greater then 50 , then print the percent
#and the message pass else fail
p=int(input("physics ="))
c=int(input("chemistry ="))
m=int(input("maths ="))
b=int(input("bio ="))
phy=int(input("physical ="))
per=(p+c+m+b+phy)*100/500
if(per>50):
    print("pass and percentage is =",per)
else:
    print("fail and your percentage is =",per)


