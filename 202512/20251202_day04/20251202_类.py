# 开发者：Annona
# 创建时间：2025/12/2 20:46
# 1、类的继承
# ①单继承
# 继承的逻辑和规则总结：
# A、类的构造方法__init__()：创建实例时会自动调用；可以用来初始化类的实例，self表示实例的本身，也可以是this,但是最好还是使用self
class Animals:
    def __init__(self,name,species):
        self.name=name;
        self.species=species;
        self.__private_attr = "Animal私有"
        print('我的名字是{},我的科目是{}'.format(self.name,self.species))
    def eat(self):
        print(f"{self.name}正在吃东西")
    def info(self):
        return f"{self.name}是{self.species}"

class Dog(Animals):
    def __init__(self,name,breed):
        super().__init__(name,'犬科')
        self.breed=breed
    def speak(self):
        print('汪汪！！！')

    def eat(self):
        super().eat()
        print('我还比较爱吃骨头')
    def info(self):
        super().info()
        return f"我是{self.breed}"
# a = Animals('猫科目','雌性')
d = Dog('元宝','男')
d.info()

# ②多继承
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

# 2、多态
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

# 3、封装
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