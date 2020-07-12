'''冒泡排序'''

def bubble_sort(list):
    n = len(list)
    count = 0
    for j in range(n-1):
        for i in range(n-1-j):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                count += 1
        if count == 0:
            return

#list有n个数，需要进行n-1次排序
#从左往右排序，第一次排序移动n-2次，第二次排序移动n-3次...

if __name__ == '__main__':
    list = [65,12,33,72,5,8,45,28]
    print(list)
    bubble_sort(list)
    print(list)