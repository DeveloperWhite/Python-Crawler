#简单爬虫，爬取网站：https://movie.douban.com/top250
# 1.从服务器拿到网页的源代码(urllib.request)
from urllib.request import Request , urlopen
def get_html(url):
    # 1.准备请求信息，请求头User-Agent
    # 如果反爬，就把浏览器请求信息一个个往里面加，更加真实的模仿浏览器的行为
    r = Request(url, headers={
        # 模拟浏览器
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    })
    # 2.发送请求，获取响应
    html = urlopen(r)
    # 下面的编码格式每个网址都不一样，需要自己试
    return html.read().decode("utf-8")

# 2.从网页源代码中提取出我们需要的信息(re)
import re
# 我要获取排名，电影名，评分，评价人数
def parse_html(html):
    obj =re.compile(r'<div class="item">.*?<em class="">(?P<rate>.*?)</em>.*?'
                    r'<span class="title">(?P<Title>.*?)</span>.*?'
                    r'<span class="rating_num" property="v:average">(?P<rating_num>.*?)</span>.*?'
                    r'<span>(?P<person_num>.*?)人评价</span>',re.S)
    # re.S可以让正则中的.匹配换行符
    res=obj.finditer(html)
    lst=[]
    for i in res:
        # 返回一个字典
        dic=i.groupdict()
        lst.append(dic)
    return lst

# 启动函数
def main():
    # 写入文件中
    f=open("top250.xlsx",mode="w",encoding="utf-8")
    # 用来分页，获取不同页数的数据
    for i in range(10):
        s=get_html(f"https://movie.douban.com/top250?start={i*25}&filter=")
        result=parse_html(s)
        for d in result:
            # 写入一条数据，换行
            f.write(str(d))
            f.write("\n")

main()
