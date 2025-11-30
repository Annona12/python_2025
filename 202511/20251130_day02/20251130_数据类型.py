# 开发者：Annona
# 创建时间： 11:14
# 2、python中常用的几个数据类型
# ①字典：dictionary，在python中使用dict表示字典类型，使用键值对的方式存储数据，是而可变的无序数据结构
# 创建字典的语法1:
from sys import orig_argv

dict1 = {'name':'Annona','age':25,'sex':'女生'}
print(dict1)
# 创建字典的语法2:
dict2 = dict(name='Annona',age=25,sex='女生')
print(dict2)
# 创建字典的语法3:
dict3 = dict([('name','Annona'),('age',25),('sex','女生')])
print(dict3)
# 增删改查字典内容
# 增
dict1['name1'] = '增加字典内容'
print(dict1)
# 改
dict1['age'] = '21'
print(dict1)
# 查
print(dict1['name'])
# 删除
del dict1['name']
print('del删除字典特定键值对内容后',dict1)
dict1.pop('name1')
print('pop删除字典特定键值对内容后',dict1)
dict1.clear()
print('清空删除字典特定键值对内容后',dict1)
del dict1
# print('del删除字典后',dict1)
# 字典的一些其他方法
print(dict2.keys())
print(dict2.values())
print(dict2.items())
li1=['name','age']
li2=['Annona',26]
print(dict(list(zip(li1,li2))))
# ②列表:可变长度的顺序序列数据结构，使用list表示列表
# 创建列表的语法一
list1=[1,34,5,6,2]
print(list1)
# 创建列表的语法二
list2=list('123827')
print(list2)
# 列表的增、删、改、查
# 增
list1.append('yu')
print(list1)
list1.insert(2,'hahha')
print(list1)
list1.extend('kjh')
print(list1)
# 删
list1.remove('hahha')
print(list1)
list1.pop(4)
print(list1)
# del list1[1]
# print(list1)
# list1.clear()
# print(list1)
# 改
list1[0]=99
print(list1)
# 查
print(list1[0])
print(list1[1:6:2])

# 列表的一些其他的常用方法
# 返回指定元素在列表中出现的次数
list4=[1,2,3,8,9,0,1,2,3,3,3,3]
print('3出现的次数：',list4.count(3))
# 查找某一个元素在例表中的最小索引
print('1的最小索引：',list4.index(1))
# 将列表翻转
list4.reverse()
print('列表翻转',list4)
list4.sort()
print('列表排序',list4)
# 列表切片获取
print('列表获取切片',list4[9:0:-1])
# ③元组:对于元组来说只有查看权限，不能被改变，是不可变序列，使用tuple表示元组类型,数据安全性较高，性能更好
# 当只有一个元素时，最后需要加上小逗号，元组的元素允许重复且可以时任何类型的值
# 定义元组语法一
tuple1=(1,2.3,4.5,8,3)
print(tuple1)
#定义元组语法二
tuple2=tuple([1,3,4,5,6,3])
print(tuple2)
# 查询元组的元素
print(tuple1[0])
# 元组的一些内置方法
print('最大值：',max(tuple1))
print('最小值：',min(tuple1))
print('长度：',len(tuple1))
print(sorted(tuple1,reverse=True))

# ④字符串:使用单引号、双引号、三引号引起来的内容都是字符串，字符串中有单引号时，可以使用双引号括起来；
# 字符串使用+拼接，多次输出同一样的字符使用*
# 字符串需要转换成数字或者浮点数必须要符合数字或者浮点数的规则
str1='123'
print(str1*3)
print(len(str1))
# ⑤集合：集合是无序、不重复的可变序列，使用ste表示集合类型
# 创建集合的语法一
set1 = {1,2,3,3,4,5}
print(set1)
# 创建集合的语法二
set2 =set('12345634')
print(set2)
# 集合的增删改查
# 增
set1.add(9)
print(set1)
set1.update('er')
print(set1)
# 删除
set1.remove(9)
print(set1)
set1.clear()
print(set1)
# ⑥数值
# 整型、浮点型、布尔、复数




