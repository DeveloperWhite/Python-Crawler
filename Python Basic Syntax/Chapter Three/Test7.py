#迭代器：iterator
# 统一的循环方式
# 查询不同数据类型可执行操作dir（）
print(dir(str)) #有——iter——，可迭代
print(dir(list)) #有——iter——，可迭代
print(dir(dict)) #有——iter——，可迭代
print(dir(int)) #无——iter——，不可迭代
print(dir(bool)) #无——iter——，不可迭代
# 所有可迭代对象都可以使用for循环，都有__iter__方法
lst= [1,2,3,4,5]
# 拿到迭代器方法
it = lst.__iter__()
# 迭代下一个元素
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__()) 
# 使用步骤
# 1.拿到迭代器对象
# 2.使用迭代器对象的方法next()获取下一个元素
# 3.反复第2步，如果元素取完了，抛出StopIteration异常
# 坑
# 1.迭代器对象只能使用一次，想用第二次拿到第一个数据，需要重新获取迭代器对象
# 还可以使用iter()函数，来获取迭代器
lst1 = [1,2,3,4,5]
it1 = iter(lst1)
print(next(it1)) #1
print(next(it1)) #2
print(next(it1)) #3
print(next(it1)) #4
print(next(it1)) #5
print(next(it1)) #StopIteration
# 迭代器：能一个个往外拿数据的东西
# 可迭代对象：可以拿到迭代器对象的东西
