year=int(input('請輸入年份：'))
s = ['猴' ,'雞' ,'狗' ,'豬' ,'鼠' ,'牛' ,'虎' ,'兔' ,'龍' ,'蛇' ,'馬' ,'羊']
print('这一年生肖为{}'.format(s[year%12]))
