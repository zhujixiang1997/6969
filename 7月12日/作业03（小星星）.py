# for x in range(1,6):
#     for y in range(1,6):
#         print('*', end='')
#     print()
#
# num2=0
# while num2<=5:
#     num=1
#     while num <= 5:
#         print('*', end='')
#         num += 1
#     print(end='\n')
#     num2+=1

for x in range(1,6):
    for y in range(1,6):
        print('*', end='')
        if x==y:
            break
    print()

for x in range(1,6):
    for y in range(1,7-x):
        print('*',end='')
    print()

# m=0
# while m<5:
#     n = 0
#     while n < 1:
#         print('*')
#         n += 1
#         print()
#         m+=1
# for x in range(1,6):
#     for y in range(1,6):
#         print('*',end='')
#     print()

