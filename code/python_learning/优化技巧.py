# 字符串操作，使用"join"代替'+'
s_list = [i for i in "abc"]
s = "".join(s_list)
print(s_list)

# 字典按键值进行排序
s_dict = {'a': 123, 'b': 45, 'c': 245, 'd': 12}
values_sorted = sorted(s_dict.items(), key=lambda d: d[1], reverse=False)
print(values_sorted)
# 字典按键进行排序
keys_sorted = sorted(s_dict.items(), key=lambda d: d[0], reverse=False)
print(keys_sorted)
