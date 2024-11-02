# 流程控制if语句
# 单分支，第二行是一个tab缩进
"""
if 条件：
    结果（属于同一个代码块）
    """
money=int(input("请输入你的工资："))
if money>3000:
    print("来一瓶雪花")
    print("来一瓶百威")

print("努力挣钱")

# 双分支
'''
if 条件1:
    结果1
else:
    结果2
    '''
money=int(input("请输入你的工资："))
if money>5000:
    print("来一瓶五粮液")
else:
    print("努力挣钱")
print("该干嘛干嘛")

# 多分支
'''
if 条件1:
    结果1
elif 条件2:
    结果2
elif 条件3:
    结果3
else:
    结果4
    '''
# if只要符合条件就会执行，即使后面的条件满足，也会执行第一条语句
money=int(input("请输入你的工资："))
if money>10000:
    print("来一瓶茅台")
elif money>5000:
    print("来一瓶五粮液")
elif money>3000:
    print("来一瓶雪花")
else:
    print("努力挣钱")
print("该干嘛干嘛")

# if嵌套
'''
if 条件1:
    结果1
    if 条件2:
        结果2
    elif 条件3:
        结果3
    else:
        结果4
else:
    结果5
    '''
username=int(input("请输入你的用户名："))
password=int(input("请输入你的密码："))
if username=="admin":
    if password=="123456":
        print("登录成功")
    else:
        print("密码错误")
else:
    print("用户名错误")

