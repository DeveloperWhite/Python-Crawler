# 文件操作
# 完整的读文件操作
# mode代表打开文件的模式，这边是只读模式r，后面加上文件编码
f=open("/workspace/Python基础语法/第二章/wenjian.txt",mode="r",encoding="utf-8")
# 这边f是文件句柄，代表文件，负责操纵这个打开的文件
# 路径：绝对路径和相对路径
# 绝对路径：从根目录开始，从上到下，从左到右
# 相对路径：从当前目录开始，从上到下，从左到右
# 从当前文件夹出来只需在前面加上../
# 出来两层就加两个../
# 模式：a，w，r
# r：只读模式

# 把所有的文件内容读取出来
# print(f.read())

# 只读取一行
# print(f.readline())

# for循环读取（重点）
# for line in f: #每次循环读取一行内容
#     print(line.strip()) # 去掉换行符

# 前面一行单独读取，后面数据循环读取
print(f.readline())
print("-----------")
for line in f:
    print(line.strip())


# w:只写模式,重新创建文件,会覆盖之前的内容
f=open("/workspace/Python基础语法/第二章/wenjian1.txt",mode="w",encoding="utf-8")
f.write("hello world")
f.write("\n") #换行
f.write("hello world")


# a:追加模式,在文件末尾追加内容,不会重新创建文件，如果文件不存在，会创建，不会覆盖之前的内容
f=open("/workspace/Python基础语法/第二章/wenjian2.txt",mode="a",encoding="utf-8")
f.write("aaa") 


# b：bytes，二进制模式，一般用于处理图片，视频，音频等
# 不能指定encoding，否则报错
# rb：读取字节
# wb：写入字节
# ab：追加字节
# 这边是从文件读取内容，写入到另一个文件中
f1=open("/workspace/Python基础语法/第二章/1.jpg",mode="rb")
f2=open("/workspace/Python基础语法/第二章/2.jpg",mode="wb")
for line in f1:
    f2.write(line)


# +：扩展 r+表示读写追加（不好区分），w+表示写读，a+表示追加读写（这些方式非常不推荐）
f=open("/workspace/Python基础语法/第二章/wenjian3.txt",mode="r+",encoding="utf-8")
print(f.read())
f.write("hello world")

# 另类的一种写法可以省略close，不需要close关闭
with open("/workspace/Python基础语法/第二章/wenjian3.txt",mode="r",encoding="utf-8") as f, \
     open("/workspace/Python基础语法/第二章/wenjian4.txt",mode="w",encoding="utf-8") as f1:
    for line in f:
        f1.write(line)
# 下面不需要写close，自动关闭


