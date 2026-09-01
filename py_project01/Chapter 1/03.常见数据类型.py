# # type() 获取指定的字面量或变量的类型
# print("Hello")
# print(type("Hello")) #str
#
# print(type(10)) # int
# print(type(3.14)) # float
# print(type(True)) # bool
# print(type(False)) # bool
# print(type(None)) # NoneType
#
# num = 100
# print(type(num)) # int
#
# #is instance(数据，类型)--> bool值 --> 判定数据是否是指定类型，如果是:True,否则:False
# print(isinstance(num,int)) # True
# print(isinstance(num,float)) # False
# print(isinstance(num,bool)) # False

# 字符串的三种定义:
print("Hello world") # 双引号
print('Hello world') # 单引号
print("""尊敬的客户:
感谢您选择我们公司的产品
我们将会为您竭诚的服务
祝好~
""") # 三引号

# 转义字符
# \' 表示单引号
# \" 表示双引号
# \n 开始新的一行
# \t 增加缩进，缩进一个制表符(tab)的大小

print('It\'s very good')
print("It's very good")

print("Hello的意思是\"您好\"")
print('Hello的意思是"您好"')

print("欢迎大家进入到Python!\n大家请耐心学习哦~") # \n换行

print("\t欢迎大家进入到Python!\t大家请耐心学习哦~") # \t tab缩进

# 字符串拼接
msg = "人生苦短";msg1 = "我用Python"
print("吉罗·范罗苏姆:",msg + "," + msg1) # "+"只能将字符串与字符串之间拼接起来

# 案例:
name = "金哥"
age = 18
pro = "软件工程"
hobby ="Python Java"
print("大家好,我是" + name + ",今年" + str(age) + ",学习的是" + pro + ",爱好" + hobby) # 用str(int) 将int类型的数字转换字符串

# 字符串格式化
# 方式一:
print("大家好, 我是 %s , 今年 %s , 学习的是 %s , 爱好 %s" %(name,age,pro,hobby)) # "%s" 占位符

# 方式二:
print(f"大家好, 我是 {name} , 今年 {age} , 学习的是 {pro} , 爱好 {hobby}") # f"..{变量名/表达式}.."---> 推荐方式
