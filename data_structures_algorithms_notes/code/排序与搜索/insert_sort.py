'''插入排序'''
def insert_sort(list):
    n = len(list)
    for j in range(1,n):
        i = j
        while i > 0:
            if list[i] < list[i-1]:
                list[i],list[i-1] = list[i-1],list[i]
                i -= 1
            else:
                break

#i代表能蹭循环起始值
#i=j执行从右边的无序序列中取出第一个元素，即i位置，插入前面正确的位置

if __name__ == '__main__':
    list = [65, 12, 33, 72, 5, 8, 45, 28]
    print(list)
    insert_sort(list)
    print(list)