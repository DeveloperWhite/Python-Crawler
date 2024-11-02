# 知识点补充

# 列表和字典在循环的时候不能删除
# is和==的区别
# while....else...


# 列表的删除
lst=["张三分","张五","张翠山","张武侠"]
# 删除所有姓张的
# 下面的写法会删不干净
# 删除之后指针指向最后一个元素，
# 删除前一个元素，列表中的元素会自动向前移动
# 导致错开的元素不会被删除
# for name in lst:
#     if name.startswith("张"):
#         lst.remove(name)
# print(lst)
# 下面的写法可以删除所有姓张的
# 把要删除的内容记录在一个新列表中
# 循环新列表，删除原列表中的元素

# 第一种方法
'''
lst1=[]
for name in lst:
    if name.startswith("张"):
        lst1.append(name)
for a in lst1:
    lst.remove(a)
print(lst)
'''

# 第二种方法（浅拷贝）
for name in lst[:]:
    if name.startswith("张"):
        lst.remove(name)
print(lst)


# 字典的删除
# 在循环这个字典的时候，不能删除字典中的元素
# 字典中删除是会报错的
d={"name":"张三","age":18,"sex":"男"}
# for key in d:
#     d.pop(key)

# 把要删除的内容记录在一个新列表中
# 循环列表，删除字典
# 通过keys()方法获取所有的key，把key记录在一个新列表中
lst=list(d.keys())
for key in lst:
    d.pop(key)
print(d)

# 这边必须拿列表或字典来进行比较
# python对于数字和字符串的比较区分没有那么严格
a=[10,20,30]
b=[10,20,30]
# 判断两个列表的内存地址是否一致
print(a is b) # False
# 判断两个列表是否相等
print(a == b) # True
# 一般用is来判空
c=None
if c is None:
    print("c是空")
else:
    print("c不是空")


# while循环
# while循环的else语句
# while循环的else语句会在循环条件不满足时执行
i=0
while i<10:
    print(i)
    i+=1
else: # 条件不满足时执行else下面的语句
    print("循环结束")

# 练习：让用户随便输入一个数字，判断是否是质数
# 质数只能被1和自身整除
# 这边对被除数进行遍历，只要发现除下来，余数有0，就不是质数
i=2
money=input("请输入一个数字：")
if money.isdigit():
    number=int(money)
    while i<number:
        if number%i==0:
            print("不是质数")
            break
        else:
            i+=1
    else:
        print("是质数")
else:
    print("请输入数字")





