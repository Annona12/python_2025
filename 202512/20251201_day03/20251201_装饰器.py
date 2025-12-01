# 开发者：Annona
# 创建时间：2025/12/1 21:02
# 1、什么是装饰器：装饰器本质上也是Python的一个函数或者类，
# 它可以让其他函数或者类再不需要做任何代码修改的前提下增加额外的功能，
# 装饰器的返回值也是一个函数或者类
# 2、经常使用的场景：插入日志、性能测试、事务处理、缓存、权限校验等场景
# 3、有了装饰器我们可以抽离出大量与函数功能本身无关的雷同代码到装饰器中并重复使用，装饰器：就是为已经存在的对象添加额外的功能
import logging
# 案例1：在执行函数的时候，除了正常执行函数外，还有要输出下日志信息，如输入xx函数正在执行
# def fun1():
#     print('执行fun1中')
#     logging.warning('---日志信息，正在执行fun1')
# fun1()

# 问题2：如果其他函数也有类似的需求，怎么做？
# def fun1():
#     print('执行fun1中')
# def fun2():
#     print('执行fun2中')
# def loginfo(fun_name):
#     logging.warning('{}函数正在执行中'.format(fun_name.__name__))
# loginfo(fun1)
# loginfo(fun2)

# 上面的实现方法最终结果没问题，但是我们调用的时候并不是调用的实际业务逻辑而是调用了loginfo函数
# 案例：使用装饰器来解决执行函数添加日志，并且不改变调用方式的问题。
#
# def loginfo(fun_name):
#     def wrapper():
#         logging.warning('{}函数正在执行中'.format(fun_name.__name__))
#         return fun_name()
#     return wrapper
# @loginfo
# def fun1():
#     print('执行fun1中')
# @loginfo
# def fun2():
#     print('执行fun2中')
# fun1()
# fun2()



# 3、带参数的装饰函数
def loginfo(fun_name):
    def wrapper(*args,**kwargs):
        logging.warning('{}函数正在执行中'.format(fun_name.__name__))
        return fun_name(*args,**kwargs)
    return wrapper
@loginfo
def fun1():
    print('运行函数fun1()')
@loginfo
def fun2(name,addr):
    print('姓名：{}，地址：{}'.format(name,addr))
fun1()
fun2("Annona",'杭州')
# ②问题:后续执行的函数，日志打印还在先执行的函数的日志打印前面
# A）当同时调用fun1()和fun2()函数时，由于这两个函数都在同一个线程中执行，logging的输出操作和print的输出操作会共享同一个输出流对象，从而导致打印的日志信息和函数执行结果的顺序会混乱，出现异步打印的情况。
# B）为了避免这种异步打印的情况，可以使用多进程或多线程对这两个被装饰的函数进行并行调用，在多个进程或线程中各自维护自己的输出流对象，可以避免输出的顺序混乱的问题，进而避免异步打印的情况。