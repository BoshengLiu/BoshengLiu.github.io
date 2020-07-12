# 变量类型
## 1. Python变量的定义和使用
### 1.1 Python变量的赋值
Python 使用'='来实现赋值，在 Python 中，变量是不需要自己定义的，可以是数值、字符串、url、表达式等等。如下所示：

```python
a = 100
b = 'python'
c = 'www.python.org'
c = lambda x : x+2
```

### 1.2 Python变量的定义
在 Python 中，变量名就像指针一样指向数据，举个例子：
```python
a = 'python'
b = 'python'
print(id(a),id(b))
```
&#8195; 从运行结果可以发现它们的 id 是一样的，说明 a 和 b 都指向`python`这个数据。

* 让我们继续下去
```python
a = 'C++'
d = b
b = a
print(d,b)
```
此时 a 指向了'C++'这个数据，同时 d 指向了`python`，而 b 指向了`C++`。

* 解释：
    * 一开始 a 和 b 是指向`python`这个数据；
    * 然后 a 指向`C++`这个数据，此时`python`这个数据依然存在，只是没有变量指向它；
    * 接着 d 指向 b，又因为 b 指向`python`，所以 d 指向了`python`；
    * 最后 b 指向 a，又因为 a 指向`C++`，所以 b 指向了`C++`。



---

# 运算符




