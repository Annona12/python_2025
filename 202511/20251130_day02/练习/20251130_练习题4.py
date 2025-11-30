# 开发者：Annona
# 创建时间： 16:45
# 实例004：这天第几天
# 题目 输入某年某月某日，判断这一天是这一年的第几天？
def isLeapYear(y):
    return y%400==0 or (y % 4 == 0 and y % 100 != 0)
DofM=[0,31,28,31,30,31,30,31,31,30,31,30]
res=0
year=int(input('Year:'))
month=int(input('Month:'))
day=int(input('day:'))
if isLeapYear(year):
    DofM[2]+=1
for i in range(month):
    res+=DofM[i]
res=res+day
print('这是今年的第%d天'%res)