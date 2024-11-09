# traceback模块:用来打印异常信息
import traceback
import logging
'''
try:
    print(1/0)
except:
    print("程序出错了")
    print(traceback.format_exc()) #打印异常信息
print("程序继续执行")
'''

# 下面模仿真实开发中,这几个模块的用法,完整异常处理流程
# 准备好记录日志的文件
logging.basicConfig(filename="x2.txt",encoding="utf-8",
                    format="%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=10) #当前配置表示10以上分数的错误都会被记录,记录文件日志中的最低等级,一般记录为0,能记录所有错误
#正常写程序
try:
    print(1/0)
except:
    print("程序出错了")
    logging.error(traceback.format_exc()) #打印异常信息,写入日志
print("程序继续执行")