#Q= user defined list 
n=int(input("NO. OF ELEMENTS ="))
li=[]
for b in range(0,n,1):
    a=int(input("any no. = "))
    li.append(a)
print(li,end=",")
print()    

a=(1,2,3,45,6,8,4,5,7)
x=1
for i in a:
    if 2 in a:
        print("exist") 
        x=x+1
        break
if x==1:
    print("do not exist")

#Q
a=(1,2,3,45,6,8,4,5,7)
x=1
k=24
for i in a:
    if (i==k):
        print("exist") 
        x=x+1
        break
if x==1:
    print("do not exist")

