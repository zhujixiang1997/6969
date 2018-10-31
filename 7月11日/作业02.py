'''
2.写一段代码判断一个人的体重是否合格：
公式:(身高-108）*2=体重，可以有10斤左右的浮动
'''
weight = eval(input('请输入体重（单位斤）：'))
height = eval(input('请输入身高（单位cm）：'))
if (height - 108)*2 >= weight - 10 and (height - 108)*2 <= weight+10:
    print('恭喜你的体重合格！')
else:
    print('兄dei,不行呀！')