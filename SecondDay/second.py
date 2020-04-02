# lst1=[1,'abc',[True,'hello'],3]
# # print(lst1)

# lst1.append('world')
# print(lst1)
# print('#################################')
# u=lst1.pop(1)
# print(u)
# print(lst1)
# print('#################################')
# 最基础的操作


# print('abc')
# print(100)
# print(True)

# print('abc',100)
# print('-------------------------')
# print(int('100')+100)

# print('abc','def','hij',end='--',sep=',')
# print('hello world')

# i=100
# j=None

# if j==None:
#     print('i不为空')
#python是存粹的面向对象语言,比java还要存粹

# print(int('100')+200)
# myint=int
# print(myint('100')+200)
# int=str
# print(int('100')+'200')

# True=1
# False=0
# b=None

# 数据类型
# print(1e3)
# int float str bool
# 结构类型
# list tuple set map

# 常用函数
# 工厂方法
# print(str(100)+'abc')
# from datetime import *
# print(datetime.now())
# 数学函数
# + - * / // %  ** pow
# print(2**3)
# print(pow(2,3))
# 位运算
#      &  |  ^   <<    >>
# print(10>>2)
#逻辑运算
#   and  or   not
# if not age>19 and ssex='男':
#     print('true')
# else:
#     print('false')
# 系统的内置函数
# i=100
# print(type(True))
# <class 'int'>
# <class 'bool'>
# print(isinstance(bool(1),bool))
# i=0
# i+=1
# i-=3
# i*=4    i=i*4
# i//=5  i=i//5     i/=3   i|=3
# i=j=k=10       i,j=10,20
# def getInfo():
#     return 'hello','world','abc'
# a,b,c=getInfo()
# print(a)
# print(b)
# print(c)
# i,j=5,6
# i,j=j,i
# a,b,c=1,1,2
# a,b,c=b,c,b+c

# 控制语句
# mk=int(input('请输入均分'))
# if mk>90:
#     i='优秀'
# elif mk>80:
#     i='良好'
# else:
#     i='差'

# 循环
# while循环和for循环
# s,i=0,0
# while i<=100:
#     s,i=s+i,i+1
# print(s)

# break和continue

# i=0
# while i<100:
#     i+=1
#     if i%2==0:
#         continue
#     print(i)
# for i in range(1,100,2):
#     print(i)
# for i in 'hel lo':
#     print(i)
# 可迭代器:序列sequence
# print(range(1,100))

# for i,j in zip([0,2,4,8],'abcde'):
#     print(i,j)

def abc():
    print("This is abc")

# lst=[1,True,abc,'hello',5]
# print(lst)
# print('----------------------------')
# for unit in lst:
#     print(unit)

# lst1=list('abc')
# print(lst1)

#切片
# i=list('abcdefhijk')
# print(i[2])
# print(i[2:5])
# print(i[2:])
# print(i[:5])
# print(i[:])
# print(i[2::2])
# print(i[-3:])
# print(i[-1])
# print(i[-1:-3])
# print(i[2:7:2])
# print(i[7:2:-1])
# print(i[::-1])
# ['a','b','c','d','h','i','j','k']
# 深拷贝和浅拷贝

# 关于引用
# i=100
# j=50
# print(id(i))
# print(id(j))

# s='abc'
# print(id(s))
# s+='d'
# print(id(s))
# 任何操作系统中,任何语言中,连续字符串具备"不变性"

# s=''
# for i in range(10000):
#     s+=str(i)

# String类,StringBuffer类和StringBuilder类有什么区别?

# i=100
# print(id(i))
# i+=1
# print(id(i))
# lst1=[1,2,3]
# print(id(lst1))
# lst1.append(4)
# print(id(lst1))

# del lst1[0]
# print(id(lst1))

# print('hello'[1:4])

# lst1=[10,True,'hello']
# lst2=lst1
# lst1[0]=200
# print(lst2)
# python解释器在运行时需要加载基础类和基础库
# 那么python有那么多的类库,以及互联网中不断提交的新的功能类和库
# python不能在解释器开始运行前将所有的类库都实现加载
# 那样会导致解释器臃肿和占用海量内存,效率变得非常低下
# 所以python和java一样,默认仅仅加载最常用的基础类
# 而其他的类库,则是什么时候用到,什么时候请编码者自己用import语句将其
# 导入内存
# import copy
# lst1=[10,'abc',True]
# lst2=copy.deepcopy(lst1)
# lst1[0]=20
# print(lst1)
# print(lst2)

