n=1
sum=0
while True:
    cj =input('请输入学生成绩：')
    if cj=='over':
        print('结束输入！')
        break
    elif eval(cj)<0:
        print('录入错误，请重新输入')
        continue
    sum+=eval(cj)
    n+=1
print('总成绩为：%.2f'%sum)
print('你一共录入了%d个成绩'%(n-1))
print('平均分是%.2f'%(sum/n))