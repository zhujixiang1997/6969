# for i in range(0,10,2):
#     print(i)

# a=0
# while a<9:
#     print('a=%d'%a)
#     a=a+1
# print('Good bye!')

# i=0
# while i<10:
#     i+=1
#     if i%2==0:
#         continue
#     print(i)

# i=0
# while i<20:
#     print(i)
#     i+=1
#     if i>10:
#         break

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# sum=0
# n=0
# while n<101:
#     sum+=n
#     n=n+1
# print(sum)

# for x in range(1,10):
#     for y in range(1, 10):
#         print('%d*%d=%d'%(y,x,x * y),'\t',end='')
#         if y==x:
#             break
#     print()

for x in range(1,10):
    for y in range(1,10):
        print('%d*%d=%d'%(y,x,x*y),'\t',end='')
        if x==y:
            break
    print()