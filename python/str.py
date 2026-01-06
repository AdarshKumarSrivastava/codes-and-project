'''a="Raman_Singh"
print(type(a))
print()
#Q= lenght
a="Raman_Singh"
x=len(a)
print(x)
print()
#Q= loop
a="Raman_Singh"
for i in a:
    print(i,end="")
print()
#Q=
a="Raman_Singh is a good boy"
if "boy" in a:
    print("yes")
else:
    print("no")
print()
#Ques
a="Raman_Singh"
if "boy" not in a:
    print("no it is not present")
else:
    print("yes it is present")
print()
#Ques
a="Raman_Singh"
a.upper()
print(a)
#Ques
a="Raman_Singh"
a.lower()
print(a)

#Ques= strip 
a=" ram is playing  "
a.strip()
print(a)
print()
#Ques=replace
a="ram is playing,ram is going "
a.replace()
print(a)
print()
#Ques=split
a="ram is playing,ram is going,he is eating "
a.split(",")
print(a)
print()
#Ques= concatenate (+)
a="ram"
b="adarsh"
c="sam"
d="IIT"
e=a+b+c+d
print(e)
print()
#Ques= formating
a=int(input("no.="))
x=f"i have a {a} copy"
print(x)'''
#Ques= WAP IN PYTHON TO INPUT A CHARACTER AND FIND IF IT IS NUMERIC VALUE OR TEXT VALUE OR ANY SPECIAL
inp=input("anything=")
if(inp>="a" and inp<="z"):
    print("it is a txt")
elif(inp>="A" and inp<="Z"):
    print("text")
elif(inp>="0"):
    print("numeric")
else:
    print("special value")      

#Ques= allfunction of IS
a="  "
a.isspace()
print(a)
print()
#
a="HE Is Going"
a.title(a)
print()
#
a="hello"
a.islower()
print(a)
print()
a="123456"
x=a.isnumeric
print(x)
