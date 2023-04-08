import numpy as np

# load the preprocessed images and their labels from the file
data = np.load('preprocessed_images.npz')
images = data['images']
labels = data['labels']

# check the shape of the arrays
print('Shape of images:', images.shape)   # e.g., (50000, 64, 64, 3)
print('Shape of labels:', labels.shape)   # e.g., (50000,)

# do something with the preprocessed images and their labels, e.g., train a GAN
