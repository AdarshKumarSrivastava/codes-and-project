#Ques= write a program in python in which we break the list where user want....
a=int(input("no.of elements="))
li=[]
for i in range(a):
    b=input("anything=")
    li.append(b)
print()
print("list=",li)
print()
n=input("enter the value where you want to slice =")
for i in range(a):
    if li[-1]==str(n):
        print("new list =",li[0:a+1])
        a=a-1
        break
    else:
        li.pop()
if li==[]:
    print("given element doesnot exist")
    print("list",li)

#Q2=     
a=["raman","raghav","ram","arohi","ankit","awantika"]
x=a.index("raghav")
print("",x)
print()
y=a.index("arohi")
print(y)


a=["raman","raghav","ram","arohi","ankit","awantika"]
x=a.index("ram")
print("index no.of ram is =",x)
print(a[x:len(a)])

#
a=["vibha","saksham","ansh","raman","raghav","ram","arohi","ankit","awantika"]
x=a.index("ansh")
y=a.index("arohi")
for i in a:
    if "ansh" in a and "arohi" in a:
        x=a.index("ansh")
        y=a.index("arohi")
        c=1
    elif("ansh" in a and "arohi"not in a):
        x=a.index("ansh")
        c=2
    elif("arohi" in a and "ansh"not in a):
        y=a.index("arohi")
        c=3
    else:
        x=0
        y=len(a)
for i in a:
    if(c==1):
        print(a[x:y])
    elif(c==2):
        print(a[x:len(a)])
    elif(c==3):
        print                

