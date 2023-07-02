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
    x_train, x_test, y_train, y_test = np.load("./animal.npy")
