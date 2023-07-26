import tensorflow as tf

# Load the model.
model = tf.keras.models.load_model("animal_cnn_aug.h5")

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open("animal_cnn_aug.tflite", "wb") as f:
    f.write(tflite_model)
