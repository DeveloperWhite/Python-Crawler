# shutil模块
# 主要封装了文件和文件夹的操作,包括复制,移动,删除等
import shutil
# 把dir1中的a.txt文件移动到dir2中
# shutil.move("dir1/a.txt","dir2")
# 复制两个文件句柄
f1=open("dir2/a.txt",mode="rb")
f2=open("dir1/b.txt",mode="wb")
# 文件复制
# shutil.copyfileobj(f1,f2)
# 指定两个文件路径来进行复制，参数1是源文件路径，参数2是目标文件路径
# shutil.copyfile("dir2/a.txt","dir1/c.txt")
# 不但要复制文件内容，还要复制文件权限
# shutil.copy("dir2/a.txt","dir1/d.txt")
# 复制文件的内容，权限和修改时间
# shutil.copy2("dir2/a.txt","dir1/e.txt")
# 修改时间，权限复制
# shutil.copystat("dir2/a.txt","dir1/e.txt")
# 只复制权限(从一个文件复制到另一个文件)
# shutil.copymode("dir2/a.txt","dir1/e.txt")
# 复制文件夹
# shutil.copytree("dir1","dir3")
# 删除文件夹
# shutil.rmtree("dir3")