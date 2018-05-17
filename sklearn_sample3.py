from sklearn.learning_curve import learning_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np 
 
digits = load_digits()
dig_x,dig_y = digits.data,digits.target
tarin_size,train_loss,test_loss = learning_curve(SVC(gamma=0.001),dig_x,dig_y,cv=10,
            scoring='neg_mean_squared_error',train_sizes=[0.1,0.25,0.50,0.75,1])
train_loss_mean = -np.mean(train_loss,axis=1)
test_loss_mean = -np.mean(test_loss,axis=1)

plt.plot(tarin_size,train_loss_mean,'o-',color='r',label='train_loss')
plt.plot(tarin_size,test_loss_mean,'o-',color='blue',label='test_loss')
plt.legend(loc='best')
plt.show()
