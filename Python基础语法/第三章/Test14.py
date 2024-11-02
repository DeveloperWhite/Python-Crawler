# 三元表达式和递归
a=10
b=20
# 三元表达式
# 相当于如果a>b 返回a，否则返回b
c=a if a>b else b
print(c)
# 递归
# 递归函数：函数自己调用自己
import sys
print(sys.getrecursionlimit()) # 获取最大递归深度1000，超过1000会报错
sys.setrecursionlimit(10000) # 设置最大递归深度，也可以设置
# 递归可以完美帮忙我们遍历一个文件夹
# os模块，可以访问计算机的文件夹系统
# 很重要，重点理解***
import os
# 获取当前文件夹的路径
# ceng表示文件的层数
def read(path,ceng): # path是文件夹的路径
    lst=os.listdir(path) # 用来遍历文件夹
    for name in lst:
        # 需要拼接出正确的文件路径，把文件路径和文件名拼接起来
        real_path=os.path.join(path,name)
        if os.path.isdir(real_path):
            # 如果是文件夹就继续执行该函数递归里面的文件名
            #文件夹
            # 进入递归
            print("\t"*ceng,name)
            read(real_path,ceng+1)
        else:
            # 如果是文件，就直接打印文件名
            # 普通文件
            print("\t"*ceng,name)
read('D:\pycharmwenjian',0)