# import copy
# lsta=[1,2,3]
# lstx=['hello',lsta]
# lsty=copy.deepcopy(lstx)
# lstx[1][1]=20
# print(lstx)
# print(lsty)
# print(lstx[0][0])
# 切片不仅仅操作列表,可以操作任意可迭代元素
# lst1=[1,2,3]
# # lst2=['a']
# lst3=lst1+['a']
# print(lst3)
# print(lst3*3)

# lst1=[1,'ab',True]
# i=False
# print(i not in lst1)
# in和not in同样不仅仅针对列表,可以对任意可迭代元素进行操作
# print('e' in 'hallo')
# print(150 in range(1,120))

# 列表的内置函数:
# print(cmp([10,20,30],[6,22,33]))
# 字符串本身是可迭代查询元素
# 所有可迭代元素都可以通过[]进行查找和切片

# print(len('abc'))
# print(len([1,2,3,[4,10],5,60]))
# lst1=[1,20,33,2,4]
# lst2=list(reversed(lst1))
# print(lst2)

# lst1=['中国','上海','北京']
# lst3=sorted(lst1,reverse=True)
# print(lst3)
# lst4=sorted(lst1,reverse=False)
# print(lst4)

# print(max(lst1),min(lst1),sum(lst1))
# print(max(lst1))
# 汉语拼音的顺序排列的字母编码

# 列表生成式,现在学习的第二个表达式,第一个是三元表达式
# lst=[]
# for i in range(0,101):
#     if i%2==1:
#         lst.append(i)
# print(lst)

# lst=[i**2 for i in range(0,11) if i%2==1]
# print(lst)
# names=['张三','李四','王五','马六']
# fruits=['梨子','苹果','樱桃']
# 请快速的生成一个列表,列表中的元素为'张三喜欢吃梨子','李四喜欢吃苹果'..
# 最后打印这个列表
# lst=[names[i]+'喜欢吃'+fruits[i] for i in range(0,3)]
# print(lst)

# lst=[name+'喜欢吃'+fruit for name,fruit in zip(names,fruits)]
# print(lst)

# lst=[name+'喜欢吃'+fruit for name in names for fruit in fruits]
# print(lst)

# lst=[str(j)+'*'+str(i)+'='+str(i*j) for i in range(1,10) for j in range(1,i+1)]
# print(lst)

# for i in range(1,10):
#     print([str(j)+'*'+str(i)+'='+str(i*j) for j in range(1,i+1)])

# for i in range(1,10):
#     print('\t'.join([str(j)+'*'+str(i)+'='+str(i*j) for j in range(1,i+1)]))
# [print('\t'.join([str(j)+'*'+str(i)+'='+str(i*j) for j in range(1,i+1)])) for i in range(1,10)]

# 字符串具有不变性
# i='abc'
# j='ab'
# j=j+'c'
# k='ab'+'c'
# print(id(i),id(j),id(k))
# i==k != j
# 这里的结果和java完全保持一致
# 静态缓冲池
# 先编译再执行
# 而编译在做什么?
# 1:语法检查
# 2:常量对象的构建
# 3:将文字翻译成二进制

# String s1="hello";
# String s2="world";
# String s3="hello"+"world";
# String s4=s1+st2;
# String s5="helloworld";
# print(s3==s4)
# print(s5==s4)
# print(s3==s5)

# i=100
# print(i.bit_length())
# i=100000
# print(i.bit_length())
# 所有的对象都可以通过.来进行寻址
# i=100
# python一切皆是对象
# print('hello world'.count('o'))
# s='hello world'
# print(s.upper())
# 3&4    1==1 and 2>1
# 位运算和逻辑运算不要弄混淆

# ip1='192.168.11.33'
# mask1='255.255.254.0'
# def getNetId(ip,mask):
#     return '.'.join([str(int(a)&int(b)) for a,b in zip(ip.split('.'),mask.split('.'))])

# def getNetId(ip,mask):
#     lst=[]
#     for a,b in zip(ip.split('.'),mask.split('.')):
#         lst.append(str(int(a)&int(b)))
#     return '.'.join(lst)

# print(getNetId(ip1,mask1))
# python基础解释器,没有互联网中各个工程师后期编写的库函数
# pip install numpy
lst=[1,2,3,4,5]
print(sum(lst))