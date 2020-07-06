# numpy使用教程
* 打开 .txt文件，建议用pandas库

        file_content = numpy.genfromtxt("numpy_test.txt",delimiter=",",dtype=str)

* 数组以及向量

        vector = numpy.array([1, 2, 4, 8])     #生成向量
        matrix = numpy.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 1, 2]])      #生成4x3的矩阵
        vector.shape        #结果为(4,)
        matrix.shape        #结果为(4x3)，查看矩阵的阶数（行x列）
        注：矩阵的下标从0开始，和列表一样
         
* dtype操作

        要求array里面的元素都是一种类型，如：
        numbers = numpy.array([1, 2, 3, 4.0])
        numbers.dtype   #结果将所有的元素都转换为float型

* 矩阵的截取

        matrix = numpy.array([[1, 2, 3],[4, 5, 6],[7, 8, 9])
        matrix[:,1]     #取出第二列的所有元素为数组
        matrix[:,0:2]    #取出前两列元素为新的矩阵
        matrix[0:2,:]    #取出前两行元素为新的矩阵
        matrix[1][1]    #查看矩阵第2行第2列的元素
        注：[a:b,x:y]，其中a、b为行，x、y为列

* 矩阵元素的判断

        matrix = numpy.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
        matrix == 10    #判断所有的元素是否为10，是为True，否为false
        matrix == 10 | matrix == 5  #判断矩阵内的元素是否有10和5，符合的值为true，否则为false

* 矩阵生成

        numpy.zeros(5)      #生成5个0的数组
        numpy.ones(4)       #生成4个1的数组
        numpy.zeros((2,3))  #生成2x3的矩阵，元素为0
        numpy.random.random((6)).reshape(3,2)   #生成一个3x2的矩阵，元素为随机数
        numpy.arange(0,40,5,dtype=numpy.int32)  #生成0到40之间5的倍数
        numpy.arange(12)    #生成0-11共12个数
        numpy.linspace(0,2*pi,50)   #在0到2π之间生成50间隔相等的数

* 矩阵操作

        对于矩阵A、B
        A*B:        #叉乘操作，即对应位置相乘
        A.dot(B)    #点乘操作，也可以写成numpy.dot(A,B)
        C = A       #对C进行赋值，C替代A，指向同一个对象
        A.view()    #对A进行浅拷贝（不推荐使用）
        A.copy()    #对A进行复制，两个指向不同的对象
        numpy.tile(A,(3,2))     #对矩阵A进行复制，复制成3x2的矩阵
        
* 矩阵的常用函数(B)

        numpy.exp(B)            #对矩阵B进行e的幂次方操作
        numpy.sprt(B)           #对矩阵B进行开方操作
        numpy.floor(10*numpy.random.random((3,4)))  #生成一个3x4的矩阵，元素向下取整
        B.ravel()               #将矩阵转换为向量
        B.T                     #将矩阵进行转置
        numpy.vstack((A,B))     #将矩阵按照行拼接
        numpy.hstack((A,B))     #将矩阵按照列拼接
        numpy.vsplit(D,4)       #将矩阵按照行平均切割成4份
        numpy.vsplit(D,(3,4))   #将矩阵在第3,4行位置切割
        numpy.hsplit(D,4)       #将矩阵按照列切割成4份
        numpy.sort(B, axis=1)   #对矩阵B的数值按行正序
        numpy.argsort(B, axis=1)   #对矩阵B的索引按行正序
        
        data = numpy.sin(numpy.arange(20)).reshape(5,4)      
        ind = data.argmax(axis=0)       #每列最大值所在下标，axis=1时按行查找 
        data_max = data[ind,range(data.shape[1])]       #每列最大值

