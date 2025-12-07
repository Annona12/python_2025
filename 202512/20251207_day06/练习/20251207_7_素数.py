# 开发者：Annona
# 创建时间：2025/12/7 18:10
# 实例012：100到200的素数
# 题目 判断101-200之间有多少个素数，并输出所有素数。
# 程序分析 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。用else可以进一步简化代码.
import math


def is_prime_sqrt(n):
    """优化方法：只需检查到√n"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):  # 只检查奇数
        if n % i == 0:
            return False
    return True


# 测试
print(is_prime_sqrt(47))  # True
print(is_prime_sqrt(100))  # False