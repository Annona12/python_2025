# 开发者：Annona
# 创建时间：2025/12/1 21:02
# 1、捕获异常：即使Python程序的语法是正确的，在运行的时候也可能会发生错误，运行期间检测到的错误称异常
# ①捕获语法一
# try:
#     num = int(input('请输入一个数字：'))
#     print('您输入的数字是：',num)
# except:
#     print('sorry，您输入的不是数字，无法解析！')
# # ②捕获语法二
# try:
#     num = int(input('请输入一个数字：'))
#     print('您输入的数字是：',num)
# except:
#     print('sorry，您输入的不是数字，无法解析！')
# else:
#     print('没有异常输出这段内容！！！')
# # ③捕获异常语法三
# try:
#     num = int(input('请输入一个数字：'))
#     print('您输入的数字是：',num)
# except:
#     print('sorry，您输入的不是数字，无法解析！')
# else:
#     print('没有异常输出这段内容！！！')
# finally:
#     print('无论是否有异常都会输出这段内容！！！')

# 2、抛出异常：使用raise,raise唯一的一个参数指定了要被抛出的异常
#    它必须是一个异常的实例或者是异常的类（也就是Exception的子类）
# x=10
# if x>5:
#     raise Exception('x不能大于5，x的值为{}'.format(x))

# 3、用户自定义异常类以及应用：我们可以通过创建一个新的异常类来拥有自己的异常，新创建的异常类继承自Exception
# 可以直接继承或者间接继承，使用raise，但是不处理
class myError(Exception):
    def __init__(self,leng):
        self.leng=leng
    def __str__(self):
        print('姓名的长度是：' + str(self.leng) + ',超过长度了')

# name='1234567890'
# if len(name)>5:
#     raise myError(len(name))

# 捕获用户抛出的异常
try:
    name = '1234567890'
    if len(name) > 5:
        raise myError(len(name))
except myError as e:
    print(e)
