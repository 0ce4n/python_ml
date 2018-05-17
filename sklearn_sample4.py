from sklearn.learning_curve import validation_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np 

param_range = np.logspace(-6,-2.3,5)
digits = load_digits()
dig_x,dig_y = digits.data,digits.target
train_loss,test_loss = validation_curve(SVC(),dig_x,dig_y,cv=10,
            param_name='gamma',param_range=param_range,scoring='neg_mean_squared_error')
train_loss_mean = -np.mean(train_loss,axis=1)
test_loss_mean = -np.mean(test_loss,axis=1)

plt.plot(param_range,train_loss_mean,'o-',color='r',label='train_loss')
plt.plot(param_range,test_loss_mean,'o-',color='blue',label='test_loss')
plt.legend(loc='best')
plt.show()