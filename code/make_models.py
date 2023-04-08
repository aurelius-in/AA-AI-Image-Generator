import tensorflow as tf
from tensorflow.keras import layers

# The make_generator_model() function defines the generator model using DCGAN architecture, 
# which consists of several convolutional transpose layers, batch normalization, and activation functions. 
# The generator model takes a random noise vector of shape (batch_size, 100) as input and outputs a generated image of shape (batch_size, 32, 32, 3).

# Define the generator model using DCGAN architecture
def make_generator_model():
    model = tf.keras.Sequential()
    model.add(layers.Dense(4*4*256, use_bias=False, input_shape=(100,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Reshape((4, 4, 256)))
    assert model.output_shape == (None, 4, 4, 256) 

    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    assert model.output_shape == (None, 8, 8, 128)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    assert model.output_shape == (None, 16, 16, 64)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(3, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    assert model.output_shape == (None, 32, 32, 3)

    return model

# The make_labeler_model() function defines the image labeler model using CNN architecture, which consists of several convolutional layers, 
# max pooling, flatten, and dense layers. The image labeler model takes an input image of shape (batch_size, 32, 32, 3) and outputs a label of 
# shape (batch_size, 4) representing the probability distribution over the four possible image sources.

# Define the image labeler model using CNN architecture
def make_labeler_model():
    model = tf.keras.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(4))

    return model
