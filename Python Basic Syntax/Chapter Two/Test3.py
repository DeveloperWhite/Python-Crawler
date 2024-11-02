#基本数据类型
#基本数据类型bytes
# 图片，视频读取会用到
s="中国" #内存中存储的是unicode编码
# 编码，encode
# 想进行传输或者存储，需要将字符串转换成其他编码
bs=s.encode("utf-8")
print(bs)
# b'\xe4\xb8\xad\xe5\x9b\xbd'
# 看下他的数据类型
print(type(bs))
s="中国"
bs1=s.encode("gbk")
print(bs1) # b'\xd6\xd0\xb9\xfa'
# 首先一开始是字符串，在传输存储的时候，需要将字符串转换成编码，传输存储过去后，需要将编码转换成字符串
# 解码，decode
# 不同的编码之间是不能直接进行转换的
print(bs.decode("utf-8"))
print(bs1.decode("gbk"))
# 如果想要进行转换，需要先知道编码类型
# 首先是utf-8的编码，先转化成字符串，然后再转化成gbk的编码
m=bs.decode("utf-8")
print(m.encode("gbk"))

# 基本数据类型bool
# 数字，0当成false，其他当成true
a=10
b=bool(a)
print(b) #True
a=0 
b=bool(a)
print(b) #False
# 字符串，空字符串当成false，其他当成true（空格也算）
a=""
b=bool(a)
print(b) #False
a=" "
b=bool(a)
print(b) #True
# 列表，空列表当成false，其他当成true
a=[]
b=bool(a)
print(b) #False
a=[1,2,3]
b=bool(a)
print(b) #True
# 所有空的都当成false，其他都当成true
# 对于int，str，bool，相互转化，用这些东西把东西装起来
# 数字转化成字符串
a=10
b=str(a)
print(type(b)) #str
# 字符串转化成数字
a="10"
b=int(a)
print(type(b)) #int

# 基本数据类型str
s="中国真好"
# 索引：从0开始，取出一个字符
s1=s[0]
print(s1) #中
s2=s[1]
print(s2) #国
# 倒数索引：从-1开始
print(s[-1]) #好
print(s[-2]) #真

# 切片，从开始索引到结束索引，可以取出一段字符串
# 顾头不顾尾，前闭后开，需要多往后取一位
print(s[0:2]) #中国
# 后面什么都不写，表示取到最后
print(s[0:])  #中国真好
# 前面什么都不写，表示从开头取
print(s[:2])  #中国
# 前后都不写，表示取全部
print(s[:])   #中国真好
# 从右往左数，需要给出第三个参数，表示步长为负
# 也可以从左往右数
s="0123456789"
print(s[0:10:2]) #02468
print(s[10:0:-2]) #97531    
# 练习:把一句话倒过来，判断这句话是否是回文，
# 回文就是正着读和倒着读是一样的
# 上海自来水来自海上
content=input("请输入一句话：")
content1=content[::-1]
if content==content1:
    print("是回文")
else:
    print("不是回文")

# 字符串的常用操作

# 大小写
# 切记：字符串是不可变的对象，任何操作对源字符串没有影响
# 返回一个新字符串
s="hello WORLD"
s1=s.capitalize() #首字母大写
print(s1)  #Hello world
s2=s.upper() #全部大写，用来忽略大小写（验证码）
print(s2)  #HELLO WORLD
s3=s.lower() #全部小写
print(s3)  #hello world
s4=s.casefold() #全部小写，范围更广
print(s4)  #hello world
# 下面的代码在输入大写的时候不会退出循环，处理一下
'''
while True:
    s4=input("请输入一个字符串：")
    if s4=="q":
        break
    print("我想对你说:",s4)
    '''
# 不管输入的什么全部转化为大写来判断，忽略大小写
while True:
    s4=input("请输入一个字符串：")
    if s4.upper()=="Q":
        break
    print("我想对你说:",s4)
print(s.swapcase()) #大写变小写，小写变大写
ss="hello world"
print(ss.title()) #首字母大写，其他小写
# 把一连串的字符首字母大写，其他小写即Hello World

