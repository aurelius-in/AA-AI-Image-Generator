import tensorflow as tf
import numpy as np
import PIL.Image

# Loads the generator model that was previously trained and saved to a file called "aa_ai_image_generator.pb". 
# generates some random noise and passes it through the generator to generate a batch of 64 fake images. 
# Finally, we save these generated images to a file called "generated_images.png" using the 
# PIL.Image.save() function from Python's Pillow library.

# Load generator model
model = tf.keras.models.load_model("aa_ai_image_generator.pb")

# Generate random noise
noise = tf.random.normal([64, 100])

# Generate fake images
fake_images = model.predict(noise)

# Rescale pixel values to 0-255
fake_images = (fake_images + 1) * 127.5
fake_images = np.clip(fake_images, 0, 255).astype(np.uint8)

# Save generated images to file
images_grid = PIL.Image.fromarray(tf.keras.preprocessing.image.array_to_img(fake_images, scale=False))
images_grid.save("generated_images.png")
