n=int(input("Enter range:"))
l=[]
sum=0;
avg=0.0;
for i in range(0,n):
    x=int(input("Enter:"))
    l.append(x)
for i in range(0,n):
    sum=sum+l[i]
avg=sum/n
print(sum)
print(avg)
