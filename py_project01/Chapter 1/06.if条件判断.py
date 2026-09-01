# 1.if条件判断的基本格式
# if 要判断的条件:
# 条件成立时,要执行的对应操作1
# 条件成立时,要执行的对应操作2

# if条件判断案例1: 如果分数超过680,我就去清华读书
# score = int(input("请输入您的分数"))
# if score > 680:
#     print("欢迎你来清华读书")
#     print("也恭喜你即将踏入精彩的大学生活")
# if score <= 680:
#     print("抱歉分数不够")

# 2.if语句的注意事项
# 判断条件的结果一定是布尔值
# 不要忘记判断条件后的冒号(:)
# if语句里面的代码块,需要在前方缩进空格(建议四个空格,Tab),通过缩进来描述代码的层级关系(归属)

# if案例:结合前面学习的输入输出及if条件判断的知识,完成B站登录功能的实现(正确的账号和密码分别为18888888888/666888)
# 正确的账号和密码:
# ok_account = "18888888888"
# ok_password = "666888"

# 1.接收用户输入的账号和密码
# account = input("请输入您的B站账号:")
# password = input("请输入您的B站密码:")

# 2.判断账号和密码是否全部正确,如果都正确,则登录成功,进入B站首页
# if account == ok_account and password == ok_password:
#     print("登录成功")
#     print("欢迎进入B站首页")

# 3.判断账号和密码是否有错误,如果有任何一个错误,则登录失败,提示错误信息
# if account != ok_account or password != ok_password:
#     print("登录失败")
#     print("账号或密码有误")

# if语句进阶---if...else...
# 正确的账号和密码:
# ok_account = "18888888888"
# ok_password = "666888"

# 1.接收用户输入的账号和密码
# account = input("请输入您的B站账号:")
# password = input("请输入您的B站密码:")

# 2.判断账号和密码是否全部正确,如果都正确,则登录成功,进入B站首页
# if account == ok_account and password == ok_password:
#     print("登录成功")
#     print("欢迎进入B站首页")
# else:
#     print("登录失败")
#     print("账号或密码有误")

# 案例1.:根据用户输入的年份,判断这一年是闰年还是平年(非整百年份,且能被4整除的年份是闰年;整百年份(如1900,2000)必须被400整除才是闰年
# year = int(input("请输入年份"))

# 如果是非整百年份,且能被4整除就是闰年;整百年份,必须被400整除才是闰年
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# 1.if...else语句的语法
# if要判断的条件:
#    条件成立时,执行对应的操作1
# else:
#    条件不成立时,执行的操作2

# 2.if...else语句注意事项
# else是不需要条件判断的,当if条件不成立时,else就执行了
# else代码块,也需要使用空格缩进(建议4个空格)

# 作业1:根据用户输入的数字,判断该数字是奇数还是偶数
# num = int(input("请输入数字"))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")

# 作业2:根据用户输入的年龄,判断用户是否已经成年
# age = int(input("请输入年龄"))
# if age >= 18:
#     print("您是成年人")
# else:
#     print("您是未成年人")

# 作业3:根据用户输入的考试分数,判断该分数成绩是否及格
# power = float(input("请输入您的考试分数"))
# if power >= 60:
#     print("您的成绩已及格")
# else:
#     print("您的成绩不及格")

# if语句进阶---if...elif...else
# 案例1:根据用户输入的数字,判断该数字是正数还是负数还是0
# n = float(input("请输入数字"))
# if n > 0:
#     print(f"{n}为正数")
# elif n < 0:
#     print(f"{n}为负数")
# else:
#     print(f"{n}既不为正数也不为负数")

# 案例2:根据输入用户名和密码进行登录系统 ---> admin/666888   root/114514    zhangsan/123456
# username = input("请输入用户名")
# password = input("请输入密码")
#
# if username == "admin" and password == "666888":
#     print("登录成功")
# elif username == "root" and password == "114514":
#     print("登录成功")
# elif username == "zhangsan" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败,用户名或密码错误")

# 作业1:根据输入的考试成绩,判断成绩等级
# 大于等于85分为优秀    60-84为及格    否则就是不及格
# num1 = float(input("请输入您的考试成绩"))
# if num1 >= 85:
#     print("您的成绩为优秀")
# elif 60 <= num1 < 85:
#     print("您的成绩为及格")
# else:
#     print("您的成绩不及格")

# 作业2:购物折扣计算:根据输入的购物车的商品总额,以及如下的折扣规则,计算实际应付金额
# 金额 >= 500: 8折     300 <= 金额 < 500: 9折     100 <= 金额 < 300: 95折     金额 < 100: 无折扣
# amount = float(input("请输入商品总额"))
# if amount >= 500:
#     print("您可享受8折优惠,实付金额为:",amount * 4/5)
# elif 300 <= amount < 500:
#     print("您可享受9折优惠,实付金额为:",amount * 9/10)
# elif 100 <= amount < 300:
#     print("您可享受95折优惠,实付金额为:",amount * 19/20)
# else:
#     print("您的商品总额不足100无法享受折扣")

"""
案例3:三角形类型判断:根据输入的三个边的边长(正整数),判定是等边三角形,等腰三角形,普通三角形,还是不能构成三角形
    1.构成三角形的条件:俩边之和大于第三边
    2.三角形判定规则:
        三个边都相等:等边三角形
        俩个边相等:等腰三角形
        三个边都不相等:普通三角形
"""
# 1.接受输入的三角形三个边的边长
# a = int(input("请输入第一条边"))
# b = int(input("请输入第二条边"))
# c = int(input("请输入第三条边"))

# 2.判断三角形类型---pass是一个空语句,起到一个语法占位的作用
# if a + b > c and a + c > b and b + c > a: # 条件成立,构成三角形
#     if a == b and b == c:
#         print(f"{a},{b},{c}这三个边长构成等边三角形")
#     elif a == b or a == c or b == c:
#         print(f"{a},{b},{c}这三个边长构成等腰三角形")
#     else:
#         print(f"{a},{b},{c}这三个边长构成普通三角形")
# else:
#     print(f"{a},{b},{c}这三个边长不能构成三角形!!!")

# 作业1:
# num = float(input("请输入用电度数"))
# if num < 0:
#     print("度数不能为0!请重新输入")
# elif num <= 2880:
#     print(f"您的年度用电度数为{num},用电电费为:",num * 0.4883,"元")
# elif num <= 4800:
#     print(f"您的年度用电度数为{num},用电电费为:", 2880 * 0.4883 + (num - 2880) * 0.5383,"元")
# else:
#     print(f"您的年度用电度数为{num},用电电费为:",2880 * 0.4883 + 1920 * 0.5383 + (num - 4800) * 0.7883,"元")