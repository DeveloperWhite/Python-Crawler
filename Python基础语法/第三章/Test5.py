# 装饰器
# 作用：在不改变原函数的情况下，给函数增加功能
def wrapper(fn): #把被装饰函数当成参数传入
    def inner(): #定义一个函数，用来接收被装饰函数
        # 我可以在执行被装饰函数之前执行一些代码
        print("before")
        fn()  #执行被装饰函数
        # 我可以在执行被装饰函数之后执行一些代码
        print("after")
    return inner #返回inner函数

@wrapper
# add = wrapper(add) 相当于@wrapper
def add():
    print("add111")
# a = wrapper(add) #将add函数作为参数传入wrapper函数
# 这样就实现了不改变add函数的情况下，给add函数增加功能
# a() #执行inner函数
# 但是我原来调用add函数，现在新增完功能后调用的是a函数
# 所以我需要将add函数重新指向a函数，不然调用改动的点就很大
# 但是下面这句话很绕口，有比较简化的语法
# add = wrapper(add)
# 想要装饰哪个函数就在哪个函数上加上@装饰函数名
add() #执行inner函数

# 通用装饰器
# 装饰的函数有参数和返回值
def wrapper1(fn):
    # 这边把参数聚合传入进去
    def inner1(*arges,**kwargs):
        print("before")
        # 这边把参数打散传出
        fn(*arges,**kwargs)
        print("after")
    return inner1
@wrapper1
def dnf(username,password):
    print("dnf")
dnf("aaa",123)  #执行inner1函数
# 上面的装饰器可以实现动态传参
@wrapper1
def dnf1(username):
    print("dnf1")
dnf1("aaa")  #执行inner1函数

# 如果目标函数有返回值，装饰器函数返回值也要有返回值

def wrapper2(fn): #把被装饰函数当成参数传入
    def inner(): #定义一个函数，用来接收被装饰函数
        # 我可以在执行被装饰函数之前执行一些代码
        print("before")
        # 装饰函数这边需要能接收返回值
        ret=fn()  #执行被装饰函数
        # 我可以在执行被装饰函数之后执行一些代码
        print("after")
        # 返回返回值
        return ret
    return inner #返回inner函数

@wrapper2
def dnf2():
    print("dnf2")
    return "dnf22222222"
print(dnf2()) #执行inner函数

# 通用装饰器写法
def wrapper3(fn):
    def inner(*arges,**kwargs):
        """在执行被装饰函数之前执行一些代码"""
        ret=fn(*arges,**kwargs)
        """在执行被装饰函数之后执行一些代码"""
        return ret
    return inner
