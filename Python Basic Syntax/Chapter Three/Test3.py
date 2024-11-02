# global和nonlocal的关键字
# 现在的需求是：定义一个变量a，需要在函数fun1中修改a的值，但是在python中不允许直接修改全局变量，需要使用global关键字
# 因为如果第一个函数中修改了全局变量，那么第二个函数中就引进的新的全局变量，而不是修改原来的全局变量，就会有安全性问题
a=10
def fun1():
    global a #当前fun1函数中使用的a是全局变量，强行改掉了
    a+=1
    print(a)
fun1()
print(a)
# global关键字作用是把全局变量引入到局部
# nonlocal的工作空间必须在函数中，不能在全局中（局部）
# nonlocal关键字作用是把函数中的变量引入到嵌套函数中，前提变量必须为局部变量
def fun2():
    a=10
    def fun3():
        nonlocal a
        a+=1
        print(a)
    fun3()
fun2()

# 案例
# 这里用global来记录登陆状态，随着叫函数调用，状态发生改变
flag = False
def login():
    global flag
    username = input("请输入用户名：").strip()
    password =input("请输入密码：").strip()
    if username == "admin" and password == "123":
        print("登陆成功")
        flag = True
    else:
        print("登陆失败")
# 增删改查的前提是登陆成功
def add():
    if flag:
        pass
    else:
        print("请先登陆")
        login()
add()



