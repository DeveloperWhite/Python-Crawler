# while循环
'''
while 条件：
    循环体
    '''
'''
while True:
    print("hello world")
    '''
i=0
while i<10:
    print(i)
    i+=1
    
# 累加计算
i=0
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)

# 结束循环
# 第一种方式
flag=True
while flag:
    content=input("请输入你要说的话(q退出):")
    if content=="q":
        flag=False
    else:    
        print("你输入的内容是："+content) 


# 流程控制break和continue
# 第二种方式，优雅的退出循环（break）
# break表示立即跳出循环
# continue表示停止本次循环，继续执行下次循环
# 无限喷人
while True:
    content=input("请输入你要发给打野的话(q退出):")
    if content=="q":
        break   
    print("我想对打野说的话是："+content)

# 换成continue
# 结束当前循环，继续执行下次循环
while True:
    content=input("请输入你要发给打野的话(q退出):")
    if content=="q":
        continue   
    print("我想对打野说的话是："+content)
