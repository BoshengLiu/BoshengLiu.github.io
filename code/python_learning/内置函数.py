'''
sorted(iterable[, cmp[, key[, reverse]]])
其中：
iterable：可迭代对象；
cmp：比较两个对象x和y，如果x > y返回正数，x < y 返回负数；x == y，返回0；比较什么由key决定。只适用于 python 2.x;
key：用来决定在排序算法中 cmp 比较的内容，key 可以是任何可被比较的内容，比如元组（python 中元组是可被比较的）;
reverse：排序规则, reverse = True(降序) 或者 reverse = False(升序，默认)
'''
# 有一个字典，根据字典中的属性值来排序，返回一个排好序的元组：
a = {'a': 1, 'e': 3, 'c': 5, 'f': 4, 'd': 6}
sorted_a = sorted(a.items(), key=lambda i: i[1])
# print(sorted_a)

# 给定一个只包含大小写字母、数字的字符串，对其进行排序，保证：
# 所有的小写字母在大写字母前面，所有的字母在数字前面，所有的奇数在偶数前面
b = 'Sorting1234'
sorted_b = "".join(sorted(b, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x)))
print(sorted_b)
# 这里，lambda函数将输入的字符转换为一个元组，然后sorted函数将根据元组（而不是字符）来进行比较，进而判断每个字符的前后顺序


'''
map(function, sequence[, sequence, ...]) -> list
返回将函数应用于参数序列项目的结果的列表。如果给出了多个序列，则使用由每个序列的对应项组成的参数列表调用该函数，如果并非所有序列都具有相同的长度，
则将None替换为缺失值。如果该函数为None，则返回序列项列表（如果有多个序列，则返回一个元组列表）。
'''
c = [39.2, 36.5, 37.3, 37.8]
map_c = [i for i in map(lambda x: (float(9) / 5) * x + 32, c)]
print(map_c)

d, e, f = [1, 2, 3, 4], [17, 12, 11, 10], [-1, - 4, 5, 9]
map_def = [i for i in map(lambda x, y, z: x + y + z, d, e, f)]
print(map_def)

'''
reduce(function, sequence[, initial]) -> value
从左到右，将两个自变量的函数累加到序列的各个项上，以将序列缩减为单个值。例如，reduce（lambda x，y：x + y，[1,2,3,4,5]）计算（（（（（1 + 2）+3）+4）+5）。如果存在initial，则将其放在计算中序列的项目之前，并在序列为空时用作默认值。
'''
from functools import reduce

d = lambda a, b: a if (a > b) else b
reduce_d = reduce(d, [47, 11, 42, 102, 13])
reduce_sub = reduce(lambda x, y: x + y, range(1, 101))
print(reduce_d)
print(reduce_sub)

'''
zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
返回一个元组列表，其中每个元组包含每个参数序列中的第i个元素。返回的列表的长度被截断为最短参数序列的长度。
'''
e1 = [1, 2, 3]
e2 = [4, 5, 6]
zip_e = [i for i in zip(e1, e2)]
print(zip_e)

'''
filter(function or None, sequence) -> list, tuple, or string
返回那些函数（项目）为真的序列项。如果function为None，则返回true。如果sequence是元组或字符串，则返回相同的类型，否则返回列表。
'''


def f(x):
    return x % 2 != 0 and x % 3 != 0


filter_f = [i for i in filter(f, range(2, 25))]
filter_g = [i for i in filter(lambda x: x != 'a', 'abcdef')]
print(filter_f)
print(filter_g)
