from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import ActivationLayer, Dropout, flatten, Dense
from keras.utils import np_utils
import numpy as np

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50


# メインの関数を定義する
def main():
    #    X_train,X_test,y_train,y_test = np.load("./animal.npy")
    X_train = np.load("./x_train.npy", allow_pickle=True)
    X_test = np.load("./x_test.npy", allow_pickle=True)
    y_train = np.load("./y_train.npy", allow_pickle=True)
    y_test = np.load("./y_test.npy", allow_pickle=True)

    X_train = X_train.astype("float") / 256
    X_test = X_test.astype("float") / 256
    y_train = y_train.to_categorical(y_train, num_classes)
    y_test = y_test.to_categorical(y_test, num_classes)

    model = model_train(X_train, y_train)
    model_eval(model, X_test, y_test)


def model_train():
    model = Sequential()
    model.add(Conv2D(32, 3, 3), padding="same", input_shape=X_train.shape[1:])
    model.add(Activation('relu')