a=float(input('输入第一个数：'))
b=float(input('输入第二个数：'))
c=float(input('输入第二个数：'))
if a>=b and a>=c:
     print('最大值：',a)
elif b>=a and b>=c:
     print('最大值：',b)
else:
     print('最大值;',c)
# print(max(a,b,c))