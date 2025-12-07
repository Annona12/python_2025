# 开发者：Annona
# 创建时间：2025/12/7 11:09
# 类的继承
# 1、父类中如果存在与子类中一样的方法名字，会被子类的方法覆盖掉；
# 2、子类实例调用方法时，会优先调用子类中的方法，只有当子类中的方法没有实现时，才会去父类中找同名的方法
# 类的多态
class Aninals:
    def __init__(self,name):
        self.name = name
        print('我是{}'.format(self.name))

    def speak(self):
        pass

class Dog(Aninals):
    def __init__(self,name,speed):
        super().__init__(name)
        self.speed = speed
        print('我是{}品种'.format(self.speed))

    def speak(self):
        print('汪汪')

class Cat(Aninals):
    def __init__(self,name,speed):
        super().__init__(name)
        self.speed = speed
        print('我是{}品种'.format(self.speed))

    def speak(self):
        print('喵喵')
cat = Cat('元宝','布偶')
cat.speak()
dog = Dog('元宝','巴哥')
dog.speak()
