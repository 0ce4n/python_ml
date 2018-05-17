import tensorflow as tf 

sess = tf.Session()

#单次迭代
# dataset = tf.data.Dataset.range(100)
# iterator = dataset.make_one_shot_iterator()
# next_data = iterator.get_next()
# for i in range(100):
#     x = sess.run(next_data)
#     print(x)


#可初始化迭代
# max_v = tf.placeholder(dtype=tf.int64,shape =[])
# dataset = tf.data.Dataset.range(max_v)
# iterator = dataset.make_initializable_iterator()
# next_data = iterator.get_next()
# #注意对迭代器初始化
# sess.run(iterator.initializer,feed_dict={max_v:10})
# for i in range(10):
#     y = sess.run(next_data)
#     print(y)
# sess.run(iterator.initializer,feed_dict={max_v:100})
# for i in range(100):
#     y = sess.run(next_data)
#     print(y)


#可重新初始化迭代
# Define training and validation datasets with the same structure.
# training_dataset = tf.data.Dataset.range(100).map(
#     lambda x: x + tf.random_uniform([], -10, 10, tf.int64))
# validation_dataset = tf.data.Dataset.range(50)

# # A reinitializable iterator is defined by its structure. We could use the
# # `output_types` and `output_shapes` properties of either `training_dataset`
# # or `validation_dataset` here, because they are compatible.
# iterator = tf.data.Iterator.from_structure(training_dataset.output_types,
#                                            training_dataset.output_shapes)
# next_element = iterator.get_next()

# training_init_op = iterator.make_initializer(training_dataset)
# validation_init_op = iterator.make_initializer(validation_dataset)

# #Run 20 epochs in which the training dataset is traversed, followed by the
# #validation dataset.
# for _ in range(20):
#   # Initialize an iterator over the training dataset.
#   sess.run(training_init_op)
#   for _ in range(100):
#     sess.run(next_element)

#   # Initialize an iterator over the validation dataset.
#   sess.run(validation_init_op)
#   for _ in range(50):
#     sess.run(next_element)


# # Define training and validation datasets with the same structure.
# training_dataset = tf.data.Dataset.range(100).map(
#     lambda x: x + tf.random_uniform([], -10, 10, tf.int64)).repeat()
# validation_dataset = tf.data.Dataset.range(50)

# # A feedable iterator is defined by a handle placeholder and its structure. We
# # could use the `output_types` and `output_shapes` properties of either
# # `training_dataset` or `validation_dataset` here, because they have
# # identical structure.
# handle = tf.placeholder(tf.string, shape=[])
# iterator = tf.data.Iterator.from_string_handle(
#     handle, training_dataset.output_types, training_dataset.output_shapes)
# next_element = iterator.get_next()

# # You can use feedable iterators with a variety of different kinds of iterator
# # (such as one-shot and initializable iterators).
# training_iterator = training_dataset.make_one_shot_iterator()
# validation_iterator = validation_dataset.make_initializable_iterator()

# # The `Iterator.string_handle()` method returns a tensor that can be evaluated
# # and used to feed the `handle` placeholder.
# training_handle = sess.run(training_iterator.string_handle())
# validation_handle = sess.run(validation_iterator.string_handle())

# # Loop forever, alternating between training and validation.
# while True:
#   # Run 200 steps using the training dataset. Note that the training dataset is
#   # infinite, and we resume from where we left off in the previous `while` loop
#   # iteration.
#   for _ in range(200):
#     sess.run(next_element, feed_dict={handle: training_handle})

#   # Run one pass over the validation dataset.
#   sess.run(validation_iterator.initializer)
#   for _ in range(50):
#     sess.run(next_element, feed_dict={handle: validation_handle})


dataset = tf.data.Dataset.range(5)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()

result = tf.add(next_element,next_element)
sess.run(iterator.initializer)
while True:
    try:
        x = sess.run(result)
    except tf.errors.OutOfRangeError:
        break
    print(x)