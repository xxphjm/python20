s=input("請輸入請輸入連續字元：")
a=reversed(list(s))
if list(a)==list(s):
    print("YES")
else:
    print("NO")