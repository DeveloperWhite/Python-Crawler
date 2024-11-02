# 基本数据类型(元祖)tuple
# 相当于不可变的列表，一旦创建，不能修改
t=("a","b","c")
print(t)
print(type(t)) # <class 'tuple'>
# 用索引取值
print(t[0])
# 切片
print(t[:2])

# 元祖只有一个元素时，需要加逗号(,)，否则会当成字符串
t1=(1,)
print(t1)
print(type(t1)) # <class 'tuple'>
t2=(1)
print(t2)
print(type(t2)) # <class 'int'>
# 元祖不能修改，但是可以给元祖的元素赋值
# 比如这里是列表，可以给列表的元素赋值，并不是元祖本身修改
t3=(1,[],3)  
t3[1].append(4)
print(t3) # (1, [4], 3)