# 切来切去
sss="hello world"
# 表示把原来的字符串变成30个字符，不够的用空格补齐
print(sss.center(30))
# 表示把原来的字符串变成30个字符，不够的用*补齐
print(sss.center(30,"*"))
# 去掉字符串左右两边空格,\t,\n
ssss="  helloworld \t\n "
print(ssss.strip())

username=input("请输入用户名：").strip()
password=input("请输入密码：").strip()
# 若果我在用户名后面加上空格就会报错，需要去掉空格
if username=="admin" and password=="123":
    print("登录成功")
else:
    print("登录失败")
# 还能去掉左右两边的字符
sssss="helloworld"
print(sssss.strip("h"))

# replace字符串替换
a="hello world"
print(a.replace("l","L")) #把l替换成L
# 去掉一句话中所有的空格
b="     hello world      "
print(b.replace(" ",""))

# 字符串切割split()
c="张无忌_张翠山_张三丰"
# 通过_切割，用什么切就写啥，返回一个列表，用lst接收
lst=c.split("_")
print(lst) #['张无忌', '张翠山', '张三丰']

# 把一个列表变成一个字符串，用join()
lst=["张无忌","张翠山","张三丰"]
# 表示用该字符把列表拼接起来
m="爱".join(lst)
print(m) #张无忌爱张翠山爱张三丰

# 字符串格式化输出，用操作方法format()
name="张无忌"
age=18
d="我叫{},今年{}岁".format(name,age)
print(d) #我叫张无忌，今年18岁

# 字符串查找
# 让用户输入一个名字，判断是否以"张"开头
name=input("请输入一个名字：")
# startwith() ,判断字符串是否以某个字符开头
if name.startswith("张"):
    print("是张家人")
else:
    print("不是张家人")
# endswith() ,判断字符串是否以某个字符结尾,用法和startwith()一样

k="hello world"
# count() ,统计某个字符在字符串中出现的次数
print(k.count("l")) 
# find() ,查找某个字符在字符串中第一次出现的位置
# index() ,查找某个字符在字符串中第一次出现的位置
# 和find()用法一样，唯一的区别是index，如果找不到会报错
# 找到了返回索引下标，找不到返回-1
print(k.find("l"))
print(k.find("world")) #返回首字母索引下标

# str条件判断
# 用户只能输入数字，输入别的会报错
# money=int(input("请输入金额：").strip())
'''
if money>=1000000:
    print("土豪")
elif money>=10000:
    print("高富帅")
elif money>=1000:
    print("矮矬穷")
else:
    print("穷逼")
    '''
# 上面的代码会出现问题，当用户输入不是数字的时候会报错
money=input("请输入金额：").strip()
if money.isdigit():# 判断字符串是否以数字组成
    money=int(money) # 把字符串转化为数字
    if money>=1000000:
        print("土豪")
    elif money>=10000:
        print("高富帅")
    elif money>=1000:
        print("矮矬穷")
    else:
        print("穷逼")
else:
    print("请输入数字")
#isnumeric() #判断字符串是否以数字组成，连中文数字都可以判断
p="一二三"
print(p.isnumeric())

# 查看字符串的源代码，通过源代码可以知道更多字符串str的操作
# 打印str的操作方法
print(dir(str))
# str计算字符串长度
s5="hello world"
# 这里不需要向前面一样s.什么方法，这种直接使用len()函数即内置函数
print(len(s5))
# 迭代
# 我们可以用for循环来迭代字符串中的每一个字符
# 若不用for循环，也可以使用while循环
m3="hello world"
'''
i=0
while i<len(m3):
    print(m3[i])
    i+=1
    '''
# 用for循环迭代字符串中的每一个字符
# 把m中的字符一个一个拿出来，进行循环
# 现在in后面放的是一个变量，也可以放字典，列表，数字等等
for i in m3:
    print(i)

'''
结论：
字符串索引和切片
upper()把字符串所有字母都变成大写，主要在忽略大小写时使用
strip()去掉字符串两边的空格
replace()字符串替换
split()字符串分割
join()字符串拼接
startwith()判断字符串是否以某个字符开头
find()查找某个字符在字符串中的位置
count()统计某个字符在字符串中出现的次数
isdigit()判断字符串是否是数字
len()计算字符串长度
for 变量 in 可迭代对象:
    循环体
'''
