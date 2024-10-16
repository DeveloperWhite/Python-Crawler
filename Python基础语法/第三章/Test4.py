def fun1():
    print("fun1111")
def fun2():
    print("fun2222")
def fun3():
    print("fun3333")

# 函数当成变量(参数)使用
lst = [fun1,fun2,fun3]
print(lst)
# 列表里面每一项都是函数，拿出来运行
for item in lst:
    item()

def handle(a):
    a()
# 这边可以将函数当成参数传进去，进行执行
handle(fun1)
handle(fun2)
handle(fun3)

def handle2(*b):
    for item in b:
        item()
# 这边可以将函数当成参数动态传参，进行执行
handle2(fun1,fun2,fun3)

# 函数当成返回值
def handle3():
    def fun4():
        print("fun4444")
    return fun4
# 这边可以将函数当成返回值，进行执行
handle3()
# 上面执行完之后，返回的是fun4函数，然后执行fun4函数
a = handle3()
# a为fun4，后面加上括号就相当于执行fun4()
a() # fun4444

# 闭包：内层函数对外层函数变量的使用
# 作用1：可以让一个变量被封锁起来外界只能看到，但是改不了
# 作用2：可以让一个变量常驻内存，不会被释放
def fun5():
    a=10
    def fun6():
        print(a)
    fun6()
fun5() # 10

# 想要在函数的外面访问函数里面的局部变量，但不能进行修改
def fun7():
    a=10
    def fun8():
        print(a)
    return fun8
# 这边返回的是fun8函数，然后执行fun8函数
a = fun7()
# a为fun8，后面加上括号就相当于执行fun8()
a() # 10


