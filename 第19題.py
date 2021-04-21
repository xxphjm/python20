g=int(input("組數為："))
for i in range(1,g+1,1):
    a,b=map (int,input("第%d組：" %(i)).split(" "))
    s=a*250+b*175
    print("第%d組應收費用：%d" %(i,s))