print('***学员结业考试成绩测评***')
results=float(input('输入学员成绩：'))
if results>=90:
    print('优秀！')
elif results>=80:
    print('良好！')
elif results>=60:
    print('中等！')
else:
    print('差')