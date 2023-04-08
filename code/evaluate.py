import tensorflow as tf
from tensorflow.keras.datasets import cifar10

# Assuming that the generator, discriminator, and the GAN model have already been trained, 
# and the generated images are stored in a variable generated_images, we can  now evaluate 
# the performance of the generated images on the CNN model.

# Load the CIFAR-10 dataset
(_, _), (x_test, y_test) = cifar10.load_data()

# One-hot encode the labels
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)

# Load the pre-trained CNN model
cnn_model = tf.keras.models.load_model('cnn_model.h5')

# Evaluate the generated images on the CNN model
generated_images_normalized = generated_images / 255.0
loss, accuracy = cnn_model.evaluate(generated_images_normalized, y_test, verbose=0)

print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")
