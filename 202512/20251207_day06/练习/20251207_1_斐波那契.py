# 开发者：Annona
# 创建时间：2025/12/7 18:04
# 题目 斐波那契数列。
# 程序分析 斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和
# 1、使用递归的方法实现
def fibonacci_queue(n):
    if n<=1:
        return n
    else:
        return fibonacci_queue(n-1)+fibonacci_queue(n-2)
f_queue = fibonacci_queue(14)
print(f_queue)

# 2、使用循环的方法实现
target = int(input())
res = 0
a,b = 1,1
# a = 1
# b = 1
for i in range(target-1):
    a,b = b,a+b
    # 相当于
    # temp_a = a
    # temp_b = b
    # a = temp_b
    # b = temp_a+temp_b

print(a)

