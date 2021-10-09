from threading import Thread
import time

count = 500
i = 0
p = 18000 # 每个人的总金额3000



class cooker(Thread):
    username = ""
    num = 0

    def run(self) -> None:
        global p
        global count
        global i
        while True:
            if 0 <= i < count:
                self.num += 1
                i += 1
                print(self.username, "做了", self.num, "个")
                time.sleep(0.000001)
            elif i<0 or i>500:
                print(self.username, "休息三秒")
                print(self.username, "做了", self.num, "个")
                time.sleep(0.0001)

            elif p>= 18000:
                break



class person(Thread):
    name = ""
    p1=3000

    number = 0

    def run(self) -> None:
        global p

        while True:
            if 0 < self.p1<= 3000:
                self.number += 1
                p-=2
                print(self.name, "买了", self.number, "个", "还剩", self.p1-self.number*2, "元,蛋挞还剩", count - self.number, "个")
                self.p1-= 2
                # time.sleep(0.01)
            else:
                print(self.name, "买了", self.number, "个")
                print("钱消耗完了")

                break


p1 = cooker()
p2 = cooker()
p3 = cooker()
p1.username = "刘浩"
p2.username = "闫凯龙"
p3.username = "胖子"
p1.start()
p2.start()
p3.start()

p4 = person()
p5 = person()
p6 = person()
p7 = person()
p8 = person()
p9 = person()
p4.name = "孙佳伟"
p5.name = "心怡"
p6.name = "刘大傻"
p7.name = "刘二傻"
p8.name = "刘三傻"
p9.name = "刘四傻"
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()
