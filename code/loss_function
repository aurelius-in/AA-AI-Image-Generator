import tensorflow as tf

# The generator and discriminator are pre-trained models that take no inputs and return the generated images 
# and discriminator scores, respectively. The target_images argument contains the target set of images to be 
# generated. The mse_loss measures the pixel-wise difference between the generated and target images, while 
# the adv_loss measures the difference in the discriminator scores between the generated and real images. 

# The two losses are combined with a weighting factor of 0.001, which controls the trade-off between generating 
# visually realistic images and generating images that match the target set more closely. Finally, the total_loss
# is returned as the overall loss function for the image generator.

def image_generator_loss(generator, discriminator, target_images):
    # Generate images using the generator
    generated_images = generator()

    # Pass the generated and target images through the discriminator
    generated_scores = discriminator(generated_images)
    target_scores = discriminator(target_images)

    # Compute the mean squared error loss
    mse_loss = tf.reduce_mean(tf.square(generated_images - target_images))

    # Compute the adversarial loss based on the discriminator scores
    adv_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(
        labels=tf.ones_like(generated_scores), logits=generated_scores))

    # Combine the losses with a weighting factor
    total_loss = mse_loss + 0.001 * adv_loss

    return total_loss
