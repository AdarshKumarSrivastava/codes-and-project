#Q1= assign value
fruits=("apple","orange", "grapes")
(green,orange,purple)=fruits
print(green)
print(orange)
print(purple)
print()
print() 
#Q2=all three loop for tuple
a=(1,2,3,4,5,6)
for i in a:
    print(i,end=",")
else:
    print("series ended")    
print()
print()    
a=(1,2,3,4,5,6)
for i in range(len(a)):
    print(a[i],end=",")
else:
    print("series ended")    
print()
print() 
a=(1,2,3,4,5,6)
b=0
while(b<len(a)):
    print(a[b],end=",")
    b=b+1
else:
    print("series ended")        
print()
print() 
#QUES
a=(1,2,3,4,5,6)
b=(7,8,9,10)
c=a+b
print(c,end="")
print()
#Ques= multiply
a=(1,2,3,4,5,6)
b=a*2
print(b)
print()
#Ques= index no.
a=(1,2,3,4,5,6)
print(a.index(4,1,5))
print()
#Ques=count and lenth
a=(1,2,3,4,5,6,2,5,4,3,6,2)
print(a.count(2))
print()
print(len(a))