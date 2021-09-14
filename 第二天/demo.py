'''
    猜数字：
    需求：
        1.猜的数字是系统产生，不是自己定义
            使用random随机数技术来获取随机数
        2.键盘输入
            input("提示")
        3.循环
            while条件循环
            开始，结束，自增，任务
        4.判断
            if 判断条件  elif 判断条件.......else
    范围：0~150
    猜10次！
    如果输入大了：温馨提示：大了
    如果输入小了：温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为xxxx。
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
num = random.randint(0,10)
a = 5000
print("")
c = int(input("请输入1开始游戏:"))
print("您当前的金额为:", a)
b = int(input("您需要充值的金额:"))
if b==1000:
    b+=b*0.01
    e=a+b
    print("已充值:",b,"您当前余额为：",e)
elif b==2000:
    b+=b*0.02
    e=a+b
    print("已充值:",b,"您当前余额为：",e)
elif b==3000:
    b+=b*0.03
    e=a+b
    print("已充值:",b,"您当前余额为：",e)
elif b==5000:
    b+=b*0.05
    e=a+b
    print("已充值:",b,"您当前余额为：",e)
elif b==10000:
    b+=b*0.1
    e=a+b
    print("已充值:",b,"您当前余额为：",e)
else:
    print("请输入的金额必须为1000的倍数")

i = 0
while i < 10:

    if c == 1:
        print("游戏开始")
    else:
        print("游戏结束")
        break
    number = int(input("请输入您要猜的数："))
    #number = int(number)
    if number > num:
        e=e-500
        print("大了！您共有10次机会，此次是第",i+1,"次","剩余金币为",e)
    elif number < num:
        e-=500
        print("小了！您共有10次机会，此次是第",i+1,"次""剩余金币为",e)
    else:
        print("恭喜猜中！本次数字为：",num,"恭喜金币增加",3000)
        print("您当前账户余额为:", e+3000)
        break
    i= i + 1








