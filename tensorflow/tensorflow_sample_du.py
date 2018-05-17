import tensorflow as tf
import numpy as np 
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

datas = load_digits()
x_data = datas.data
y_data = datas.target

x_train_data,x_test_data,y_train_data,y_test_data = train_test_split(x_data,y_data,test_size=0.3)

def add_layer(inputs,input_size,output_size,activation_func=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs,Weights)+biases
    if activation_func is None:
        output = Wx_plus_b
    else:
        output = activation_func(Wx_plus_b)
    return output

a = tf.Variable(tf.random_normal([2,3]))
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(a))