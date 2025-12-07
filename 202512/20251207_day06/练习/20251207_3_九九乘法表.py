# 开发者：Annona
# 创建时间：2025/12/7 18:05
# 实例008：九九乘法表
# 题目 输出 9*9 乘法口诀表。
# 程序分析 分行与列考虑，共9行9列，i控制行，j控制列。
# 1、倒三角
# for i in range(1,10):
#     for j in range(1,10):
#         if i<=j:
#             print('{}*{}={}'.format(i, j, i * j), end='  ')
#             if j == 9:
#                 print()
# 2、
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i, j, i * j), end=' ')
    print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%2ld '%(i,j,i*j),end='')
#     print()