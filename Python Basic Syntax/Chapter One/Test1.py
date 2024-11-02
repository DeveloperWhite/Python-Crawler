print("Hello World")
"""
while 1:
    print("Hello World")
"""
# 变量
# 变量的命名规则
# 1.只能由字母、数字、下划线组成
# 2.不能以数字开头
# 3.不能与关键字重名if等等
# 4.区分大小写
# 5.不要用中文
# 6.名字要有意义
# 驼峰命名法或下划线命名法
# getElementById，get_element_by_id
a=10086
print(a)
print(a+3)
# 常量
# 比如数据库的账号和密码一般不会变会定义成常量，在python中一般用大写表示
# 如果见到大写，一般就是常量，不要去动他
PI=3.1415926
print(PI)
# 注释
# 单行注释
# 打印("Hello World")
print("Hello World")
# 多行注释
# 第一种
"""
print("Hello World11111")
"""
# 第二种
'''
print("Hello World22222")
'''
# 基本数据类型
# 整数
# 字符串
# 布尔

# 整数
c=1
b=2
print(c+b)
print(c-b)
print(c*b)
# 表示除法
print(c/b)
print(c%b)
# 表示整除
print(c//b)
# 比较
print(c>b)
print(c<b)
print(c==b)

# 字符串
# 单引号
# 双引号
# 三引号
s='aaa'
ss="bbb"
sss='''ccc'''
print(s)
print(ss)
print(sss)
# 字符串拼接
print(s+ss+sss)
# 字符传不能和整数相加，显得不伦不类
# print(s+111)
# 字符串可以和整数相乘，表示复制
print(s*3)

# 布尔值
# True和False都是关键字，不能当成变量名使用
a=100
b=200
print(a>b) #false
print(a<b) #true
print(a==b) #false

# type函数
# 用来查看数据类型
# 有时候数据是传递过来的，通过打印无法区分是什么类型，可以用type函数查看
a=100   
b='100'
print(type(a))
print(type(b))

# 用户交互
# input函数
# input带来的问题
# input接受的所有数据都是字符串类型
a=input("请输入a的值：")
b=input("请输入b的值：")
print(a+b) #这边是字符串拼接，因为a和b都是字符串类型
name = input("请输入你的名字：")
print(name)
# 将字符串类型转换成整数类型  
a=int(input("请输入a的值："))
b=int(input("请输入b的值："))
print(a+b) #这边转换成整数类型，所以是相加


