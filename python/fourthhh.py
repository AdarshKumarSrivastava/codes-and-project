#wao in python to find the eligibility of a candidate if he/she is eligible to cast his/her vote or not
a=int(input("age="))
if(a>=18):
    print("you are eligible for vote ")
else:
    print("you are not eligible for vote")    

#waP IN PYTHON TO INPUT NO. OF 5 SUB OF A STU AND PRINT THE GRADES AS PER THE FOLLOWING
# 91-100% = S GRADE
# 71-90% = A G
# 51-70% = B G
# 41-50% = C G
# >40% = FAIL    

a=int(input("maths="))
b=int(input("physics="))
c=int(input("chemistry="))
d=int(input("biology="))
e=int(input("physical ="))
p=(a+b+c+d+e)*100/500
if(p>=91 and p<=100):
    print("S")
elif(p>=71 and p<91):
    print("A grade and your percentage is ",p)    
elif(p>=51 and p<71):
    print("B grade and your percentage is",p)
elif(p>=41 and p<51):
    print("C grade and your percentage is",p)
else:
    print("fail")     
