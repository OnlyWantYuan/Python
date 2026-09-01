"""
1.while循环的语法结构

while 条件表达式:    --->返回布尔值True | False
    循环体语句1
    循环体语句2
    ...

while 条件表达式:
    循环体语句1
    循环体语句2
    ...
    条件为False,循环正常结束时执行      注:可选

2.while循环的注意事项
    条件表达式的结果为布尔类型
    通过空格缩进表示层级关系
    规划好循环终止的条件，否则将陷入无限循环(死循环)
"""

# 案例1:
# num = 0
# while num < 10:     # num < 10 循环的条件
#     print("人生苦短,我用Python")      # 条件成立时,执行的循环体逻辑
#     num += 1
# else:
#     print("循环正常结束,执行完毕")    # 条件不成立循环结束时,执行的代码
# 如果条件一直满足，就会无限循环(死循环)

# 案例1:计算1-100之间所有偶数之和
# total = 0
# num = 1
#
# while num <= 100:
#     if num % 2 == 0:
#         total += num
#     num += 1
# print(f"和为{total}")

# total = 0
# num = 2
#
# while num <= 100:
#     total += num
#     num += 2
# print(f"和为{total}")





