import numpy as np
n,m=map (int,input("請輸入n及m：").split(" "))
p=[]
for i in range(1,n+1,1):
    a= input("請輸入第%d列:" %(i))
    a =a.split(' ')
    p.append(a)
p=np.array(p)
p=np.transpose(p) 
for x in  range(0,m,1):
    print("輸出矩陣第%d列：" %(x+1),end="")
    for f in range(0,n,1):

        print(p[x,f],end=" ")
    print(" ")