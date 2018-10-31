month=int(input('请输入月份：'))
if month>12 or month<1:
    print('*我爸不让我和傻子玩，再见！*')
elif month==12 or month==2 or month==1:
    print('*冬季*')
elif month>=9:
    print('*秋季*')
elif month>=6:
    print('*夏季*')
else:
    print('*春季*')