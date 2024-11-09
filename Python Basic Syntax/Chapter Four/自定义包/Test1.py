import os
# 创建文件夹
os.makedirs('glance1/api')
os.makedirs('glance1/cmd')
os.makedirs('glance1/db')
# 创建文件
l=[]
l.append(open('glance1/__init__.py','w'))
l.append(open('glance1/api/__init__.py','w'))
l.append(open('glance1/api/policy.py','w'))
l.append(open('glance1/api/versions.py','w'))
l.append(open('glance1/cmd/__init__.py','w'))
l.append(open('glance1/cmd/manage.py','w'))
l.append(open('glance1/db/__init__.py','w'))
l.append(open('glance1/db/models.py','w'))
# 关闭文件
map(lambda f:f.close(),l)

# 可以导入glance包，再导入一个包的时候默认执行的是这个包下的__init__.py文件
# 这种方案可以解决这个问题，一般导入包的形式
from glance1.api import policy
policy.get_policy()
# 绝对导入：相对于整个包，你要导入模块的位置
# from glance1.cmd import manage
# 相对导入：启动在包外面相对导入
from glance1.cmd import manage
manage.get_manage()

"""
包--->模块--->类--->函数--->变量
"""


