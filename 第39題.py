n=int(input("請輸入整數n:"))


for a in range(1,n,2):
    for j in range(1,n,1):
        print(" ",end="")
    print(a)
for i in range(1,n+2,2):
    print(i,end=" ")
for i in range(n-2,0,-2):
    print(i,end=" ")
print(" ")
for a in range(n-2,0,-2):
    for j in range(n,1,-1):
        print(" ",end="")
    print(a)