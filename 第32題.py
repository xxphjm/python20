while True:
    n= int(input("輸入一正整數："))
    if 11<= n <= 1000:
        if n%2==0 and n%11==0 and n%5!=0 and n%7!=0:
            print("YES")
        else:
            print("NO")
        break
        
    else:
        print('錯誤')
        continue