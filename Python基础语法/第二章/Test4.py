# 基本数据类型列表list，不限制长度，不限制类型
a=[1,True,"hello world",1.23,[1,2,3],{"name":"张三","age":18}]
print(a)
# 列表的索引和切片和字符串一样
list=[1,2,3,4,5,6,7,8,9,10]
print(list[0])
print(list[1:6:2])

# list新增
# 列表是可变的和字符串不同，增加之后会改变原来的列表
list1=[1,2,3]
# 这里不需要重新赋予变量
list1.append(4)
# 在某个位置插入元素，在索引下标为1的位置插入0，本身的数据后移
list1.insert(1,0)
# 迭代新增，表示把n中的元素依次添加到list1中
n=[5,6,7]
list1.extend(n)
print(list1)

# list删除
list2=[1,2,3,4,5,6,7,8,9,10]
# 删除某个元素
list2.remove(1)
# 默认删除最后一个元素
list2.pop()
# 删除某个位置的元素
list2.pop(1)
del list2[1]
print(list2)
# 清空列表
list2.clear()

# list修改
list3=[1,2,3,4,5,6,7,8,9,10]
list3[0]=100
print(list3)

# list查询
list4=[1,2,3,4,5,6,7,8,9,10]
# 首先遍历所有元素
for i in list4:
    print(i)
# 虽然for循环能遍历元素，但不能直接获取索引，需要使用index方法
# 让for循环数数，range()搭配for循环
'''
从0开始,到n-1结束
range(n)
从m数到n-1结束,步长为k
range(m,n,k)
'''
for i in range(len(list4)):
    print(i)
    print(list4[i])

# 用例：
# 在列表中找到姓王的，把姓王的名字改成张三
# 需要同时拿到索引和值
list5=["张三","李四","王五","赵六","王五","王五","王五"]
for i in range(len(list5)):
    if list5[i]=="王五":
        list5[i]="张三"
print(list5)

# list其他操作
list6=[1,6,3,4,5,6,7,6,9,10]
# 列表中某个元素出现的次数
print(list6.count(6))
# 翻转倒排序
list6.reverse()
print(list6)
# 排序，从小到大
list6.sort()
print(list6)

# 列表嵌套
list7=[1,2,3,[4,5,6,["王剑灵",8,9]]]
# 把里面嵌套的列表看成一个元素
print(list7[3][3][1])
# 需求
# 把剑改成建在放回去
list7[3][3][0]=list7[3][3][0].replace("剑","建")
print(list7)
print(list7[3][3][0][1]) #建


