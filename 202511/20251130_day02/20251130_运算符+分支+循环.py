# 开发者：Annona
# 创建时间： 16:04
# 1、运算符
# 算数运算符：+，-，*，/，%，//，**，
# 比较运算符：>、<，==，!=，>=，<=
# 赋值运算符：=，+=，-=，*=，/=， %=，**=，//=
# 逻辑运算符：逻辑运算符：一般用于判断、循环：and , or , not；not>and>or
# 成员运算符：in/not in
# ①算数优先级优先级大于比较运算符
# ②比较运算符优先级大于逻辑运算符
# ③逻辑运算符内部三个优先级 not > and > or

# 2、分支:单项分支，双项分支，多项分支和巢状分支
# 单分支
name = input('请输入用户名:')
if name == 'admin':
    print('管理员账户')
# 双分支1
username=input('请输入用户名：')
if username == 'admin':
    print("管理员登录")
else:
    print("游客登录")
# 多分支
age=int(input("请输入年龄："))
if 4 <= age <= 11:
    print("儿童票")
elif 12 <= age <= 59:
    print("成人票")
else:
    print("不要买票")
# 巢状分支
high=float(input("请输入你的身高："))
if high >= 178:
    income = float(input("请输入你的工资："))
    if income >=100:
        print("高富帅")
    else:
        print("你很高，但是并不富有")
else:
    print("你不符合我的要求")
# 3、循环:先对条件进行判断，条件结果为False，则不会进入循环体；条件结果为True，则进入执行循环体中的所有代码，循环体中代码执行完之后，会再次回到 while条件判断的位置，再次判断此时条件，如果为True，则循环体中的代码会再执行一遍，然后再回到while条件判断,直到条件为False，跳过循环体中代码，跳出while循环
# ①while后面的条件最好不为恒定值
num=0
while num<3:
    print('num=',num)
    num+=1
# ②while后面的条件为恒定值引入continue和break
# 执行过程：while循环体一旦遇到break，则立即终止while循环，从break的位置直接跳出while，去执行while之后的代码。
while True:
    print('hahha')
    break
    print('hahah1')

# 执行过程：在循环体中遇到continue之后，本次循环不再执行continue下面的代码，直接回到while条件判断的位置，开始下一次循环。
num=1
while True:
    print("hrllo world!")
    if num<3:
        num+=1
        continue
        num+=1
    else:

        break