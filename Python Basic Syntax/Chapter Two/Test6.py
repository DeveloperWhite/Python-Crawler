# 字典
# 基本数据类型dict
# 字典是一种映射类型，它的元素是键值对。{key1：value1，key2：value2.....}
# 这边的key1，key2，key3都是键，value1，value2，value3都是值
# 相当于key-value键值对，key是value的外号
# key－－hash运算－－位置
# 通常是拿key做hash运算，然后拿到位置，然后把value放在这个位置
# 下次再拿这个key来取值的时候，直接通过hash运算拿到位置，然后取出value
# key是不可变的数据类型，value是可变的数据类型
# 已知不可变（可哈希）的数据类型：int，bool，str，tuple
# 已知可变（不可哈希）的数据类型：list，dict，set
d= {123:"HEHE", True:"HAHA", "name":"ME", (1,2,3):123}
print(d)
m={"赵本山":123, "宋丹丹":456, "范伟":789}
# 通过key获取value
print(m["赵本山"]) #123

# 字典的增删改查
c={"name":"ME", "age":18, "sex":"男"}
# 增
c["height"]=180 #添加一个键值对
print(c)
# 另一种添加方式（这边会先判断是否存在）
c.setdefault("weight",120) #这边的key必须是不存在的，不然这个新增流程就不走了
print(c)
# 改
c["name"]="YOU" #修改一个键值对
print(c)
# 删
c.pop("sex") #删除一个键值对
print(c)
del c["age"] #删除一个键值对
print(c)
# 查
# 如果key不存在，则返回None，这边不会报错
print(c.get("name")) #通过get方法获取值
# 如果key不存在，直接报错
print(c["name"]) #获取所有的key

# 特殊的查询（setdefault会在执行完新增流程后根据key查value）
print(c.setdefault("name")) 

# 练习
# 【11，22，33，44，55，66，77，88，99】
# 分类，把大于50的放在一个集合，把小于等于50的放在一个集合
lst=[11,22,33,44,55,66,77,88,99]
result={} #放结果
# 第一套算法
# 遍历列表元素
for i in lst:
    if i>50:
        # 判断有无列表，没有就创建一个,这边用get来查询
        if result.get("大于50") ==None:
            result["大于50"]=[i]
        else:
        # 有这个列表，就往这个列表里面添加元素
            result["大于50"].append(i)
    else:
        if result.get("小于等于50") ==None:
            result["小于等于50"]=[i]
        else:
        # 有这个列表，就往这个列表里面添加元素
            result["小于等于50"].append(i)
print(result)

# 第二套算法
for i in lst:
    if i>50:
        # 这边能直接用setdefault，因为setdefault会先判断有无这个key
        # 有这个key，就返回这个key对应的value，没有这个key，就返回None，然后setdefault会自动创建这个key，然后把None赋值给这个key
        result.setdefault("大于50",[]).append(i)
    else:
        result.setdefault("小于等于50",[]).append(i)
print(result)


# 字典的循环
# 可以通过key来拿到value，不可以通过value来拿到key
f= {"name":"ME", "age":18, "sex":"男"}
# 第一种for循环
for key in f:
    print(key)
    print(f[key])

# 第二种借助keys()方法，通过这个方法获取所有的key
for key in f.keys():
    print(key)
    # 拿到了所有的key，然后就可以通过key拿到value了
    print(f[key])

# 第三种借助values()方法，通过这个方法获取所有的value
for value in f.values():
    print(value)

# 第四种借助items()方法，通过这个方法获取所有的键值对
# 这边items是元祖，直接通过解构直接拿到key和value
for key,value in f.items():
    print(key)
    print(value)

# 字典的嵌套
dict1={
    "name":"ME",
    "age":18,
    "sex":"男",
    "hobby":["篮球","足球","乒乓球"],
    "family":{
        "father":"赵本山",
        "mother":"宋丹丹",
        "brother":["范伟"]
    }
}
print(dict1)
print(dict1["family"]["father"])
# 给brother加一个值
dict1["family"]["brother"].append("刘能")
print(dict1)
# 这边给age加上一岁
dict1["age"]+=1
print(dict1)


