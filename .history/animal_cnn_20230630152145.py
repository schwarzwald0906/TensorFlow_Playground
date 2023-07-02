from kesas.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import ActivationLayer, Dropout, flatten, Dense
from keras.utils import np_utils
import numpy as np

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50


# メインの関数を定義する
def main():
    #    X_train,X_test,y_train,y_test = np.load("./animal.npy")
    X_train = np.load("./X_train.npy", allow_pickle=True)
    X_test = np.load("./X_test.npy", allow_pickle=True)
    y_train = np.load("./y_train.npy", allow_pickle=True)
    y_test = np.load("./y_test.npy", allow_pickle=True)

    x_train = x_train.astype("float") / 256
    x_test = x_test.astype("float") / 256
    y_train = y_train.to_categorical(y_train, num_classes)
    y_test = y_test.to_categorical(y_train, num_classes)

    mode
