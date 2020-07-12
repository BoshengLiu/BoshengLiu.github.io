# 搜索
# 一、二分法查找
## 1. 介绍
## 2. 参考程序

```python
def binary_search(list, item):
    n = len(list)
    if n > 0:
        mid = n // 2
        if list[mid] == item:
            return True
        elif item < list[mid]:
            return binary_search(list[:mid], item)
        else:
            return binary_search(list[mid+1:], item)
    return False

```
