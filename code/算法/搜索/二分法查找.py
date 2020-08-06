def binary_search(lists, item):
    """二分法查找元素-递归"""
    low, high = 0, len(lists) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lists[mid] == item:
            return mid
        elif item < lists[mid]:
            return binary_search(lists[:mid], item)
        else:
            return binary_search(lists[mid + 1:], item)
    return None


def binary_search_(lists, item):
    """二分法查找元素-非递归"""
    low, high = 0, len(lists) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lists[mid] == item:
            return mid
        elif item < lists[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


def search_left(lists, item):
    """查找第一个值等于给定值的元素"""
    low, high = 0, len(lists) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if item < lists[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(lists) and lists[low] == item:
        return low
    else:
        return None


def search_right(lists, item):
    """查找最后一个值等于给定值的元素"""
    low, high = 0, len(lists) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if item <= lists[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if high >=0 and lists[high] == item:
        return high
    else:
        return None


def search_first_large(lists, item):
    """查找第一个大于等于给定值的元素"""
    low, high = 0, len(lists) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if item < lists[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(lists) and lists[low] >= item:
        return low
    else:
        return None


def search_last_small(lists, item):
    """查找最后一个小于等于给定值的元素"""
    low, high = 0, len(lists) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if item <= lists[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if high >= 0 and lists[high] <= item:
        return high
    else:
        return None


def binary_test():
    """查找测试单元"""
    lists = [12, 31, 31, 31, 31, 33, 45, 54, 56, 65, 65, 65, 88, 99]

    # 二分法查找
    # print(binary_search(lists, 45))
    # print(binary_search(lists, 31))
    # print(binary_search_(lists, 45))
    # print(binary_search(lists, 100))

    # 查找第一个值等于给定值的元素
    # print(search_left(lists, 31))
    # print(search_left(lists, 44))
    # print(search_left(lists, 65))

    # 查找最后一个值等于给定值的元素
    # print(search_right(lists, 31))
    # print(search_right(lists, 44))
    # print(search_right(lists, 65))

    # 查找第一个大于等于给定值的元素
    # print(search_first_large(lists, 31))
    # print(search_first_large(lists, 44))
    # print(search_first_large(lists, 99))

    # 查找最后一个小于等于给定值的元素
    print(search_last_small(lists, 31))
    print(search_last_small(lists, 65))
    print(search_last_small(lists, 1))


if __name__ == '__main__':
    binary_test()
