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

def table():
    n= int(input("table no.="))    
    for i in range(1,11,1):
        p=n*i
        print(n,"*",i,"=",p)
table()        