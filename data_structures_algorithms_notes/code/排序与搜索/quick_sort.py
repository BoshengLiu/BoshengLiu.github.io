def quickSort(list):
    # 基线条件：为空或只包含一个元素的数组是“有序”的
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        # 由所有小于基准值的元素组成的子数组
        low = [i for i in list[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        high = [i for i in list[1:] if i > pivot]

        return quickSort(low) + [pivot] + quickSort(high)


if __name__ == '__main__':
    list = [65, 12, 33, 72, 5, 8, 45, 28]
    print(list)
    list = quickSort(list)
    print(list)
