n=int(input("Enter range:"))
l=[]
ce=0
co=0
for i in range(0,n):
    x=int(input("Enter:"))
    l.append(x)
for i in range(0,n):
    if(l[i]%2==0):
        ce=ce+1
    else:
        co=co+1
print(ce)
print(co)
