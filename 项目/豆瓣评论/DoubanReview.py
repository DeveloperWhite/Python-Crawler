import requests
def get_html(url):
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
  }
  resp=requests.get(url,headers=headers)
  return resp.text


import re
def page_get(html):
    # 获取电影名，评论人，评论时间
    obj=re.compile(r'< img alt="(?P<FilmTitle>.*?)" title=".*?'
                  r'class="name">(?P<Commentator>.*?)</a >.*?'
                  r'<div class="short-content">(?P<Comment>.*?)&nbsp;.*?'
                  r'class="main-meta">(?P<CommentTime>.*?)</span>.*?',re.S)
    res=obj.finditer(html)
    lst = []
    for i in res:
        # 返回一个字典
        dic = i.groupdict()
        # 去除 <p class="spoiler-tip"> 这部分
        comment = re.sub(r'<p class="spoiler-tip">.*?</p >', '', dic['Comment'],flags=re.S).strip()
        dic['Comment'] = comment
        lst.append(dic)
    return lst
# 启动函数
def main():
    # 写入文件中
    f=open("comment.xlsx", mode="w", encoding="utf-8")
    # 用来分页，获取不同页数的数据
    for i in range(5):
        s=get_html(f"https://movie.douban.com/review/best/?start={i*20}")
        # print(s)  # 打印请求的 URL
        result=page_get(s)
        for d in result:
            # 写入一条数据，换行
            f.write(str(d))
            f.write("\n")

main()