q=int(input("請輸入一個度數："))
s=0
a=0
n=1
for i in range(1,q+1):
    if i<=120:
        s+=2.10 
        a+=2.10 

    elif i>=121 and i<=330:
        s+=3.02
        a+=2.68 

    elif i>=331 and i<=500:
        s+=4.39
        a+=3.61
    
    elif i>=501 and i<=700:
        s+=4.97 
        a+=4.01

    elif i>=701 :
        s+=5.63
        a+=4.50
print("夏月:%.2f" %(s))
print("非夏月:%.2f" %(a))

    
