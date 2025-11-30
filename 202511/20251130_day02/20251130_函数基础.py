# 开发者：Annona
# 创建时间： 10:37
# 1、python的函数基础
# ①定义函数普通函数+位置参数
def introduction(name,age,sex):
    '''
    函数的注释
    :param name:
    :param age:
    :param sex:
    :return:
    '''
    print("接下来我进行自我介绍：我叫"+name,"，今年"+age+"岁","性别:",sex)
# 位置参数的应用
introduction('Annona','26','女')
# 指定参数的应用
introduction(sex="女",name='Annona',age="26")
# 缺省参数
def introduction1(name,age,sex='女'):
    '''
    函数的注释
    :param name:
    :param age:
    :param sex:
    :return:
    '''
    print("接下来我进行自我介绍：我叫"+name,"，今年"+age+"岁","性别:",sex)
# 位置参数的应用
introduction1(name='Annona',age="26")
# 不定长参数：*和**可以不定长度的实参
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    print('总和=',sum)
sum(10,20,30,40,50)
def introduction2(**kwargs):
    print("接下来我进行自我介绍：我叫"+kwargs['name'],"，今年"+kwargs['age']+"岁","性别:",kwargs['sex'])
introduction2(sex="女",name='Annona',age="26")
print(introduction.__doc__)

# ②匿名函数：在编写代码的过程中有时不需要给函数命名，使用lambda
# 普通使用场景
res= lambda x,y:x+y
print(res(30,40))
# 结合python的内置函数
min_num=lambda x:min(x)
print(min_num([10,20,30,60]))
# 已知一个列表为[1,4,6,9,12,23,25,28,36,38,41,56,63,77,88,99]，找出元素值为偶数的数据，
ls=[1,4,6,9,12,23,25,28,36,38,41,56,63,77,88,99]
print(list(filter(lambda x: x % 2==0,ls)))

# 案例3：
r6 = lambda *a: a  # 不定长参数 ，*a:代表可以输入多个或者0个值
print(r6(1, 2, 3, 4, 5, 6))

# 案例4：使用匿名函数另一种方式，直接赋值
r8 = (lambda num1, num2: num1 if (num1 >= num2) else num2)(9, 6)
print(r8)

# 2、Python中的基础常识知识点
# ①python中的保留字
import keyword
print(keyword.kwlist)
# ②字符串的截取:字符串截图，左边的内容包括，右边的内容不包括
a = 'zbjhgdfsiww'
print(a[2:5:2])
print(a[-1:-5:-1])
print(a[-5:-1:1])

# ③占位符：%d:数字;%s:字符串;%f:小数/浮点数
print('接下来我进行自我介绍：我叫%s,今年%d,性别%s,身高%f'%("Annona",26,'女',156.9))
print('接下来我进行自我介绍：我叫{},今年{},性别{},身高{}'.format("Annona",26,'女',156.9))

# ④变量
b=134
print('内存单位',id(b))
print('数据类型',type(b))
print('变量值',b)


# 匿名函数相关的内容后续有机会还是需要多多学习一下；