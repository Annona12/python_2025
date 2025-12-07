# 开发者：Annona
# 创建时间：2025/12/7 12:24
# 生成器的内容还需要再根据实际可能使用的场景学习一下
# 1、什么是迭代器
# 实现了如下的方法
# ①__iter()__:返回对象本身；
# ②__next__方法:这个方法每次返回迭代的值，在没有可迭代元素时，抛出StopIteration异常；
# 迭代器只能迭代一次，如果想要多次迭代，可以每次都迭代一个新对象；
class A:
    def __init__(self,n):
        self.index = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < self.n:
            value = self.index
            self.index+=1
            return  value
        else:
            raise StopIteration


a  = A(6)
for i in a:
    print(i)

# 2、什么是可迭代对象
# ①可以返回一个迭代器的对象，都是可迭代对象；
# ②或者说，__iter__方法返回一个迭代器，那么这个对象就是可迭代对象；
# ③一个类将迭代的细节交给另一个类，，这个类的实例就是一个可迭代对象；
