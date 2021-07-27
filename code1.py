n=int(input("Enter range:"))
l=[]
for i in range(0,n):
    x=int(input("Enter:"))
    l.append(x)
temp=l[0]
l[0]=l[n-1]
l[n-1]=temp
print(l)
