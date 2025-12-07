# 开发者：Annona
# 创建时间：2025/12/4 21:02

# 一、类的封装
# 函数在类中称之为方法：私有方法、公有方法；公有属性、私有属性
class Person:
    def __init__(self,name,sex,age,address,id):
        self.name = name
        self.sex = sex
        self.__age = age
        self.__address = address
        self.__id = id
    def work(self,type):
        print('我的工作{}'.format(type))
    def get_private_att(self):
        print('id:{},address:{},age:{}'.format(self.id,self.__address,self.__age))


class Student(Person):
    def __init__(self,name,sex,age,address,id,school):
        super().__init__(name,sex,age,address,id)
        self.school = school;

p = Person('name','sex','age','address','id')
print(p.name)
print(p.address)
# 二、类的继承
# 1、构造函数：一般作用是在初始化实例时可以自动调用，用于初始化实例的一些属性
class Animals:
    # 动物的一些公有的属性或者方法
    def __init__(self,species,name,sex,habits):
        self.species= species
        self.name = name
        self.sex = sex
        self.habits = habits
    def eat(self):
        print('我是{}，我正在吃东西'.format(self.name))
    def sleep(self):
        print('我的睡觉习惯是{}'.format(self.habits))
    def info(self):
        print('我是{}，我叫{}，是{}，我日常的习惯是{}'.format(self.species,self.name,self.sex,self.habits))

class Dog(Animals):
    def __init__(self,species,name,sex,habits,breed):
        super().__init__(species,name,sex,habits)
        self.breed = breed
    def eat(self,food):
        print('我喜欢吃{}'.format(food))
    def info(self):
        print('我是{}，我叫{}，是{}，我日常的习惯是{}'.format(self.species, self.name, self.sex, self.habits))

## 应用
a = Dog('狗','元宝','雄','汪汪','柯基')
a.info()
a.eat('骨头')
b = Animals('爬行','大型动物','雌雄同体','趴着')
b.eat()
b.sleep()


# 三、多态