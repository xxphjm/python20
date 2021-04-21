import math
x=int(input("請輸入x值："))
y=int(input("請輸入y值："))
if x>0:
    if y>0:
        s=math.pow(x,2)+math.pow(y,2)
        print("該點位於第一象限，離原點距離為根號"+str(int(s))) 
        print(str(int(s)))
    elif y<0:
        s=math.pow(x,2)+math.pow(y,2)
        print("該點位於第四象限，離原點距離為根號"+str(int(s))) 
        print(str(int(s)))
elif x<0:
    if y>0:
        s=math.pow(x,2)+math.pow(y,2)
        print("該點位於第二象限，離原點距離為根號"+str(int(s))) 
        print(str(int(s)))
    elif y<0:
        s=math.pow(x,2)+math.pow(y,2)
        print("該點位於第三象限，離原點距離為根號"+str(int(s)))
else:
    print("該點位於原點")

