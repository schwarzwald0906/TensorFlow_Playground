from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import to_categorical
import numpy as np
import keras
import tensorflow as tf

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
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    model = model_train(X_train, y_train)


# CNNのモデル訓練の定義（後でチューニング必要）
def model_train(X, y):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=X.shape[1:]))
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

    opt = tf.keras.optimizers.RMSprop(learning_rate=0.0001, learning_rate_decay=1e-6)

    # トレーニング関数の定義
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    model.fit(X, y, batch_size=32, epochs=100)
    # モデルの保存
    model.save("./animal_cnn.h5")
    return model


# テストを行う関数
def model_eval(model, x, y):
    scores = model.evaluate(x, y, verbose=1)
    print("Test Loss:", scores[0])
    print("Test Accuracy:", scores[1])


# 他のプログラムから呼ばれたときのみ実行する。
if __name__ == "__main__":
    main()
