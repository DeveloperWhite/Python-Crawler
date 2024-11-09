# zipfile模块
import zipfile
# # 1.创建压缩包
z = zipfile.ZipFile("x3.zip","w") #创建压缩包,参数1:压缩包名字,参数2:压缩包模式,参数3:压缩包内文件名
z.write("user.txt") #将x1.txt压缩到压缩包中
z.write("x2.txt") #将x2.txt压缩到压缩包中
z.close() #关闭压缩包
# # 2.解压压缩包
z = zipfile.ZipFile("x3.zip","r") #创建压缩包,参数1:压缩包名字,参数2:压缩包模式,参数3:压缩包内文件名
# 直接全部解压到当前目录，extractall
z.extractall("dir2")
# 一个个解压，extract
print(z.namelist()) #查看压缩包内文件列表
# 循环拿到每一个文件名
for name in z.namelist():
    z.extract(name,"hehe") #解压到hehe目录下
z.close() #关闭压缩包