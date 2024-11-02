# 生成器表达式
g= (i for i in range(5))
print(g)
'''
print(next(g))
print(g.__next__())
'''
# 拿空生成器中的内容
# 1.直接for循环
'''
for i in g:
    print(i)
'''
# 2.使用list，tuple，set直接把生成器中的内容取出来
print(list(g)) # [0, 1, 2, 3, 4]
# print(tuple(g)) # (0, 1, 2, 3, 4)
# print(set(g)) # {0, 1, 2, 3, 4}

# 面试题
def func(): #生成器函数
    print(111)
    yield 222

g=func() #创建生成器
g1=(i for i in g) #创建生成器
g2=(i for i in g1) #创建生成器
# 到这一步为止，生成器函数func()中的print(111)和yield 222都没有执行，因为上面都是在创建生成器
print(list(g)) # 这里g直接把数据拿空，后面g1，g2都依附于g，所以都为空
print(list(g1))
print(list(g2))

# 想拿空两个列表里面的内容
def func1():
    lst1=[1,2,3,4,5]
    lst2=[6,7,8,9,10]
    # for i in lst1:
    #     yield i
    # for i in lst2:
    #     yield i
    yield from lst1 #可以直接把列表中的内容拿空
    yield from lst2

g=func1()
print(list(g)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]