sum=0
for i in range(1,1001):
    if i%3==2 and i%5==3 and i%7==2:
        sum+=1
        print(i)
print('满足的数据一共有%d个'%sum)

n1=int(input('输入第一个数：'))
n2=int(input('输入第一个数：'))
print(str(hex(n1)))
print(str(hex(n2)))

