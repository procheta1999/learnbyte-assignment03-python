n=int(input("Enter range:"))
l=[]
pro=1;
for i in range(0,n):
    x=int(input("Enter:"))
    l.append(x)
for i in range(0,n):
    pro=pro*l[i]
print(pro)
