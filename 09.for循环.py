"""
for循环
while循环是通过条件表达式来控制是否要进行下一步循环的;而for循环,本质是一种轮询遍历机制,对一批内容进行逐个处理.

for循环的语法格式
for 元素 in 待处理数据集:
    循环体代码(对元素进行处理)
else: (可选)
    循环结束时,执行的代码
"""

# for循环: 遍历输入的字符串

# msg = input("请输入需要遍历的字符串")
#
# for s in msg: # "s"表示遍历出来的元素; "msg"表示需要遍历的数据
#     print(f"元素:{s}")
# else:
#     print("遍历结束")

# for循环与while循环的的场景

# while循环: 用于在某个条件满足时一直循环,循环的次数通常是未知的,只知道循环开始/结束的条件.(关注的是循环的条件)

# for循环: 用于对一个已知的数据集进行遍历或已知次数的循环.(关注的是遍历每一个元素)

"""
range语句
作用: 生成指定规则的数字序列

作用1: range(end) -> 获取一个从0开始到end结束的数字序列(不包含end本身)
range(5)获取的数据就是 0,1,2,3,4

作用2: range(start,end) -> 获取一个从start开始到end结束的数字序列(不包含end本身)
range(2,8)获取的数据就是 2,3,4,5,6,7

作用3: range(start,end,step) -> 获取一个从start开始到end结束的数字序列step步长(不包含end本身)
range(0,10,2)获取的数据就是 0,2,4,6,8
"""

# 案例1: 计算1-100之间所有奇数之和
# num = 0
# for i in range(1,101,2):
#     num += i
# else:
#     print(num)

# 案例2: 计算100-500之间所有3的倍数之和
# total = 0
# for x in range(100,501): # ---> end处为501,不包含end本身也就是100-500之间
#     if x % 3 == 0:
#         total += x
# else:
#     print(total)

# 用法总结:
# range(end)
# range(start,end)
# range(start,end,step)

# 嵌套循环语法:
# for循环结构
"""
for 元素 in 待处理数据集1:  ---> 外层循环      
    循环体的代码1
    循环体的代码2
    ...
    for 元素 in 待处理数据集2:  ---> 内层循环
        循环体的代码1
        循环体的代码2
        ...
    ...
"""

"""
案例1: 根据输入的长方形的长度m,宽度n,打印一个长方形

如下: 是一个长度为10,宽度为5的长方形

    *   *   *   *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *   *
    *   *   *   *   *   *   *   *   *   *
    
    print("*"): 自带换行效果,每一次执行都会输出到新的一行之中;
    print("*",end=""): end表示的是每一次输出以什么结束;默认\n,表示换行,
    
"""

# 1.接受键盘录入 m,n
# 长度
# m = int(input("请输入长度"))
# # 宽度
# n = int(input("请输入宽度"))

# 2.打印长方形
# for i in range(n):
#     for j in range(m):
#         print("*",end="    ")
#     print()

# 案例2: 打印99乘法表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} * {i} = {j * i}",end="\t")
#     print()

# 练习1: 根据输入的直角边的边长,打印等腰直角三角形

# m = int(input("请输入边长"))
# for i in range(m):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# 练习2: 根据输入的数字,打印对应的金字塔

# n = int(input("请输入数字"))
# for x in range(n):
#     for y in range(x+1):
#         print(y+1,end="\t")
#     print()

# 练习3: 根据输入的数字,打印国际象棋棋盘

size = int(input("请输入数字"))  # 棋盘大小

for row in range(size):          # 控制行
    for col in range(size):      # 控制列
        # 如果 (行号 + 列号) 是偶数，打印黑色方块，否则白色方块
        if (row + col) % 2 == 0:
            print("■", end=" ")  # 黑色方块（也可用 "#"）
        else:
            print("□", end=" ")  # 白色方块（也可用空格）
    print()  # 每行结束后换行







