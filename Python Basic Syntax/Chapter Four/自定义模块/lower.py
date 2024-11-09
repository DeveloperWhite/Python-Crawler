import Master # 模块的搜索路径，先是当前目录，然后是整个项目
print(Master.fun())
print(Master.name)
"""
当导入模块时程序会发生下面的事：
1.首先判断内存中是否已经加载了这个模块，如果已经加载，就直接使用
2.如果没加载，先开辟内存，给模块分配空间，在内存中运行要导入的模块的代码
3.把名称空间返回给import位置
"""
# 导入重名模块，这边可以起别名
# ******不要让自己定义的模块和系统模块重名
import Master as ms1
print(ms1.fun())
print(ms1.name)

from Master import fun
print(fun())