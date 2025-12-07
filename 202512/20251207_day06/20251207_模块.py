# 开发者：Annona
# 创建时间：2025/12/7 12:20
# 1、模块的定义：
# 模块是一个包含所有我定义的函数和变量的文件，后缀名字是.py，引用函数模块之后，后续都可以使用模块中的各个功能

# 2、模块的分类：标准库、开源库、自定义模块,如果需要跨模块（不同的python文件中使用）需要先导入模块，导入顺序按照：内置库、第三方库、自定义模块
# ①标准模块(内置模块)：time、sys、os、date、json、random
# ② 开源模块(第三方库)：openpyxl、xlrd、xlwt、flask
# ③自定义库

# 3、导入模块的而语法
# ① 使用import 导入：import 模块名 ；调用:模块名.函数名()
# ② 使用from... import ... ; 导入：from 模块名 import 函数名，函数名1，函数名2或者类名；调用：函数名()
# ③ 使用from... import *(一般不推荐使用)，导入模块中的所有函数，当两个模块中有相同的函数名，后面导入的会覆盖前面导入的内容
# 案例：
# 1. 获取当前的时间戳
# 2. 获取当前时间的格式化的字符串
# 3. 获取当前的结构化时间，单个获取当前年、
# 月、日
import time
print("当前的时间戳:",time.time())
#格式化当前时间
print("当前日期的格式化日期为：",time.strftime("%Y-%m-%d"))
print("当前日期的格式化日期为：",time.strftime("%Y-%m-%d %H:%M:%S"))
#结构化时间
print("当前结构化时间为:",time.localtime())
print("当前结构化时间为:",time.localtime().tm_year)

time1 = time.time()
print(time1)
# python的if __name__=='__main__'的含义
# ①当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行;
# ②当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行;