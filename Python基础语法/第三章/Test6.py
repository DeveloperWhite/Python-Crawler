#高阶装饰器
def wrapper(fn):
    def inner(*arges,**kwargs):
        print("装饰器1")
        fn(*arges,**kwargs)
        print("装饰器2")
    return inner
def wrapper1(fn):
    def inner1(*arges,**kwargs):
        print("装饰器3")
        fn(*arges,**kwargs)
        print("装饰器4")
    return inner1
def wrapper2(fn):
    def inner2(*arges,**kwargs):
        print("装饰器5")
        fn(*arges,**kwargs)
        print("装饰器6")
    return inner2
# 这边执行就近原则从下往上执行
@wrapper
@wrapper1
@wrapper2
def dnf(): #被装饰函数
    print("dnf")
dnf()

# 带参数的装饰器，就是在外面再套一层传参，并返回装饰器
def chuancan(name):
 def wrapper3(fn):
    def inner3(*arges,**kwargs):
        print(f"装饰器7{name}")
        fn(*arges,**kwargs)
        print(f"装饰器8{name}")
    return inner3
 return wrapper3
#  这边相当于先调用chuancan函数，返回wrapper3装饰器，在@装饰器进行装饰
@chuancan("外挂1")
def dnf1():
    print("dnf1")
dnf1()
@chuancan("外挂2")
def dnf2():
    print("dnf2")
dnf2()



