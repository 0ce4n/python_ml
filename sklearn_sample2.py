from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
iris_x = iris.data
iris_y = iris.target

knn = KNeighborsClassifier()

#交叉验证
score = cross_val_score(knn,iris_x,iris_y,cv=5,scoring='accuracy')

print score.mean()