import random
# random模块
print(random.random()) # 0-1之间的随机数
print(random.uniform(1, 10)) # 1-10之间的随机小数
print(random.randint(1, 10)) # 1-10之间的随机整数，能取到边界
lst = ["张三","李四","王五","赵六","田七","孙八"]
print(random.choice(lst)) # 随机从列表中取一个元素
print(random.sample(lst, 2)) # 随机从列表中取两个元素
# 练习题
# 随机生成四位验证码
# 可能会有数字，可能会有大写字母，可能会有小写字母，并转化成字符串，大小写字母范围是65-90，97-122
lst = []
def rand_num():
    return str(random.randint(0, 9))
def rand_upper():
    return chr(random.randint(65, 90))
def rand_lower():
    return chr(random.randint(97, 122))
# 每一位都有可能是数字，大写字母，小写字母
def rand_verify_code(n=4):
    for i in range(n):
        which = random.randint(1, 3)
        if which == 1:
            s = rand_num()
        elif which == 2:
            s = rand_upper()
        elif which == 3:
            s = rand_lower()
        lst.append(s)
    return "".join(lst)
print(rand_verify_code())
