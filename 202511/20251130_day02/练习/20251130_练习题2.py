# 开发者：Annona
# 创建时间： 16:45
# 实例002：“个税计算”
# 题目 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
# money = int(input('请输入您当前的月利润：'))
# sum = 0
# if money<=10:
#     sum = money*0.10
#     print('您当前的奖金总数为：',sum)
# elif 10<money<20:
#     sum = 10*0.1+(money-10)*0.075
#     print('您当前的奖金总数为：', sum)
# elif 20<=money<40:
#     sum = 10*0.1+10*0.075+(money-20)*0.05
#     print('您当前的奖金总数为：', sum)
# elif 40<=money<60:
#     sum = 10*0.1+10*0.075+20*0.05+(money-40)*0.03
#     print('您当前的奖金总数为：', sum)
# elif 60<=money<100:
#     sum = 10*0.1+10*0.075+20*0.05+20*0.03+(money-60)*0.015
#     print('您当前的奖金总数为：', sum)
# else:
#     sum = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40*0.015+(money - 60) * 0.01
#     print('您当前的奖金总数为：', sum)

profit=int(input('Show me the money: '))
bonus=0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)
