# 内置函数
# 作用域相关函数:globals，locals
a = 10


def func():
    b = 20
    print(locals())  # 查看局部作用域内容


func()
print(globals())  # 查看全局作用域内容

# 迭代器，生成器相关函数:range,iter,next
# range用来数数
for i in range(10):
    print(i)
# iter用来生成迭代器
lst = [1, 2, 3, 4, 5]
it = iter(lst)
# next函数用来获取迭代器的下一个值
print(next(it))

# 其他函数：
# dir（查看能进行哪些操作，内置属性）
print(dir(bool))
# callable（判断是否可以被调用）
print(callable(bool))
print(callable(10))
# help（查看帮助源码）用的比较少
# print(help(str))
# 导入模块（动态导入模块）__import__
# mo=input('请输入模块名：') # os
# 动态加载模块
# __import__(mo)
# 文件操作相关函数：open read write close
# f=open('test.txt','w')
# f.write('hello world')
# f.close()
# 内存相关 hash id
lst = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3]
# 查看内存地址
print(id(lst))
print(id(lst2))
# 计算哈希值
print(hash("HH"))
print(hash("HE"))
# 字符串类型代码的执行
# eval（执行字符串中的代码，有返回值）
s = "1+1"
print(s)
print(eval(s))
# exec（执行字符串中的代码,无返回值）
s1 = "print('hello world')"
print(exec(s1))
# compile（）（相当于加载，把一段字符串代码加载，后面可以通过exec和eval去执行）
# 有三个参数，代码，文件名，模式（exec，eval，single）
c1 = compile("print('hello world')", '', 'exec')
b = exec(c1)
print(b)
c2 = compile("n=int(input('输入:'))", '', 'single')
n = exec(c2)
print(n)
# 基础数据类型相关函数：int float bool complex（复数）
hg = 1.25
print(hg)
print(type(hg))
# 进制转换相关bin oct hex
print(bin(10))  # 二进制 010101
print(oct(10))  # 八进制 0-7
print(hex(10))  # 十六进制 0-9-a-f
# 数学运算
print(abs(-10))  # 绝对值
print(divmod(10, 3))  # 除法取余
print(pow(2, 3))  # 乘方
print(round(1.23456, 3))  # 四舍五入
print(max(1, 2, 3, 4, 5))  # 最大值
print(min(1, 2, 3, 4, 5))  # 最小值
print(sum([1, 2, 3, 4, 5]))  # 求和

# 数据集合相关的
# 字典
d = dict([('name', '张三'), ('age', 18)])  # 字典的创建
print(d)
# 集合
s = set([1, 2, 3, 4, 5])  # 集合的创建
print(s)
s = frozenset([1, 2, 3, 4, 5])  # 冻结集合，不能修改
print(s)
# 相关内置函数
# 列表既拿索引，又拿值
lst = ["张三", "王五", "李六"]
for i in range(len(lst)):
    print(i)
    print(lst[i])
# v可以在enumerate函数中指定索引的起始值
# 不写v就是从0开始，可以直接拿到索引和值
for i, v in enumerate(lst, 11):  # 用enumerate函数，可以同时拿到索引和值
    print(i)
    print(v)
lst = [0, "hehe", True]
print(any(lst))  # 判断列表中是否有值，相当于or
print(all(lst))  # 判断列表中是否都是值，相当于and
# zip函数，把两个列表组合成一个元组列表，水桶效应，以最短的合并为基准
lst1 = [1, 2, 3]
lst2 = ["a", "b", "c"]
for i in zip(lst1, lst2):  # 用zip函数，可以同时拿到索引和值
    print(i)
# zip可以快速构建字典
d = dict(zip(lst1, lst2))
print(d)

# 序列相关函数：reversed slice
lst = [1, 2, 3, 4, 5]
r = reversed(lst)
print(list(r))  # 翻转
a = "今天天气不错"  # 切片
a1 = "哈呵护黑你好"
# 函数可重复使用
# 切片还可以指定步长
s = slice(2, 5, 2)  # 从索引2开始，到索引5结束，不包含索引5，步长为2
print(a[s])  # 天不
print(a1[s])  # 护你
# 字符串
# 字符和数字的相互转换
print(ord('中'))  # 返回字符的ASCII码
print(chr(20013))  # 返回ASCII码对应的字符
# chr可以用来生成验证码
import random
n = chr(random.randint(65, 90))  # 生成大写字母
print(n)
# repr 用来获取字符串的原始值(字符串最规范的写法)
print(str("123"))
print(repr("123"))
# 当字符串中出现转义字符时，可以用r来取消转义
print("123\n456")
print(r"123\n456")  # 123\n456
# format 格式化字符串（想要一个定长的数字）
a = 48
print(format(a, "08"))  # 08表示8位，不够用0补齐
# 定长的二进制
print(format(a, "08b"))  # 08b表示8位，不够用0补齐，二进制
# 定长的小数点后几位
b = 1.25
print(format(b, ".8f"))  # .8f表示小数点后八位（保留八位）

# 内置函数（sorted map filter）
# 排序函数sorted
lst=[3,2,7,4,5]
print(sorted(lst))  # 默认升序
# reverse表示翻转
print(sorted(lst,reverse=True))  # 降序

lst=["赵本山","周杰","范伟","小沈阳二"]
# 可以自己定义排序规则
# 根据名字长度排序
# 这边也可以用lambda表达式，更加简洁
def func(item):
     return len(item) #返回名字长度
print(sorted(lst,key=func))  # 根据名字长度排序
lst=[{
    "ID":1,"name":"张三","age":18
},{
    "ID":2,"name":"李四","age":20
},{
    "ID":3,"name":"王五","age":19
},{
    "ID":4,"name":"赵六","age":17
}]
# 根据年龄排序
print(sorted(lst,key=lambda item:item["age"]))  # 根据年龄排序
'''
# filter函数：筛选函数
lst=[1,2,3,4,5,6,7,8,9,10]
# 请把被3整除的筛选出来
f=filter(lambda item:item%3==0,lst)
print(list(f))  # 把filter对象转换成列表
'''
# 把年龄大于等于18的筛选出来
f1=filter(lambda item:item["age"]>=18,lst)
print(list(f1))  # 把filter对象转换成列表

# map函数
lst=[1,2,3,4,5,6,7,8,9,10]
# 请把列表中的每个元素都加1
m=map(lambda item:item+1,lst)
print(list(m))  # 把map对象转换成列表
