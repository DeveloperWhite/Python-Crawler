# 函数的基本概念
# 函数是对功能或动作的封装，写好后可以重复使用
# 函数的定义
# 用def关键字来定义函数
'''
def 函数名(参数列表):
    函数体
'''
def yue():
    print("月")
    print("月")
# 函数的调用
yue()

# 函数的返回值
# 用return关键字来返回一个值
def yue1():
    print("月")
    print("月")
    return 100
# 函数的调用
a = yue1()
print(a)
# 1.函数在执行过程中遇到return语句，就停止执行后面的语句
def yue2():
    print("HH")
    return 100
    print("JJ")
b=yue2()
print(b)
# 2.函数如果没写return得到的返回值是None
def yue3():
    print("HH")
c=yue3()
print(c)
# 3.函数中写了return，但没给返回值，得到的返回值也是None
def yue4():
    print("HH")
    return
d=yue4()
print(d)
# 4.函数中写了return有多个返回值，得到的返回值是元组
def yue5():
    print("HH")
    return 100,200,300
e=yue5()
# 用元祖来接收
print(e)
# return和print的区别
# print是目前能看到程序运行结果的一种手段，但只能在函数内部使用
# return的结果可以返回给函数外面，在外面可以做进一步运算

# 函数目前里面的内容是写死的
# 如果想让函数里面的内容是可变的，需要用到参数
# 参数：函数执行的时候，由外界传递给函数内部的变量
# 接受外界传递的参数：形参，变量
# 执行的时候，给函数传递的参数：实参
# 下面就为形参（也可以传多个参数）
def yue6(application,person):
    # 这种输出格式前面f不能忘
    print(f"打开{application}")
    print(f"使用者{person}")
# 下面就为实参
yue6("QQ","小明")
yue6("WECHAT","小王")


# 实参：在函数调用的时候，给函数传递的参数
# 1.位置参数（按照位置一一对应）
def fun1(a,b):
    print(a,b)
fun1(1,2)
# 2.关键字参数（按照key=value的形式一一对应）
fun1(b=2,a=1)
# 3.混合参数（位置参数和关键字参数混着用，注意位置参数的位置）
# 先写位置参数，再写关键字参数
fun2(1,b=2)
# 形参在执行的时候，必须要有明确的数据，否则程序报错
# 实参的数量必须和形参的数量一致


# 形参：在函数申明的位置编写的变量
def fun3(a,b,c):
    print(a,b,c)
# 1.位置参数
fun3(1,2,3)
# 2.默认值参数:输入默认值，调用函数的时候可以不传递
# 常用于性别，省去输入的麻烦
def fun4(a,b,c=3):
    print(a,b,c)
fun4(1,2)


