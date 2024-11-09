"""
绝对导入：绝对于整个包，你要导入模块的位置
相对导入：相对于当前模块，你要导入模块的位置，可能会出现问题
    . 代表当前模块
    .. 代表当前模块的上一级模块
    ... 代表当前模块的上一级模块的上一级模块
"""

# 绝对导入
# from glance1.cmd import manage
# 相对导入，内部文件到外部会出现问题，在包外面访问
# from .cmd import manage
def get_policy():
    print("get_policy")
    # manage.get_manage()

if __name__ == '__main__':
    get_policy()