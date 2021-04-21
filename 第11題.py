def get_con(month, date):
    dates = (21, 19, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    con = ("摩羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蝎座", "射手座")
    if date < dates[month-1]:
        return con[month-1]
    else:
        return con[month]
a,b=map (int,input("請輸入月日：").split(" "))
print ((get_con(a,b)))