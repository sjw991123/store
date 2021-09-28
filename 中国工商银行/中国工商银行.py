import random
import pymysql

# 数据库
bank = {}
bankname = "中国工商银行北京昌平支行"  # 银行名称

host = "localhost"
user = "root"
password = "123456"
database = "bank"


def update(sql, param):  # 增删改
    con = pymysql.connect(host=host, user=user, password=password, database=database)  # 创建控制台
    kongzhi = con.cursor()  # 创建控制台
    kongzhi.execute(sql, param)  # 执行sql语句
    con.commit()  # 提交数据
    kongzhi.close()  # 关闭资源
    con.close()


def select(sql, param, mode="all", size=0):  # 查询
    con = pymysql.connect(host=host, user=user, password=password, database=database)  # 创建控制台
    kongzhi = con.cursor()  # 创建控制台
    kongzhi.execute(sql, param)  # 执行sql语句
    con.commit()  # 提交数据
    if mode == "all":
        return kongzhi.fetchall()
    elif mode == "one":
        return kongzhi.fetchone()
    elif mode == "many":
        return kongzhi.fetchmany(size)
    kongzhi.close()  # 关闭资源
    con.close()


def getRandom():  # 随机字符
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string = string + li[int(random.random() * len(li))]
    return string


# 用户输入开户信息
def userkaihu():
    name = input("请输入您的姓名：")
    ID = input("请输入您的身份证号码：")
    password = input("请设置您的密码：")
    country = input("请输入您所在的省份：")
    province = input("请输入你所在的城市：")
    street = input("请输入您所在的街道：")
    House = input("请输入您的门牌号：")
    money = int(input("请输入您的预存款："))

    account = getRandom()
    fhz = bankkaihu(name, ID, password, country, province, street, House, money, account)
    if fhz == 1:
        print("开户成功！以下是您的个人信息：")
        info = '''
        -------------------个人信息------------------
                用户名:%s                                  
                密码：******                               
                账号:%s                                    
                身份证号：%s
                地址：
                    省份:%s
                    城市:%s
                    街道：%s
                    门牌号:%s
                余额：%s
                开户行:%s
        --------------------------------------------
                            '''
        print(info % (name, account, ID, country, province, street, House, money, bankname))
    elif fhz == 2:
        print("当前用户已存在，请到其他银行办理！")
    elif fhz == 3:
        print("当前数据库已满，请联系银行工作人员！")


# 银行开户
def bankkaihu(name, ID, password, country, province, street, House, money, account):
    # 查询数据库表数据是否大于100
    sql = "select count(*) from bank "
    parm = []  # 用不到，但必须有，否侧报错
    data = select(sql, parm)
    if data[0][0] >= 100:
        return 3
    # 查询数据库里有没有重读ID
    sql = "select ID from bank where 'money' >= %s"
    param = [0]
    data = select(sql, param, mode="all")
    for i in data:  # 返回字典里的所有键
        if ID in i:  # 如果ID在数据库里，返回2
            return 2
    # 条件符合 把用户信息存到数据库
    sql = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, ID, name, password, country, province, street, House, money, bankname]
    update(sql, param)
    return 1


# 存钱
def bankcunqian(account, money):
    # 查询是否有该账号
    sql = "select * from bank where account = %s"
    param = [account]
    data = select(sql, param, mode="all")
    if not data:  # 如果不存在返回1
        return 1
    return 0  # 如果存在返回0


def cunqian():
    account = input("请输入您的账号：")
    money = int(input("请输入您的存款金额："))
    bianhao = bankcunqian(account, money)
    if bianhao == 1:
        print("账号不存在！")
    elif bianhao == 0:
        # 账号存在的情况下 存钱
        sql = "update bank set money = money + %s  where account = %s"
        param = [money, account]
        update(sql, param)
        # 存款成功后查询余额
        sql = "select money from bank where account = %s"
        param = [account]
        data = select(sql, param, mode="all")
        print("存款成功，您的当前余额为：￥", data[0][0])


# 取钱
def bankqvkuan(account, password, money):
    # 查询有没有这个账号
    sql = "select * from bank where account = %s"
    param = [account]
    data = select(sql, param, mode="all")
    if not data:  # 如果不存在返回1
        return 1
    # 判断密码对不对
    sql = "select * from bank where password = %s and account = %s"
    param = [password, account]
    data = select(sql, param, mode="all")
    if not data:  # 如果不存在返回2
        return 2
    # 判断余额
    sql = "select money from bank where account = %s"
    param = [account]
    data = select(sql, param, mode="all")
    if money > data[0][0]:
        return 3
    return 0


def qvqian():
    account = input("请输入您的账号：")
    password = input("请输密码：")
    money = int(input("请输入取款金额："))
    bianhao = bankqvkuan(account, password, money)
    if bianhao == 1:
        print("账号不存在！")
    elif bianhao == 2:
        print("密码错误！")
    elif bianhao == 3:
        print("余额不足！")
    elif bianhao == 0:
        # 账号密码都对的情况下进行取款
        sql = "update bank set money = money - %s where account = %s"
        param = [money, account]
        update(sql, param)
        # 取款成功，查询剩余余额
        sql = "select money from bank where account = %s"
        param = [account]
        data = select(sql, param, mode="all")
        print("取款成功，您的当前余额为：￥", data[0][0])


# 查询
def bankchaxun(account, password):
    # 查询是否有该账号
    sql = "select * from bank where account = %s"
    param = [account]
    data = select(sql, param, mode="all")
    if not data:
        return 1
    # 验证密码是否正确
    sql = "select * from bank where password = %s and account = %s"
    param = [password, account]
    data = select(sql, param, mode="all")
    if not data:
        return 2
    return 0


