# 模拟for循环
lst= [1,2,3,4,5]
for item in lst:
    print(item)
# 1
# 2
# 3
# 4
# 5
# for循环内部大致工作机制
# 1.拿到可迭代对象
# 2.拿到迭代器对象
# 3.使用迭代器对象的方法next()获取下一个元素
# 4.反复第3步，如果元素取完了，抛出StopIteration异常
it = lst.__iter__()
while True:
    try: #尝试执行下列代码
        # 如果一直执行下去,会报错，所以要捕获异常
        obj = it.__next__()
        print(obj)
        # 如果出现的是StopIteration异常，就执行下面的打断
    except StopIteration:
        break

