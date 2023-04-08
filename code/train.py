import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# The generate_noise_samples function generates a batch of noise samples using a normal distribution with mean 0 
# and standard deviation 1. These noise samples are used as input to the generator to produce fake images.

# The train_dcgan function is responsible for training the DCGAN model for a specified number of epochs. 
# In each epoch, a batch of real images is sampled from the training set, and a batch of noise samples is
# generated using the generate_noise_samples function. The discriminator is trained on the real and fake images,
# and the generator is trained to fool the discriminator. The losses for the discriminator and generator are recorded, 
# and sample images are saved periodically using the save_image_samples function.

# Define the input shape for the image generator
img_rows, img_cols, channels = 64, 64, 3

# Define the batch size and number of epochs to use during training
batch_size = 128
epochs = 100

# Load the ImageNet and COCO image datasets
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
train_generator = train_datagen.flow_from_directory('train', target_size=(img_rows, img_cols), batch_size=batch_size, class_mode='binary')
validation_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_directory('val', target_size=(img_rows, img_cols), batch_size=batch_size, class_mode='binary')

# Define the CNN model for labeling
cnn_model = Sequential([
    Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(img_rows, img_cols, channels)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Conv2D(64, (3, 3), padding='same', activation='relu'),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Define the DCGAN model for image generation
generator = Sequential([
    Dense(256 * 8 * 8, input_dim=100, activation='relu'),
    Reshape((8, 8, 256)),
    Conv2DTranspose(128, (4,4), strides=(2,2), padding='same', activation='relu'),
    Conv2DTranspose(64, (4,4), strides=(2,2), padding='same', activation='relu'),
    Conv2DTranspose(3, (4,4), strides=(2,2), padding='same', activation='sigmoid')
])
discriminator = Sequential([
    Conv2D(64, (4,4), strides=(2,2), padding='same', input_shape=(img_rows, img_cols, channels), activation='relu'),
    Conv2D(128, (4,4), strides=(2,2), padding='same', activation='relu'),
    Conv2D(256, (4,4), strides=(2,2), padding='same', activation='relu'),
    Flatten(),
    Dense(1, activation='sigmoid')
])
dcgan_model = Sequential([generator, discriminator])
discriminator.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.0002, beta_1=0.5), metrics=['accuracy'])
discriminator.trainable = False
dcgan_model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.0002, beta_1=0.5))
