# 开发者：Annona
# 创建时间：2025/12/7 18:08
# 实例010：给人看的时间
# 题目 暂停一秒输出，并格式化当前时间。
import time

for i in range(4):
    print(time.localtime())
    print(time.asctime(time.localtime()))
    print(time.ctime())
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)

