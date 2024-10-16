# 推导式
# python中没有元祖推导式
# 创建一个列表从1到10
lst = []
for i in range(1,11):
    lst.append(i)
print(lst)

# 列表推导式：[结果 for循环 if条件]
# 下面就想往列表里加i
lst2 = [i for i in range(1,11)]
print(lst2)
# 把所有的奇数添加到列表中
lst3 = [i for i in range(1,11) if i%2==1]
print(lst3)
# 把所有的奇数的平方添加到列表中
lst4 = [i**2 for i in range(1,11) if i%2==1]
print(lst4)
# python x 1~python x 100
lst5 = [f"python x {i}" for i in range(1,101)]
print(lst5)

# 字典推导式: {key:value for循环 if条件}
lst6=["你好","世界","python"]
d={i:lst6[i] for i in range(len(lst6))}
print(d)

# 集合推导式：{key for循环 if条件}
lst7=["你好1","世界1","python1"]
s={i for i in lst7}
print(s)