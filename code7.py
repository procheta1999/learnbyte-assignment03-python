n=int(input("Enter range:"))
l=[]
for i in range(0,n):
    x=int(input("Enter:"))
    l.append(x)
for i in range(0,n):
    if(l[i]%2!=0):
        print(l[i])
