# for x in range(1,10):
#     for y in range(1,10):
#         print('%d*%d=%d'%(y,x,x*y),'\t',end='')
#         if x==y:
#             break
#     print()

#准备数据
# array1=["1.大乔","2.庄周","3.孙膑","4.杨玉环","5.明世隐",
#         "6.凯","7.雅典娜","8.花木兰","9.杨戬","10.曹操",
#         "11.亚瑟","12.程咬金","13.廉颇","14.刘邦","15.张飞",
#         "16.虞姬","17.孙尚香","18.李元芳","19.黄忠","20.马可波罗",
#         "21.安琪拉","22.诸葛亮","23.小乔","24.甄姬","25.高渐离"
#         "26.李白","27.阿珂","28.兰陵王","29.百里玄策","30.宫本武藏"]
# array2=["1.凯","2.雅典娜","3.花木兰","4.杨戬","5.曹操"]
# array3=["1.安琪拉","2.诸葛亮","3.小乔","4.甄姬","5.高渐离"]
# array4=["1.虞姬","2.孙尚香","3.李元芳","4.黄忠","5.马可波罗"]
# array5=["1.李白","2.阿珂","3.兰陵王","4.百里玄策","5.宫本武藏"]
# array6=["1.亚瑟","2.程咬金","3.廉颇","4.刘邦","5.张飞"]
# array7=["1.大乔","2.庄周","3.孙膑","4.杨玉环","5.明世隐"]
# def into():
#     print("****************************************************")
#     print("*===================王者荣耀助手===================*")
#     print("*                    =====1.全部 =====                   *")
#     print("*                    =====2.坦克 =====                   *")
#     print("*                    =====3.战士 =====                   *")
#     print("*                    =====4.刺客 =====                   *")
#     print("*                    =====5.法师 =====                   *")
#     print("*                    =====6.射手 =====                   *")
#     print("*                    =====7.辅助 =====                   *")
#     print("*                    =====8.返回菜单 =====               *")
#     print("****************************************************")
#
# def hero(arr):
#     for i in arr:
#         print(i)
# def shuxing():
#     a=input('请输入英雄编号和名称')
#     if a in array1:
#         index=array1.index(a)
#         if 5>index>=0:
#             print('该英雄是个辅助')
#         elif 10>index>=5:
#             print('该英雄是个战士')
#         elif 15>index>=10:
#             print('该英雄是个坦克')
#         elif 20>index>=15:
#             print('该英雄是个射手')
#         elif 25>index>=20:
#             print('该英雄是个法师')
#         elif 30>index>=25:
#             print('该英雄是个刺客')
#     else:
#         print('没有这个英雄')
#
#
#
# def shuxing2(name='凯',wz='上单',cz='无尽之刃，宗师之力，电刀'):
#     print('英雄名称:%s'%name)
#     print('所在位置:%s' % wz)
#     print('大神推荐出装:%s' % cz)
#
#
#
#
#
# if __name__=='__main__':
#    into()
#    while True:
#        key=int(input('请输入选项：'))
#        if key==1:
#         hero(array1)
#         shuxing()
#
#        elif key==2:
#             hero(array2)
#             k = int(input("请输入英雄编号查看详情"))
#             if k==1:
#                 shuxing2()
#             elif k==2:
#                 shuxing2('雅典娜','上单','黑切，圣盾')
#             elif k==3:
#                 shuxing2('花木兰','上单','黑切，圣盾')
#             elif k==4:
#                 shuxing2('杨戬','上单','黑切，圣盾')
#             elif k==5:
#                 shuxing2('曹操','上单','黑切，圣盾')
#             else:
#                 print("你的输入有误！")
#        elif key==3:
#             hero(array3)
#             k = int(input("请输入英雄编号查看详情"))
#             if k == 1:
#                 shuxing2('安琪拉', '中单', '大帽，法穿')
#             elif k == 2:
#                 shuxing2('诸葛亮', '中单', '大帽，法穿')
#             elif k == 3:
#                 shuxing2('小乔', '中单', '大帽，法穿')
#             elif k == 4:
#                 shuxing2('甄姬', '中单', '大帽，法穿')
#             elif k == 5:
#                 shuxing2('高渐离', '中单', '大帽，法穿')
#             else:
#                 print("你的输入有误！")
#        elif key==4:
#             hero(array4)
#             k = int(input("请输入英雄编号查看详情"))
#             if k == 1:
#                 shuxing2('虞姬', 'ADC', '电刀，无尽')
#             elif k == 2:
#                 shuxing2('孙尚香', 'ADC', '电刀，无尽')
#             elif k == 3:
#                 shuxing2('李元芳', 'ADC', '电刀，无尽')
#             elif k == 4:
#                 shuxing2('黄忠', 'ADC', '电刀，无尽')
#             elif k == 5:
#                 shuxing2('马可波罗', 'ADC', '电刀，无尽')
#             else:
#                 print("你的输入有误！")
#        elif key==5:
#             hero(array5)
#             k = int(input("请输入英雄编号查看详情"))
#             if k == 1:
#                 shuxing2('李白', '打野', '打野刀，无尽')
#             elif k == 2:
#                 shuxing2('阿珂', '打野', '打野刀，无尽')
#             elif k == 3:
#                 shuxing2('兰陵王', '打野', '打野刀，无尽')
#             elif k == 4:
#                 shuxing2('百里玄策', '打野', '打野刀，无尽')
#             elif k == 5:
#                 shuxing2('宫本武藏', '打野', '打野刀，无尽')
#             else:
#                 print("你的输入有误！")
#        elif key==6:
#             hero(array6)
#             k = int(input("请输入英雄编号查看详情"))
#             if k == 1:
#                 shuxing2('亚瑟', '坦克', '多兰，日炎')
#             elif k == 2:
#                 shuxing2('程咬金', '坦克', '多兰，日炎')
#             elif k == 3:
#                 shuxing2('廉颇', '坦克', '多兰，日炎')
#             elif k == 4:
#                 shuxing2('刘邦', '坦克', '多兰，日炎')
#             elif k == 5:
#                 shuxing2('张飞', '坦克', '多兰，日炎')
#             else:
#                 print("你的输入有误！")
#        elif key==7:
#             hero(array7)
#             k = int(input("请输入英雄编号查看详情"))
#             if k == 1:
#                 shuxing2('大乔', '辅助', '法穿，蓝盾')
#             elif k == 2:
#                 shuxing2('庄周', '辅助', '法穿，蓝盾')
#             elif k == 3:
#                 shuxing2('孙膑', '辅助', '法穿，蓝盾')
#             elif k == 4:
#                 shuxing2('杨玉环', '辅助', '法穿，蓝盾')
#             elif k == 5:
#                 shuxing2('明世隐', '辅助', '法穿，蓝盾')
#             else:
#                 print("你的输入有误！")
#        elif key==8:
#         break
#        else:
#             print("输入有误")

