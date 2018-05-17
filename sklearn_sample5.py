from sklearn.datasets import load_iris
from sklearn.svm import SVC

clf = SVC()

iris = load_iris()
x,y = iris.data,iris.target
clf.fit(x,y)

#存储模型方法一
import pickle
#存储
with open('save/clf.pickle','wb') as f:
    pickle.dump(clf,f)
    f.close()
#读取
with open('save/clf.pickle','rb') as f:
    clf2 = pickle.load(f)
    print clf2.predict(x[0:1]) 
    f.close()

#存储模型方法二
from sklearn.externals import joblib
#存储
joblib.dump(clf,'save/clf.pkl')

#读取
clf3 = joblib.load('save/clf.pkl')
print clf3.predict(x[0:1])
