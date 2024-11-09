# 自定义模块
def fun():
    print("hello world")
    return 1
name = "Master"
print("你好，导入模块时能运行")
# 下面内容我不想别人导入该模块的时候也会去运行，而我自己在这个模块时能运行，需要进行控制
if __name__ == "__main__": #被称为程序的入口
    print("你好，导入模块时不会运行")