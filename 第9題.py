a,b=map (str,input("請輸入兩字串：").split(","))
dict={}
dict[a]=0
for x in dict.keys():
    if x in b:
        print('YES')
    else:
        print('NO')
'''a,b=map (str,input("請輸入兩字串：").split(","))
dict=[]
dict.append(a)
for x in dict:
    if x in b:
        print('YES')
    else:
        print('NO')'''
