from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import to_categorical
from PIL import Image
from sklearn import model_selection
import numpy as np
import sys, keras
import tensorflow as tf
import os, glob


classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50


def build_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(50, 50, 3)))
    model.add(Activation("relu"))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0, 25))

    model.add(Conv2D(64, 3, 3))
    model.add(Activation("relu"))
    model.add(Conv2D(64, 3, 3))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0, 25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation("relu"))
    model.add(Dropout(0, 5))
    model.add(Dense(3))
    model.add(Activation("softmax"))

    opt = tf.keras.optimizers.RMSprop(learning_rate=0.0001, rho=0.9)

    # トレーニング関数の定義
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    # モデルのロード
    model = load_model("./animal_cnn_aug.h5")
    return model


def main():
    image = Image.open(sys.argv[1])
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    x = []
    x.append(data)
    x = np.array(x)
    model = build_model()

    result = model.predict([x])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)
    print("{0}({1})".format(classes[predicted], percentage))


if __name__ == "__main__":
    main()
