n=int(input("Enter range:"))
pos1=int(input("Enter pos1:"))
pos2=int(input("Enter pos2:"))
l=[]
for i in range(0,n):
    x=int(input("Enter:"))
    l.append(x)
temp=l[pos1-1]
l[pos1-1]=l[pos2-1]
l[pos2-1]=temp
print(l)
