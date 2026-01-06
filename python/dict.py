a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
print(a)   
#Q2 constuctor method
a=dict(name="adarsh",Class="btech",sub="maths,python")
print(a)
print()
#Q3 same keys
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python","name":"adi"}
print(a)
print()
#Q4 all same keys 
a={"roll no.":12,
   "roll no.":54,
   "roll no.":45,
   "roll no.":54}
print(a)
print()
#Q5 diffrent keys
a={"hlo":78,
   "hy":78,
   "adarsh":78}
print(a)
print()
#Q6 clear
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
x=a.clear()
print(x)
#Q6
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
del a
print(a)
#Q7 lenght
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
x=len(a)
print(x)
print()
#Q8 list
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":["maths,physics,python"]}
print(a)
print()
#Q8 tuple
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":("maths,physics,python")}
print(a)
print()
#Q9= singlr use of key 
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
print(a["name"])
print(a["sub"])
print()
#Q9 GET FUNCTION
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
x=a.get("name")
y=a.get("sub")
print(x)
print(y)
print()
#Q10= items
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
x=a.items()
y=a.keys()
z=a.values()
print(x)
print(y)
print(z)
print()
#Q11 = update value
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
a["class"]="btech"
a["sub"]="java"
print(a)
print()
#
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
a.update({"sub":"computer"})
print(a)
print() 
#Q add
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
print(a)
a["promoted"]=True
print(a)
print()
#Q=pop
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
print(a)
a.pop("name")
print(a)
print()
#Q=blank pop 
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
print(a)
a.pop()
print(a)
print()
#Q= popping value
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
print(a)
a.pop("adarsh")
print(a)
print()
#Q= condition
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
print(a)
if "name"in a:
    print("mahadev")
else:
    ("adarsh")

#Q= condition as boolean
a={"name":"adarsh",
   "class":"cse(Btech)",
   "sub":"maths,physics,python"}
print(a)
print("name" in a)       
