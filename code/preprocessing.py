import os
import numpy as np
from PIL import Image

# This code loads images from the specified folders, resizes them to the desired size (in this case 64x64 pixels), 
# normalizes their pixel values to the range [-1, 1], and saves the preprocessed images and their labels to a file 
# called "preprocessed_images.npz". The labels are assigned based on the order of the folders in the data_folders list, starting from 0.

# set the path to the image folders
data_folders = ['path/to/imagenet', 'path/to/coco', 'path/to/flickr', 'c://images/']

# set the image size for DCGAN
image_size = 64

# define a function to load and preprocess the images
def load_images(folders):
    images = []
    labels = []
    for i, folder in enumerate(folders):
        print('Loading images from folder', i+1, '/', len(folders))
        for filename in os.listdir(folder):
            if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                image_path = os.path.join(folder, filename)
                try:
                    with Image.open(image_path) as img:
                        # resize the image to the desired size for DCGAN
                        img = img.resize((image_size, image_size))
                        # convert the image to a numpy array
                        img_arr = np.array(img)
                        # normalize the pixel values to the range [-1, 1]
                        img_arr = img_arr.astype('float32') / 127.5 - 1.
                        # add the image and its label to the lists
                        images.append(img_arr)
                        labels.append(i)
                except:
                    print('Error loading image:', image_path)
    # convert the lists to numpy arrays
    images = np.array(images)
    labels = np.array(labels)
    return images, labels

# load the images and their labels
images, labels = load_images(data_folders)

# save the preprocessed images and their labels to a file
np.savez('preprocessed_images.npz', images=images, labels=labels)
