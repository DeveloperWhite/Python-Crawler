# 模块
# 导入模块整体
# import time
# 从一个模块中导入一个具体的功能
# from time import sleep

# time模块，防止一直调用，爬虫会封IP，以后可以改成一个随机数
import time
print("hello world")
time.sleep(1)
print("hello world1")
# 1970年1月1日 00:00:00 到现在的时间
print(time.time())  # 时间戳，数字类型的时间
# 可以用来计算时间差
start = time.time()
for i in range(100000):
     print(i)
end = time.time()
print(end - start)

# datetime模块
from datetime import datetime
from datetime import date
# 拿到当前时间
print(datetime.now())
# 创建一个时间
print(datetime(2019, 1, 1,11,12,11))
# 时间差
t1 = datetime(2019, 1, 1,11,12,11)
t2 = datetime(2019, 1, 1,11,12,12)
print(t2 - t1)
# 格式化时间
print(t1.strftime("%Y年%m月%d日%H时%M分%S秒")) #把时间格式化成字符串
# 让用户输入两个时间,然后计算时间差
s1= input("请输入第一个时间：")
s2 = input("请输入第二个时间：")
# 用户输入的是字符串，需要转换成时间
# p表示parse转化,即str转化成时间,后面表示时间格式
t3=datetime.strptime(s1,"%Y-%m-%d %H:%M:%S")
t4=datetime.strptime(s2,"%Y-%m-%d %H:%M:%S")
# 计算时间差
print(t4 - t3)

# datetime:年月日时分秒
# date:年月日
# time:时分秒
print(date.today()) #获取当前日期
# 指定日期
print(date(2019, 1, 1))
