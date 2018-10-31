day=0
money=0
while money<100:
    money+=2.5
    day += 1
    if day%5==0:
        money-=6
print('你一共需要%d天才能存够100元'%day)