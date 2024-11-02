lst=[11,25,34,78,99,265]
n=int(input('请输入一个数字：'))
# 这套逻辑写起来跟简单，执行效率低
'''
for item in lst:
    if item==n:
        print('找到了')
        break
else:
    print('没找到')
    '''
# 二分法查找
left=0
right=len(lst)-1 #最大索引号
# 核心：跟中间去比较
'''
while left<=right:
    # //代表整除，不然会出现小数
    mid = (left + right) // 2
    if n>lst[mid]: #如果n大于中间值，说明n在右边
        left=mid+1
    elif n<lst[mid]: #如果n小于中间值，说明n在左边
        right=mid-1
    else:
        print('找到了',mid)
        break
else:
    print('没找到')
'''
# 递归版本做法
def binary_search(lst,n,left,right):
    if left>right:
        print('没找到')
        return
    mid = (left + right) // 2
    if n>lst[mid]: #如果n大于中间值，说明n在右边
        left=mid+1
    elif n<lst[mid]: #如果n小于中间值，说明n在左边
        right=mid-1
    else:
        print('找到了',mid)
        return
    binary_search(lst,n,left,right)   #进入递归
binary_search(lst,n,left,right)
