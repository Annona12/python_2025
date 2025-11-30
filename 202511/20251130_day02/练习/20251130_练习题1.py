# 开发者：Annona
# 创建时间： 15:16
# 实例001：数字组合
# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 最基础的方法
total = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (j!=k) and (i!=k):
                print(i,j,k)
                total+=1
print('总共有%d种组成方法',total)

# 解法二：使用itertools