sum=0
for banji in range(1,4):
    print('欢迎%d班同学！'%banji)
    for chengji in range(1,6):
        input('请输入第%d名同学成绩：'%chengji)
        sum+=chengji
    print('%d班同学总成绩是：%.2f'%(banji,sum))