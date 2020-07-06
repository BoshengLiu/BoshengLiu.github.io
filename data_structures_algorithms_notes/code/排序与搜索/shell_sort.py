'''希尔排序'''
def shell_sort(list):
    n = len(list)
    gap = n // 2
    while gap > 0:
        for j in range(gap,n):
            i = j
            while i > 0:
                if list[i] < list[i-gap]:
                    list[i],list[i-gap] = list[i-gap],list[i]
                    i -= gap
                else:
                    break

if __name__ == '__main__':
    list = [65, 12, 33, 72, 5, 8, 45, 28]
    print(list)
    shell_sort(list)
    print(list)