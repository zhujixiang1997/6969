sum=0
for i in range(10000,100000):
    ge=i%10
    shi=i//10%10
    bai=i//100%10
    qian=i//1000%10
    wan=i//10000%10
    if ge==wan and shi==qian and ge+shi+qian+wan==bai:
        sum+=1
        print('%d是个回文数'%i)
print('一个有%d个回文数'%sum)