n=int(input())
d=input().split()

a=[]

for i in range(n):
    d[i]=int(d[i])

for i in range(n):
    a.append(d[i])

for i in range(n-1,-1,-1):
    print(d[i],end=' ')
