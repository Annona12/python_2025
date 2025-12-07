# 开发者：Annona
# 创建时间：2025/12/7 11:52
# 1、闭包的定义：在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称之为闭包
# 2、闭包的优缺点：
# (1)优点：
# - 局部变量无法共享和长久的保存，而全局变量可能造成变量污染，闭包既可以长久的保存变量又不会造成全局污染；
# - 可以实现类似于私有变量的功能，提高程序的安全性；
# - 可以在不改动原函数的代码情况下，额外的增加一些功能，例如：日志打印等；
# - 可以读取函数内部的变量
# (2)缺点：内存未释放问题；外部通过闭包访问内部变量，在调用过程中变量依然在内存中，注意闭包使用后，对未使用的变量进行删除；

# 3、使用场景：装饰器
def parameter_decorator(fun_name):
    def wrapper(*args,**kwargs):
        print('执行函数{}前'.format(fun_name.__name__))
        return fun_name(*args,**kwargs)
    return wrapper
@parameter_decorator
def my_address(name,age,address):
    print("我的个人信息为：姓名：{}，年龄：{}，地址：{}".format(name,age,address))
@parameter_decorator
def my_address1(name,age,address):
    print("1我的个人信息为：姓名：{}，年龄：{}，地址：{}".format(name,age,address))
my_address = my_address('Annona',26,'浙江杭州')
my_address1 = my_address1('Annona1',27,'江西上饶')
