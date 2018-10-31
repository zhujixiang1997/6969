sum=0
for i in range(100,1000):
    ge=i%10
    shi=i//10%10
    bai=i//100%10
    if i==ge**3+shi**3+bai**3:
        sum+=1
        print('%d是水仙数' % i)
print('一共有%d个水仙数'%sum)