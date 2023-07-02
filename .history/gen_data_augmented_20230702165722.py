import imghdr
from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50
num_testdata = 100

X_train = []
Y_train = []
X_test = []
Y_test = []

for index, cls in enumerate(classes):
    photos_dir = "./" + cls
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 200:
            break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image).astype(np.float32)

        if i < num_testdata:
            X_test.append(data)
            Y_test.append(index)
        else:
            X_train.append(data)
            Y_train.append(index)

            for angle in range(-20, 20, 5):
                # 回転
                img_r = imghdr.rotate(angle)
                data = np.asarray(img_r)
                X_train.append(data)
                Y_train.append(index)

                # 反転
                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                data = np.asarray(img_trans)
                X_train.append(data)
                Y_train.append(index)


X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y)
np.save("./x_train.npy", x_train)
np.save("./x_test.npy", x_test)
np.save("./y_train.npy", y_train)
np.save("./y_test.npy", y_test)
