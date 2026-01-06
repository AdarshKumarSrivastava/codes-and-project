a=int(input("first no."))
b=int(input("second no."))
print("before swaping")
print("a=",a)
print("b=",b)
c=a
a=b
b=c
print("after swaping")
print("a=",a)
print("b=",b)

print("without using third variable")
a=int(input("first no."))
b=int(input("second no."))
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)

print("by multiplication")
a=int(input("first no."))
b=int(input("second no."))
a=a*b
b=a//b
a=a//b
print("a=",a)
print("b=",b)
