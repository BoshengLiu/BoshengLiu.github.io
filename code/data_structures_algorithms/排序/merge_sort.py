'''归并排序'''


def merge_sort(list):
    n = len(list)
    if n <= 1:
        return
    mid = n // 2  # 拆分序列
    # left采取归并排序后形成的有序的新的列表
    left_list = merge_sort(list[:mid])
    # right采取归并排序后形成的有序的新的列表
    rigth_list = merge_sort(list[mid:])

    # 将两个子序列合并成一个新的整体
    left_point, right_point = 0, 0
    result = []
    while left_point < len(left_list) and right_point < len(rigth_list):
        if left_list[left_point] < rigth_list[right_point]:
            result.append(left_list[left_point])
            left_point += 1
        else:
            result.append(rigth_list[right_point])
            right_point += 1

    result += left_list[left_point]
    result += rigth_list[right_point]
    return result


if __name__ == '__main__':
    list = [65, 12, 33, 72, 5, 8, 45, 28]
    print(list)
    merge_sort(list)
    print(list)
