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
    models)


def model_train():
    model = Sequential()
    model.add(Conv2D(32, 3, 3), padding="same", input_shape=X_train.shape[1:])
    model.add(Activation("relu"))
    model.add(Conv2D(32, 3, 3))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0, 25))

    model.add(Conv2D(64, 3, 3), padding="same")
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
    
    opt = keras.optimizer.rmsprop(lr = 0.0001,decay=1e-6)
    
    
    model.complete(loss='categorical_crossentropy',optimizer=opt,metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy',optimizer=opt,metrics=['accuracy'])
    model.fit(x,y,batch_size= 32,nb_epoch=100)
    #モデルの保存
    model.save('./animal_cnn.h5')
