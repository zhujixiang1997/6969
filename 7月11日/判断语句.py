'''
判断程序的过程:从上到下，从左到右依次执行
判断语句：if 判断条件：
                    满足条件后执行的代码块
当所有条件都不满足就执行else语句，else语句只能放在最后，可以不写
判断i语句必须是if开始
chr()字符 会将数字转换成对应的ASCCII
ASCII
a=97    b=98
A=65    B=66
'''

a=float(input('请输入:'))
if a==10:
    print(a,'等于10')
elif a<10:
    print(a,'小于10')
else :
    print(a,'大于10')



