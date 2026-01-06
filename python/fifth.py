#WAP IN PYTHON TO INPUT MARKS OF 5 SUB OF A STU AND PRINT PASS IF HE GET MORE THAN 40 IN EACH SUB AND MORE THAN 50% ELSE :FAIL
a=int(input("maths="))
b=int(input("physics ="))
c=int(input("chemistry="))
d=int(input("biology="))
e=int(input("physical ="))
p=(a+b+c+d+e)*100/500
if(a==b==c==d==e >40 and p>50):
    print("passs",p)
else:
    print("fail",p)

#WAP IN PYTHON TO INPUT MARKS OF 5 SUB OF A STU AND PRINT PASS HE GET 40+ IN ANY SUB OR HE GET MORE THAN 50% ELSE:FAIL 
a=int(input("maths="))
b=int(input("physics ="))
c=int(input("chemistry="))
d=int(input("biology="))
e=int(input("physical ="))
p=(a+b+c+d+e)*100/500
if(a>=40):
    print("pass")
elif(b>=40):
    print("pass")
elif(c>=40):
    print("pass")
elif(e>=40):
    print("pass") 
elif(p>50):
    print("pass")
else:
    ("fail")    

#WAP IN PYTHON TO INPUT A NO. FROM USER IF THE NO. IS EVEN AND GREATER THAN 100 THEN PRINT ELSE: PRINT SQUARE 
# IF THE NO. IS ODD AND GREATER THAN 100 THEN PRINT NO. ELSE:CUBE OF THE NO.
a=int(input("any no. ="))
if(a%2==0 and a>100):
    print(a)
elif(a%2==0 and a<100):
    print("square of the no.",a**2)
elif(a%2!=0 and a>100):
    print(a)
else:
    print("cube of the no.",a**3)                 