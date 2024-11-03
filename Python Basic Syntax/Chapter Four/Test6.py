# shutil模块
# 主要封装了文件和文件夹的操作,包括复制,移动,删除等
import shutil
# 把dir1中的a.txt文件移动到dir2中
shutil.move("dir1/a.txt","dir2")
# 复制两个文件句柄
f1=open("dir2/a.txt",mode="rb")
f2=open("dir1/b.txt",mode="wb")
