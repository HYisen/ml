import tensorflow as tf
from proto.util import *

orig, _ = load(bank_mapper)
mapper = gen_mapper(orig)
test, train = divide_data(orig, 1000)
x_test, y_test = map_to_vector(test, mapper)
x_train, y_train = map_to_vector(train, mapper)

mnist = tf.keras.datasets.mnist

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(2, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)


def think(line):
    vec = mapper(line)
    predict = model.predict(np.array(vec).reshape(1, 30))
    result = np.argmax(predict)
    return 'yes' if result == 1 else 'no'


exam(test, think)
