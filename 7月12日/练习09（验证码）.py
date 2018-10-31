import random
num=0
s=''
while num<5:
    num+=1
    c=random.randint(1, 2)
    if c==1:
        a=str(random.randint(0, 9))
        s+=a
    else:
        b=chr(random.randint(65, 90))
        s+=b
print('验证码为：%s'%s)