# 获取键盘上输入的数据 -- input(...)
name = input("请输入您的姓名:")
age = input("请输入您的年龄:")
print(f"欢迎您,{name},您的年龄为:{age}")

# 案例1: 模拟银行卡ATM取款
# 总金额
money = 10000
# 1. 输入密码
password = input("请输入您的银行卡密码:")
print(f"密码正确，您的密码为:{password}")

# 2. 输入取款金额
num = input("请输入您的取款金额")

# 3. 计算余额并输出
print(f"取款成功,当前余额：{money - int(num)}") # int(..)将其他类型转换为int类型

# 案例2:
# 根据用户输入的俩个数字 计算俩数之和 并输出到控制台
s1 = input("请输入您的第一个数字:")
s2 = input("请输入您的第二个数字:")
print(f"俩数之和为:{int(s1) + int(s2)}")




