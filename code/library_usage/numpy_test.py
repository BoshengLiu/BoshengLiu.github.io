import numpy
from numpy import pi

# file_content = numpy.genfromtxt("numpy_test.txt",delimiter=",",dtype=str)
# print(help(numpy.genfromtxt))

vector = numpy.array([1,2,4,8])
matrix = numpy.linspace(0,2*pi,50)

A = numpy.array([[1,1],[0,1]])
B = numpy.array([[2,0],[3,4]])
C = numpy.floor(10*numpy.random.random((3,4)))
D = numpy.floor(10*numpy.random.random((4*16)))
E = numpy.arange(12)

# print(vector)
# print(matrix[:,1])    #取出第二列元素为横向量
# print(matrix[0:2,0:2])    #取出前两列元素为新的矩阵

# print((matrix == 10) | (matrix ==5))  #判断矩阵内的元素是否有10和5，符合的值为true，否则为false

# a1 = numpy.zeros(5)
# print(a1)
# a2 = numpy.ones(4)
# print(a2)
# a3 = numpy.random.random((6)).reshape(3,2)
# print(a3)
# a4 = numpy.zeros((2,3))
# print(a4)

# print(matrix.shape)
# print(vector.shape)

# print(A)
# print('-'*10)
# print(B)
# print('-'*10)
# print(A*B)
# print('-'*10)
# print(A.dot(B))

# data = numpy.sin(numpy.arange(20)).reshape(5,4)
# print(data)
#
# ind = data.argmax(axis=0)
# print(ind)
#
# data_max = data[ind,range(data.shape[1])]
# print(data_max)

# F = numpy.tile(A,(3,2))
# print(F)

G = numpy.sort(B, axis=1)   #对矩阵B的数值按行正序
print(G)

