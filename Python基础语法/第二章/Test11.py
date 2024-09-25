# 文件操作必回技能
# 基本功


# 文件修改操作
'''
读取文件内容
把要修改的内容进行修改
把新内容写到一个副本文件中
把原来的文件删除
把副本文件重命名为原来的文件名
'''
with open("/workspace/Python基础语法/第二章/a.txt",mode="r",encoding="utf-8") as f, \
    open("/workspace/Python基础语法/第二章/a_副本.txt",mode="w",encoding="utf-8") as f1:
   for line in f:
       if "阿" in line:
           line=line.replace("阿","阿达")
    #    把数据写到副本文件中    
       f1.write(line)
# 删除原来的文件，必须借助os模块
# 导入os模块
import os   
# 删除文件
os.remove("/workspace/Python基础语法/第二章/a.txt") 
# 重命名文件
os.rename("/workspace/Python基础语法/第二章/a_副本.txt","/workspace/Python基础语法/第二章/a.txt")


# 读取规则文件
# 我们要对b.txt文件进行格式化读取，例如他是excel这类的文件
'''
[
    {"序号"：1，"部门"："python"，"人数"：100},
    {"序号"：2，"部门"："java"，"人数"：100},
    {"序号"：3，"部门"："c++"，"人数"：100}, 
]
'''
# 最终以上面格式的数据进行返回
# 1.打开文件
with open("/workspace/Python基础语法/第二章/b.txt",mode="r",encoding="utf-8") as f:
    # 第一行单独读取
    head=f.readline()
    # 把头处理成列表
    head_lst=head.split() #默认是空格切割
    print(head_lst)
    # 准备列表
    lst111=[]
    for line in f:
        # 切割数据
        data_lst=line.split()
        print(data_lst)
        # 现在把他们组装成字典
        # 准备字典
        dict={}
        # 拿到索引才能一一对应
        for i in range(len(head_lst)):
            # 向字典中添加数据
            dict[head_lst[i]]=data_lst[i]
        lst111.append(dict)
print(lst111)

