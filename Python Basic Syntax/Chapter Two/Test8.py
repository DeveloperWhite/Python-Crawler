# 难点
# 深浅拷贝
lst1=[11,22,33]
# 这边复制的是内存地址，没有创建新的列表，两者指向同一个内存地址（列表）
lst2=lst1
print(lst1)
print(lst2)
# 在第一个列表里加一个元素，看看第二个列表有没有变化
lst1.append(44)
print(lst1)
print(lst2) # lst2也跟着变化了
# 查看内存地址
print(id(lst1))
print(id(lst2))
lst3=lst1.copy() #产生一个新的列表
# lst3=lst1[:]这边也是产生一个新的列表，用的是切片
print(lst3)
lst1.append(55)
print(lst1)
print(lst3) # lst3没有变化
# 查看内存地址，不同
print(id(lst1))
print(id(lst3))

# 特殊情况
lst4=[11,22,[33,44]]
# 这里都进行变化的原因是，lst4[2]也是一个列表，他和lst4不是一个列表
# 但是下面只是把lst4复制了，内部衍生的列表没有拷贝，所以lst4[2]和lst5[2]都会变化
# 这种拷贝第一层内容，内部列表没有拷贝，称为浅拷贝
lst5=lst4.copy()
print(lst4)
print(lst5)
lst4[2].append(55)
print(lst4)
print(lst5) # lst5也跟着变化了

# 深拷贝必须使用copy模块，深拷贝两者之间完全划分开，互相独立
# 完全复制一块新的列表
# 导入copy模块
import copy
# 使用deepcopy()方法
lst6=copy.deepcopy(lst4)
print(lst6)
lst4[2].append(66)
print(lst4)
print(lst6) # lst6没有变化



