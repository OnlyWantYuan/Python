# 模式匹配 match...case...
# 执行流程:
# 1.首先计算match指定的表达式的值
# 2.从上到下依次和case后面的值进行匹配,匹配正确,就执行对应语句
# 3.如果前面所有的case都没有匹配上,就会默认执行case _:

"""
 1.match...case...语法    注:该语法为Python3.10版本中的新语法,在早期版本中并不支持
    match 表达式:
        case 值1:
            操作1
        case 值2 if: 条件表达式:   ---> 满足条件且值为2
            操作2
        case 值3 | 值4:   ---> 匹配值3或值4
            操作3
        case _:     ---> 匹配其他情况
            操作4

 2.match...case...应用场景

    match:基于某个变量的多个固定值进行分支判断时,可以使用match模式匹配

    if:条件判断涉及复杂的逻辑判断,范围比较及组合条件时

"""

# 案例1:
# day = input("请输入星期几")
# match day:
#     case "1":
#         print("周一,工作会议日")
#     case "2":
#         print("周二,学习培训日")
#     case "3":
#         print("周三,项目开发日")
#     case "4":
#         print("周四,代码审查日")
#     case "5":
#         print("周五,总结规划日")
#     case "6" | "7":               # 其中的"|"表示或者,匹配多个模式中的任意一个
#         print("周末,休息放松")
#     case _:                       # 匹配其余所有情况
#         print("输入错误!")

# 案例2:基于match...case...实现一个简易的计算器,可以实现 + - * / 运算,用户输入需要运算的俩个数以及运算符之后,就可以进行计算
# num1 = float(input("请输入第一个数"))
# num2 = float(input("请输入第二个数"))
# oper = input("请输入运算符(+ - * /)")
#
# match oper:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0:  #if条件成立,才匹配这个case
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("操作错误!")

# 作业1:简单游戏指令系统
# 请你编写一个游戏角色控制系统,根据玩家输入的不同指令,控制游戏角色执行相应的动作(输出控制台)
game = input("请输入您的操作")
match game:
    case "w" | "W":
        print("角色向上移动")
    case "s" | "S":
        print("角色向下移动")
    case "a" | "A":
        print("角色向左移动")
    case "d" | "D":
        print("角色向右移动")
    case "j" | "J":
        print("执行攻击")
    case " ":
        print("执行跳跃")
    case _:
        print("输入有误")