def chaxun():
    account = input("请输入您要查询的账号：")
    password = input("请输入密码：")
    bianhao = bankchaxun(account, password)
    if bianhao == 1:
        print("账号不存在！")
    elif bianhao == 2:
        print("密码错误！")
    elif bianhao == 0:
        # 查询账号信息
        sql = "select * from bank where account = %s"
        param = [account]
        data = select(sql, param, mode="all")
        print("查询成功，以下是您的个人信息！")
        info = '''
        -------------------个人信息------------------
                用户名:%s                                  
                密码：******                               
                账号:%s                                    
                身份证号：%s
                地址：
                    省份:%s
                    城市:%s
                    街道：%s
                    门牌号:%s
                余额：%s
                开户行:%s
        --------------------------------------------
        '''
        print(info % (
        data[0][2], data[0][0], data[0][1], data[0][4], data[0][5], data[0][6], data[0][7], data[0][8], data[0][9],))


# 转账
def bankzhuanzhang(account1, account2, password, money, lei):
    if lei == "1":
        # 判断转出账号是否存在
        sql = "select * from bank where account = %s"
        param = [account1]
        data = select(sql, param, mode="all")
        if not data:  # 如果不在
            return 1
        # 判断密码对不对
        sql = "select * from bank where account = %s and password = %s"
        param = [account1, password]
        data = select(sql, param, mode="all")
        if not data:  # 如果不在
            return 2
        # 判断转入账号是否存在
        sql = "select * from bank where account = %s"
        param = [account2]
        data = select(sql, param, mode="all")
        if not data:  # 如果不在
            return 3
        # 剩余判断金额是否>=转出金额
        sql = "select money from bank where account = %s"
        param = [account1]
        data = select(sql, param, mode="all")
        if money > data[0][0]:
            return 4
        if account1 == account2:
            return 5
        return 0
    elif lei == "2":
        # 判断转出账号是否存在
        sql = "select * from bank where account = %s"
        param = [account1]
        data = select(sql, param, mode="all")
        if not data:  # 如果不在
            return 1
        # 判断密码对不对
        sql = "select * from bank where account = %s and password = %s"
        param = [account1, password]
        data = select(sql, param, mode="all")
        if not data:  # 如果不在
            return 2
        # 判断转入账号是否存在
        sql = "select * from abcbank where account = %s"
        param = [account2]
        data = select(sql, param, mode="all")
        if not data:  # 如果不在
            return 3
        # 剩余判断金额是否>=转出金额
        sql = "select money from bank where account = %s"
        param = [account1]
        data = select(sql, param, mode="all")
        if money > data[0][0]:
            return 4
        if account1 == account2:
            return 5
        return 0
    else:
        print("输入错误！")


def zhuanzhang():
    lei = input("请选择您的转账类型，\n1.普通转账\n2.跨行转账\n")
    account1 = input("请输入您的转出账号：")
    password = input("请输入密码：")
    account2 = input("请输入转入账号：")
    money = int(input("请输入您的转账金额："))
    bianhao = bankzhuanzhang(account1, account2, password, money, lei)
    if bianhao == 1:
        print("转出账号不存在！")
    elif bianhao == 2:
        print("密码错误！")
    elif bianhao == 3:
        print("转入账号不存在！")
    elif bianhao == 4:
        print("余额不足！")
    elif bianhao == 5:
        print("转入账号和转出账号不能相同！")
    elif bianhao == 0:
        if lei == "1":
            # 进行转账,转出账户减掉金额
            sql = "update bank set money = money - %s where account = %s"
            param = [money, account1]
            update(sql, param)
            # 转入账户加金额
            sql = "update bank set money = money + %s where account = %s"
            param = [money, account2]
            update(sql, param)
            # 转账成功，查询余额
            sql = "select money from bank where account = %s"
            param = [account1]
            data = select(sql, param, mode="all")
            print("转账成功，转出账户余额为：￥", data[0][0])
            # 转账成功，查询转入账户余额
            sql = "select money from bank where account = %s"
            param = [account2]
            data = select(sql, param, mode="all")
            print("转账成功，转入账户余额为：￥", data[0][0])
        elif lei == "2":
            # 进行转账,转出账户减掉金额
            sql = "update bank set money = money - %s where account = %s"
            param = [money, account1]
            update(sql, param)
            # 转入账户加金额
            sql = "update abcbank set money = money + %s * 0.998 where account = %s"
            param = [money, account2]
            update(sql, param)
            # 转账成功，查询转出账户余额
            sql = "select money from bank where account = %s"
            param = [account1]
            data = select(sql, param, mode="all")
            print("转账成功，转出账户余额为：￥", data[0][0])
            # 转账成功，查询转入账户余额
            sql = "select money from abcbank where account = %s"
            param = [account2]
            data = select(sql, param, mode="all")
            print("转账成功，转入账户余额为：￥", data[0][0])


# 首页面
def welcom():
    print("-------------------------------------------")
    print("-            中国工商银行账户管理系统          -")
    print("-------------------------------------------")
    print("- 1.开户                                   -")
    print("- 2.存钱                                   -")
    print("- 3.取钱                                   -")
    print("- 4.转账                                   -")
    print("- 5.查询                                   -")
    print("- 6.Bys!                                  -")
    print("-------------------------------------------")


while True:
    welcom()  # 打印首页面
    bianhao = input("请输入您要办理的业务编号：")
    if bianhao == "1":
        userkaihu()
    elif bianhao == "2":
        cunqian()
    elif bianhao == "3":
        qvqian()
    elif bianhao == "4":
        zhuanzhang()
    elif bianhao == "5":
        chaxun()
    elif bianhao == "6":
        print("欢迎下次使用！")
        break
    else:
        print("输入有误，请重新输入！")
