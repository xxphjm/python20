a= int(input("甲方的數字："))
b= int(input("乙方的數字："))
l=[]
k=[]
while (a>0):
    l.append(a%10)
    a//=10
l=list(reversed(l))
while (b>0):
    k.append(b%10)
    b//=10
k=list(reversed(k))

print("洗刷刷結果：",end="")
for i in range(0,len(l),1):
    if l[i]>k[i]:
        print("贏",end="")
    elif l[i]==k[i]:
        print("和",end="")
    elif l[i]<k[i]:
        print("輸",end="")
print(" ")