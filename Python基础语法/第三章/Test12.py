# 获取一个数的平方
def func(n):
    return n**2
print(func(2)) #
# 匿名函数又被称为lambda表达式
# 多个参数用逗号隔开
# 若要返回多个数据要加上括号
# lambda 参数列表:返回值
fn=lambda n:n**2
print(fn(2)) #4
fn1=lambda a,b:(a+b,a-b)
print(fn1(2,3)) #(5, -1)