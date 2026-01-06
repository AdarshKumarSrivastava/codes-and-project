'''f= open("notes.txt","r")
print(f.read())

# add item
f= open("notes.txt","a")
f.write("i can do it")
f.close()
f= open("notes.txt","r")
print(f.read())'''

# to make a new note pad 
f= open("new.txt","w")
f.write("hard work is the key of success.")
f.close()
f=open("new.txt","r")
print(f.read())
