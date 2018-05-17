import numpy as np

array = np.array([[1,2,3],[4,5,6]],np.int32)

#shape dim size等属性

#dtype 数据类型
print(array.dtype)

a = np.zeros(shape = (3,4))
print(a)

a = np.arange(10,20,2)
print(a)

a = np.linspace(0,10,6)
print(a)
#reshape重新定义形状
a = a.reshape(2,3)
print(a)

#dot点乘运算

b = np.random.random((3,2))
print(b)
print(a.dot(b)) #np.dot(a,b)

#max,min等类似
print(np.sum(b))
print(np.sum(b,axis = 0))
print(np.sum(b,axis = 1))

A = np.arange(2,14).reshape((3,4))
print(A)

#获取索引
print(np.argmin(A))
print(np.argmax(A))

#平均值
print(np.mean(A))

#中位数
print(np.median(A))

#累加
print(np.cumsum(A))

#累差
print(np.diff(A))

#非零 nonzero  排序 sort

#矩阵的转置
print(np.transpose(A))
print(A.T)

print(np.clip(A,5,9))

#可以类似list的操作
print(A[1][0:2])

#将矩阵变成一维
print(A.flatten()) #A.flat 返回的是迭代器

#合并两个矩阵

A = np.array([1,1,1])
B = np.array([2,2,2])

print(np.vstack((A,B)))
print(np.hstack((A,B)))

print(np.concatenate((A,B,B,A),axis = 0))

#添加新的维度
print(A[np.newaxis,:])
print(A[:,np.newaxis])


#分割矩阵
A = np.arange(12).reshape(3,4)

print(A)
#等分
print(np.split(A,2,axis = 1))

#不等量分割
print(np.array_split(A,2,axis=0))

print(np.vsplit(A,3))
print(np.hsplit(A,2))


