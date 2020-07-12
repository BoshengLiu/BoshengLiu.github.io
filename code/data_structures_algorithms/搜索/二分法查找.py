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


if __name__ == '__main__':
    list = [12, 33, 45, 65, 88, 99, 54]
    print(binary_search(list, 12))
    print(binary_search(list,100))
