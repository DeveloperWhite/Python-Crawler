# 格式化输出
# 输入下列格式
'''
-----------------info of Sylar-----------
Name: Sylar
Age: 18
Job: Student
Hobby: Singing
---------------------end-----------------
'''
# 请编写程序，输出以上格式,下面打印的效果不太好
Name=input("请输入姓名:")
Age=input("请输入年龄:")
Job=input("请输入职业:")
Hobby=input("请输入爱好:")
'''
print("-----------------info of"+name+"-----------------")
print("Name:"+name)
print("Age:"+age)
print("Job:"+job)
print("Hobby:"+hobby)
print("---------------------end-----------------")
'''
# 字符串格式化输出(比较老的方法)
s="""-----------------info of %s-----------
Name: %s
Age: %s
Job: %s
Hobby: %s
---------------------end-----------------
"""%(Name,Name, Age, Job, Hobby)
print(s)
# %s表示字符串占位，%d表示整数占位，%f表示浮点数，f前面数字表示小数点后保留几位
print("我的名字叫%s,今年%d岁,我的职业是%s,我的爱好是%s"%("周杰伦",28,"teacher","football"))
# 字符串格式化输出(比较新的方法)py3.5
# f-string
name="周杰伦"
age=28
job="teacher"
hobby="football"
print(f"我的名字叫{name},今年{age}岁,我的职业是{job},我的爱好是{hobby}")

