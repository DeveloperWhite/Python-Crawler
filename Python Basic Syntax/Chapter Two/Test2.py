# 运算符
# 算术运算
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# 计算商
print(a//b)
# 计算余数
print(a%b)
# 次幂计算
print(a**b)
# 比较运算
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
# 赋值运算
a=10
b=3
a+=b
print(a)
# 逻辑运算
'''
and  并且,and都为真才为真
or   或者,or有一个为真就为真
not  否
'''
# 优先级：()>not>and>or
print(True and False)
print(True or False)
print(not True)
print(True or( False and False) or not False and True)
# 非0为真，0为假
print(1 or 2 and 3)
# 登陆
username=input("请输入用户名:")
password=input("请输入密码:")
if username=="admin" and password=="123456":
    print("登陆成功")
else:
    print("登陆失败")
# 成员运算
# in,not in
# 让用户输入评论信息，判断是否包含敏感词
# 判断是否包含敏感词
content=input("请输入评论信息:")
'''
if "敏感词" in content:
    print("含有敏感词")
else:
    print("没有敏感词")
    '''
# 如果多个敏感词
if "敏感词" in content or "敏感词" in content:
    print("含有敏感词")
else:
    print("没有敏感词")

# 编码
# ascii:8bit,主要用来存放英文，数字，特殊符号
# unicode:16bit和32bit两个版本,
# 平时我们用16bit这个版本，全世界所有国家的文字信息，
# 缺点：浪费空间（存储和传输）
# utf-8:可变长度unicode，英文：8bit，中文：24bit，
# 欧洲文字：16bit，一般数据传输和存储的时候使用
# gbk:16bit,主要存放中文和亚洲字符，兼容ascii




