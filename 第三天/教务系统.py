
import random
names = ["刘浩","胖子","富有","瘦子"]
print("------------------欢迎来到教务管理系统---------------------")
while True:
    chose = input("请输入教务业务(1.随机点名， 2.随机处罚)>>>:")
    if chose == "1":
        index = random.randint(0,len(names)-1)
        print(names[index])
    elif chose == "2":
        num = random.randint(0,200)
        print("恭喜您，你被处罚了",num,"遍！")
    elif chose == "q"  or chose  == 'Q':
        print("欢迎下次使用！再见！")
        break
    else:
        print("输入错误，请重新输入！")























