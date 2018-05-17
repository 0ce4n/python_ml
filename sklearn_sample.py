import numpy as nu
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#获取数据
iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target

#将训练数据与测试数据进行分割
x_train,x_test,y_train,y_test = train_test_split(iris_x,iris_y,test_size = 0.3)

#确定使用的训练模型
knn = KNeighborsClassifier()

#进行训练
knn.fit(x_train,y_train)

#结果对比
print(knn.predict(x_test))
print(y_test)