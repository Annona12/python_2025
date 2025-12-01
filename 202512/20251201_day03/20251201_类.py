# 开发者：Annona
# 创建时间：2025/12/1 22:21
# 类是一种用户定义的数据类型，它代表着一类具有相同属性和方法的对象集合
# 实例是类的具体实现，是类的具体的个体，可以使用类定义的属性和方法
# 在类名后面加括号创建实例
# 类的构造方法__init()__
# 可以用来初始化类的实例，self表示实例的本身，也可以是this,但是最好还是使用self
class Cat:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
mycat = Cat('元宝','男')

# Python类的属性有公有属性、私有属性、实例属性、静态属性
# 公有属性
# 指没有加前缀双下划线__的属性，可以在类内外被访问，也可以被继承和重写。
# 可以通过实例的self.属性名访问和修改
# ②私有属性
# 指加了前缀双下划线__的属性，只能在类内被访问和修改，而在类外部无法访问或修改。
# 属性名字前面加"__"，无法通过实例调用，只能通过内部的方法进行访问和修改
# ③实例属性
# 指定义在 init 方法中，以 self.属性名 的形式定义的属性，每个实例都独立拥有一个自己的实例属性，它们随实例创建和销毁。
# ④静态属性
# 指在类下直接定义的属性，可以使用类名直接访问，它们是类的属性，每个实例都共享一个静态属性。
# class Person:
#     species = 'human'  # 定义类属性
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_species(self):  # 定义实例方法
#         return self.species
# class Student:
#     def __init__(self, name, age):
#         self.__name = name  # 私有属性
#         self.__age = age  # 私有属性
#     def get_name(self):
#         return self.__name
#     def set_age(self, age):
#         self.__age = age
# Python 中的封装、继承、多态详解
# 1、封装
class BankAccount:
    def __init__(self, account_holder, balance):
        # 私有属性（名称前加双下划线）
        self.__account_holder = account_holder
        self.__balance = balance
        self.__transactions = []

    # 公有方法 - 外部接口
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"存入: {amount}")
            print(f"成功存入 {amount} 元")
        else:
            print("存款金额必须大于0")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"取出: {amount}")
            print(f"成功取出 {amount} 元")
        else:
            print("余额不足或金额无效")

    # Getter方法 - 提供受控的访问
    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder

    # 只读属性 - 更Pythonic的方式
    @property
    def balance(self):
        return self.__balance

    @property
    def account_holder(self):
        return self.__account_holder

    # 只显示最近的交易记录
    @property
    def recent_transactions(self):
        return self.__transactions[-5:] if len(self.__transactions) > 5 else self.__transactions


# 使用示例
account = BankAccount("张三", 1000)
account.deposit(500)  # 成功存入 500 元
account.withdraw(200)  # 成功取出 200 元

print(account.get_balance())  # 1300
print(account.balance)  # 1300 (使用属性访问)

# 无法直接访问私有属性
# print(account.__balance)    # AttributeError
# 但Python的私有只是名称修饰，实际上可以通过 _类名__属性名 访问（不推荐）
print(account._BankAccount__balance)  # 1300# 2、继承

# 2、继承：继承允许一个类（子类）获取另一个类（父类）的属性和方法。
# ①单继承
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.__private_attr = "Animal私有"

    def speak(self):
        raise NotImplementedError("子类必须实现此方法")

    def eat(self):
        print(f"{self.name}正在吃东西")

    def info(self):
        return f"{self.name}是{self.species}"


# 子类继承父类
class Dog(Animal):
    def __init__(self, name, breed):
        # 调用父类的构造方法
        super().__init__(name, "犬科")
        self.breed = breed

    # 方法重写
    def speak(self):
        return "汪汪！"

    # 扩展父类方法
    def info(self):
        base_info = super().info()
        return f"{base_info}, 品种是{self.breed}"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "猫科")
        self.color = color

    def speak(self):
        return "喵喵！"

    def climb_tree(self):
        print(f"{self.name}正在爬树")


# 使用继承
dog = Dog("旺财", "金毛")
cat = Cat("小花", "橘色")

print(dog.info())  # 旺财是犬科, 品种是金毛
print(dog.speak())  # 汪汪！
print(cat.info())  # 小花是猫科
print(cat.speak())  # 喵喵！
cat.climb_tree()  # 小花正在爬树


class Flyable:
    def __init__(self, max_altitude=1000):
        self.max_altitude = max_altitude

    def fly(self):
        print(f"飞行中，最大高度{self.max_altitude}米")


class Swimmable:
    def __init__(self, max_depth=50):
        self.max_depth = max_depth

    def swim(self):
        print(f"游泳中，最大深度{self.max_depth}米")


# 多重继承
class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
        # 手动初始化所有父类
        Flyable.__init__(self, 500)
        Swimmable.__init__(self, 10)

    def quack(self):
        print(f"{self.name}: 嘎嘎！")


# MRO（方法解析顺序）
print(Duck.__mro__)
# (<class '__main__.Duck'>, <class '__main__.Flyable'>, <class '__main__.Swimmable'>, <class 'object'>)

duck = Duck("唐老鸭")
duck.fly()  # 飞行中，最大高度500米
duck.swim()  # 游泳中，最大深度10米
duck.quack()  # 唐老鸭: 嘎嘎！



# 3、多态：多态允许不同类的对象对同一消息做出不同的响应
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        """计算工资 - 父类定义接口"""
        raise NotImplementedError("子类必须实现此方法")

    def work(self):
        return "工作中..."


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

    def work(self):
        return f"{self.name}经理正在管理团队"


class Developer(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def work(self):
        return f"{self.name}开发正在编写代码"


class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

    def work(self):
        return f"{self.name}实习生正在学习"


# 多态性的体现
def process_employees(employees):
    total_salary = 0
    for emp in employees:
        print(emp.work())
        salary = emp.calculate_salary()
        print(f"{emp.name}的工资: {salary}")
        total_salary += salary
    print(f"总工资支出: {total_salary}")
    return total_salary


# 创建不同类型的员工
employees = [
    Manager("张三", 10000, 5000),
    Developer("李四", 200, 160),
    Developer("王五", 180, 180),
    Intern("赵六", 3000)
]

process_employees(employees)