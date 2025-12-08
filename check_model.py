import tensorflow as tf

model = tf.keras.models.load_model("cat_dog_model.keras")
model.summary()
