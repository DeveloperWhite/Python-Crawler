# json模块(非常重要)
# json举例(前端叫json，Python后端叫字典)
"""
wf={
    "name":"汪峰",
    "age":18,
    "hobby":"上头条",
    "wife":{
        "name":"子怡",
        "age":18,
        "hobby":["跳舞","唱歌","演戏"]
    }
}
"""
import json
# 1.把python字典或者列表转换成json字符串
dic = {
    "name":"汪峰",
    "age":18,
    "hobby":"上头条",
    "wife":{
        "name":"子怡",
        "age":18,
        "hobby":["跳舞","唱歌","演戏"]
    }
}
# 比如我们字典是中文的，那么我们用ensure_ascii=False，这样就不会把中文转成ascii码了
s=json.dumps(dic,ensure_ascii=False)
print(s,type(s))
# 2.把前端json字符串转换成python字典或者列表
s1='{"name": "汪峰", "age": 18, "hobby": "上头条", "wife": {"name": "子怡", "age": 18, "hobby": ["跳舞", "唱歌", "演戏"]}}'
d=json.loads(s1)
print(d,type(d))
print(d["wife"]["name"])

# 1.dumps()把python字典或者列表转换成json字符串
# 2.loads()把前端json字符串转换成python字典或者列表

# 前端的json和后端的python字典或者列表的区别
# 前端：
# {"id": 1, "isLogin": true, "hasGirl": null}
# 字典
d={"id":1,"isLogin":True,"hasGirl":None}
# 可以看出数据类型写法不一样
print(json.dumps(d))

# 列表一样可以这样转化
lst=["张三","李四","王五"]
m=json.dumps(lst,ensure_ascii=False)
print(m,type(m))

# json写入文件中
# json.dump(dic,open("wf.txt",mode="w",encoding="utf-8"),ensure_ascii=False)
m2=json.load(open("wf.txt",mode="r",encoding="utf-8"))
print(m2,type(m2))