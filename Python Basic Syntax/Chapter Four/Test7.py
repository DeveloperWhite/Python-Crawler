# logging模块
# 日志模块
# 1.导入日志模块
import logging
# filename:文件名
# format:数据的格式化输出,最终在日志文件中的样子
# 时间-名称-级别-模块:错误信息
# datefmt:时间格式
# level:错误的级别权重,当错误的级别大于等于这个值的时候才会被记录
logging.basicConfig(filename="log.txt",encoding="utf-8",
                    format="%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=10) #当前配置表示10以上分数的错误都会被记录,记录文件日志中的最低等级,一般记录为0,能记录所有错误
# 2.记录日志
logging.critical("这是一个致命错误") #最高级别日志信息 50
logging.error("这是一个错误") # 普通程序错误 40
logging.warning("这是一个警告") # 警告 30
logging.info("这是一个信息") # 普通信消息 20
logging.debug("这是一个调试信息") # 最低等级的调试信息 10

# 日志归类
# 创建一个操作日志的对象logger(依赖FileHandler)
file_handler = logging.FileHandler("l1.log",'a',encoding="utf-8")
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s"))
logger1 = logging.Logger("s1系统",level=10) #创建一个操作日志的对象
logger1.addHandler(file_handler) #给日志对象设置文件信息

# 创建一个操作日志的对象logger(依赖FileHandler)
file_handler2 = logging.FileHandler("l2.log",'a',encoding="utf-8")
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s"))
logger2 = logging.Logger("s2系统",level=10) #创建一个操作日志的对象
logger2.addHandler(file_handler2) #给日志对象设置文件信息


# 项目一出错
logger1.error("我是A系统")
# 项目二出错
logger2.error("我是B系统")

# 日志级别不够用
logger1.log(11,"没事")