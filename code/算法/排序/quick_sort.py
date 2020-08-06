import random


def quickSort(list):
    """分而治之"""
    # 基线条件：为空或只包含一个元素的数组是“有序”的
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        # 由所有小于基准值的元素组成的子数组
        low = [i for i in list[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        high = [i for i in list[1:] if i > pivot]

        return quickSort(low) + [pivot] + quickSort(high)


def quick_sort(lists, low, high):   # low = 0, high = len(lists) - 1
    """原地快排"""
    if low < high:
        # 取第一个元素为基准元素 pivot，j 表示小于 pivot 的下标，初始化 j 为0
        pivot, j = lists[low], low
        # 遍历数组，当数组的值小于 pivot 时，j 向右移动一位，j、i 位置交换元素
        # 当数组的值大于对比值时，j 位置不变，i 继续遍历
        # 遍历完的结果为：pivot [小于 pivot 的元素] [大于 pivot 的元素]
        # 此时 j 指向 [小于 pivot 的元素] 最后一个位置
        # 最后将 pivot 和 j 指向的元素交换位置
        for i in range(low + 1, high + 1):
            if lists[i] <= pivot:
                j += 1
                lists[j],lists[i] = lists[i],lists[j]
                print(lists)
        lists[low],lists[j] = lists[j],lists[low]

        # 递归
        quick_sort(lists,low,j-1)
        quick_sort(lists,j+1,high)

    return lists


def _partition(a, low: int, high: int):
    pivot, j = a[low], low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]  # swap
    a[low], a[j] = a[j], a[low]
    return j


if __name__ == '__main__':
    lists = [35, 12, 33, 72, 5, 8, 45, 28]
    # l1 = quickSort(lists)
    l2 = quick_sort(lists, 0, len(lists) - 1)
    # print(l2)
