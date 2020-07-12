# 排序
# 一、冒泡排序
## 1. 介绍

## 2. 参考程序

```python
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

```

---

# 二、插入排序
## 1. 介绍

## 2. 参考程序

```python
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

```

---

# 三、快速排序
## 1. 介绍

## 2. 参考程序

```python
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

```

---

# 四、选择排序
## 1. 介绍

## 2. 参考程序

```python
def select_sort(list):
    n = len(list)
    for j in range(0,n-1):
        min_index = j
        for i in range(j+1,n):
            if list[min_index] > list[i]:
                min_index = i
        list[j],list[min_index] = list[min_index],list[j]

```

---

# 五、希尔排序
## 1. 介绍

## 2. 参考程序

```python
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

```




---

# 六、归并排序
## 1. 介绍

## 2. 参考程序

```python
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

```