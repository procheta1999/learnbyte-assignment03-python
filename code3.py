n=int(input("Enter range:"))
x=int(input("Enter el:"))
l=[]
count=0
for i in range(0,n):
    x=int(input("Enter:"))
    l.append(x)
for i in range(0,n):
    if x==l[i]:
        count=count+1
print(count)
