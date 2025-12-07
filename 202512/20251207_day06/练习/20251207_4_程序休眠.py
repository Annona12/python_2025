# 开发者：Annona
# 创建时间：2025/12/7 18:06
# 实例009：暂停一秒输出
# 题目 暂停一秒输出,对于列表或者字符串切片的理解
# 程序分析 使用 time 模块的 sleep() 函数。
import time
for i in range(4):
    print(time.time())
    print(str(int(time.time()))[-2:])
    time.sleep(1)

a = '192820383'
print(a[-2:])