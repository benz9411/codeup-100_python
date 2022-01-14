a=int(input())
list=input().split()

d=[]

for i in range(24):
    d.append(0)

for i in range(a):
    list[i] = int(list[i])

for i in range(a):
    d[list[i]]+=1

for i in range(1,24):
    print(d[i], end=" ")


