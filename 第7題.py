a,b=map (int,input("請輸入月租費及月租費及通話時間：").split(","))

if a==186:
    b*=0.09
   
    if b>=a and b<2*a:
        b*=0.9
    elif b>=2*a:
        b*=0.8
    print("通話費為：%.1f" %(b))
elif a==386:
    b*=0.08
  
    if b>=a and b<2*a:
        b*=0.8
    elif b>=2*a:
        b*=0.7
    print("通話費為：%.1f" %(b))
elif a==586:
    b*=0.07
   
    if b>=a and b<2*a:
        b*=0.7
    elif b>=2*a:
        b*=0.6
    print("通話費為：%.1f" %(b))
elif a==986:
    b*=0.06
   
    if b>=a and b<2*a:
        b*=0.6
    elif b>=2*a:
        b*=0.5
    print("通話費為：%.1f" %(b))


