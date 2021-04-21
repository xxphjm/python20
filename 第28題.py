import random
def check(k):
    for i in range(0,len(k)):
        if k.count(k[i])>1:
            return False
a=random.randint(1000,10000)
l=[]
while (a>0):
    l.append(a%10)
    a//=10
l=list(reversed(l))
ac=0
bc=0
b=1
o="0"
while b!=0:
    k=[]
    b=int(input("請輸入："))
    while (b>0):
        k.append(b%10)
        b//=10
    k=list(reversed(k))
    while check(k)==False:
        k=[]
        b=int(input("請重新輸入："))
        while (b>0):
            k.append(b%10)
            b//=10
    k=list(reversed(k))
    for i in range(0,4,1):
        for j in range(0,4,1):
                    if str(b)==o:
                        quit()
                    elif i==j and l[i]==k[j]:
                        ac+=1
                    elif l[i]==k[j]:
                        bc+=1
                   
    print('{0}A{1}B'.format(ac,bc))
    ac=0
    bc=0
    b=1
