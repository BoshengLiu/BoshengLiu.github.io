'''选择排序'''
def select_sort(list):
    n = len(list)
    for j in range(0,n-1):
        min_index = j
        for i in range(j+1,n):
            if list[min_index] > list[i]:
                min_index = i
        list[j],list[min_index] = list[min_index],list[j]

#将最左边的的值作为初始值与右边的值进行对比，当右边的值小于初始值，交换元素，直到整个右边对比完
#将对比的结果作为最左边的值，从第二位开始，重复第一步的步骤

if __name__ == '__main__':
    list = [65, 12, 33, 72, 5, 8, 45, 28]
    print(list)
    select_sort(list)
    print(list)
