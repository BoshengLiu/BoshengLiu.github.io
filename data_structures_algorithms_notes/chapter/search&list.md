# 搜索
# 二分法查找
## 1. 介绍
&#8195; 二分查找针对的是一个有序的数据集合，查找思想有点类似分治思想。每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为 0。

&#8195; 举个例子，我们假设有 10 个订单，订单金额分别是：8，11，19，23，27，33，45，55，67，98。还是利用二分思想，每次都与区间的中间数据比对大小，缩小查找区间的范围。其中，low 和 high 表示待查找区间的下标，mid 表示待查找区间的中间元素下标。

![](https://upload-images.jianshu.io/upload_images/16911112-2b4993a5056d6ac9.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 二分查找是一个非常高效的查找方式，它的时间复杂度只有 log(n)。我们假设数据大小是 n，每次查找后数据都会缩小为原来的一半，也就是会除以 2。最坏情况下，直到查找区间被缩小为空，才停止。

![](https://upload-images.jianshu.io/upload_images/16911112-da11950120617ed0.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 可以看出来，这是一个等比数列。其中 $n/2^k=1$ 时，k 的值就是总共缩小的次数。而每一次缩小操作只涉及两个数据的大小比较，所以，经过了 k 次区间缩小操作，时间复杂度就是 O(k)。通过 $n/2^k=1$，我们可以求得 $k=log_2n$，所以时间复杂度就是 O(logn)。

## 2. 局限性
### 2.1 注意事项
**1. 循环退出条件<br>**

&#8195; 注意是 low<=high，而不是 low<high。

**2.mid 的取值**<br>

&#8195; 实际上，mid=(low+high)/2 这种写法是有问题的。因为如果 low 和 high 比较大的话，两者之和就有可能会溢出。改进的方法是将 mid 的计算方式写成 low+(high-low)/2。更进一步，如果要将性能优化到极致的话，我们可以将这里的除以 2 操作转化成位运算 low+((high-low)>>1)。因为相比除法运算来说，计算机处理位运算要快得多。

**3.low 和 high 的更新**<br>

&#8195; low=mid+1，high=mid-1。注意这里的 +1 和 -1，如果直接写成 low=mid 或者 high=mid，就可能会发生死循环。比如，当 high=3，low=3 时，如果 a[3]不等于 value，就会导致一直循环不退出。

### 2.2 局限性
**1. 首先，二分查找依赖的是顺序表结构，简单点说就是数组。**

&#8195; 主要原因是二分查找算法需要按照下标随机访问元素。我们在数组和链表那两节讲过，数组按照下标随机访问数据的时间复杂度是 O(1)，而链表随机访问的时间复杂度是 O(n)。所以，如果数据使用链表存储，二分查找的时间复杂就会变得很高。二分查找只能用在数据是通过顺序表来存储的数据结构上。如果你的数据是通过其他数据结构存储的，则无法应用二分查找。

**2. 其次，二分查找针对的是有序数据。**

&#8195; 二分查找对这一点的要求比较苛刻，数据必须是有序的。如果数据没有序，我们需要先排序。前面讲到排序的时间复杂度最低是 O(nlogn)。所以，如果我们针对的是一组静态的数据，没有频繁地插入、删除，我们可以进行一次排序，多次二分查找。这样排序的成本可被均摊，二分查找的边际成本就会比较低。

&#8195; 但是，如果我们的数据集合有频繁的插入和删除操作，要想用二分查找，要么每次插入、删除操作之后保证数据仍然有序，要么在每次二分查找之前都先进行排序。针对这种动态数据集合，无论哪种方法，维护有序的成本都是很高的。所以，二分查找只能用在插入、删除操作不频繁，一次排序多次查找的场景中。针对动态变化的数据集合，二分查找将不再适用。

**3. 再次，数据量太小不适合二分查找。**

&#8195; 如果要处理的数据量很小，完全没有必要用二分查找，顺序遍历就足够了。比如我们在一个大小为 10 的数组中查找一个元素，不管用二分查找还是顺序遍历，查找速度都差不多。只有数据量比较大的时候，二分查找的优势才会比较明显。

&#8195; 不过，这里有一个例外。如果数据之间的比较操作非常耗时，不管数据量大小，我都推荐使用二分查找。比如，数组中存储的都是长度超过 300 的字符串，如此长的两个字符串之间比对大小，就会非常耗时。我们需要尽可能地减少比较次数，而比较次数的减少会大大提高性能，这个时候二分查找就比顺序遍历更有优势。

**4. 最后，数据量太大也不适合二分查找。**

&#8195; 二分查找的底层需要依赖数组这种数据结构，而数组为了支持随机访问的特性，要求内存空间连续，对内存的要求比较苛刻。比如，我们有 1GB 大小的数据，如果希望用数组来存储，那就需要 1GB 的连续内存空间。

&#8195; 注意这里的“连续”二字，也就是说，即便有 2GB 的内存空间剩余，但是如果这剩余的 2GB 内存空间都是零散的，没有连续的 1GB 大小的内存空间，那照样无法申请一个 1GB 大小的数组。而我们的二分查找是作用在数组这种数据结构之上的，所以太大的数据用数组存储就比较吃力了，也就不能用二分查找了。

## 3. 参考程序

* 二分查找-递归

```python
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

```

* 二分查找-非递归

```python
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

```

## 4. 拓展
### 4.1 查找第一个值等于给定值的元素

&#8195; 比如下面这样一个有序数组，其中，a[5]，a[6]，a[7]的值都等于 8，是重复的数据。我们希望查找第一个等于 8 的数据，也就是下标是 5 的元素。

![](https://upload-images.jianshu.io/upload_images/16911112-6c3f3921f0543845.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&#8195; 如果我们使用二分法查找，那么得到的结果是下标为 7 的 8，虽然结果是8，但并不是我们需要找的 8，所以我们要在二分法的基础上进行修改。

* 参考程序

```python
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

```


### 4.2 查找最后一个值等于给定值的元素

* 参考程序

```python
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

```


### 4.3 查找第一个大于等于给定值的元素

* 参考程序

```python
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

```

### 4.4 查找最后一个小于等于给定值的元素

* 参考程序

```python
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

```






