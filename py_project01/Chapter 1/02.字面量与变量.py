# # # 字面量的写法
# # print(100) # 整数(int)
# # print(3.14) # 浮点数/小数(float)
# # print(True) # 布尔(bool)
# # print(False) # 布尔(bool)
# # print("Hellp World") # 字符串(str)
# # print(None) # 空值(NoneType)
# # # 布尔类型本质也是整数类型在进行算术运算时(True - 1;False - 0)
# # print(True + 1) # 2
# # print(False -1) # -1
# # 变量 ------ Python是动态类型语言，一个变量是可以存储不同类型的数据(但是项目开发中，推荐变量只存储一种类型的数据)
# num = 1114.1
# print(num)
# num = num + 1
# print(num)
# # 案例
# a,b = 20,50
# print("未来一个月播放量:",a + b)
# print("未来俩个月播放量:",a + b + b)
# # 标识符 是程序员在代码中为变量 函数 类等元素所起的名字
# # 命名规则(规定)：
# # 1.只能包含字母(a-z,A-Z) 数字(0-9) 下划线(" _ ")
# # 2.不能以数字开头(但可以包含数字)
# # 3.不能使用关键字:True False None and or if else elif for while等
# # 4.严格区分大小写 如:age Age AGE是三个变量
# # 变量交换案例1:
# c = 10
# d = 20
# e = c # e = 10
# c = d # c = 20
# d = e # d= 10
# print("c=",c,"d=",d)
# 变量交换案例2:
a,b,c = 100,200,300
print(a,b,c)
c,a,b = a,b,c
print(a,b,c)
