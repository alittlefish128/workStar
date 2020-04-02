
# print("hello world")
# print("abc")
# print('你好')
# if 1==1:
#     print("1的确等于1")
# else:
#     print("1是不等于1的")
#     print('程序结束')

# print('ab\'c')
# print("bc'd")

# s1='hello"world'
# s2="hello'world"
# s3="""abc
# bcd
# def"""
# s4='''a
# b"""
# c
# d'''
# s5='中文';#这个是注释
# # 你好
# if 1==1:
#     print('a')
# else:
#     print('b')
# pth=r"c:\now\xyz.txt"
# print(pth)
# h='hello'
# w="world"
# hw=h+' '+w
# print(hw*3)
# print('hello','world','你好',sep=',')
# print('回家',end='')
# print('吃饭',end='')
# print('abc')
# print()

# i=5
# if i>5:
# ==  >   >=   <   <=  !=
# i=5
# free(i)
# i='hello world'
# i='zhangsan'
# 变量和值分离了
# 变量只有一种类型:地址
# 值的类型有:
# 1:整形  int+long 
# i=50000000000000000000000000000000000000000000000000000000000000
# print(i)
# # 2:浮点  float
# i=3.1415926
# print(i)
#3:科学计数类型 
# i=15e3;#1.5*10^3
# print(int(i))
# i=15
# j=float(i)
# print(j)
# print(15*1.0)
# print("10"+15)
#4:布尔类型
# b1=True
# b2=False
# print(b1,b2)
# print(b1*b2)
# if False/True:
#     print("1就是真")
# # 5:字符串 str()
# s='hello world'
# s1='100'
# i=100
# print(i*2)
# print(str(i)*2)

# i=100;j=100
# i=100,j=100
# i=j=100
# i,j=100,200
# i,j=getRet()
# def getRet():
#   return 100,200
# print("")

# if 1<10<100:
#     print("1小于10小于100")

# if 条件表达式:
#     语句
# elif 条件表达式:
#     语句
# else:
#     语句

# nm=input("请输入学生的姓名:")
# ag=float(input("请输入学生的均分:"))
# if ag>90:
#     print(nm+'的成绩优秀')
# elif ag>80:
#     print(nm+'的成绩良好')
# elif ag>70:
#     print(nm+'的成绩普通')
# elif ag>=60:
#     print(nm+'的成绩差')
# else:
#     print(nm+'的不及格')

# if 1:
#     a=100
# else:
#     a=200

# # c语言的三元表达式
# a=100 if 0 else 200
# print(a)
# if a>50:
#     if a>60:
#         print("gt 60")
#     else:
#         print("gt 50 and lt 60")

# 循环
# while循环和for循环
# s,i=0,1
# while i<=100 and (not i<=0):
#     s+=i
#     i+=1
# print(s)

# 条件中支持与或非的逻辑运算
# 条件1 && 条件2 ||  条件3
# 条件1 and 条件2 or 条件3    not
# fbra数列 1 1 2 3 5 8 13 21 34 
# 实现上述的50之前的数列的打印
# a+b==c

# a,b,c=1,1,2
# print(a,b,end=' ')
# while c<=50:
#     print(c,end=' ')
#     a,b=b,c; c=a+b

# foreach循环
# for i in range(1,100):
#     print(i)
# 请用for循环实现1-100之间求和
# s=0
# for i in range(101):
#     s+=i
# print(s)
    
# + - * / // %   pow

# print(10/3,pow(2,3),2**3)
# 请快速打印所有的水仙花数字
# for abc in range(100,1000):
#     a,b,c=abc//100,abc//10%10,abc%10
#     if abc==a**3+b**3+c**3:
#         print(abc,end=' ')

# for abc in range(100,1000):
#     a,b,c=abc//100,abc//10%10,abc%10
#     x=print(abc,end=' ') if abc==a**3+b**3+c**3 else 0

# x=100 if 1==1 else 200    x=print(abc,end=' ') if abc==a**3+b**3+c**3 else 0
# if 1==1:                  if abc==a**3+b**3+c**3:
#     x=100                    x=print(abc,end=' ')
# else:                     else:
#     x=200                    x=0

# 数据结构
# 列表   元组   map
# 列表的本质,列表类似一个可变长数组
# ar=[1,2,3,4]
# ar=list(1,2,3,4)
# # for a in ar:
# #     print(a)
# print(ar[0])
# print(ar[3])
# # print(ar[4])
# # ar[4]=5
# ar.append(5)
# print(ar[4])
#     #  1,2,3,4,5
#     # 0 1 2 3 4 5
# ar.insert(3,100)
# print(ar)
# del ar[3]
# print(ar[3])
# print(ar)

# import random
# lst=[]
# names=['张三','李四','王五']
# fruits=['苹果','梨子','桃子','樱桃','哈密瓜']

# for x in range(3):
#     name=names[random.randint(0,len(names)-1)]
#     fruit=fruits[random.randint(0,len(fruits)-1)]
#     print(name+"喜欢吃"+fruit)

#实现找出0-15之间10个不重复的随机数
import random
lst1=list(range(100))
print(lst1)
lst2=[]
for i in range(15):
    l=len(lst1)
    idx=random.randint(0,l-1)
    lst2.append(lst1.pop(idx))
print(lst2)

# for y in range(10):
#     for x in range(10):
#         idx=y*10+x
#         flag=False
#         for u in lst2:
#             if u==idx:
#                 flag=True
#                 break
#         v=1 if flag==True else 0
#         print(v,end=' ')
#     print()
# 仿造我上面的程序编写一个扫雷的初始化代码
# 要求打印10*10的棋盘,棋盘上一共15颗雷,雷用1打印,不是雷的棋子用0打印
# 打印10行,每行10颗棋子,棋子和棋子之间间隔一个空格

# 请回去实现菱形和等腰三角形的打印,打印*
# 打印乘法口诀

# nfc = ["火箭队", "湖人队"]
# afc = ["老鹰队", "热火队"]
# for teama, teamb in zip(nfc, afc):
#      print(teama + " vs. " + teamb)

# teams = ["火箭队", "湖人队", "老鹰队", "热火队"]
# for index, team in enumerate(teams):
#     print(index, team)