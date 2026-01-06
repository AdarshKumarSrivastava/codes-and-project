f=open("new.txt","r")
print(f.readline())
print(f.tell())
f.seek(5)
print(f.readline())


'''#ques=
f=open("new.txt","a")
f.writelines("adarsh is a good coader","chicken")
f.close()
f= open("new.txt","r")
print(f.read())'''

#q=it gives you error because we worked on closed file
f=open("new.txt","r")
print(f.readline())
print(f.tell())
f.seek(5)
print(f.readline())
f.close()
print(f.read())