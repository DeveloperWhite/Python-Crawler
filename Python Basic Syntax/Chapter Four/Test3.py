# pickle模块
# 把python对象写入到文件中，而文件只能看懂bytes字节流，所以pickle模块把python对象转化成bytes字节流，再写入到文件中
import pickle
lst= ["张三","李四","王五","赵六","田七","孙八"]
# 转化为bytes流(字节)
bs=pickle.dumps(lst)
print(bs)
# 从bytes流(字节)中还原出python对象
lst2=pickle.loads(bs)
print(lst2)
# 现在需要把账号密码写到文件中
# dic = {"name":"张三","password":123}
# pickle.dump(dic,open("d.data","wb"))
# 从文件中读取账号密码
dic2 = pickle.load(open("d.data","rb"))
print(dic2)

# 1.dumps：将python对象转化为bytes流
# 2.loads：将bytes流转化为python对象
# 3.dump：将python对象写入文件中
# 4.load：从文件中读取python对象
