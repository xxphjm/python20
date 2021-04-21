l=int(input("請輸入整數n:"))
for i in range(1,l//2+1,1):
    for n in range(5-i,0,-1):
        print(' ' ,end='')
        
    for n in range(0,2*i-1,1):
        print('*',end='')

    print()
for i in range(l//2+1,0,-1):
    for n in range(0,5-i,1):
        print(' ' ,end='')
        
    for n in range(0,2*i-1,1):
        print('*',end='')

    print()
