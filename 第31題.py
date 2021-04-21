dict1 = {'國文':0, '英文': 0, '微積分': 0, '體育': 0, '程式設計': 0}
while True:
    a= int(input("國文："))
    if 0 <= a <= 100:
        ad={"國文":a}
        dict1.update(ad)  
    else:
        print('錯誤')
        continue

    b= int(input("英文："))

    if 0 <= b <= 100:
        ad={"英文":b}
        dict1.update(ad)   
    else:
        print('錯誤')
        continue
    c= int(input("微積分："))
    if 0 <= c <= 100:
        ad={"微積分":c}
        dict1.update(ad) 
    else:
        print('錯誤')
        continue
    d= int(input("體育："))
    if 0 <= d <= 100:
        ad={"體育":d}
        dict1.update(ad)
        
    else:
        print('錯誤')
        continue
    e= int(input("程式設計："))
    if 0 <= e <= 100:
        ad={"程式設計":e}
        dict1.update(ad)
        break
    else:
        print('錯誤')
        continue
sum = 0
for i in dict1: 
        sum = sum + dict1[i] 
ma = max(dict1, key = dict1.get)
mi = min(dict1, key = dict1.get)
a=(max(dict1.values()))
i=(min(dict1.values()))
print("平均分數:%.2f" %(sum/5))
print("最高分科目:%s%d分" %(ma,a))
print("最低分科目:%s%d分" %(mi,i))