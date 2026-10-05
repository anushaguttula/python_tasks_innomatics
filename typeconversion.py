a=10
b=5.5
c=True
d="hero"
print("data type of a=",type(a))
print("data type of b=",type(b))
print("data type of c= ",type(c))
print("data type of d=",type(d)) 
c=a+b
print("data type of c =",type(c))
#implict conversion
n1=20
n2=True
n3=n1+n2
print(n3)
#explicit conversion
a="10"
print("type of a before =",type(a))
a=int(a)
print("type of a after =",type(a))
a=10
print(bool(a))
a="10"
b=5
a=int(a)
c=a+b
print(c)
