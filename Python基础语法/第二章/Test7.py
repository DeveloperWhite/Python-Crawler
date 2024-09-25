# 基本数据类型set
# set集合是无序的，不重复的元素集合
# set={"皮长山","李长山","皮长山"}
# 会去除重复的元素，集合的主要用途是去重
# print(set)
# 因为lst中存在重复的元素，所以去重后只有两个元素
lst=[11,22,11]
print(lst)
s=set(lst)
print(s)
# set集合的交集，并集，差集
zhangsan={"上海","北京","广州","深圳"}
lisi={"北京","广州","杭州","深圳"}
# 交集
print(zhangsan&lisi)
# 并集
print(zhangsan|lisi)
# 差集
print(zhangsan-lisi)

# 集合的增删改查
# 增
s=set()
s.add("皮长山")
s.add("李长山")
s.add("皮长山")
print(s)
# 删
s.remove("皮长山")
print(s)
# 改（没有所谓的改，这里只能先把要改的删除在加上新的）
# 查询
for i in s:
    print(i)

