# 开发者：Annona
# 创建时间： 16:45
# 实例005：# 三数排序
# 题目 输入三个整数x,y,z，请把这三个数由小到大输出。
# x= int(input('请输入第一个数'))
# y= int(input('请输入第二个数'))
# z= int(input('请输入第三个数'))
# print(sorted((x,y,z)))
raws=[]
for i in range(3):
    x = input('int%d: '%(i))
    raws.append(x)
print(sorted(raws))

raw=[]
for i in range(3):
    x=int(input('int%d: '%(i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)