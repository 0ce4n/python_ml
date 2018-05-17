import numpy as np
import tensorflow as tf 

def input_evaluation_set():
    features = {'SepalLength': np.array([6.4, 5.0]),
                'SepalWidth':  np.array([2.8, 2.3]),
                'PetalLength': np.array([5.6, 3.3]),
                'PetalWidth':  np.array([2.2, 1.0])}
    labels = np.array([2, 1])
    return features, labels

a,b = input_evaluation_set()


data = tf.data.Dataset.from_tensor_slices((dict(a),b))
print(data)

# my_feature_columns = []
# for key in a.keys():
#     my_feature_columns.append(tf.feature_column.numeric_column(key=key))

# print my_feature_columns[0]
