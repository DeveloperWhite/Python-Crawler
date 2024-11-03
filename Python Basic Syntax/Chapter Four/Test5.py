# hashlib模块
# 里面有很多加密算法，比如md5，sha1，sha256，sha512
# 本节主要讨论md5
# 比如用户输入密码,对于程序员来说,是直接能在数据库中查到的,所以不是很安全,所以要做加密,不应该是明文,而是加密后的密文
# 首选用md5加密,因为是不可逆的,所以安全性高
import hashlib
# 首先创建md5对象
obj=hashlib.md5()
# 把要加密的字符串传给obj,要求一定是字节
obj.update("2096164171".encode("utf-8"))
# 调用hex digest()方法,返回加密后的字符串
s=obj.hexdigest()
print(s)
# 但是我们可以把这个密文拿到cmd5.com网站去解密,他不是依靠逆向,而是依靠撞库,人家库里面有这条记录,而不是解密出来的,是查询出来的
# 正常的默认加密过程是容易撞库的
# 解决撞库问题,就是加盐,就是把密码和盐混合在一起,然后加密,这样,即使撞库,也撞不到,因为盐是唯一的
# 首先创建md5对象,这边加了一把盐,这样一定查不到
obj=hashlib.md5(b'agddjhgdhfhfhfhf')
# 把要加密的字符串传给obj,要求一定是字节
obj.update("66666".encode("utf-8"))
# 调用hex digest()方法,返回加密后的字符串
s=obj.hexdigest()
print(s)


# 需要在注册密码前进行加密

def func(salf,s):
    obj=hashlib.md5(salf)
    obj.update(s.encode("utf-8"))
    return obj.hexdigest()

# # 用户注册
# user_name=input("请输入用户名:")
# pass_word=input("请输入密码:")
# # 如果这边直接输入盐的话程序员也能看到,所以把用户名或密码设成盐,这样每个人都不一样
# # 这边属于动态加盐
# mi_password=func(user_name.encode("utf-8"),pass_word)
# f=open("user.txt",mode="w",encoding="utf-8")
# f.write(user_name+"\n")
# f.write(mi_password)


# # 登录
# user_name=input("请输入用户名:")
# pass_word=input("请输入密码:")
# f=open("user.txt",mode="r",encoding="utf-8")
# user_name1=f.readline().strip()
# mi_password1=f.readline().strip()
# # 这边需要把用户填写的密码进行加密和数据库中的密文进行对比
# if user_name==user_name1 and func(user_name.encode("utf-8"),pass_word)==mi_password1:
#     print("登录成功")
# else:
#     print("登录失败")

# 文件也可以进行md5加密
obj=hashlib.md5(b'agddjhgdhfhfhfhf')
f=open("user.txt",mode="rb")
for line in f:
    obj.update(line)
# 得到加密后的结果
s=obj.hexdigest()
print(s)
# 主要用来判断文件一致性
# 用户上传文件,服务器端保存文件,然后进行md5加密,然后和用户上传的md5进行对比,如果一致,直接用之前上传过的文件发送,速度很快不需要再进行上传,如果没有,则重新上传
