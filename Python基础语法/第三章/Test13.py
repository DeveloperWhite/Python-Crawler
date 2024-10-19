# 内置函数
# 作用域相关函数:globals，locals
a=10
def func():
    b=20
    print(locals()) #查看局部作用域内容
func()
print(globals()) #查看全局作用域内容

# 迭代器，生成器相关函数:range,iter,next
# range用来数数
for i in range(10):
    print(i)
# iter用来生成迭代器
lst = [1,2,3,4,5]
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
lst = [1,2,3,4,5]
lst2=[1,2,3]
# 查看内存地址
print(id(lst))
print(id(lst2))
# 计算哈希值
print(hash("HH"))
print(hash("HE"))
# 字符串类型代码的执行
# eval（执行字符串中的代码，有返回值）
s="1+1"
print(s)
print(eval(s))
# exec（执行字符串中的代码,无返回值）
s1="print('hello world')"
print(exec(s1))
# compile（）（相当于加载，把一段字符串代码加载，后面可以通过exec和eval去执行）
# 有三个参数，代码，文件名，模式（exec，eval，single）
c1=compile("print('hello world')",'','exec')
b=exec(c1)
print(b)
c2=compile("n=int(input('输入:'))",'','single')
n=exec(c2)
print(n)
#基础数据类型相关函数：int float bool complex（复数）
hg=1.25
print(hg)
print(type(hg))
# 进制转换相关


