# 异常处理:程序运行时候,发生的错误
"""
try:
     print(1/0)
except:
     print("出错了")
"""
"""
try:
     try-代码
except: 错误1 as 变量1:
     except1代码
except: 错误2 as 变量2:
     except2代码
except: Exception as e: #表示所有异常的根,上面都不符合就是这个
     最终代码
"""
try:
    # print(1/0)
    # open("hehehehehe",mode="r").read() #文件不存在报错
    lst = []
    # lst.__iter__().next()
except ZeroDivisionError as e:
    print("除数不能为0")
except FileNotFoundError as e: #文件不存在报错
    print("文件不存在")
except Exception as e: #万能报错
    print("系统错误")
finally:
    print("不管有没有错,都执行我")  # 无论是否报错,都执行,相当于收尾

# 程序可以自己抛出异常raise
def func(a,b): #a,b必须为整数
    if type(a) == int and type(b) == int:
         return a+b
    else:
        raise Exception("参数类型错误") #抛出异常
func("hehe",2)

