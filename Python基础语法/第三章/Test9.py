# 生成器:本质是迭代器
# 通过生成器函数来创建生成器对象
def func():
    print("123")
    # 当函数中有yield时,函数就变成了生成器函数
    # yield后面也表示返回值，当调用next时，才会返回后面的东西
    yield "a"

gen = func()
# 下面打印得到的是生成器
print(gen) # <generator object func at 0x0000023735361748>
print(gen.__next__()) # 123 # a
# 在一个生成器函数中可以有多个yield
def func2():
    print("123")
    yield "a"
    print("456")
    yield "b"
    print("789")
    yield "c"
gen2 = func2()
print(gen2.__next__()) # 123 # a
print(gen2.__next__()) # 456 # b
print(gen2.__next__()) # 789 # c
# print(gen2.__next__()) # StopIteration

# ****节省内存
# 买一万件衣服
# def order():
#     lst = []
#     for i in range(10000): #会比较消耗资源
#         lst.append(f"衣服{i}")
#     return lst #列表占用内存
# a=order()
# print(a)

# 第一种改进,生成器版本，什么时候要用什么时候生成
def order():
    lst = []
    for i in range(10000): 
        yield f"衣服{i}"
a=order()
print(a.__next__()) #衣服0
print(a.__next__()) #衣服1
print(a.__next__()) #衣服2

# 一次50件衣服
def order1():
    lst = []
    for i in range(10000): 
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst
            # 拿完50件衣服，列表清空
            lst = []
a1=order1()
print(a1.__next__()) #衣服0-49
print(a1.__next__()) #衣服50-99

def order2():
    print("111")
    a=yield "hahaha"
    print("222",a)
    b=yield "b"
    print("333",b)
    c=yield "c"
g=order2()
print(g.__next__()) #111 # hahaha
print(g.send("123")) #222 123 # b
# send会给上一个yield赋值
# next和send的区别
# 相同点：都可以让生成器继续执行
# 不同点：next不传值，send传值（给上一个yield传值）