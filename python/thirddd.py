p=int(input("physics ="))
c=int(input("chemistry ="))
m=int(input("maths ="))
b=int(input("bio ="))
phy=int(input("physical ="))
per=(p+c+m+b+phy)*100/500
t=(p+c+m+b+phy)
if (per>40 and t>250):
    print("pass")
else:
    print("fail because your total is less than 250 or your percentage is less than 40")
    print("your percentage",per,"and your total is ",t)    