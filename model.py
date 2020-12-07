from keras.layers import *
from keras.models import Sequential
from keras.datasets import mnist
from keras.utils import to_categorical
import os

# Load Dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the dataset
def ProcessData(x, y):
    x = x.reshape((-1, 28, 28, 1))
    y = to_categorical(y)
    return x, y

x_train, y_train = ProcessData(x_train, y_train)
x_test, y_test = ProcessData(x_test, y_test)


# Building a CNN model 
model = Sequential()
model.add(Conv2D(32, (3, 3), activation = "relu", input_shape = (28, 28, 1)))
model.add(MaxPool2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation = "relu", input_shape = (28, 28, 1)))
model.add(MaxPool2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation = "relu", input_shape = (28, 28, 1)))
model.add(MaxPool2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation = "relu"))
model.add(Dense(10, activation = "softmax"))

model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])
history = model.fit(x_train, y_train, epochs = 20, validation_split = 0.1, batch_size = 128)

# If there is no model exists -> create a directory to do so
if not os.path.exists("./model"):
	os.mkdir("./model")

model.save("./model/model.h5")
